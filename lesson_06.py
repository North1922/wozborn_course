song = input('Введите название песен (через запятую):')
singers = input('Введите название исполнителей (через запятую):')
song = song.split(', ')
singers = singers.split(', ')
playlist = []
group_playlist = {}
for name, singer in zip(song, singers):
    playlist.append(f'{name} - {singer}')
    if singer not in group_playlist:
        group_playlist[singer] = [name]
    elif singer in group_playlist:
        group_playlist[singer].append(name)

playlist = enumerate(playlist, 1)
print('-----------------')
print('Плейлист: ')
print('-----------------')
for num, trak in playlist:
    print(f'{num}.{trak}')
print('-----------------')
print('Группировка по исполнителям: ')
print('-----------------')
for name, trak in group_playlist.items():
    print(f'{name}: {", ".join(trak)}')
#Группировка по исполнителям:
#Создайте словарь, где ключ – это имя исполнителя, а значение – список песен этого исполнителя
#(если исполнитель встречается несколько раз, добавляйте все соответствующие песни).
print('-----------------')

#Yesterday, Bohemian Rhapsody, Imagine, Hotel California, We Will Rock You
#The Beatles, Queen, John Lennon, Eagles, Queen