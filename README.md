# Python structure

![GitHub repo size](https://img.shields.io/github/repo-size/PitPietro/python-project)
![GitHub](https://img.shields.io/github/license/PitPietro/python-project)

This repository contains all the tests about the topic I learn learning in Python, from the very first script I wrote.

## Notes

The slice needs to be properly rearranged in a `docs/` folder.

### Avoid errors

#### Recursive functions

If the compiler (or the user) try to call a *recursive function* passing as parameter a huge number, it will get
self `RecursionError: maximum recursion depth exceeded in comparison`. Python stop calling recursive function
after `1000` calls by default. To avoid this error, you need to **import** the *[sys](#sys)* module and write the
following line on top of the classes that implements recursive functions:

```python
import sys

sys.setrecursionlimit(3000)
```

Reference: [maximum-recursion-depth-exceeded-in-comparison](https://stackoverflow.com/questions/20034023/maximum-recursion-depth-exceeded-in-comparison)

### Resolve problems

#### Import problem

To solve any import problem, take a look at [Real Python](https://realpython.com/absolute-vs-relative-python-imports/)
page about the topic.

## Used modules

### sys

The [sys module](https://docs.python.org/3.6/library/sys.html) (Python 3.6) provides access to some variables used or
maintained by the interpreter and to functions that interact strongly with the interpreter.

### openpyxl

Working with Excel files.<br>

```bash
pip install openpyxl
```

### PyPDF2

Working with PDFs. It can only extract text.

```bash
pip install pypdf2
```

### Word Documents

Working with .docx files.

```bash
pip install python-docx
```

## Prerequisites

[PyCharm](https://www.jetbrains.com/pycharm/download/) or another Python IDE of your choose.

I also suggest you to install [Anaconda](https://www.anaconda.com) python package manager by following those links:

1. [Anaconda Installation](https://docs.anaconda.com/anaconda/install/)
2. [Configure a Conda virtual environment](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html)

## Installing

Clone the repository on your computer and test yourself the library:

```bash
git clone https://github.com/PitPietro/python-project.git
```

Move to the directory where is placed the file you want to execute and type:

```bash
python [file-name].py
# python hello-world.py

# or, in case you only need python3
python3 [file-name].py
# python3 hello-world.py
```

## Resources
- [astrotech.io](https://python.astrotech.io)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/PitPietro/python-project/tags).

## Author

**Pietro Poluzzi** - [PitPietro](https://github.com/PitPietro)\
See also the list of [contributors](https://github.com/PitPietro/python-project/contributors) who participated in this
project.
