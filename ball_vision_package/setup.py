from setuptools import setup
import os
from glob import glob

package_name = 'ball_vision_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='A ROS 2 package for ball tracking using OpenCV and DepthAI',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ball_tracker = ball_vision_package.ball_tracker_node:main',
            'yolo_tracker = ball_vision_package.yolo_node:main'
        ],
    },
)

