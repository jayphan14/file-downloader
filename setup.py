from setuptools import setup

setup(
    name='file_downloader',
    version='1.0',
    py_modules=['file_downloader'],
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'file_downloader=file_downloader:main',
        ],
    },
)

