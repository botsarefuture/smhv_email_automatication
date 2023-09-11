from setuptools import setup, find_packages

setup(
    name='smhv-mailer',
    version='0.1',
    description='SMHV custom email sender package for Python',
    author='SMHV',
    author_email='verso.vuorenmaa@sinimustaahallitustavastaan.org',
    url='https://github.com/botsarefuture/smhv_email_automatication',
    packages=find_packages(),
    install_requires=[
    'smtplib',
    'email',
    # Add any other dependencies here
],
)
