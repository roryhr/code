"""How much Wes Anderson?

Usage:
$ export FLASK_APP=main.py
$ flask run

Access at http://localhost:5000/
"""
import os
import pickle
from pathlib import Path

import keras
import numpy as np
import pandas as pd
from flask import (
    Flask,
    render_template,
    flash,
    request,
    redirect,
    url_for,
)
from keras import backend as K
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image
from werkzeug.utils import secure_filename

assert K.image_data_format() == "channels_last"

if os.environ.get("FLASK_ENV") == "development":
    from dotenv import load_dotenv

    load_dotenv()

ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".gif"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static"

model = VGG16(weights="imagenet", include_top=False)
small_model = keras.models.load_model("small_cnn_2.h5")

with open("rf_classifier_11_07_2019.pickle", "rb") as f:
    clf = pickle.load(f)


def allowed_file(filename):
    return Path(filename).suffix in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            return redirect(url_for("wes_probability", filename=filename))
    return render_template("index.html")


def vgg_features(img_path):
    """Compute VGG features

    Parameters
    ----------
    img_path : _io.BytesIO
        File path or Byte stream

    Returns
    -------
    df : pandas.core.frame.DataFrame
        DataFrame with 1 row of features
    """
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    features = model.predict(x)
    df = pd.DataFrame(data=features.ravel()).transpose()
    return df


@app.route("/predict")
def predict(image_file):
    features_df = vgg_features(image_file)
    probability = clf.predict_proba(features_df)
    return probability[0][1]


def predict_small_cnn(img_path):
    """Compute VGG features

    Parameters
    ----------
    img_path : _io.BytesIO
        File path or Byte stream

    Returns
    -------
     : float
        Probabillity it is Wes
    """
    img = image.load_img(img_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    proba = small_model.predict(x)
    return proba[0][0]


@app.route("/wes_probability/<filename>")
def wes_probability(filename):
    """Load image and render html result"""
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    proba = round(predict_small_cnn(filepath), 2)
    result = f"{int(100*proba)}% Wes Anderson"
    return render_template(
        "wes_result.html",
        image_link=filename,
        result=result,
    )


if __name__ == "__main__":
    print(predict())
