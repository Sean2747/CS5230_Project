from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import EnvironmentVariable, PathJoinSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    # Use $HOME/ros2_ws/worlds/enclosed.sdf
    world_path = PathJoinSubstitution([
        EnvironmentVariable('HOME'),
        'ros2_ws',
        'worlds',
        'enclosed.sdf'
    ])

    #world_path = '/home/shanj/ros2_ws/src/scout_controller/worlds/enclosed.sdf'

    # Set LIBGL_ALWAYS_SOFTWARE=1 for software rendering
    set_libgl_env = SetEnvironmentVariable(
        name='LIBGL_ALWAYS_SOFTWARE',
        value='1'
    )

    # Launch Gazebo world
    gazebo = ExecuteProcess(
        cmd=[
            'ign', 'gazebo',
            '-r',
            '-v', '4',
            world_path
        ],
        output='screen'
    )

    # Start ros_gz_bridge parameter_bridge for your topics
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/scan@sensor_msgs/msg/LaserScan@ignition.msgs.LaserScan',
            '/model/vehicle/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/model/vehicle/odometry@nav_msgs/msg/Odometry@gz.msgs.Odometry',
            '/clock@rosgraph_msgs/msg/Clock@gz.msgs.Clock',
        ],
        output='screen'
    )

    return LaunchDescription([
        set_libgl_env,
        gazebo,
        bridge,
    ])
