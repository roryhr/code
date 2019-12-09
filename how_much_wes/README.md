# How Much Wes

This app lives at https://how-much-wes.herokuapp.com/

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
