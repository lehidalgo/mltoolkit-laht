from setuptools import setup, find_packages

setup(
    name="mltoolkit-laht",
    version="0.2.2",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "mltoolkit-laht": ["data/BankReviews.csv"],
    },
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
    ],
    author="Leandro Alexis Hidalgo Torres",
    author_email="le.hidalgot@gmail.com",
    description="A data science and machine learning toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lehidalgo/mltoolkit-laht",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
