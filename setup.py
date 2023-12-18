from setuptools import setup, find_packages

setup(
    name='jmcwatch',
    version='0.1.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jmcwatch=jmcwatch.cli:main',
        ],
    },
    install_requires=[
        'click',
        'watchdog',
        'jmcfunction @ git+https://github.com/WingedSeal/jmc.git#subdirectory=src',
    ],
    author='amandin',
    author_email='amawwdin@email.com',
    description='Watch and compile JMC files. Simply type `jmcwatch` to use.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)
