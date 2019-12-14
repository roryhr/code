"""Reder donuts_template.html using data from Facebook.

Loads photo album metadata and links to images. Renders
donut_template.html using Jinja2. 

"""
import json
import os
from jinja2 import Template
from datetime import datetime
from pathlib import Path
import pandas as pd


def leaflet_json(points_df, output_file='output/map_data.json'):
    """Generate GeoJSON object to render with Leaflet.js
    
    Needs latitude, longitude, and title for each marker.
    """
    points_df = points_df.dropna(subset=['longitude', 'latitude'])
    point_list = []
    for point in points_df.itertuples():
        x = {
            'properties': {                                                
                'popupContent': point.name,
                'description': point.description,
            },
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [point.longitude, point.latitude]
            },
        }
        point_list.append(x)

    result = {
        'type': 'FeatureCollection',
        'features': point_list
    }
    
    with open(output_file, 'w') as f:
        json.dump(result, f)


# Link file name to relative path in donuts/ so just Donutselfies_bMxPRLTyVg
donut_selfies_path = '/Users/rory/public_code/website_code/content/images/donuts/Donutselfies_bMxPRLTyVg'
p = Path(donut_selfies_path)
image_paths = {
    # path.name: path.absolute()
    path.name: os.path.join(*path.parts[-2:])
    for path
    in p.glob('*.jpg')
}

def render_template(photos_df, output_file='output/donuts.html'):
    """Populate data to render donuts_template.html.

    Parameters
    ----------
    photos_df : pandas.core.frame.DataFrame
        DataFrame of photos

    Returns
    -------
    donuts: list
        List of donuts for donuts_template.
    """
    donuts = []
    for photo in photos_df.itertuples():
        p = Path(photo.uri)
        dt = datetime.fromtimestamp(photo.creation_timestamp)
        x = {                                                
            'title': photo.name,
            'text': photo.description,
            'created_at': dt.strftime('%Y-%m-%d'),
            'url': image_paths.get(p.name),
            'creation_timestamp': photo.creation_timestamp
        }
        donuts.append(x)
    
    sorted_donuts = sorted(donuts, key=lambda x: x['creation_timestamp'], reverse=True)

    with open('donuts_template.html') as f:
        template = Template(f.read())

    html_text = template.render(donuts=sorted_donuts)

    with open(output_file, 'w') as f:
        f.write(html_text)


def main():
    df = pd.read_csv('donut_album.csv')

    leaflet_json(df.copy())
    render_template(df)


if __name__ == '__main__':
    main()

