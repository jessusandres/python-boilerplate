#!/bin/bash

echo "* * * * * * * * STARTING CLOUD FUNCTION * * * * * * * *"

work_directory=`pwd`

# Rename the virtual environment according to your project
venv_name="boilerplate-venv"

echo "PWD directory: $work_directory"

#work_directory=$work_directory/lab/fb
#echo "work_directory: $work_directory"

venv_path="${work_directory}/${venv_name}"
executable_file="${venv_path}/bin/python"

echo "Python executable file: $executable_file"

if [ -f $executable_file ]
then
  echo "The python interpreter exists"

  echo "Using existing venv"
  source "${venv_path}/bin/activate"
else
  echo "The python interpreter does not exist"
  echo "Creating venv..."
  python3 -m venv $venv_name


  echo "Using new venv"
  source "${venv_path}/bin/activate"

  pip install -r requirements.txt
fi

PORT=8085 functions-framework-python --target main --debug
