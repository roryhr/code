import json
import pandas as pd 
import requests


photos_and_videos = '~/data/facebook-3629808/photos_and_videos/Donutselfies_10103384416189657/'

with open('/Users/rory/data/facebook-3629808/photos_and_videos/album/0.json') as f:      
    album = json.load(f)
    
result = []
for photo in album['photos']:
    if photo.get('media_metadata') is None:
        print('Passing media metadata')
    
    if photo.get('media_metadata').get('photo_metadata').get('latitude') is None:
        print('Passing latitude')
        continue

    photo_metadata = photo.get('media_metadata').get('photo_metadata')
    x = {}
    x['properties'] = {                                                
        'popupContent': photo['description'].split('\n')[0],
        'description': photo['description'],
    }

    x["type"] = "Feature"

    x["geometry"] = {
        "type": "Point",
        "coordinates": [
            photo_metadata['longitude'],
            photo_metadata['latitude']
        ]
    }
    result.append(x)

print(json.dumps(result))