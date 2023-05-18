#!/bin/bash

echo "create virtual env for python"
pip3 install virtualenv
python3 -m venv venv
echo "activation virtualenv"
. ./venv/bin/activate

if [ -f "requirements.txt" ]; 
then

# if file exist the it will be printed 
echo "File is exist"
pip3 install -r requirements.txt
else

# is it is not exist then it will be printed
echo "File is not exist"
fi

pytest  --html=index.html --self-contained-html