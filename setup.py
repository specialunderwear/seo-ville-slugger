"""
Seo ville slugger will solve the problems you are having with django, media
files and filenames.

Django's default storage backend has some pretty annoying behaviour.
When uploading the same file for the second time, you get a second file on disk
with some kind of crazy hash value added at the end.

There are 2 kinds of people that are not happy with that.

1. The person that has to pay for disk space
2. The SEO people your customer has hired.

This storage backend stores files named after their hash value and adds a symlink
with the original name. No duplication and you SEO your heart out.
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
