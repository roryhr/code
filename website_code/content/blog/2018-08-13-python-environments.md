Title:  Python Environments
Date:   2018-08-13
Category: python, miniessays

1. Why should I care about environments?
2. How do I manage environments? 
3. Demo

# Why should I care about environments?

Suppose you work on two projects, one is old and written in Python 2, the other is new and uses Python 3. 
The only way to work on this pair of projects is with a pair of `Python.exe`s and their respective packages.
Environments let you work with different Python interpreters.

Even for different projects in the same Python version (let's assume 3) you can have packages with differing dependencies. Smaller and specialized packages may need a specific version of numpy that, say, Pandas doesn't support.
The approach is to separate the package requirements by project -- only install what you need for a given project.
Environments let you isolate dependencies.

Bob just joined a project that Alice is maintaining. Bob runs the code and pip installs packages that he sees in the code but it doesn't work. Alice responds, "It works for me!"
Environments can be copied exactly. 
This way Bob will have the exact same packages as Alice and everything will work. 

# How do I manage environments? 

1. virtualenv
2. pipenv
3. conda
4. manually

All of these basically boil down to the same formula: put everything you need in a folder. That's it!
If you don't trust me and want to do it manually -- knock yourself out. 

# Demo

I use `conda` which is both a package manager and virtual enviornment manager. 
Since `conda` also supports R it's a popular choice in data science circles. 
`pipenv` is popular among developers.

The Anaconda Python/R Distribution is a collection of packages that Anaconda.com curates.
It includes the hits like `Pandas`, `matplotlib`, `requests`...

1. Install conda and anaconda https://www.anaconda.com/download

2. run `$ conda` do a `$ which python` and convince yourself that everything is okay

3. Now let's make a new environemtn for web development. It needs `pelican` and `markdown`.

4. `$ conda create -n web_env pelican markdown`


```
$ conda create -n web_env pelican markdown
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - pelican
```

Not to worry! We can make an environment and then pip install whatever we can find on conda.


```
$ conda create -n web_env python=3
```

```
$ source activate web_env
(web_env) $ pip install pelican markdown
```

Check out our handiwork and save our dependencies. 
```
$ conda list
$ pip freeze > requirements.txt
```

And that's about all there is to it!
