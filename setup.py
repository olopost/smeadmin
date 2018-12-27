import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


with open("requirements.txt", "r") as rp:
    req = rp.read()

setuptools.setup(
    name="smeadmin",
    version="0.0.2",
    author="Samuel MEYNARD",
    author_email="samuel@meyn.fr",
    description="SME admin tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olopost/smeadmin",
    packages=setuptools.find_packages(),
    package_dir={'smeadmin': 'smeadmin'},
    package_data={
        'smeadmin': [
            'templates/*.html',
        ],
    },
    install_reqs=req,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)