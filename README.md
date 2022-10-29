# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This is an algorithm to convert bitmap images to lowpoly images using Delaunay Triangulation.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Python
Pip
```

### Installing

There should be 2 folders, input and output, if not, create input and then put any images you want to convert in it.

This algorithm accepts any bitmap image format and it may take up to several hours to complete the task.

First you have to install project dependencies it can be found on `requirements.txt` file and can be installed with:

```
    $ pip install -r requirements.txt
``` 

To run the code you have 2 alternatives convert one image or convert more all at once.


To convert one:
```
    python low_poly.py "image-name.png"
```
To convert more, first you need to rename all images to numbers from 1 to whatever quantity you want, then open run.sh and change the `15` from `i < 15` to the total number of images to iterate, feel free to modify this script as you need:
```
    sh run.sh
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Add notes about how to use the system.
