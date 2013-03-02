from distutils.core import setup

setup(
  name='MyPackage',
  version='0.1.0',
  author='B. Reuderink',
  author_email='b.reuderink@gmail.com',
  packages=['mypackage'],
  scripts=['bin/example_script'],
  url='http://github.com/breuderink',
  license='LICENSE.txt',
  description='Useful towel-related stuff.',
  long_description=open('README.rst').read(),
  install_requires=[
    "numpy>=1.6.2",
  ],
)
