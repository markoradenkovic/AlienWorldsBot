"""Setup script for realpython-reader"""

# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "COMPILING_NEW_DIST_INSTRUCTIONS.md").read_text()

# This call to setup() does all the work
setup(
    name="alien-worlds-bot",
    version="1.0.0",
    description="Play alien-worlds",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    author="Alien World",
    author_email="info@alienworlds.io",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["bot_logic", "alienworlds_program_data", "help_scripts", "instances_of_chrome", "program_files"],
    include_package_data=True,
    install_requires=["pygetwindow", "pyautogui", "selenium", "webdriver_manager", "pyscreeze", "opencv-python",
                      "Pillow", "PyMsgBox", "PyRect", "cachetools", "certifi", "charset-normalizer", "configparser",
                      "idna", "numpy", "outcome", "pefile", "pycparser", "setuptools", "json"],
    entry_points={"console_scripts": ["alien-worlds-bot=program_files.__main__:main"]},
)
