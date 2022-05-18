from flask import Flask, jsonify, render_template, request
import json
import threading, webbrowser, random
import subprocess
import json
from utils.set_directories import directory_wizard
from flaskwebgui import FlaskUI
import configparser
import glob, os
import requests
from utils.filesystem import get_games, prepare_artwork

import psutil

import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('debug.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

config = configparser.ConfigParser()
config.read('config.ini')

PCSX2_PATH = config['default']['PCSX2_PATH']
if not PCSX2_PATH:
  # directory_wizard('Please navigate to the folder your PCSX2 executable is and select the .exe file', 'PCSX_PATH')
  # PCSX2_PATH = config['default']['PCSX2_PATH']
  pass

ROMS_FOLDER = config['default']['ROMS_FOLDER']
if not ROMS_FOLDER:
  # directory_wizard('Please select the folder your ROMS are in (.iso, .bin, etc.)', 'ROMS_FOLDER')
  # ROMS_FOLDER = config['default']['ROMS_FOLDER']
  pass


PCSX2_FLAGS = ' --fullscreen --nogui'

def exit_app():
  psutil.Process(os.getpid()).terminate()

app = Flask(__name__)
ui = FlaskUI(app, maximized=True, idle_interval=4294966, on_exit=exit_app)

games = get_games()
prepare_artwork(games) # prepare artwork for games by copying it to the "covers" directory so that they can be served by Flask.

@app.route('/')
def index():
    return render_template('index.html', games = games)

@app.route("/api")
def me_api():
    return jsonify(games)

@app.route("/run_game", methods=['POST'])
def open_project():
  # get json data from request
  data = request.get_json()
  isoPath = data['game']
  isosPath = data['games']
  # print(isoPath)
  # print(PCSX2_PATH + ' ' + '"' + isoPath + '"' + PCSX2_FLAGS)
  subprocess.Popen(PCSX2_PATH + ' ' + '"' + isoPath + '"' + PCSX2_FLAGS)
  return render_template('index.html', games = games)

if '__main__' == __name__:
  # app.run(debug=True)

  # PRODUCTION ONLY ---------
  ui.run()
  # PRODUCTION ONLY ---------