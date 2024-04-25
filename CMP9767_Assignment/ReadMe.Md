LIMO Robot pothole Detector/Counter


Installing ROS2 Humble desktop
    https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

Installing LIMO Simulation native
    https://github.com/LCAS/CMP9767_LIMO/wiki/Simulator-Setup
	
Source the limo robot
	
	1. cd limo_ros2
	2. source install/setup.bash

Build and Source the Packege
    1. Build the packege
        cd ~/ros2_ws
        colcon build
    2. Source the packege
        source install/setup.bash

Launch the world map

    1. Pothole simple world
        ros2 launch limo_gazebosim limo_gazebo_diff.launch.py world:=src/limo_gazebosim/worlds/potholes_simple.world 


ROS2 Commands to launch nodes

    ros2 run pothole_detector moveCar
    ros2 run pothole_detector detectPothole
    ros2 run pothole_detector countPothole

Summary

In summary, we have 3 nodes to move the robot, detect and count potholes. Firstly, the moveCar uses rclpy component to move the car and turns right or left by detecting obstacles using laser scan. Secondly, the detect potholes utilizes color segmentation to detect potholes and identifies its coordinates. Moreover, the countPothole stores these coordinates to avoid counting same potole twice and displays the unique potholes count on terminal.


