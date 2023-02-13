"""How much Wes Anderson?

Run it locally:
$ flask --app main --debug run

Access at http://localhost:5000/
"""
import logging
import os
import pickle
from pathlib import Path

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
from tensorflow.keras import utils
from tensorflow.keras.applications.vgg16 import preprocess_input
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".gif"}

logging.info("creating flask app")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "tmp"


def allowed_file(filename):
    return Path(filename).suffix in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    print("App route index")

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
            return redirect(url_for("wes_probability", filename=filepath))
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
    print("loading pickled vgg")

    with open("vgg_model.pickle", "rb") as f:
        model = pickle.load(f)

    img = utils.load_img(img_path, target_size=(224, 224))
    x = utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    features = model.predict(x)
    df = pd.DataFrame(data=features.ravel()).transpose()
    return df


def predict(image_file):

    logging.info("loading picled models")

    with open("rf_classifier_2023.pickle", "rb") as f:
        clf = pickle.load(f)
    features_df = vgg_features(image_file)
    probability = clf.predict_proba(features_df)
    return probability[0][1]


@app.route("/wes_probability/<filename>")
def wes_probability(filename):
    """Load image and render html result"""
    if filename in ["wes_image_1.jpg", "grand_budapest_hotel-0136_cropped.jpg"]:
        filepath = os.path.join("static", filename)
    else:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    proba = round(predict(filepath), 2)
    result = f"{int(100*proba)}% Wes Anderson"
    return render_template(
        "wes_result.html",
        image_link=filename,
        result=result,
    )


# if __name__ == "__main__":
#     print(predict("static/grand_budapest_hotel-0136_cropped.jpg"))
