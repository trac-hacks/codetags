#!/usr/bin/env python
from setuptools import setup
import os

PACKAGE = 'codetags'
VERSION = '0.3'

if os.path.exists('.git/HEAD'):
    tag_hash = os.popen('git rev-list --max-count=1 %s .' % (VERSION,)).read()
    head_hash = os.popen('git rev-list --max-count=1 HEAD .').read()
    if tag_hash != head_hash:
        import datetime
        date = os.popen('git log --pretty=format:%%ct --max-count=1 %s' % (head_hash,)).read()
        date = datetime.datetime.utcfromtimestamp(long(date))
        VERSION += date.strftime('-%Y%m%d%H%M%S')

setup(
    name=PACKAGE,
    version=VERSION,
    install_requires='Trac >= 0.10',
    author='Giel van Schijndel',
    author_email='me@mortis.eu',
    url='http://trac-hacks.org/wiki/CodeTagsPlugin',
    download_url='http://git.mortis.eu/codetags.git',
    license='BSD',
    classifiers=[
        'Framework :: Trac',
        'License :: OSI Approved :: BSD License',
    ],
    keywords='trac plugin',
    packages=['codetags'],
    package_data={
        'codetags' : ['templates/*.cs', 'templates/*.html', 'htdocs/*.css']
    },
    entry_points = {
        'trac.plugins': ['codetags = codetags']
    }
)
