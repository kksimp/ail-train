class Store:
    def __init__(s, data, refs):
        s.data, s.refs = data, refs
    def write(s, m, logical, text):
        p = m[logical]
        if s.refs[p] > 1:
            s.refs[p] -= 1
            s.data.append(text)
            s.refs.append(1)
            m[logical] = len(s.data) - 1
        else:
            s.data[p] = text
    def drop(s, m):
        for p in m:
            s.refs[p] -= 1
    def report(s, label, m):
        view = "".join(s.data[p] for p in m)
        live = sum(1 for r in s.refs if r > 0)
        print(f"{label:<20} map {m} reads {view}  physical in use {live}")

st = Store(["a", "b", "c", "d", "e"], [1, 1, 1, 1, 1])
vol = [0, 1, 2, 3, 4]
st.report("volume", vol)
snap1 = list(vol)
for p in snap1:
    st.refs[p] += 1
st.write(vol, 1, "B")
st.write(vol, 3, "D")
st.report("after 2 writes", vol)
st.report("snapshot 1", snap1)
snap2 = list(vol)
for p in snap2:
    st.refs[p] += 1
st.write(vol, 1, "X")
st.write(vol, 4, "E")
st.report("after snapshot 2", vol)
st.drop(snap1)
st.report("snapshot 1 deleted", vol)
st.report("snapshot 2", snap2)
