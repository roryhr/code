import json
from jinja2 import Template
from datetime import datetime
from pathlib import Path

with open('/Users/rory/data/facebook-3629808/photos_and_videos/album/0.json') as f:      
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

# print(json.dumps(result))


# For Jinja2

p = Path('/Users/rory/public_code/website_code/content/images/Donutselfies_10103384416189657/')
image_paths = {
    path.name: path.absolute()
    for path
    in p.glob('*.jpg')
}

donuts = []
for photo in album['photos']:
    p = Path(photo['uri'])

    x = {                                                
        'title': photo['description'].split('\n')[0],
        'text': photo['description'],
        'created_at': str(datetime.fromtimestamp(photo['creation_timestamp'])),
        'url': image_paths.get(p.name),
    }

    donuts.append(x)



template_file = '/Users/rory/public_code/website_code/content/images/donut_template.html'

with open(template_file) as f:
    text = f.read()

template = Template(text)
html_text = template.render(donuts=donuts)

with open('donuts.html', 'w') as f:
    f.write(html_text)
