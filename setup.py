from setuptools import setup, find_packages

setup(
    name='oriented-unfolding',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'filelock',
        'h5py',
        'numpy-quaternion',
        'opencv-python',
        'openexr',
        'potpourri3d==0.0.4',
        'pyquaternion',
        'ray[default]',
        'scipy',
        'tensorboardx',
        'transformations',
        'transforms3d',
        'trimesh',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author='Gu',
    author_email='guningquan@outlook.com',
    description='A Python package for Oriented-Unfolding',
    url='https://github.com/xxx',
    python_requires='>=3.9',
)
