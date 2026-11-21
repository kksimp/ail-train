class Voter:
    def __init__(s, term, voted, last_term, last_index):
        s.term, s.voted, s.last_term, s.last_index = term, voted, last_term, last_index
    def request(s, cand, term, last_term, last_index):
        if term < s.term:
            return f"no: term {term} is older than {s.term}"
        if term > s.term:
            s.term = term
            s.voted = ""
        if s.voted != "" and s.voted != cand:
            return f"no: already voted for {s.voted} in term {term}"
        if last_term < s.last_term or (last_term == s.last_term and last_index < s.last_index):
            return f"no: log ({last_term}, {last_index}) is behind ({s.last_term}, {s.last_index})"
        s.voted = cand
        return "yes"

v = Voter(4, "", 3, 7)
asks = [("n2", 3, 3, 9), ("n3", 4, 2, 12), ("n4", 4, 3, 6), ("n5", 4, 3, 7), ("n2", 4, 3, 9), ("n5", 4, 3, 7), ("n3", 5, 4, 1)]
for cand, term, lt, li in asks:
    answer = v.request(cand, term, lt, li)
    print(f"{cand} asks in term {term}: {answer}")
print(f"voter now in term {v.term}, voted for {v.voted}")
