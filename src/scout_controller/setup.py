from setuptools import find_packages, setup
from glob import glob   ###
import os               ###

package_name = 'scout_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),     ###
            glob(os.path.join('launch', '*.launch.py'))),   ###
        (os.path.join('share', package_name, 'description'),
            glob(os.path.join('description', '*.xacro'))),
        (os.path.join('share', package_name, 'config'),
            glob(os.path.join('config', '*.*'))),
        (os.path.join('share', package_name, 'worlds'),
            glob(os.path.join('worlds', '*.world'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shanj',
    maintainer_email='shanj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "wander_node = scout_controller.wander:main"
        ],
    },
)
