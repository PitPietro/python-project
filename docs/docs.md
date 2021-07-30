# Docs
This `docs.md` file it temporary. 

## Avoid errors

### Recursive functions

If the compiler (or the user) try to call a *recursive function* passing as parameter a huge number, it will get
self `RecursionError: maximum recursion depth exceeded in comparison`. Python stop calling recursive function
after `1000` calls by default. To avoid this error, you need to **import** the *[sys](#sys)* module and write the
following line on top of the classes that implements recursive functions:

```python
import sys

sys.setrecursionlimit(3000)
```

Reference: [maximum-recursion-depth-exceeded-in-comparison](https://stackoverflow.com/questions/20034023/maximum-recursion-depth-exceeded-in-comparison)

## Resolve problems

### Import problem

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