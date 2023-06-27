from setuptools import setup

package_name = 'articubot_one'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tiredtaurus',
    maintainer_email='tiredtaurus@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'audio_processing_node = articubot_one.audio_processing_node:main',
            'robot_controller = articubot_one.robot_controller:main',
            'audio_playback_node = articubot_one.audio_playback_node:main',
            'robot_speed_subscriber = articubot_one.robot_speed_subscriber:main'

        ],
    },
)
