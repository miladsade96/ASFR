# importing relevant modules
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

VERSION = "1.0.0"

def readme() -> str:
    """
    prints long description
    :return: None
    """
    with open("README.md", "r") as f:
        return f.read()


class VerifyVersionCommand(install):
    """
    Custom command to verify that the git tag matches our version
    """
    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")
        if tag != VERSION:
            info = f"Git tag: {tag} does not match the version of this package: {VERSION}"
            sys.exit(info)


setup(
    name="frp",
    version=VERSION,
    author="EverLookNeverSee",
    author_email="EverLookNeverSee@ProtonMail.ch",
    description="Attendance system using facial recognition",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/EverLookNeverSee/frp",
    packages=find_packages(),
    cmdclass={
        "verify":VerifyVersionCommand
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "dlib=19.18.0",
        "face_recognition=1.3.0",
        "numpy=1.19.4",
        "opencv-python=4.4.0",
        "twine=3.2.0",
    ]
)
