# ref: https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode
# ref: https://dzone.com/articles/executable-package-pip-install
# ref: https://stackoverflow.com/questions/47362271/python-upgrade-my-own-package

# install for develop:
#   python setup.py develop

import pathlib
path = pathlib.Path(__file__).parent.resolve()

import re
re_version = r'version\s=\s"(\d+.\d+.\d+)"'
with open(f"{path}/src/oqhlib/__init__.py", "r") as fp:
    for line in fp:
        match = re.match(re_version, line)
        if match is not None:
            version = match[1]
print(version)

import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='oqhlib',
    version=version,
    author="Miguel Angelo",
    author_email="masbicudo@gmail.com",
    description="oqh command line interface library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://raw.githubusercontent.com/masbicudo/oqueeh/main/_tools/lib",

    # include all packages under src, except for tests
    packages=setuptools.find_packages(where="src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),

    # tell distutils packages are under src
    package_dir={"": "src"},

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache-2.0",
        "Operating System :: OS Independent",
    ],
)