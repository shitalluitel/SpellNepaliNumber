try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# description = "Commandline tool to listen all radio stations of Nepal"

# long_description = open("README.rst").read()

classifiers = ['Environment :: Console',
               'Programming Language :: Python :: 3'
               ]

# version = open('CHANGES.txt').readlines()[0][1:].strip()

setup(name='SpellNepaliNumber',
      version='1.1.0',
      description="To know Nepali numbers in words",
      author='Shital Babu Luitel',
      author_email='ctalluitel@gmail.com',
      url='https://github.com/shitalluitel/SpellNepaliNumber',
      scripts=['src/SpellNepaliNumberl'],
      install_requires=requirements,
      packages=['SpellNepaliNumber'],
      package_dir = {'SpellNepaliNumber': 'src/SpellNepaliNumber'},
      classifiers=classifiers
      )