from setuptools import setup, find_packages

setup(
    name='polygon_clipping',
    version='0.0.1',
    author='Dan-Patterson',
    description='Polygon clipping using Shapely',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bluewhalekr/polygon_clipping',
    packages=find_packages(),
    install_requires=[
        'shapely',
        'numpy',
        'npg'
    ],
    python_requires='>=3.8'
)
