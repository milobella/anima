from setuptools import setup

setup(
    name='anima',
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
    description='Natural language generation service of Milobella.'
)
