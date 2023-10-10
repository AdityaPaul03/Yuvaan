# Autonomous navigation mission of Yuvaan IITG Mars Rover

## Prerequisites
- Have Ubuntu and ROS installed

## Cloning the repo
From home directory create /yuvaan_ws/src folder and run the following command
```
mkdir -p yuvaan_ws/src
cd yuvaan_ws/src
git clone https://github.com/ritesh27gole/yuvaan_autonomous.git
```

## Updating Dependencies
```
cd ~/yuvaan_ws
rosdep update
rosdep install --from-paths src --ignore-src -r -y --rosdistro noetic
```

## Installing Controllers For Robot
```
sudo apt-get update
sudo apt-get install ros-noetic-ros-controllers
```


## Building package
First build the project and source the setup file so that the system knows where to look for your build files
Note that package name is "mobrob" and not "yuvaan"
```
cd ~/yuvaan_ws
catkin_make
source devel/setup.bash
```

## Launch the robot
```
roslaunch mobrob yuvaan.launch
```

# Commit to this repository

Go to ~/yuvaan_ws/src/<your directory name> and run this commands in terminal
```
git status
git add .
git status
git commit -m "type your message here"
git push
```
