#!/usr/bin/env bash

set -e

export PATH=/opt/python/bin:/opt/phantomjs/bin:$PATH

venv="virtualenv"
venv_command='virtualenv --no-site-packages '

if [ ! -d ${venv} ]; then
  echo "############################ Create virtualenv ############################"
  rm -rf ${venv}
  ${venv_command} ${venv}
  source ${venv}/bin/activate
  pip install -r requirements.txt
fi

echo "############################ Run tests ############################"
source ${venv}/bin/activate
./run_integration_tests.sh
