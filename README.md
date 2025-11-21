# Group 7 Project: Search and Rescue

We are using ROS2 Humble and Gazebo Fortress to simulate a rescue scenario using an autonomous lidar-equipped robot.

## Build Steps
Building the ROS package (scout_controller)
```
colcon build --symlink-install
source install/setup.bash
```
Running the launch file
```
ros2 launch scout_controller gazebo_with_bridge.launch.py
```

Running the Wander Node
```
ros2 run scout_controller wander_node
```

Running the ROS2 to Gazebo bridge
```
ros2 run ros_gz_bridge parameter_bridge   /scan@sensor_msgs/msg/LaserScan@ignition.msgs.LaserScan   /cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist /model/vehicle/odometry@nav_msgs/msg/Odometry@gz.msgs.Odometry
```

Running Gazebo
```
ign gazebo -r -v 4 worlds/enclosed.sdf
```

## Miscellaneous Debug
Running rviz (ROS2 Visualizer)
```
rviz2
```
