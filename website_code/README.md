# Website Code

Here's code for my static website that is hosted on Github. 
I use the Pelican to generate the html from markdown files. 

## Quick Start

Start a local server that watches the `content/` and sends HTML to the `output/` folder. 

```commandline
conda activate py39 
 pip install "pelican[markdown]"
   
make dev
```
Browse at http://localhost:8000/



The output is hosted in a separate git repo at 
https://github.com/roryhr/roryhr.github.io

