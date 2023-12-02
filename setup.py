# from setuptools import setup

# with open('requirements.yml') as f:
#     requirements = f.read().splitlines()

# setup(
#     name='osdt',
#     version='0.1',  # Specify the version of your package
#     install_requires=requirements,
#     packages=['osdt'],  # Replace 'osdt' with the actual package name
#     # Other metadata such as author, author_email, description, etc.
# )


from setuptools import setup

setup(
    name='osdt',
    version='0.1.0',  # Specify the version of your package
    install_requires=[
        'bzip2==1.0.8',
        'ca-certificates==2023.01.10',
        'libffi==3.4.2',
        'openssl==1.1.1t',
        'python==3.11.3',
        'setuptools==66.0.0',
        'sqlite==3.41.2',
        'tk==8.6.12',
        'vc==14.2',
        'vs2015_runtime==14.27.29016',
        'wheel==0.38.4',
        'xz==5.2.10',
        'zlib==1.2.13',
        'gmpy2==2.1.5',
        'joblib==1.2.0',
        'numpy==1.24.3',
        'pandas==2.0.1',
        'python-dateutil==2.8.2',
        'pytz==2023.3',
        'scikit-learn==1.2.2',
        'scipy==1.10.1',
        'six==1.16.0',
        'threadpoolctl==3.1.0',
        'tzdata==2023.3'
    ],
    packages=['osdt'],  # Replace 'osdt' with the actual package name
    # Other metadata such as author, author_email, description, etc.
)
