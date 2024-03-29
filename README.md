# README #

To get and use this repository, please install [Mercurial](https://mercurial.selenic.com/) and [Python](https://www.python.org/) first. You may then use the following commands:

    clone https://bitbucket.org/stephen-paul-chappell/qtpipe
    cd qtpipe
    echo Hello World | qtpipe.py

### What is this repository for? ###

* This repository is designed to hold code for the QTpipe utility. The QTpipe utility is designed to pipe data over network connections. This allows data to be piped across two terminal sessions either on the same computer or somewhere on a common network.
* The latest version of QTpipe is 1.0.2 and can be found in the source of the `qtpipe.py` file.
* If you wish to contribute to this README file and are unfamiliar with [Markdown](http://daringfireball.net/projects/markdown/), please consider [learning markdown](https://bitbucket.org/tutorials/markdowndemo) before attempting to contribute.

### How do I get set up? ###

* To get this repository on your computer, you will need [Mercurial](https://mercurial.selenic.com/) installed. Once complete, you should be able to issue the following command wherever you want the repository located: `clone https://bitbucket.org/stephen-paul-chappell/qtpipe`
* To run `qtpipe.py`, you will need [Python](https://www.python.org/) installed. Please note that there are two versions of Python in popular use, Python 2 and Python 3. QTpipe is currently designed for use with Python 3.
* QTpipe has no dependencies beyond Python's standard library that comes bundled with its installation. Once Python 3 is installed, this utility should work without need for changes.
* There are several settings at the top of `qtpipe.py` that may be changed if needed. In particular `DEFAULT_HOST` and `DEFAULT_PORT` may be set to other values if appropriate.
* To test the program to see if it is working properly, open two terminals on the same computer and pipe data into one and out of the other. You may also do the same across a network by specifying the appropriate command line arguments.
* You may deploy the program as-is across a network as long as Python 3 is installed on the target machines. For development, [PyCharm](https://www.jetbrains.com/pycharm/) is supported by making use of the `.idea` directory in the repository.

### Contribution guidelines ###

* Feel free to write tests for this utility. Specifically, it has only been tested on Windows and should be tested to see if it works on other operating systems.
If you see any problems with the code or the style with which it was written, please provide a code review stating the deficiencies that you have found and how to fix them.
* This repository may be forked, and you are welcome to improve on the programming that has been provided. If you improve on what you find and would like to see it included here, you are welcome to make a pull request.

### Who do I talk to? ###

* [Stephen Chappell](mailto:Noctis.Skytower@gmail.com?subject=QTpipe)
* [Jacob Bridges](mailto:him@jacobandkate143.com?subject=QTpipe)