import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\Tomek\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_camera() -> None:
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad() -> None:
    os.startfile(paths['notepad'])


def open_discord() -> None:
    os.startfile(paths['discord'])

def open_cmd() -> None:
    os.system('start cmd')

def open_calculator() -> None:
    sp.Popen(paths['calculator'])