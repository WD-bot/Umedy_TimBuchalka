from Nested_data import albums

SONGS_LIST_INDEX=3  # if in all CAPITAL then it is a contants
# and should NOT be changed
SONG_TITLE_INDEX=1

while True:
    print("Please choose your album(invalid choice exits):")
    for index, (artist, title, year, songs) in enumerate(albums):
        print("{}: {}, {}".format(index + 1, title, artist))
    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index, value)
    choice =int(input())
    if 1 <=choice <= len(albums): #in for the required range
        songs_list=albums[choice-1][SONGS_LIST_INDEX]
    else:
        break
    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
       print("{}: {}".format(index + 1, song))
    song_choice = int(input())
    if 1<= song_choice<= len(songs_list):
        title=songs_list[song_choice-1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))

    print("_"*40)