#!/usr/bin/env bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ] ; do SOURCE="$(readlink "$SOURCE")"; done
SCRIPTDIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

export PYTHONWARNINGS="ignore"
cd "$SCRIPTDIR/.."

pip install -r ../requirements.txt