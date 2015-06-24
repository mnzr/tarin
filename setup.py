from setuptools import setup

setup(
    name='Tarin',
    version='1.0',
    py_modules=['tarin'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tarin=tarin:tarin
    '''
)
