#!/usr/bin/env bash

# Note: it makes a difference if there is a "__init__.py" is the source dir directory !!!

cd $(dirname $0)

sphinx-apidoc -f -o . ../../../src/mframework/
# sed -i -e '1,3d' modules.rst

