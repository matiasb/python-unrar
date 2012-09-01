
python-unrar
============

Work with RAR archive files through unrar library using ctypes.


Install UnRAR library
---------------------

You can download UnRAR library sources from:

    http://www.rarlab.com/rar_add.htm

and compile (you may need to rename the makefile that you want to use according to your OS) and install it from there:

    $ make lib
    $ make install-lib

(current sources: http://www.rarlab.com/rar/unrarsrc-4.2.4.tar.gz)

For Windows you can also download the already compiled library (http://www.rarlab.com/rar/UnRARDLL.exe).

If you prefer not to install the library, you should make it "findable" by adding the library file to a directory where libraries are searched (or change required environment variable).

As an alternative, you can also set UNRAR_LIB_PATH variable in your environment to the library path and python-unrar will try to load the UnRAR library from there.
