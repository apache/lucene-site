Title: Building PyLucene
URL: pylucene/install.html
save_as: pylucene/install.html
template: lucene/pylucene/page

## Building PyLucene

PyLucene is completely code-generated by JCC whose sources are included with the
PyLucene sources.

## Requirements

To build PyLucene a Java Development Kit is required; use of the resulting PyLucene binaries requires only a Java Runtime Environment (JRE).
A recent C/C++ compiler is also required.

**Attention:** Starting with release 9.x, Lucene requires Java 11 or above.<br/>
**Attention:** Starting with release 6.x, Lucene requires Java 1.8.

On macos and linux, the [Temurin JDK](https://adoptium.net/) is recommended.
See "Notes for Linux" at [this page](jcc/install.html) for installation instructions on Linux Debian 11.

On any system, if you're upgrading your Java installation, please rebuild
JCC as well. You must use the same version of Java for both JCC and PyLucene.

A modern version of setuptools is required for building JCC in shared mode.
See JCC's [installation instructions](jcc/install.html) for more information.

## For the Impatient Ones

- **pushd jcc**
- **edit _setup.py_ to match your environment**
- **python setup.py build**
- **sudo python setup.py install**
- **popd**
- **edit _Makefile_ to match your environment**
- **make**
- **make test** (look for failures)
- **sudo make install**

## For the Rest of Us

Before building PyLucene, JCC must be built first. See JCC's
[installation instructions](jcc/install.html) for building and installing it.

Once JCC is built and installed, PyLucene is built via _make_ which invokes JCC.
See PyLucene's _Makefile_ for configuration instructions.

There are limits to both how many files can fit on the command line and how large
a C++ file the C++ compiler can handle. By default, JCC generates one large C++
file containing the source code for all wrapper classes.

Using the --files command line argument, this behaviour can be tuned to workaround
various limits, for example:

- to break up the large wrapper class file into about 2 files:<br/>`--files 2`
- to break up the large wrapper class file into about 10 files:<br/>`--files 10`
- to generate one C++ file per Java class wrapped:<br/>`--files separate`

## Notes for Solaris 11 with Sun Studio C++ 12

PyLucene's Makefile is a GNU Makefile. Be sure to use _gmake_ instead of plain _make_.

Just as when building JCC, Python's distutils must be nudged a bit to invoke the
correct compiler. Sun Studio's C compiler is called _cc_ while its C++ compiler is
called _CC_.

To build PyLucene, use the following shell command to ensure that the C++ compiler
is used:<br/>`$ CC=CC gmake`

## Notes for Solaris 11.1 with GCC 4.5

PyLucene's Makefile is a GNU Makefile. Be sure to use gmake instead of plain make.

- Edit Makefile and do the following changes: Insert and enable a Solaris-Section
with the following content

```
\# Solaris   (Solaris 11.1, Python 2.6, 32-bit, Java 1.7)
PREFIX_PYTHON=/usr
ANT=/usr/bin/ant
PYTHON=$(PREFIX_PYTHON)/bin/python
JCC=$(PYTHON) -m jcc.\_\_main\_\_ --reserved DEFAULT_TYPE
NUM_FILES=4
```

- gmake
- su gmake install
