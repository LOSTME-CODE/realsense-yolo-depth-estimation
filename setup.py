from setuptools import setup

package_name = 'realsense_yolo'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='RealSense D435i with YOLO and Depth Estimation',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'realsense_yolo_node = realsense_yolo.realsense_yolo_node:main',
        ],
    },
)

