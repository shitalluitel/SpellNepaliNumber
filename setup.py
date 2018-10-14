try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# requirements = [pkg.split('=')[0] for pkg in open('requirements.txt').readlines()]

# description = "Commandline tool to listen all radio stations of Nepal"

# long_description = open("README.rst").read()

classifiers = ['Environment :: Console',
               'Programming Language :: Python :: 3'
               ]

# version = open('CHANGES.txt').readlines()[0][1:].strip()

setup(
  name='SpellNepaliNumber',
  version='1.2.2',
  description="To Spell Out Nepali Numbers In Nepali Language.",
  author='Shital Babu Luitel',
  author_email='ctalluitel@gmail.com',
  url='https://github.com/shitalluitel/SpellNepaliNumber',
  scripts=['src/spellnepalinumber'],
  # install_requires=requirements,
  packages=['SpellNepaliNumber'],
  package_dir = {'SpellNepaliNumber': 'src/SpellNepaliNumber'},
  classifiers=classifiers
) 