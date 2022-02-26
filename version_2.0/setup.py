from distutils.core import setup  # Need this to handle modules
import py2exe
import traceback
import time
import sys
import HelpScripts
import bot_logic
import instances_of_chrome
import data
import bot
import pathlib
import pygetwindow
import pyautogui
import os
import shutil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json


setup(console=['main.py'])  # Calls setup function to indicate that we're dealing with a single console application
