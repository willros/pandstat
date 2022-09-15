from setuptools import setup

setup(
    name="pandstat",
    version="0.1.5",
    description="Package for easy statistical testing in Pandas",
    url="https://github.com/willros/pandstat",
    author="William Rosenbaum",
    author_email="william.rosenbaum88@gmail.com",
    license="MIT",
    packages=["pandstat"],
    install_requires=["pandas", 
                      "statsmodels", 
                      "pandas-flavor",
                      "altair"],
)
