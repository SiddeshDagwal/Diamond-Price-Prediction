#!/bin/bash
cd ~
sudo apt update
sudo apt install python3-pip -y
pip install flask
pip install sklearn
pip install xgboost
git clone https://B1_56602_Siddesh:SiddeshD@gitlab.com/b1_56602_siddesh1/project.git
cd project
python3 server.py