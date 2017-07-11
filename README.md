# How to compile for Windows with PyInstaller

1. Install newest Python 3 version.
2. `pip install pyinstaller requests`
3. `pyinstaller main.py --hidden-import queue`
4. Copy `dist/main.exe`, `start_main.bat` and `config.ini` to target.
7. Run `start_main.bat`.

# How to compile for Windows with py2exe (doesn't work with Python 3.5+)
1. Insatll the newest Python 2 version.
2. `pip install py2exe`
3. `pip install requests`
4. `python setup.py py2exe`
5. Copy `dist/main.exe`, `start_main.bat` and `config.ini` to target.
6. Run `start_main.bat`
