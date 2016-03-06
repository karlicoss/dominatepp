from setuptools import setup

setup(
    name='dominatepp',
    version='0.1.1',
    description='Dominate++ is a collection of utility functions for HTML rendering based on Dominate',
    url='https://github.com/karlicoss/dominatepp',
    author='Flying Circus',
    author_email='karlicoss@gmail.com',
    classifiers=[
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    license='MIT',
    packages=['dominatepp'],
    tests_require=[
        'html5print',
    ],
    install_requires=[
        'dominate',
        'typing',
    ],
    zip_safe=False,
)
