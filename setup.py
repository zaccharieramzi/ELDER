import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# taken from https://github.com/CEA-COSMIC/ModOpt/blob/master/setup.py
with open('requirements.txt') as open_file:
    install_requires = open_file.read()

setuptools.setup(
    name="ELDER",
    version="0.0.1",
    author="Jiaming Liu",
    author_email="jiaming.liu@wustl.edu",
    description="Deep Equilibrium Learning of Explicit Regularizers for Imaging Inverse Problems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wustl-cig/ELDER",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    extras_require={
        'test': ['pytest'],
    },
    python_requires='>=3.6',
)
