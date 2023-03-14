"""Donuts

Run it locally:
$ flask --app main --debug run

Access at http://localhost:5000/

Reder donuts_template.html using data from Facebook.

Loads photo album metadata and links to images. Renders
donut_template.html using Jinja2. 

Usage:
$ cd donut_reviews
$ python render_donuts.py
"""
import json
import os
from jinja2 import Template
from datetime import datetime
from pathlib import Path
import pandas as pd
from pathlib import Path
import secrets


from flask import (
    Flask,
    render_template,
)


app = Flask(__name__)
app.secret_key = secrets.token_hex()


def leaflet_json(points_df, output_file="output/map_data.json"):
    """Generate GeoJSON object to render with Leaflet.js
    
    Needs latitude, longitude, and title for each marker.
    """
    points_df = points_df.dropna(subset=["longitude", "latitude"])
    point_list = []
    for point in points_df.itertuples():
        x = {
            "properties": {
                "popupContent": point.name,
                "description": point.description,
            },
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [point.longitude, point.latitude],
            },
        }
        point_list.append(x)

    result = {"type": "FeatureCollection", "features": point_list}

    with open(output_file, "w") as f:
        json.dump(result, f)



p = Path("static")
image_paths = {
    # path.name: path.absolute()
    path.name: os.path.join(*path.parts[-3:])
    for path in p.rglob("*.jpg")
}


def make_data(photos_df):
    """Populate data to render donuts_template.html.

    Parameters
    ----------
    photos_df : pandas.core.frame.DataFrame
        DataFrame of photos

    Returns
    -------
    sorted_donuts : list
        List of donuts for donuts_template.
    """
    donuts = []
    for photo in photos_df.itertuples():
        p = Path(photo.uri)
        dt = datetime.fromtimestamp(photo.creation_timestamp)
        x = {
            "title": photo.name,
            "text": photo.description,
            "created_at": dt.strftime("%Y-%m-%d"),
            "url": image_paths.get(p.name),
            "creation_timestamp": photo.creation_timestamp,
        }
        donuts.append(x)

    sorted_donuts = sorted(donuts, key=lambda x: x["creation_timestamp"], reverse=True)

    return sorted_donuts


@app.route("/")
def index():
    df = pd.read_csv("donut_album.csv")

    data = make_data(df)
    print(data[0])
    return render_template("index.html", donuts=data)
