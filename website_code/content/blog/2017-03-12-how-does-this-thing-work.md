Title:  How does this thing work?
Date:   2017-03-12
Category: python, documentation

Updated: 2022-12-12

Added a `requirements.txt` to capture dependencies and ported to MacOS. 

Updated: 2024-09-19
entry-point is the Makefile 

# Introduction

After 9 months I'm returning to this website.
My first question was "How does this thing work?"
Of course, I didn't document it and I don't remember. Lesson learned.

**The things we take for granted are the most important to document.**

This post is for myself and anyone interested in using Pelican to make a Github-hosted website.

# How does this thing work?

## High level overview

This site is hosted for free by [GitHub](https://github.com/) from the special repository [roryhr/roryhr.github.io](https://github.com/roryhr/roryhr.github.io). 
Thanks, GitHub!

I used a static site generator called Pelican that generates html, which comprises this website, from Markdown text files in a particular directory structure (more on that in a bit).
These files are in a separate repository at
[roryhr/code/website_cost](https://github.com/roryhr/code/tree/master/website_code).

## Recipes

Content for the website goes in the `content` directory. 
Generate the website

	:::bash
	(py39) ~/p/website_code> pelican content
	Done: Processed 13 articles, 0 drafts, 4 pages, 0 hidden pages and 0 draft pages in 0.85 seconds.

The output html goes to the `output` directory which gets pushed to `roryhr.github.io` repo.

	:::bash
	((blog)) rory@rory-Satellite-S75-B:~/Projects/site-code/output$ git status
	On branch master
	Your branch is up-to-date with 'origin/master'.
	Changes not staged for commit:
	  (use "git add <file>..." to update what will be committed)
	  (use "git checkout -- <file>..." to discard changes in working directory)

		modified:   archives.html
		modified:   author/rory-hartong-redden.html
		modified:   authors.html
		modified:   category/opinion.html

	Untracked files:
	  (use "git add <file>..." to include in what will be committed)

		how-does-this-thing-work.html

	no changes added to commit (use "git add" and/or "git commit -a")
	((blog)) rory@rory-Satellite-S75-B:~/Projects/site-code/output$ git remote -v
	origin	https://github.com/roryhr/roryhr.github.io (fetch)
	origin	https://github.com/roryhr/roryhr.github.io (push)
	((blog)) rory@rory-Satellite-S75-B:~/Projects/site-code/output$

### Development

In `pelicanconf.py` enable relative URLs by setting `RELATIVE_URLS=True` and comment out `ANALYTICS`. 
Neither are necessary.

Take advantage of Pelican script to recompile the site as you edit it (very cool!).

Across my various projects I like to have a consistent make entrypoint because remembering the particulars of Pelican, Flask, Django across different versions is hard.
```bash
(py39) ~/p/website_code> make dev
```
In this case that command is 

```commandline
source activate py39 && pelican --listen --autoreload --relative-urls
```

Navigate to `http://localhost:8000`


# Repository contents


	:::bash
	site-code/
		content/
			blog/
				blog-posts-go-here.md
			images/
				images-go-here.jpg
				and-other-static-files.html
			pages/
				about.md
				contact.md
				index.md
				projects.md
		output/
			index.html
			lots of other html files
		LICENSE
		pelicanconf.py  
		README.md

## Wiring the site up

I made a custom landing page with `pages/index.md` which becomes `index.html`

	:::python
	title:
	save_as: index.html

	Thanks for stopping by my little website.

	-- Rory Hartong-Redden

In `site-code/pelicanconf.py` I wire up the buttons so they're labeled and go to the appropriate place (this took some fiddling).

	:::python
	MENUITEMS = [('Home', '/'),
	             ('Articles', '/archives'),
	             ('About', '/pages/about'),
	             ('Projects', '/pages/projects'),
	             ('Contact', '/pages/contact')]
