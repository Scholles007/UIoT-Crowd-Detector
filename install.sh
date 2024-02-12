#!/bin/bash

# Install python3 
sudo apt-get update
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim
wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
sudo tar zxf Python-3.8.0.tgz
cd Python-3.8.0
sudo ./configure --enable-optimizations
sudo make -j 4
sudo make altinstall

# Install pip3 and stuff
sudo apt install python-pip3
pip3 install -r requirements.txt
virtualenv venv
source venv/bin/activate
wget -O ./crowd_detector/models/yolo.weights \
https://pjreddie.com/media/files/yolov3.weight


