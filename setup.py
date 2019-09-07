"""
Seo ville slugger will solve the problems you are having with django, media
files and filenames.
"""
from setuptools import setup, find_packages


__version__ = "0.0.1"


setup(
    # package name in pypi
    name='seo-ville-slugger',
    # extract version from module.
    version=__version__,
    description="One of those things",
    long_description=__doc__,
    classifiers=[],
    keywords='',
    author='Boie ktule',
    author_email='boie@permanentmarkers.nl',
    url='https://github.com/specialunderwear/seo-ville-slugger',
    license='GPL',
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'setuptools',
        'Django'
    ],
)
