from setuptools import setup

with open('requirements.yml') as f:
    requirements = f.read().splitlines()

setup(
    name='osdt',
    version='0.1',  # Specify the version of your package
    install_requires=requirements,
    packages=['osdt'],  # Replace 'osdt' with the actual package name
    # Other metadata such as author, author_email, description, etc.
)
