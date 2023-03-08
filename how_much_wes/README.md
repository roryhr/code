# How Much Wes

# Getting the data

Download trailers from YouTube.

```
from pytube import YouTube

def download_youtube(url):
    yt = YouTube(url)

    (yt.streams
        .filter(progressive=True, file_extension='mp4')
        .order_by('resolution')
        .desc()
        .first()
        .download()
    )

```

Use ffmpeg to convert movies to images

`ffmpeg -i FANTASTIC\ MR\ FOX\ -\ Official\ Theatrical\ Trailer.mp4 -r 1 -f image2 fantastic_mr_fox/fantastic_mr_fox-%04d.jpeg`

Model training follows the Keras example of training a binary model on very little data
https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

# Google App Engine Notes

Original runtime is Python 3.6. The minimum runtime App Engine accepts is 3.7.

If `entrypoint` is not defined in app.yaml, App Engine will look for an app
called `app` in `main.py`.

```
conda create -n new_wes python=3.8 keras flask pandas scikit-learn matplotlib h5py pillow requests tensorflow jupyter

```

For tests

```
conda install pytest
```

# Docker

Needs 1GB of memory to build and run.

```
docker build --tag slim-wes .
docker run --publish 8080:8080 slim-wes
```

TensorFlow was using 800MB of memory so I ported this to TensorFlow Lite so I can stay on the free tier of Fly.
