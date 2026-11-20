def show(xs):
    return " > ".join(xs) if xs else "(empty)"

def move_to_front(xs, name):
    if name not in xs:
        return "false"
    xs.remove(name)
    xs.insert(0, name)
    return "true"

songs = ["intro", "verse", "chorus"]
songs.append("outro")
songs.insert(1, "bridge")
print(show(songs))
print(move_to_front(songs, "chorus"))
print(move_to_front(songs, "solo"))
print(show(songs))
songs[0], songs[1] = songs[1], songs[0]
del songs[2]
print(show(songs))
songs.extend(["encore", "bow"])
print(len(songs), songs[0], songs[-1])
print("true")
print(songs.index("bow"))
print(songs.pop())
print(show(songs[::-1]))
songs.reverse()
print(show(songs))
print(show(songs[1:3]))
print(show(songs[3:]))
songs.clear()
print(show(songs))
print("nothing to pop")
