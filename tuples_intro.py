# t= ("a","b","c")  #paranteces used () on tuples
# print(t)

songs= [("Taylor Swift", "Speak now", 2010),
        ("Harry Styles", "Harry's House", 2022),
        ("Billie Eilish", "Hit me hard and soft", 2024),
        ("Tems", "Born in the Wilde", 2024),]

print(len(songs))

for artist, album, year in songs:
    print("Artist: {}, Album: {}, Year: {}"
          .format(artist, album, year))


# swift = "Mine", "Speak now", 2010
# styles = "Mathilda", "Harrys  House", 2022
# billie = "Wild Flower", "hit me hard and soft", 2024
# tems = "Love me JeJe", "Born in the Wilde", 2024
# 
# # print(tems)
# # print(tems[0])
# # print(tems[1])
# # print(tems[2])
# 
# #tuples are immutable --
# #Good to protect integrity of data
# 
# title, album, year=swift
# 
# print(title)
# print(album)
# print(year)
# 
# table= ("Dinner table",200,100,75,52.5)
# print(table[1]*table[2])
# 
# name, length, width, height, price = table
# print(length*width)