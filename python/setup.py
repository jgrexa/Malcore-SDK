from setuptools import find_packages, setup
import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("MSDK_VERSION"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name="msdk",
    packages=find_packages(),
    version=get_version("msdk/lib/settings.py"),
    description="SDK for Malcore API",
    author="Thomas Perkins",
    author_email="contact@malcore.io",
    install_requires=["requests==2.31.0"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Internet-2-0/Malcore-SDK",
)
