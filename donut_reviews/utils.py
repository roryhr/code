import json
import pandas as pd


def export_facebook(album_file):
    with open(album_file) as f:
        album = json.load(f)

    photos = album['photos']

    photo_list = []
    for photo in photos:
        x = photo.copy()
        x.update(photo['media_metadata']['photo_metadata'])
        photo_list.append(x)
    
    df = pd.DataFrame(photo_list)
    df['name'] = df.description.apply(lambda x: x.split('\n')[0].strip())

    df.to_csv('exported_donut_album.csv')

if __name__ == '__main__':
    export_facebook('/Users/rory/data/facebook-3629808/photos_and_videos/album/0.json')