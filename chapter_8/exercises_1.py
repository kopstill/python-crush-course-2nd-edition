def city_country(city, country):
    message = f"{city}, {country}"
    return message.title()


result = city_country('santiago', 'chile')
print(result)
result = city_country('beijing', 'china')
print(result)
result = city_country('liverpool', 'england')
print(result)

print("---")


def make_album(singer_name, album_name, song_count=None):
    album = {"singer_name": singer_name, "album_name": album_name}
    if song_count:
        album['song_count'] = song_count
    return album


album_info = make_album('a', 'b')
print(album_info)
album_info = make_album('a', 'b', None)
print(album_info)
album_info = make_album('a', 'b', False)
print(album_info)
album_info = make_album('a', 'b', 10)
print(album_info)

print('---')


def make_album():
    album_list = []

    while True:
        singer_name = input('Input singer name: ')
        if singer_name == 'q':
            break
        album_name = input('Input album name: ')
        if album_name == 'q':
            break

        album_detail = {'singer_name': singer_name, 'album_name': album_name}
        album_list.append(album_detail)

    return album_list


albums = make_album()
print(albums)
