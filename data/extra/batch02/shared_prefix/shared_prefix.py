import os
for ws in [["flower", "flow", "flight"], ["interview", "internet", "interval"], ["dog", "car"], ["solo"], []]:
    print(f"[{' '.join(ws)}] -> '{os.path.commonprefix(ws)}'")
files = ["report_2024_q1.csv", "report_2024_q2.csv", "report_2023_q4.csv"]
cp = os.path.commonprefix(files)
print(f"shared: {cp}")
print(" ".join(f[len(cp):] for f in files))
