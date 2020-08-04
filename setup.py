#coding=utf-8
import os

from setuptools import setup

setup(
    name='rotationconverter',
    version='1.0.0',
    description='A converter for Euler Angle,Axis Angle,Quaternion,Rotation Matrix ',
    url='https://github.com/li-xl/3drotation',
    author='li-xl',
    author_email='lixl19@mails.tsinghua.edu.cn',
    license='MIT',
    install_requires=['numpy'],
    packages=['rotationconverter'],
    platforms=['any']
)