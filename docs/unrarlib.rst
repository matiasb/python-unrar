:mod:`unrarlib` --- ctypes wrapper for UnRAR library
====================================================

.. module:: unrarlib
   :synopsis: Read RAR-format archive files.
.. moduleauthor:: Matías Bordese <mbordese@gmail.com>
.. sectionauthor:: Matías Bordese <mbordese@gmail.com>

The RAR file format is a common archive and compression standard. This module
provides a `ctypes <http://docs.python.org/library/ctypes.html>`_ wrapper for UnRAR library (provided by `RARLAB <http://rarlab.com/>`_).

Most of this information is extracted from RAR library documentation.

The module defines the following items:

.. exception:: UnrarException

   The error raised for possible library errors.


.. class:: RAROpenArchiveDataEx

    Class mapping the library RAROpenArchiveDataEx C struct::

        struct RAROpenArchiveData{
            char         *ArcName;
            wchar_t      *ArcNameW;
            unsigned int OpenMode;
            unsigned int OpenResult;
            char         *CmtBuf;
            unsigned int CmtBufSize;
            unsigned int CmtSize;
            unsigned int CmtState;
            unsigned int Flags;
            unsigned int Reserved[32];
        };

    Using the name fields described above you can access the respective
    values through an instance as they were instance attributes.

    See section :ref:`rar-archive` for details.


.. class:: RARHeaderDataEx

    Class mapping the library RARHeaderDataEx C struct::

        struct RARHeaderDataEx{
            char         ArcName[1024];
            wchar_t      ArcNameW[1024];
            char         FileName[1024];
            wchar_t      FileNameW[1024];
            unsigned int Flags;
            unsigned int PackSize;
            unsigned int PackSizeHigh;
            unsigned int UnpSize;
            unsigned int UnpSizeHigh;
            unsigned int HostOS;
            unsigned int FileCRC;
            unsigned int FileTime;
            unsigned int UnpVer;
            unsigned int Method;
            unsigned int FileAttr;
            char         *CmtBuf;
            unsigned int CmtBufSize;
            unsigned int CmtSize;
            unsigned int CmtState;
            unsigned int Reserved[1024];
        };

    See section :ref:`rar-headerdata` for details.


.. function:: dostime_to_timetuple(dostime)

    Convert an MS-DOS format date time to a Python time tuple.

.. function:: RAROpenArchiveEx(archive_data)

    Open RAR archive and allocate memory structures.   *archive_data* should be
    a pointer to an initialized :class:`RAROpenArchiveDataEx`.
    When it succeeds, it loads the archive information into *archive_data* and
    returns a handle identifying the open archive,
    to be used as argument to the other functions in the module.
    In case of error, it raises an UnrarException (you can confirm which the error was by checking :attr:`RAROpenArchiveDataEx.OpenResult`).

.. function:: RARCloseArchive(handle)

    Close RAR archive and release allocated memory. It must be called when
    archive processing is finished, even if the archive processing was stopped
    due to an error.

.. function:: RARReadHeaderEx(handle, header_data)

    Read header of file in archive.   *header_data* should be
    a pointer to an initialized :class:`RARHeaderDataEx`, that would get
    filled with the member details.

.. function:: RARProcessFile(handle, operation, dest_path, dest_name)

    Performs action and moves the current position in the archive to
    the next file. Extract or test the current file from the archive
    opened in :mod:`constants`.RAR_OM_EXTRACT mode. If the mode
    :mod:`constants`.RAR_OM_LIST is set,
    then a call to this function will simply skip the archive position
    to the next file.

    Possible operations are:

        :mod:`constants`.RAR_SKIP
            Move to the next file in the archive. If the
            archive is solid and :mod:`constants`.RAR_OM_EXTRACT mode was set
            when the archive was opened, the current file will
            be processed - the operation will be performed
            slower than a simple seek.

        :mod:`constants`.RAR_TEST
            Test the current file and move to the next file in
            the archive. If the archive was opened with
            :mod:`constants`.RAR_OM_LIST mode, the operation is equal to
            :mod:`constants`.RAR_SKIP.

        :mod:`constants`.RAR_EXTRACT
            Extract the current file and move to the next file.
            If the archive was opened with :mod:`constants`.RAR_OM_LIST mode,
            the operation is equal to :mod:`constants`.RAR_SKIP.
    
.. function:: RARSetPassword(handle, pwd)

    Set a password to decrypt files when processing.

.. function:: RARGetDllVersion( )

    Return library API version.

.. _rar-archive:

RAROpenArchiveDataEx
--------------------

.. class:: RAROpenArchiveDataEx(filename[, mode=constants.RAR_OM_LIST])

    Initialize a RAROpenArchiveDataEx instance to open *filename* using the
    indicated mode.    *mode* should be one of the possible open modes
    defined in :mod:`constants`.

.. attribute:: RAROpenArchiveDataEx.ArcName

    Input parameter, a string containing the archive name.

.. attribute:: RAROpenArchiveDataEx.ArcNameW

    Input parameter, a Unicode string containing the archive name or None if
    Unicode name is not specified.

.. attribute:: RAROpenArchiveDataEx.OpenMode

    Input parameter.

    Possible values:

    :mod:`constants`.RAR_OM_LIST
        Open archive for reading file headers only.

    :mod:`constants`.RAR_OM_EXTRACT
        Open archive for testing and extracting files.

    :mod:`constants`.RAR_OM_LIST_INCSPLIT
        Open archive for reading file headers only. If you open an archive
        in such mode, RARReadHeaderEx will return all file headers,
        including those with "file continued from previous volume" flag.
        In case of :mod:`constants`.RAR_OM_LIST such headers
        are automatically skipped.
        So if you process RAR volumes in :mod:`constants`.RAR_OM_LIST_INCSPLIT
        mode, you will
        get several file header records for same file if file is split between
        volumes. For such files only the last file header record will contain
        the correct file CRC and if you wish to get the correct packed size,
        you need to sum up packed sizes of all parts.

.. attribute:: RAROpenArchiveDataEx.OpenResult

    Output parameter.

    Possible values:

    :mod:`constants`.SUCCESS
        Success

    :mod:`constants`.ERAR_NO_MEMORY
        Not enough memory to initialize data structures

    :mod:`constants`.ERAR_BAD_DATA
        Archive header broken

    :mod:`constants`.ERAR_BAD_ARCHIVE
        File is not valid RAR archive

    :mod:`constants`.ERAR_UNKNOWN_FORMAT
        Unknown encryption used for archive headers
        
    :mod:`constants`.ERAR_EOPEN
        File open error

.. attribute:: RAROpenArchiveDataEx.CmtBuf

    Buffer for archive comments. Maximum comment size is limited to 64Kb.
    If the comment text is larger than the buffer size, the comment text will be truncated.

.. attribute:: RAROpenArchiveDataEx.CmtBufSize

    Input parameter which should contain size of buffer for archive
    comments.

.. attribute:: RAROpenArchiveDataEx.CmtSize

    Output parameter containing size of comments actually read into the
    buffer, cannot exceed :attr:`CmtBufSize`.

.. attribute:: RAROpenArchiveDataEx.CmtState

    Output parameter.

    Possible values:

    :mod:`constants`.RAR_NO_COMMENTS
        Comments not present

    :mod:`constants`.RAR_COMMENTS_SUCCESS
        Comments read completely

    :mod:`constants`.ERAR_NO_MEMORY
        Not enough memory to extract comments

    :mod:`constants`.ERAR_BAD_DATA
        Broken comment

    :mod:`constants`.ERAR_UNKNOWN_FORMAT
        Unknown comment format
        
    :mod:`constants`.ERAR_SMALL_BUF
        Buffer too small, comments not completely read

.. attribute:: RAROpenArchiveDataEx.Flags

    Output parameter. Combination of bit flags.

    Possible values:

        | 0x0001  - Volume attribute (archive volume)
        | 0x0002  - Archive comment present
        | 0x0004  - Archive lock attribute
        | 0x0008  - Solid attribute (solid archive)
        | 0x0010  - New volume naming scheme ('volname.partN.rar')
        | 0x0020  - Authenticity information present
        | 0x0040  - Recovery record present
        | 0x0080  - Block headers are encrypted
        | 0x0100  - First volume (set only by RAR 3.0 and later)

.. attribute:: RAROpenArchiveDataEx.Reserved

    Reserved for future use. Must be zero.


.. _rar-headerdata:

RARHeaderDataEx
---------------

.. class:: RARHeaderDataEx( )

    Initialize an empty RARHeaderDataEx instance, to be populated with the
    details returned by :func:`RARReadHeaderEx`.


.. attribute:: RARHeaderDataEx.ArcName

    Output parameter which contains a zero terminated string of the
    current archive name.  May be used to determine the current volume
    name.

.. attribute:: RARHeaderDataEx.FileName

    Output parameter which contains a zero terminated string of the
    file name in OEM (DOS) encoding.

.. attribute:: RARHeaderDataEx.Flags

    Output parameter which contains file flags:

        | 0x01 - file continued from previous volume
        | 0x02 - file continued on next volume
        | 0x04 - file encrypted with password
        | 0x08 - file comment present
        | 0x10 - compression of previous files is used (solid flag)

        | [bits 7 6 5]
        |       0 0 0    - dictionary size   64 Kb
        |       0 0 1    - dictionary size  128 Kb
        |       0 1 0    - dictionary size  256 Kb
        |       0 1 1    - dictionary size  512 Kb
        |       1 0 0    - dictionary size 1024 Kb
        |       1 0 1    - dictionary size 2048 KB
        |       1 1 0    - dictionary size 4096 KB
        |       1 1 1    - file is directory

    Other bits are reserved.

.. attribute:: RARHeaderDataEx.PackSize

    Output parameter means packed file size or size of the
    file part if file was split between volumes.

.. attribute:: RARHeaderDataEx.UnpSize

    Output parameter - unpacked file size.

.. attribute:: RARHeaderDataEx.HostOS

    Output parameter - operating system used for archiving:

        | :mod:`constants`.RAR_DOS
        | :mod:`constants`.RAR_OS2
        | :mod:`constants`.RAR_WIN
        | :mod:`constants`.RAR_UNIX


.. attribute:: RARHeaderDataEx.FileCRC

    Output parameter which contains unpacked file CRC. In case of file parts
    split between volumes only the last part contains the correct CRC
    and it is accessible only in :mod:`constants`.RAR_OM_LIST_INCSPLIT listing mode.

.. attribute:: RARHeaderDataEx.FileTime

    Output parameter - contains date and time in standard MS DOS format.

.. attribute:: RARHeaderDataEx.UnpVer

    Output parameter - RAR version needed to extract file.
    It is encoded as 10 * Major version + minor version.

.. attribute:: RARHeaderDataEx.Method

    Output parameter - packing method.

.. attribute:: RARHeaderDataEx.FileAttr

    Output parameter - file attributes.

.. attribute:: RARHeaderDataEx.CmtBuf

    File comments support is not implemented in the new DLL version yet.    Now :attr:`CmtState` is always :mod:`constants`.RAR_NO_COMMENTS.

.. attribute:: RARHeaderDataEx.CmtBufSize

    Input parameter which should contain size of buffer for archive
    comments.

.. attribute:: RARHeaderDataEx.CmtSize

    Output parameter containing size of comments actually read into the
    buffer, should not exceed :attr:`CmtBufSize`.

.. attribute:: RARHeaderDataEx.CmtState

    Output parameter.

    Possible values:

        :mod:`constants`.RAR_NO_COMMENTS
            Absent comments

        :mod:`constants`.RAR_COMMENTS_SUCCESS
            Comments read completely

        :mod:`constants`.ERAR_NO_MEMORY
            Not enough memory to extract comments

        :mod:`constants`.ERAR_BAD_DATA
            Broken comment

        :mod:`constants`.ERAR_UNKNOWN_FORMAT
            Unknown comment format

        :mod:`constants`.ERAR_SMALL_BUF
            Buffer too small, comments not completely read


.. seealso::

   UnRAR Manual
      :download:`UnRAR library manual <./unrar_manual.txt>`

   `RARLAB`_
      Official RAR site.

   `RAR addons <http://www.rarlab.com/rar_add.htm>`_
      RAR addons where you can download UnRAR library sources.
      Check source files to get more detailed information.
