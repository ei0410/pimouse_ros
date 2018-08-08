#!/bin/bash -xve

sudo pip install --upgrade pip
#sudo apt-get install -y python3-venv
#python3 -m venv env
#source ./env/bin/activate
#python -m pip install pip
pip install catkin_pkg
pip install empy
pip install pyyaml
pip install rospkg

cd ..
git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu14.04_server.git
cd ./ros_setup_scripts_Ubuntu14.04_server
bash ./step0.bash
bash ./step1.bash

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
source /opt/ros/indigo/setup.bash
catkin_init_workspace
cd ~/catkin_ws
catkin_make
