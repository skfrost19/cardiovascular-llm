#!/bin/bash

# Create a conda environment or if not exists, create a virtual environment (python based)

# check if conda is installed
if command -v conda &> /dev/null
then
    echo "conda is installed"
    conda create -p myenv python=3.8 -y
    echo "\nRestart the terminal and run the following command to activate the environment\n"
    pip install -r requirements.txt
else
    echo "conda is not installed"
    python3 -m venv myenv
    source venv/bin/activate
    pip install -r requirements.txt
fi