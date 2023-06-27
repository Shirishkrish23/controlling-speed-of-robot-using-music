import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    package_name = 'articubot_one'

    audio_processing_node_executable = os.path.join(
        os.getcwd(), 'install', package_name, 'lib', package_name, 'audio_processing_node'
    )

    audio_playback_node_executable = os.path.join(
        os.getcwd(), 'install', package_name, 'lib', package_name, 'audio_playback_node'
    )

    ld = LaunchDescription()

    audio_processing_node = Node(
        package=package_name,
        executable=audio_processing_node_executable,
        name='audio_processing_node',
        output='screen'
    )

    audio_playback_node = Node(
        package=package_name,
        executable=audio_playback_node_executable,
        name='audio_playback_node',
        output='screen'
    )

    ld.add_action(audio_processing_node)
    ld.add_action(audio_playback_node)

    return ld
