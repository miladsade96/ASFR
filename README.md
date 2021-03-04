# ASFR [![CodeFactor](https://www.codefactor.io/repository/github/everlookneversee/asfr/badge)](https://www.codefactor.io/repository/github/everlookneversee/asfr)

## Attendance system using facial recognition
This project is built using python and javascript programming languages
([python][python] for backend and [javascript][javascript] for frontend and gui).
We used [Eel][eel] package to make connections between frontend and backend.

## Requirements
* [eel][eel-pypi] >= 0.14.0
* [pytest][pytest-pypi] >= 6.2.2
* [cmake][cmake-pypi] >= 3.18.4
* [numpy][numpy-pypi] >= 1.19.4
* [khayyam][khayyam-pypi] >= 3.0.17
* [setuptools][setuptools-pypi] >= 50.3.2
* [face-recognition][face-recognition-pypi] >= 1.3.0
* [opencv-python][opencv-python-pypi] >= 4.4.0.46

## Getting started and run
First of all you should clone the project on your local machine inorder to run
it:  
```shell
git clone https://github.com/EverLookNeverSee/ASFR.git
```
navigate to project root directory:  
```shell
cd ASFR/
```
install all requirements using pip:
```shell
python -m pip install -r requirements.txt
```
navigate to asfr subdirectory:
```shell
cd asfr/
```
and then run the program using command below:
```shell
python main.py
```
command above will fire up the program and its gui will appear on the screen.


[python]: https://python.org
[javascript]: https://javascript.com
[eel]: https://github.com/ChrisKnott/Eel
[eel-pypi]: https://pypi.org/project/Eel/
[cmake-pypi]: https://pypi.org/project/cmake/
[numpy-pypi]: https://pypi.org/project/numpy/
[pytest-pypi]: https://pypi.org/project/pytest/
[khayyam-pypi]: https://pypi.org/project/Khayyam/
[setuptools-pypi]: https://pypi.org/project/setuptools/
[opencv-python-pypi]: https://pypi.org/project/opencv-python/
[face-recognition-pypi]: https://pypi.org/project/face-recognition/