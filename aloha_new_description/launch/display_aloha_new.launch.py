import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    aloha_new_description_pkg = get_package_share_directory('aloha_new_description')
    robot_description = os.path.join(aloha_new_description_pkg, 'urdf', 'aloha_new.urdf')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open(robot_description).read()}],
            output='screen'
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            # arguments=['-d', os.path.join(aloha_new_description_pkg, 'rviz', 'aloha.rviz')]
        )
    ])