#!/usr/bin/env python3

# Author: Bishop Pearson

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import ThisLaunchFileDir
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
  omo_r1mini_mcu_parameter = LaunchConfiguration(
    'omo_r1mini_mcu_parameter',
    default=os.path.join(
      get_package_share_directory('omo_r1mini_bringup'),
      'param/omo_r1mini_mcu.yaml'
    )
  )

  use_sim_time = LaunchConfiguration('use_sim_time', default='false')

  omo_r1mini_description_dir = LaunchConfiguration(
    'omo_r1mini_description_dir',
    default=os.path.join(
      get_package_share_directory('omo_r1mini_description'),
      'launch'
    )
  )

  rplidar_dir = LaunchConfiguration(
    'rplidar_dir',
    default=os.path.join(
      get_package_share_directory('rplidar_ros'),
      'launch'
    )
  )

  return LaunchDescription([
    DeclareLaunchArgument(
      'omo_r1mini_mcu_parameter',
      default_value=omo_r1mini_mcu_parameter
    ),


    IncludeLaunchDescription(
      PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/omo_r1mini_mcu.launch.py']),
      launch_arguments={'omo_r1mini_mcu_parameter': omo_r1mini_mcu_parameter}.items()
    ),

    IncludeLaunchDescription(
      PythonLaunchDescriptionSource([rplidar_dir, '/rplidar_s3_launch.py']),
    ),
    
    IncludeLaunchDescription(
      PythonLaunchDescriptionSource([omo_r1mini_description_dir, '/omo_r1mini_state_publisher.launch.py']),
      launch_arguments={'use_sim_time': use_sim_time}.items(),
    ),
  ])
