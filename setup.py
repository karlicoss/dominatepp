from setuptools import setup, find_packages

setup(
    name='dominatepp',
    version='0.2',
    description='Dominate++ is a collection of utility functions for HTML rendering based on Dominate',
    url='https://github.com/karlicoss/dominatepp',
    author='Dmitrii Gerasimov',
    author_email='karlicoss@gmail.com',
    classifiers=[
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={'': ['_resources/*']},
    include_package_data=True,
    tests_require=[
        'html5print',
        'beautifulsoup4',
    ],
    install_requires=[
        'dominate',
        'typing',
    ],
    zip_safe=False,
)
