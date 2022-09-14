a, b = 3, 4
print("a = {}".format(a))
print("b = {}".format(b))
print(a, b)
a, b = b, a
print("a = {}".format(a))
print("b = {}".format(b))
a = b = c = d = 4
print(a, b, c, d)
print()
print("*"*100)
print()
# challenge of tuples
Taylor = "Reputation", "Taylor Swift", 2018, ((1, "Ready for it"), (2, "Blank Space"), (3, "I don't wanna live forever"), (4, "Look what you made me do"))
title, artist, year, tracks = Taylor
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("Track number:{}\tTitle:{}".format(track, title))

