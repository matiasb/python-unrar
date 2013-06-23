#! /bin/bash

set -e
set -x

pushd unrar-src/unrar/
make lib
popd

export UNRAR_LIB_PATH=./unrar-src/unrar/libunrar.so
PYTHONPATH=unrar python -m unittest discover -s unrar/
