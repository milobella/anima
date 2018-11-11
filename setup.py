from setuptools import setup

setup(
    name='anima',
    version='0.1-dev',
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
