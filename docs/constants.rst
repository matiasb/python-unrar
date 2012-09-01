:mod:`constants` --- constants used by the UnRAR library
========================================================

.. module:: constants
   :synopsis: Constants values used by unrarlib
.. moduleauthor:: Matías Bordese <mbordese@gmail.com>
.. sectionauthor:: Matías Bordese <mbordese@gmail.com>

:strong:`General`

| :mod:`constants`.SUCCESS = 0


:strong:`Open Modes`

| :mod:`constants`.RAR_OM_LIST = 0
| :mod:`constants`.RAR_OM_EXTRACT = 1
| :mod:`constants`.RAR_OM_LIST_INCSPLIT = 2


:strong:`Processing operations`

| :mod:`constants`.RAR_SKIP = 0
| :mod:`constants`.RAR_TEST = 1
| :mod:`constants`.RAR_EXTRACT = 2
| :mod:`constants`.RAR_CANCEL_EXTRACT = -1


:strong:`Errors`

| :mod:`constants`.ERAR_END_ARCHIVE = 10
| :mod:`constants`.ERAR_NO_MEMORY = 11
| :mod:`constants`.ERAR_BAD_DATA = 12
| :mod:`constants`.ERAR_BAD_ARCHIVE = 13
| :mod:`constants`.ERAR_UNKNOWN_FORMAT = 14
| :mod:`constants`.ERAR_EOPEN = 15
| :mod:`constants`.ERAR_ECREATE = 16
| :mod:`constants`.ERAR_ECLOSE = 17
| :mod:`constants`.ERAR_EREAD = 18
| :mod:`constants`.ERAR_EWRITE = 19
| :mod:`constants`.ERAR_SMALL_BUF = 20
| :mod:`constants`.ERAR_UNKNOWN = 21
| :mod:`constants`.ERAR_MISSING_PASSWORD = 22


:strong:`Comments`

| :mod:`constants`.RAR_NO_COMMENTS = 0
| :mod:`constants`.RAR_COMMENTS_SUCCESS = 1


:strong:`Host OS`

| :mod:`constants`.RAR_DOS = 0
| :mod:`constants`.RAR_OS2 = 1
| :mod:`constants`.RAR_WIN = 2
| :mod:`constants`.RAR_UNIX = 3
