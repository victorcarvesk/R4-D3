import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    
    package_name = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
    package_path = get_package_share_directory(package_name)
    
    rviz_config_arg = DeclareLaunchArgument(
        name='rviz_config',
        description='A display config file (.rviz) to load',
        default_value='r4d3.rviz',
        )
    
    rviz_config_file = LaunchConfiguration('rviz_config')
    
    rviz_config_file = PathJoinSubstitution([
        package_path, 'rviz', rviz_config_file
        ])
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        )
    
    tags = ['arg', 'node', 'launch']

    ld = LaunchDescription()

    entities = locals().copy()

    for entity in entities:
        if any(tag in entity for tag in tags):
            ld.add_action(eval(entity, locals()))
    
    return ld