# Installation requirements

## Visual Studio Code (VSCode)

VSCode is an IDE (Integrated Development Environment). It's essentially a text or code editor, however, it supports developers with many features, such as code auto completion, code formatting, code versioning, etc.

Please go to [Visual Studio Code](https://code.visualstudio.com/) and download and install the latest version of VSCode to your computer.

## Python 3

We will be using Python 3 for our course (not Python 2 which is not compatible in some cases!).

If you have been working with Python before, you may already have a version installed. Please check that by running the following commands in a Terminal or Shell:

```
python --version
python3 --version
```

At least the second command should show a version of `3.6` or `3.7`. If it shows something like `python not found` or the version is only `2.x`, please go to [Python downloads](https://www.python.org/downloads/) and download and install Python `3.8.2`.

If you're using macOS and have Homebrew installed, you may be interested in installing Python using:

```
brew install python
```

## Pip

Pip is the default package manager for Python with which we will be installing libraries e.g. for extracting information from data or plotting graphs. It is usually installed together with Python itself but please check that the following commands use Python 3 versions:

```
pip --version
pip3 --version
```

## VSCode Python extension

Open your freshly installed VSCode and then open the `Extensions` view. You can find that button in the left menu bar (it consists of four square blocks). Then enter `python` into the search and install the Python extension by Microsoft. It may ask you to restart VSCode.

## Notes on why we're not using Jupyter Notebooks

Some of you may be familiar with Jupyter Notebooks. They have become very popular for all sorts of data science tasks, however, they are not the best fit for our project. In the end, we want to develop a script that runs a schedule in the background. Thus, we don't want to have a Jupyter Notebook running all the time. We could have started off using a Notebook but I thought I give you an intro to a development environment right away.
