"""Run 3 builder step (called by tools/build_data.py): adds the appfn, appfile, testfn, repair and behave items.

See tools/run3_families.py for what each family is. Every item built here is train-only (groups apps/, repair/,
behave/) and comes from train-split programs, real app code, agent trials or the phase 3 harvest.
"""

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile

from run3_families import (APPFILE_CAP_REPO, APPFILE_TOTAL, APPFN_CAP_COMPILER, APPFN_CAP_REPO, APPFN_TOTAL,
                           BEHAVE_MUT_TOTAL, REPAIR_MUT_TOTAL, RULE, TEST_OK, TESTFN_TOTAL, AppRunner, ail_files,
                           app_packages, appfile_item, appfn_candidates, appfn_item, apply_edits, behave_edit,
                           behave_prompt, fence, fn_text, mutate, ratio, repair_prompt, sha, testfn_cands, trap_of,
                           usable_files)


def check_tools_programs(ail_root, ail, commit, cache):
    """tools/ programs of the pinned tree (files with `fn main`): path -> passes `ail check`. Checked on one scratch
    copy of compiler/, std/ and tools/, cached by content."""
    progs = {}
    for p, s in ail_files(ail_root, "tools").items():
        if p.endswith(".ail") and re.search(r"^fn main\(", s, re.M):
            progs[p] = s
    out, todo = {}, []
    for p, s in sorted(progs.items()):
        path = os.path.join(cache, sha("toolcheck", commit, p, s) + ".json")
        try:
            with open(path, encoding="utf-8") as f:
                out[p] = json.load(f)["ok"]
        except (OSError, ValueError):
            todo.append((p, path))
    if todo:
        tmp = tempfile.mkdtemp(prefix="ailtools-")
        try:
            for d in ("compiler", "std", "tools"):
                shutil.copytree(os.path.join(ail_root, d), os.path.join(tmp, d))
            env = dict(os.environ, AIL_FIX="0")
            for p, path in todo:
                try:
                    r = subprocess.run([ail, "check", "--no-fix", os.path.basename(p)],
                                       cwd=os.path.join(tmp, os.path.dirname(p)), capture_output=True, text=True,
                                       env=env, timeout=300)
                    ok = r.returncode == 0
                except subprocess.TimeoutExpired:
                    ok = False
                out[p] = ok
                with open(path, "w", encoding="utf-8") as f:
                    json.dump({"ok": ok}, f)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    return out


def stdin_cases_pass(ail, commit, cache, src, cases):
    """Pinned `ail check`, then `ail run` (10 s, 512 MB) on each (stdin, expected stdout); cached by content."""
    path = os.path.join(cache, sha("stdincases", commit, src, json.dumps(cases)) + ".json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)["ok"]
    except (OSError, ValueError):
        pass
    tmp = tempfile.mkdtemp(prefix="ailtask-")
    ok = True
    try:
        with open(os.path.join(tmp, "main.ail"), "w", encoding="utf-8") as f:
            f.write(src)
        env = dict(os.environ, AIL_FIX="0")
        c = subprocess.run([ail, "check", "--no-fix", "main.ail"], cwd=tmp, capture_output=True, text=True, env=env,
                           timeout=300)
        ok = c.returncode == 0
        for inp, want in cases if ok else []:
            r = subprocess.run([ail, "run", "--timeout", "10000", "--max-memory", "512", "main.ail"], cwd=tmp,
                               input=inp, capture_output=True, text=True, env=env, timeout=120)
            if r.stdout != want or "trap[" in r.stderr:
                ok = False
                break
    except subprocess.TimeoutExpired:
        ok = False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"ok": ok}, f)
    return ok


def pick_capped(cands, cap_of, total):
    """cands: tuples (hash, bucket, ...); in hash order keep at most cap_of(bucket) per bucket and TOTAL in all."""
    seen, out = {}, []
    for c in sorted(cands, key=lambda c: c[0]):
        b = c[1]
        if seen.get(b, 0) >= cap_of(b):
            continue
        seen[b] = seen.get(b, 0) + 1
        out.append(c)
        if len(out) >= total:
            break
    return out


def build(ctx):
    """ctx: comp (build_data.Compiler), res (compiler results of step 1), progs, drafts, trials, seed, ail_root,
    apps_dir, apps_lock, harvest_dir, cache, train_group(group) -> bool, spec_ok(out) -> bool, spec_task(task, out),
    header_text(src), add(id, group, family, source, prog, user, assistant), drop(id, reason), notes (list).
    Returns a stats dict for the manifest."""
    comp, add, seed = ctx["comp"], ctx["add"], ctx["seed"]
    drop, notes = ctx["drop"], ctx["notes"]
    stats = {}

    # Train-split single-file programs that pass check and reproduce their output.
    good = []
    for g, source, name, src, py, out in ctx["progs"]:
        if not ctx["train_group"](g) or ctx["res"]["check:" + g]["rc"] != 0:
            continue
        if out is not None and ctx["res"]["run:" + g]["stdout"] != out:
            continue
        good.append((g, source, name, src, py, out))

    def tasks_of(src, py, out):
        t = []
        head = ctx["header_text"](src)
        if head:
            t.append(head)
            if out is not None and ctx["spec_ok"](out):
                t.append(ctx["spec_task"](head, out))
        elif out is not None and ctx["spec_ok"](out):
            t.append("Write an AIL program that prints exactly:\n\n```\n{}```".format(out))
        if py is not None:
            t.append("Port this Python program to AIL.\n\n```python\n{}\n```".format(py.rstrip("\n")))
        return t

    # ---- apps: appfn, appfile, testfn from real packages
    runner = AppRunner(comp.ail, comp.commit, ctx["cache"])
    tool_ok = check_tools_programs(ctx["ail_root"], comp.ail, comp.commit, ctx["cache"])
    notes.append("ail tools/ programs passing check: {} of {}".format(sum(tool_ok.values()), len(tool_ok)))
    fn_cands, file_cands, test_cands = [], [], []
    for repo, root, entry in app_packages(ctx["ail_root"], ctx["apps_dir"], ctx["apps_lock"]):
        if repo == "ail-compiler":
            files = {}
            for d in ("compiler", "std", "tools"):
                files.update(ail_files(root, d))
        else:
            files = ail_files(root)
        usable, dropped = usable_files(repo, root, entry, files, runner, tool_ok, notes)
        stats.setdefault("apps", {})[repo] = {"files": len([p for p in files if p.endswith(".ail")]),
                                              "usable": len(usable), "dropped": sorted(dropped)}
        by_label = {}
        for p, s in usable.items():
            lab = repo if repo != "ail-compiler" else "ail/" + p.split("/")[0]
            by_label.setdefault(lab, {})[p] = s
        for lab, fs in sorted(by_label.items()):
            for h, _, p, it, its in appfn_candidates(lab, fs, seed):
                fn_cands.append((h, lab, p, it, its))
            for p in sorted(fs):
                file_cands.append((sha(str(seed), "appfile", lab, p), lab, p, fs[p], files))
        if repo != "ail-compiler" and not dropped:
            t = runner.run(root, files, ["test"], entry)
            ok_names = set(TEST_OK.findall(t["out"]))
            stats["apps"][repo]["tests_ok"] = len(ok_names)
            if ok_names:
                def passed(n, ok_names=ok_names):
                    return n in ok_names or any(x.endswith("." + n) for x in ok_names)
                for p in sorted(usable):
                    for h, fname, user, ans in testfn_cands(repo + "/" + p, p, usable[p], passed):
                        test_cands.append((h, repo, "apps/{}/{}".format(repo, p), user, ans, usable[p]))
    per = {}
    for h, lab, p, it, its in pick_capped(
            fn_cands, lambda b: APPFN_CAP_COMPILER if b == "ail/compiler" else APPFN_CAP_REPO, APPFN_TOTAL):
        user, ans = appfn_item(lab, p, it, its)
        add("appfn:{}/{}#{}".format(lab, p, it["name"]), "apps/{}/{}".format(lab, p), "appfn", "apps",
            fn_text(it), user, ans)
        per[lab] = per.get(lab, 0) + 1
    stats["appfn_per_repo"] = per
    stats["appfn_candidates"] = len(fn_cands)
    per = {}
    for h, lab, p, src, files in sorted(file_cands, key=lambda c: c[0]):
        if sum(per.values()) >= APPFILE_TOTAL:
            break
        if per.get(lab, 0) >= APPFILE_CAP_REPO:
            continue
        r = appfile_item(lab, p, src, files)
        if not r:
            continue
        per[lab] = per.get(lab, 0) + 1
        add("appfile:{}/{}".format(lab, p), "apps/{}/{}".format(lab, p), "appfile", "apps", src, r[0], r[1])
    stats["appfile_per_repo"] = per

    # ---- testfn from train programs with @test functions (only tests that pass `ail test`)
    jobs = [("test:" + g, {name + ".ail": src}, ["test"], name + ".ail")
            for g, source, name, src, py, out in good if re.search(r"^@test", src, re.M)]
    tres = comp.many(jobs)
    for g, source, name, src, py, out in good:
        t = tres.get("test:" + g)
        if not t:
            continue
        ok_names = set(TEST_OK.findall(t["out"]))
        for h, fname, user, ans in testfn_cands(g, name + ".ail", src, lambda n, s=ok_names: n in s):
            test_cands.append((h, source, "testfn/" + g, user, ans, src))
    seen_files, picked = set(), {}
    for h, bucket, grp, user, ans, prog in sorted(test_cands, key=lambda c: (not c[2].startswith("apps/"), c[0])):
        if grp in seen_files or sum(picked.values()) >= TESTFN_TOTAL:
            continue
        seen_files.add(grp)
        src_name = "apps" if grp.startswith("apps/") else bucket
        picked[src_name] = picked.get(src_name, 0) + 1
        add("testfn:" + grp, grp if grp.startswith("apps/") else "apps/" + grp, "testfn", src_name, prog, user, ans)
    stats["testfn_per_source"] = picked
    stats["testfn_candidates"] = len(test_cands)

    # ---- repair-mut: 1 to 4 injected mistakes, whole-program answer; a quarter carry a same-rule repeat note
    jobs, meta = [], {}
    for g, source, name, src, py, out in good:
        tasks = tasks_of(src, py, out)
        if not tasks:
            continue
        for v in range(2):
            key = "{}#rm{}".format(g, v)
            n = 1 + int(sha(key, "n")[:4], 16) % 4
            edits = mutate(src, key, n)
            if not edits:
                continue
            bad = apply_edits(src, edits)
            prev = None
            if int(sha(key, "repeat")[:4], 16) % 4 == 0:
                extra = mutate(bad, key + "+", 1)
                if extra:
                    prev = apply_edits(bad, extra)
                    jobs.append(("rmprev:" + key, {"main.ail": prev}, ["check", "--no-fix"], "main.ail"))
            meta[key] = (g, src, bad, tasks[int(sha(key, "task")[:4], 16) % len(tasks)], prev)
            jobs.append(("rm:" + key, {"main.ail": bad}, ["check", "--no-fix"], "main.ail"))
    rres = comp.many(jobs)
    rm_cands = []
    for key, (g, src, bad, task, prev) in sorted(meta.items()):
        c = rres["rm:" + key]
        if c["rc"] == 0 or c["out"] == "timeout":
            continue
        rule = None
        if prev is not None:
            p = rres["rmprev:" + key]
            common = sorted(set(RULE.findall(p["out"])) & set(RULE.findall(c["out"])))
            rule = common[0] if p["rc"] != 0 and common else None
        rm_cands.append((sha(str(seed), "rm", key), key, g, src, bad, task, c["out"], rule))
    notes_rep = 0
    for _, key, g, src, bad, task, diag, rule in sorted(rm_cands)[:REPAIR_MUT_TOTAL]:
        add("repair-mut:" + key, "repair/" + g, "repair", "repair-mut", src,
            repair_prompt(task, bad, diag.strip(), key, rule), fence(src))
        notes_rep += rule is not None
    stats["repair_mut_candidates"] = len(rm_cands)
    stats["repair_mut_with_repeat_note"] = notes_rep

    # ---- repair-draft: agent drafts joined to their own trial's final by key (same run, task and trial)
    finals = {}
    for t in ctx["trials"]:
        if t["metrics"].get("correct") and len(t["files"]) == 1 and "src/main.ail" in t["files"]:
            finals[(t["run"].split(".tgz")[0], t["task"], t["trial"])] = t
    jobs, dmeta = [], {}
    for d in ctx["drafts"]:
        t = finals.get((d["run"], d["task"], d["trial"].split("/")[-1]))
        if not t:
            continue
        final = t["files"]["src/main.ail"]
        if ratio(d["source"], final) < 0.6:
            drop("repair-draft:" + d["key"], "draft too far from its own final")
            continue
        dmeta[d["key"]] = (d, t, final)
        jobs.append(("rd:" + d["key"], {"src/main.ail": d["source"]}, ["check", "--no-fix"], "src/main.ail"))
        jobs.append(("rdf:" + d["key"], {"src/main.ail": final}, ["check", "--no-fix"], "src/main.ail"))
    dres = comp.many(jobs)
    n_rd = 0
    for key, (d, t, final) in sorted(dmeta.items()):
        c, f = dres["rd:" + key], dres["rdf:" + key]
        if c["rc"] == 0 or f["rc"] != 0:
            drop("repair-draft:" + key, "draft passes or final fails check")
            continue
        add("repair-draft:" + key, "repair/task/" + t["task"], "repair", "repair-draft", final,
            repair_prompt(t["spec"].strip(), d["source"], c["out"].strip(), key), fence(final))
        n_rd += 1
    stats["repair_draft_joined"] = len(dmeta)

    # ---- behave-mut: semantic edits that pass check, finish within 10 s and print something else
    pend = {g: (source, src, out) for g, source, name, src, py, out in good
            if out is not None and ctx["spec_ok"](out) and ctx["header_text"](src)}
    found = {}
    for attempt in range(3):
        jobs, tried = [], {}
        for g, (source, src, out) in sorted(pend.items()):
            if g in found:
                continue
            e = behave_edit(src, g, attempt)
            if e:
                tried[g] = e
                # A mutated program can recurse or allocate without end: cap time and memory (an unbounded one
                # took the whole WSL VM down once).
                jobs.append(("bm:{}#{}".format(g, attempt), {"main.ail": e[1]},
                             ["run", "--timeout", "10000", "--max-memory", "512"], "main.ail"))
        bres = comp.many(jobs)
        for g, (kind, new) in sorted(tried.items()):
            r = bres["bm:{}#{}".format(g, attempt)]
            source, src, out = pend[g]
            trap = trap_of(r["out"])
            if r["out"] == "timeout" or "run.limit" in trap or "time limit" in trap:
                continue
            if "error[" in r["out"] and not trap:
                continue  # the edit broke `ail check`
            if r["stdout"] == out:
                continue
            found[g] = (kind, new, r["stdout"], trap)
    bm = []
    for g, (kind, new, got, trap) in sorted(found.items()):
        source, src, out = pend[g]
        bm.append((sha(str(seed), "bm", g), g, kind, src, new, got, trap,
                   ctx["spec_task"](ctx["header_text"](src), out)))
    kinds = {}
    for _, g, kind, src, new, got, trap, task in sorted(bm)[:BEHAVE_MUT_TOTAL]:
        kinds[kind] = kinds.get(kind, 0) + 1
        add("behave-mut:" + g, "behave/" + g, "behave", "behave-mut", src, behave_prompt(task, new, got, trap),
            fence(src))
    stats["behave_mut_candidates"] = len(bm)
    stats["behave_mut_kinds"] = kinds

    # ---- task: input-driven programs (data/extra/tasksNN/NAME/{spec.md,NAME.ail,NAME.py,cases/N.in,N.out}).
    # Kept only when the pinned check passes and the AIL program prints every case's .out (which the Python
    # reference produced) for its .in. user = spec + two example cases, answer = the program.
    extra = os.path.join(ctx["root"], "data", "extra")
    n_task, bad_task = 0, []
    for grp in sorted(os.listdir(extra)):
        gdir = os.path.join(extra, grp)
        if not grp.startswith("tasks") or not os.path.isdir(gdir):
            continue
        for name in sorted(os.listdir(gdir)):
            d = os.path.join(gdir, name)
            try:
                spec = open(os.path.join(d, "spec.md"), encoding="utf-8").read().strip()
                src = open(os.path.join(d, name + ".ail"), encoding="utf-8").read()
                cases = []
                for k in range(1, 6):
                    cases.append((open(os.path.join(d, "cases", "{}.in".format(k)), encoding="utf-8").read(),
                                  open(os.path.join(d, "cases", "{}.out".format(k)), encoding="utf-8").read()))
            except OSError:
                bad_task.append(name)
                continue
            if not stdin_cases_pass(comp.ail, comp.commit, ctx["cache"], src, cases):
                bad_task.append(name)
                drop("task:" + name, "task program fails its cases")
                continue
            ex = cases[:2]
            user = spec + "\n\nExamples:\n\n" + "\n\n".join(
                "Input:\n```\n{}```\nOutput:\n```\n{}```".format(i if i.endswith("\n") or not i else i + "\n",
                                                               o if o.endswith("\n") or not o else o + "\n")
                for i, o in ex)
            add("task:{}/{}".format(grp, name), "task2/{}/{}".format(grp, name), "task", "tasks", src, user,
                fence(src))
            n_task += 1
    stats["task_items"] = n_task
    stats["task_rejected"] = bad_task

    # ---- harvest (phase 3): the model's own drafts on train tasks, corrected and confirmed by the pinned compiler
    hpath = os.path.join(ctx["harvest_dir"], "items.jsonl") if ctx["harvest_dir"] else ""
    if hpath and os.path.isfile(hpath):
        with open(hpath, "rb") as f:
            stats["harvest_sha256"] = hashlib.sha256(f.read()).hexdigest()
        n = 0
        for line in open(hpath, encoding="utf-8"):
            h = json.loads(line)
            fam = h["family"]  # repair or behave
            add("{}-harvest:{}".format(fam, h["id"]), "{}/harvest/{}".format(fam, h["id"]), fam, fam + "-harvest",
                h["prog"], h["user"], h["answer"])
            n += 1
        stats["harvest_items"] = n
    return stats
