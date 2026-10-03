"""
Setup configuration for the EmotionDetection package.
"""
from setuptools import find_packages, setup

setup(
    name='EmotionDetection',
    version='1.0.0',
    description='Emotion detection package using IBM Watson NLP',
    author='Vedant Loya',
    packages=find_packages(),
    install_requires=[
        'requests',
        'Flask',
    ],
)
