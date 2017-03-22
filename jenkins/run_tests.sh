#!/usr/bin/env bash

set -e

export PATH=/opt/python/bin:/opt/phantomjs/bin:$PATH

venv="virtualenv"
venv_command='virtualenv -p /opt/python/bin/python2.7 --no-site-packages '

if [ ! -d ${venv} ]; then
  echo "############################ Create virtualenv ############################"
  rm -rf ${venv}
  ${venv_command} ${venv}
  source ${venv}/bin/activate
  pip install -r requirements.txt
  source ${venv}/bin/activate
  rm -rf linkchecker
  git clone https://github.com/linkcheck/linkchecker.git
  cd linkchecker
  python setup.py install
  rm -rf linkchecker
  cd -
fi

echo "############################ Run tests ############################"
source ${venv}/bin/activate
./run_integration_tests.sh
