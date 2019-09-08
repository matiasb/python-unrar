:mod:`rarfile` --- Work with RAR archives
=========================================

.. module:: rarfile
   :synopsis: Read RAR-format archive files.
.. moduleauthor:: Matías Bordese <mbordese@gmail.com>
.. sectionauthor:: Matías Bordese <mbordese@gmail.com>

The RAR file format is a common archive and compression standard. This module
provides tools to read and list a RAR file.

This module is based on the UnRAR library (provided by `RARLAB <http://rarlab.com/>`_) through a ctypes wrapper, and inspired on Python's ZipFile.

The module defines the following items:

.. exception:: BadRarFile

   The error raised for bad RAR files.


.. class:: RarFile

   The class for reading RAR files.  See section
   :ref:`rarfile-objects` for constructor details.


.. class:: RarInfo

   Class used to represent information about a member of an archive. Instances
   of this class are returned by the :meth:`getinfo` and :meth:`infolist`
   methods of :class:`RarFile` objects.  Most users of the :mod:`rarfile` module
   will not need to create these, but only use those created by this
   module. *header* should be a RARHeaderDataEx instance as returned by :mod:`unrarlib`; the fields are described in section
   :ref:`rarinfo-objects`.


.. function:: is_rarfile(filename)

   Returns ``True`` if *filename* is a valid RAR file based on its magic number,
   otherwise returns ``False``.


.. seealso::

   `RARLAB`_
      Official RAR site.

   `RAR addons <http://www.rarlab.com/rar_add.htm>`_
      RAR addons where you can download UnRAR library sources.


.. _rarfile-objects:

RarFile Objects
---------------


.. class:: RarFile(file[, mode='r'])

   Open a RAR file, where *file* should be a path to a file (a string).   The *mode* parameter should be ``'r'`` to read an existing
   file (only allowed mode at the moment).

   RarFile is also a context manager and therefore supports the with statement.

.. versionadded:: 0.4
    Added the ability to use RarFile as a context manager.

.. method:: RarFile.getinfo(name)

   Return a :class:`RarInfo` object with information about the archive member
   *name*.  Calling :meth:`getinfo` for a name not currently contained in the
   archive will raise a :exc:`KeyError`.


.. method:: RarFile.infolist()

   Return a list containing a :class:`RarInfo` object for each member of the
   archive.  The objects are in the same order as their entries in the actual RAR
   file on disk if an existing archive was opened.


.. method:: RarFile.namelist()

   Return a list of archive members by name.


.. method:: RarFile.open(member[, pwd])

   Extract a member from the archive as a file-like object
   (see Python's :py:class:`io.BytesIO`).
   *member* is the name of the file in the archive, or a :class:`RarInfo` object.
   *pwd* is the password used for encrypted files.

   .. versionadded:: 0.3


.. method:: RarFile.read(name[, pwd])

   Return the bytes of the file *member* in the archive.  *member* is the name of the
   file in the archive, or a :class:`RarInfo` object. *pwd* is the password used for encrypted  files and, if specified, it will override the default password set with :meth:`setpassword`.

   .. versionadded:: 0.3


.. method:: RarFile.extract(member, path=None, pwd=None)

   Extract a member from the archive to the current working directory; *member*
   must be its full name or a :class:`RarInfo` object).  Its file information is
   extracted as accurately as possible.  *path* specifies a different directory
   to extract to.  *member* can be a filename or a :class:`RarInfo` object.
   *pwd* is the password used for encrypted files.


.. method:: RarFile.extractall(path=None, members=None, pwd=None)

   Extract all members from the archive to the current working directory.  *path*
   specifies a different directory to extract to.  *members* is optional and must
   be a subset of the list returned by :meth:`namelist`.  *pwd* is the password
   used for encrypted files.

   .. warning::

      Never extract archives from untrusted sources without prior inspection.
      It is possible that files are created outside of *path*, e.g. members
      that have absolute filenames starting with ``"/"`` or filenames with two
      dots ``".."``.


.. method:: RarFile.printdir()

   Print a table of contents for the archive to ``sys.stdout``.


.. method:: RarFile.setpassword(pwd)

   Set *pwd* as default password to extract encrypted files.


.. method:: RarFile.testrar()

   Read all the files in the archive and check their CRC's and file headers.
   Return the name of the first bad file, or else return ``None``.


The following data attribute is also available:


.. attribute:: RarFile.comment

   The comment text associated with the RAR file, if any.



.. _rarinfo-objects:

RarInfo Objects
---------------

Instances of the :class:`RarInfo` class are returned by the :meth:`getinfo` and
:meth:`infolist` methods of :class:`RarFile` objects.  Each object stores
information about a single member of the RAR archive.

Instances have the following attributes:


.. attribute:: RarInfo.filename

   Name of the file in the archive.


.. attribute:: RarInfo.date_time

   The time and date of the last modification to the archive member.  This is a
   tuple of six values:

   +-------+--------------------------+
   | Index | Value                    |
   +=======+==========================+
   | ``0`` | Year (>= 1980)           |
   +-------+--------------------------+
   | ``1`` | Month (one-based)        |
   +-------+--------------------------+
   | ``2`` | Day of month (one-based) |
   +-------+--------------------------+
   | ``3`` | Hours (zero-based)       |
   +-------+--------------------------+
   | ``4`` | Minutes (zero-based)     |
   +-------+--------------------------+
   | ``5`` | Seconds (zero-based)     |
   +-------+--------------------------+

   .. note::

      The RAR file format does not support timestamps before 1980.


.. attribute:: RarInfo.compress_type

   Type of compression for the archive member.


.. attribute:: RarInfo.comment

   Comment for the individual archive member.


.. attribute:: RarInfo.create_system

   System which created RAR archive.


.. attribute:: RarInfo.extract_version

   RAR version needed to extract archive.


..
    attribute:: RarInfo.reserved
    Must be zero.


.. attribute:: RarInfo.flag_bits

   RAR flag bits.


..
    attribute:: RarInfo.volume
    Volume number of file header.


.. attribute:: RarInfo.CRC

   CRC-32 of the uncompressed file.


.. attribute:: RarInfo.compress_size

   Size of the compressed data.


.. attribute:: RarInfo.file_size

   Size of the uncompressed file.

