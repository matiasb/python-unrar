python-unrar
============

Work with RAR archive files through unrar library using ctypes.

[![Build Status](https://travis-ci.org/matiasb/python-unrar.png?branch=master)](https://travis-ci.org/matiasb/python-unrar)


Install UnRAR library
---------------------

python-unrar requires UnRAR library. You can download UnRAR library sources from:

    http://www.rarlab.com/rar_add.htm

and compile (you may need to rename the makefile that you want to use according to your OS) and install it from there:

    $ make lib
    $ make install-lib

(current sources: http://www.rarlab.com/rar/unrarsrc-5.0.7.tar.gz)

For Windows you can also download the already compiled library (http://www.rarlab.com/rar/UnRARDLL.exe).

If you prefer not to install the library, you should make it "findable" by adding the library file to a directory where libraries are searched (or change required environment variable).

As an alternative, you can also set UNRAR_LIB_PATH variable in your environment to the library path and python-unrar will try to load the UnRAR library from there.


Install python-unrar
--------------------

To install python-unrar:

    $ pip install unrar


Examples
--------

    >>> from unrar import rarfile
    >>> rar = rarfile.RarFile('sample.rar')
    >>> rar.namelist()
    [u'test_file.txt']
    >>> rar.printdir()
    File Name                                             Modified             Size
    test_file.txt                                  2013-04-14 08:20:28           17
    >>> rar.testrar()
    >>> info = rar.infolist()[0]
    >>> info.filename
    u'test_file.txt'
    >>> info.file_size
    17L
    >>> info.date_time
    (2013L, 4L, 14L, 8L, 20L, 28L)
    >>> rar.extractall()


Docs
----

Check full documentation in http://python-unrar.readthedocs.org.
