from tkinter import Tk, messagebox
from tkinter.filedialog import askdirectory
import json
import configparser

def directory_wizard(instructions, ini_variable_name):
  from tkinter import Tk
  from tkinter.filedialog import askdirectory
  root = Tk()
  root.withdraw()
  messagebox.showinfo('Select your projects root folder', "Select your projects root folder. You can change it later by running the 'set_projects_directory' program. Currently only 1 root directory is supported.")
  path = askdirectory(title=instructions).replace('/', '\\') # shows dialog box and return the path
  config = configparser.ConfigParser()
  sections = config.sections()
  # check if sections contains 'default'
  if not 'default' in sections:
    config.add_section('default')
    config['default'][f'{ ini_variable_name }'] = path
    with open('./config.ini', 'w') as configfile:
      config.write(configfile)