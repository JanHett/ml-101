# Python environment setup

> This section is specifically about the system environment and ecosystem around Python. If you want to learn about the language, check out [the official Python site's compilation of resources](https://www.python.org/about/gettingstarted/).
> 
> Please note that we are using Python 3 - it is similar, but not identical to the recently obsoleted Python 2.

## Python installation

You can install Python from the official website or via `brew install Python` on macOS.

## The ecosystem

The Python ecosystem works a little differently than JS's does.

First, let's start with similarities:

- there is a package repository like NPM, called [PyPi](https://pypi.org/)
- there is a package manager like `npm` or `yarn` called `pip` (and it even comes with most Python installations)
- there are packages for nearly everything you could want to do
- there is a way to install packages for just a single project

That last point, however, is where the differences start: package installations are global by default - in fact, Python packages tap heavily into the system environment (think installing a C library) and making them not global is a bit of a challenge. To help us with that we need...

## Virtual environments

Python comes with [a utility called `venv`](https://docs.python.org/3/tutorial/venv.html). It allows setting up an environment within which you can link your packages at will without polluting the global environment. However, using it for larger projects is a bit of a pain, therefore [we are using `pipenv`](https://pipenv.pypa.io/en/latest/).

With this knowledge in hand, let's dive in!

### Installing pipenv

Assuming you have Python and pip installed you can get pipenv by running `pip install --user pipenv`. This will install pipenv for your user on your machine.

### Creating a virtual environment

With pipenv at the ready we can go ahead and create our first virtual environment. Navigate to the `playground` directory of this module and run

```sh
pipenv install numpy
```

This will both create a virtual environment and install the `numpy` package - which is to ML what `express` is to server development in JS. You'll notice a `Pipfile` and a `Pipfile.lock` appeared - they're the `package.json` and `yarn.lock` of Pythonland.

Now that we have an environment within which to work, let's go ahead and play!

### Using the virtualenv's packages in scripts

You won't be able to use `numpy` yet because you are still "outside" the virtual environment. To get "inside", run `pipenv shell`.

Go ahead and check if you can run the `deep_thought.py` script.

If you do not get an error, your virtual environment is working and activated (you'll also notice that by using `numpy` we can get the calculation time of The Answer from 7.5 million years down to a few milliseconds).

## Notebooks

Scripts are cool and all, but ML is about data so we want tables and graphs and cool layouts to show off our oh-so-perfect f-scores. And ideally we want all of that close to our code without having to set up something hugely complicated.

Luckily, there's a py-thing for that: [Jupyter Notebooks](https://jupyter.org/). Admittedly they aren't Python-specific, but they do work with Python.

### The VS Code Python extension

The easiest way to work with notebooks is by using the [VS Code Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python). Go ahead and install it before we continue.

With this extension, you can open the Jupyter notebook titled `scrabble.ipynb`. It contains instructions for how to use it.
