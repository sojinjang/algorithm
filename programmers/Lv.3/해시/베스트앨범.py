from collections import defaultdict


def solution(genres, plays):
    genre_dict = defaultdict(dict)
    play_dict = {}
    answer = []

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_dict[genre][idx] = play
    for genre, song_info in genre_dict.items():
        total_play = sum(song_info.values())
        play_dict[total_play] = sorted(song_info, key=lambda x: song_info[x], reverse=True)
    for song_list in sorted(play_dict.items(), reverse=True):
        answer.append(song_list[1][:2])

    return [y for x in answer for y in x]
