playlist = {
    'Title': 'Good Music',
    'Owner': 'Anavila',
    'Songs':[
        {'Title': 'Song 1', 'Artist': ['Artistman'], 'Duration': 360},
        {'Title': 'Song 2', 'Artist': ['Artwoman','Composser'], 'Duration': 300},
        {'Title': 'Song 3', 'Artist': ['Musician'], 'Duration': 320},
    ]
}

playlist_lenght = 0

for song in playlist['Songs']:
    playlist_lenght += song['Duration']

print(playlist_lenght)