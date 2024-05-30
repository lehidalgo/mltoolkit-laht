from setuptools import setup, find_packages

setup(
    name='my-ds-ml-toolkit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
    ],
    author='Your Name',
    author_email='le.hidalgot@gmail.com',
    description='A data science and machine learning toolkit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my-ds-ml-toolkit',
)