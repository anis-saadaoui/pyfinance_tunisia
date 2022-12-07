from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='pyfinance_tunisia',
    version='0.0.8',
    description='A python library that can help developer to see much informations about tunisian companies in stock market',
    author= 'Anis SAADAOUI',
#    url = 'https://github.com/Spidy20/PyMusic_Player',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="./src"),
    keywords=['financial ratios', 'BVMT', 'Ilboursa','Finance','Tunisia'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
    py_modules=['pyfinance_tunisia'],
    package_dir={"":"src"},
    install_requires = [
        'beautifulsoup4',
        'requests'],
    #include_package_data=True,
    #package_data={'': ['data/*.csv']},
)
