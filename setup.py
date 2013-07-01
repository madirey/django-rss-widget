#!/usr/bin/env python

from distutils.core import setup

setup(name='django-rss-widget',
      version='0.5',
      description='Django RSS Widget',
      author='Matt Caldwell',
      author_email='matt.caldwell@gmail.com',
      url='https://github.com/mattcaldwell/django-rss-widget/',
      packages=['rss_widget', 'rss_widget.templatetags']
)
