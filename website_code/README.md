# Website Code

Here's the code and content for my static website hosted on Github. 
I use the Pelican to generate HTML from the markdown files. 

## Quick Start

Start a local server that watches the `content/` and sends HTML to the `output/` folder. 

```commandline
conda activate py39 
pip install "pelican[markdown]"
   
make dev
```
Browse at http://localhost:8000/


The output HTML is another Github repo
https://github.com/roryhr/roryhr.github.io
