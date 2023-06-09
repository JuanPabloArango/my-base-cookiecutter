#Librerías Externas.
from setuptools import setup, find_packages

#Librerías Internas.
from src.version import __version__


with open("README.md") as readme:
    readme = readme.read()

with open("requirements.txt") as req:
    requirements = req.read().splitlines()

setup_requirements = []
test_requirements = ['pytest','pytest-mock','pytest-cov' ]


if __name__ == "__main__":

    setup(name = "{{cookiecutter.project_name}}",
          keywords = "CookieCutter",
          author = "{{cookiecutter.author}}",
          author_email = "{{cookiecutter.mail}}",
          description = "{{cookiecutter.description}}",
          long_description = readme,
          license = "MIT License",
          classifiers = ["Intended Audience :: Developers",
                         "Natural Language :: Spanish",
                         "License :: OSI Approved :: MIT License",
                         "Programming Language :: Python :: 3",
                         "Topic :: Scientific/Engineering :: Artificial Intelligence"],
          install_requires = requirements,
          extras_require = {"tests": test_requirements},
          test_suite = "pytest",
          setup_requires = setup_requirements,
          include_package_data = True,
          package_dir = find_packages(where = "src"),
          url = "",
          zip_safe = False,
          version = __version__)