from setuptools import setup

setup(
    name='dominatepp',
    version='0.1',
    description='Dominate++ is a collection of utility functions for THML rendering based on Dominate',
    url='https://github.com/karlicoss/dominatepp',
    author='Flying Circus',
    author_email='karlicoss@gmail.com',
    classifiers=[
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    license='MIT',
    packages=['dominatepp'],
    install_requires=[
        'dominate',
        'typing',
    ],
    zip_safe=False,
)
