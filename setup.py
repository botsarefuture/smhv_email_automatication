from setuptools import setup, find_packages

setup(
    name='my-custom-email-package',
    version='0.1',
    description='A custom email sender package for Python',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my-custom-email-package',
    packages=find_packages(),
    install_requires=[
        # List any dependencies here
    ],
)
