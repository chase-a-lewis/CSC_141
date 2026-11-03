def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album
album1 = make_album("Soundgarden", "Superunknown")
album2 = make_album("Audioslave", "Audioslave")
album3 = make_album("Nirvana", "Nevermind")
album4 = make_album("Evanescence", "Fallen")
print(album1)
print(album2)
print(album3)
print(album4)