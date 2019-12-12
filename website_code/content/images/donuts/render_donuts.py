"""Reder donuts_template.html using data from Facebook.

Loads photo album metadata and links to images. Renders
donut_template.html using Jinja2. 

"""
import json
import os
from jinja2 import Template
from datetime import datetime
from pathlib import Path

with open('/Users/rory/data/facebook-3629808 (1)/photos_and_videos/album/4.json') as f:      
    album = json.load(f)

# JSON for donut_data.js
result = []
for photo in album['photos']:
    if photo.get('media_metadata').get('photo_metadata').get('latitude') is None:
        # print('Passing latitude')
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

with open('donut_map.json', 'w') as f:
    json.dump(result, f)
# print(json.dumps(result))


# Link file name to relative path images/donuts/Donutselfies_bMxPRLTyVg/
donut_selfies_path = '/Users/rory/public_code/website_code/content/images/donuts/Donutselfies_bMxPRLTyVg'
p = Path(donut_selfies_path)
image_paths = {
    path.name: os.path.join('images/donuts/Donutselfies_bMxPRLTyVg', path.name)
    for path
    in p.glob('*.jpg')
}

donuts = []
for photo in album['photos']:
    p = Path(photo['uri'])
    dt = datetime.fromtimestamp(photo['creation_timestamp'])
    x = {                                                
        'title': photo['description'].split('\n')[0],
        'text': photo['description'],
        'created_at': dt.strftime('%Y-%m-%d'),
        'url': image_paths.get(p.name),
        'creation_timestamp': photo['creation_timestamp']
    }
    donuts.append(x)
    
print(donuts[0])

template_file = '/Users/rory/public_code/website_code/content/images/donuts/donuts_template.html'
with open(template_file) as f:
    text = f.read()

sorted_donuts =  sorted(donuts, key=lambda x: x['creation_timestamp'], reverse=True)
template = Template(text)
html_text = template.render(donuts=sorted_donuts)

with open('donuts.html', 'w') as f:
    f.write(html_text)
