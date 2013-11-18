#! /bin/bash

set -e
set -x

pushd dependencies/unrar/
make lib
popd

export UNRAR_LIB_PATH=./dependencies/unrar/libunrar.so
PYTHONPATH=unrar python -m unittest discover -s unrar/
