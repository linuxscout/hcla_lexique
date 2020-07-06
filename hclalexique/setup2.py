#! /usr/bin/python
from distutils.core import setup
from glob import glob
import py2exe

# to install type:
# python setup.py install --root=/

setup (name='Bahith', version='0.5',
      description='BaHith',
      author='Taha Zerrouki',
      author_email='taha_zerrouki@gawab.com',
      url='http://www.csla.dz/',
      license='GPL',
      console= [
        {
            "script": "main_gui.py",
            "icon_resources": [(1, "images/logo.png")]
        }
    ],
      windows = [
        {
            "script": "main_gui.py",
            "icon_resources": [(1, "images/logo.png")]
        }
    ],

      #scripts=['Qutrub'],
      classifiers=[
          'Development Status :: 5 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS independent',
          'Programming Language :: Python',
          ],
      data_files=[
          #('images',['f:\gui/qutrub/libqutrub/images/save.png']),
          ('images',['./images/logo.jpg']),
          ('data',
          [
          './data/officelexique.db',
          './data/financelexique.db',
          './data/mecaniquelexique.db',
          ]
       ),
       ('ar',
       ['./ar/style.css',
       './ar/hcla_body.html',
       './ar/about.html',
       './ar/help_body.html']
       ),
       ('ar/images',
          [	  './ar/images/print.png',
          './ar/images/save.png',
          './ar/images/preview.png',
          './ar/images/copy.png',
          './ar/images/cut.png',
          './ar/images/font.png',
          './ar/images/help.jpg',
          './ar/images/new.png',
          './ar/images/exit.png',
          './ar/images/zoomin.png',
          './ar/images/zoomout.png',
          './ar/images/logo.png' ])
          ]);

