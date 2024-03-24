from setuptools import setup, find_packages

setup(
    name='jmcwatch',
    version='1.5.9',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jmcwatch=jmcwatch.__main__:main',
        ],
    },
    install_requires=[
        'click',
        'watchdog',
        'jmcfunction'
    ],
    author='amandin',
    author_email='amawwdin@email.com',
    description='Watch and compile JMC related files. Simply type `jmcwatch` to use.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)
