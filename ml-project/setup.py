from setuptools import setup,find_packages

setup(
    name='ml-project',
    version='0.0.1',
    author='swastika',
    author_email='swastikadhakal376@gmail.com' ,
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'flask',
        'scikit-learn',
        'seaborn',
        'matplotlib',
        'xgboost',
        'streamlit',
    ],
)