"""How much Wes Anderson?

Run it locally:
$ flask --app main --debug run

Access at http://localhost:5000/
"""
import os
from pathlib import Path

import tensorflow as tf
from flask import (
    Flask,
    render_template,
    flash,
    request,
    redirect,
    url_for,
)
from tensorflow import keras
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".gif"}


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "tmp"

loaded_model = tf.keras.models.load_model("tuned_xception.keras")


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


def predict(image_file):
    img = keras.preprocessing.image.load_img(
        image_file,
        target_size=(150, 150),
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis

    predictions = loaded_model.predict(img_array)
    return float(predictions)


@app.route("/wes_probability/<filename>")
def wes_probability(filename):
    """Load image and render html result"""
    if filename in ["wes_image_1.jpg", "grand_budapest_hotel-0136_cropped.jpg"]:
        filepath = os.path.join("static", filename)
    else:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    score = round(100 * (predict(filepath)))
    result = f"This image is {score}% Wes Anderson"
    return render_template(
        "wes_result.html",
        image_link=filename,
        result=result,
    )