# Website Code

Here's the code and markdown for my static website hosted on GitHub. 
I use the [Pelican](https://getpelican.com/) static site generator to make HTML from the markdown files. 

## Quick Start
Start a local server that watches the `content/` folder and sends HTML to the `output/` folder. 

```commandline
conda activate py39 
pip install "pelican[markdown]"
   
make dev
```
Browse at http://localhost:8000/


The website is hosted from another GitHub [repo](https://github.com/roryhr/roryhr.github.io).
