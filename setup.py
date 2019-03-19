from setuptools import setup

version = None
with open('VERSION.txt', 'r') as fp:
    version = fp.read()

setup(
    name='anima',
    version=version,
    packages=["anima"],
    entry_points={
      'console_scripts': [
          'anima_launcher=anima.__main__:main'
      ]
    },
    url='',
    license='',
    author='Célian Garcia',
    author_email='celian.garcia1@gmail.com',
    description=''  
)
