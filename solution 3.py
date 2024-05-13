import datetime
import random


class Track:
    '''
    A class representing a music track.
    '''
    all_tracks = []
    menu = ''
    song_start_end = {}

    def __init__(self, ptr):
        '''
        Initialize the track with its song, duration, singer, and release year
        '''
        ptr = ptr.split(';')
        self.song = ptr[0]
        self.time = ptr[1]
        self.singer = ptr[2]
        self.year = ptr[3]
        Track.all_tracks.append(self)

    def __str__(self):
        return f'{self.singer} - {self.song} {self.time}'

    def __repr__(self):
        return str(f'{self.singer} - {self.song} {self.time}')

    @classmethod
    def cr_menu(cls):
        '''
        Create a menu for selecting tracks.
        '''
        for i in range(len(Track.all_tracks)):
            Track.menu += f'{i + 1}. {Track.all_tracks[i]}{'\n'}'

        choice = int(input(f'{Track.menu}Введите номер выбранного трека.{'\n'}'
                           f'Если хотите прослушать плейлист по порядку, '
                           f'введите 0.{'\n'}'
                           f'Если хотите прослушать плейлист вперемешку, '
                           f'нажмите -1.{'\n'}'))
        if choice == 0:
            for i in range(1, len(Track.all_tracks) + 1):
                Track.turn_on(i)
                cont = int(input(f'Завершить прослушивание плейлиста?{'\n'}'
                                 f'1. Да.{'\n'}'
                                 f'2. Нет.{'\n'}'))
                if cont == 1:
                    break

        elif choice == -1:
            song_num = random.randint(1, len(Track.all_tracks))
            for i in range(1, len(Track.all_tracks) + 1):
                Track.turn_on(song_num)
                cont = int(input(f'Завершить прослушивание плейлиста?{'\n'}'
                                 f'1. Да.{'\n'}'
                                 f'2. Нет.{'\n'}'))
                if cont == 1:
                    break
                else:
                    song_num = random.randint(1, len(Track.all_tracks))
        elif 1 <= choice <= len(Track.all_tracks):
            Track.turn_on(choice)
            next_song = int(input(f'{Track.menu}Введите номер следующей песни, '
                                  f'которую хотите прослушать. '
                                  f'Если хотите завершить прослушивание, '
                                  f'нажмите 0.{'\n'}'))
            while next_song != 0:
                Track.turn_on(next_song)
                next_song = int(input(f'{Track.menu}Введите номер следующей песни, '
                                      f'которую хотите прослушать. '
                                      f'Если хотите завершить прослушивание, '
                                      f'нажмите 0.{'\n'}'))

    @classmethod
    def turn_on(cls, song_num):
        '''
        Turn on the selected track.
        '''
        song_ch = Track.all_tracks[int(song_num) - 1]

        for i in range(len(Track.all_tracks)):
            Track.menu += f'{i + 1}. {Track.all_tracks[i]}{'\n'}'

        for song in Track.all_tracks:
            Track.song_start_end[song] = []
        time_start = datetime.datetime.now()
        print(f'Проигрывание {Track.all_tracks[song_num - 1].singer} '
              f' - {Track.all_tracks[song_num - 1].song} началось. '
              f'Длительность: {Track.all_tracks[song_num - 1].time}{'\n'}')
        time = datetime.timedelta(days=0,
                                  seconds=int(Track.all_tracks[song_num - 1].time.split(':')[1]),
                                  microseconds=0,
                                  milliseconds=0,
                                  minutes=int(Track.all_tracks[song_num - 1].time.split(':')[0]),
                                  hours=0,
                                  weeks=0)
        time_end = time_start + time

        Track.song_start_end[song_ch] = [time_start, time_end]
        delta_pause = datetime.timedelta(days=0,
                                         seconds=10,
                                         microseconds=0,
                                         milliseconds=0,
                                         minutes=0,
                                         hours=0,
                                         weeks=0)
        pause_time = time_start + delta_pause
        time_now = datetime.datetime.now()

        while time_end > time_now:
            time_now = datetime.datetime.now()
            if pause_time < time_now:
                pause_time += delta_pause

                pause = input(f'Нажмите 1, если хотите поставить трек на паузу.{'\n'}'
                              f'Нажмите 0, чтобы выключить трек.{'\n'}'
                              f'Нажмите Enter, чтобы продолжить прослушивание.{'\n'}')
                if pause == '1':
                    print('Вы на паузе.')
                    time_now = datetime.datetime.now()
                    print(f'До конца прослушивания:{time_end - time_now}')
                    time_end += delta_pause

                elif pause == '0' or pause == 0:
                    print('Песня выключена.')
                    break

                else:
                    print(f'До конца прослушивания:{time_end - time_now}')
                    pause_time = datetime.datetime.now() + delta_pause
                    time_now = datetime.datetime.now()
            else:
                continue
        print(
            f'Проигрывание {Track.all_tracks[song_num - 1].singer} - '
            f'{Track.all_tracks[song_num - 1].song} '
            f'закончилось{'\n'}')


with open('tracks.txt', 'r', encoding='utf-8') as f:
    for ptr in f:
        Track(ptr)
# print(Track.all_tracks)
Track.cr_menu()
# Track.turn_on(2)
# Track.turn_on(3)
