from setuptools import setup, find_packages

setup(
    name='rofimoji',
    version='4.0.0',
    description='Simple character picker using rofi',
    author='fdw',
    author_email='5821180+fdw@users.noreply.github.com',
    url='https://github.com/fdw/rofimoji',
    keywords='rofi emoji emoji-picker picker emoticon smiley',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ],

    packages=['picker'],
    package_data={
        'picker': ['data/*.csv']
    },
    install_requires=[
        'pyxdg==0.26',
        'ConfigArgParse>1.0.0,<2.0.0'
    ]
)
