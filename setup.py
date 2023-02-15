from setuptools import setup

setup(
    name="pandstat",
    version="0.1.8",
    description="Package for easy statistical testing and useful dataframe methods in pandas!",
    url="https://github.com/willros/pandstat",
    author="William Rosenbaum",
    author_email="william.rosenbaum88@gmail.com",
    license="MIT",
    packages=["pandstat"],
    install_requires=["pandas", "statsmodels", "pandas-flavor", "altair"],
)
