import datetime
today = datetime.date(2024, 3, 10)
for id_, issued, terms in [("A-1", "2024-01-15", 30), ("A-2", "2024-02-20", 14), ("A-3", "2024-02-28", 30), ("A-4", "2023-02-29", 30), ("A-5", "2023-12-20", 60)]:
    try:
        y, m, d = map(int, issued.split("-"))
        start = datetime.date(y, m, d)
    except ValueError:
        print(f"{id_}: bad date {issued}")
        continue
    due = start + datetime.timedelta(days=terms)
    diff = (today - due).days
    state = f"OVERDUE by {diff}" if due < today else f"due in {-diff}"
    print(f"{id_}: due {due.isoformat()}, {state}")
