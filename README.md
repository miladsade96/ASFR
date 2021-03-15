![](web/images/logo.png)
[![CodeFactor](https://www.codefactor.io/repository/github/everlookneversee/asfr/badge)](https://www.codefactor.io/repository/github/everlookneversee/asfr)

## Attendance system using facial recognition
This project is built using python and javascript programming languages
([python][python] for backend and [javascript][javascript] for frontend and gui).
We used [Eel][eel] package to make connections between frontend and backend.

## Authors
Milad Sadeghi DM - initial work - [@EverLookNeverSee][github-profile]  
See also the list of [contributors][contributors] who participated in this project.

## Requirements
For more details, see [requirements.txt](requirements.txt)

## Getting started and running
First of all you should clone the project on your local machine:  
```shell
git clone https://github.com/EverLookNeverSee/ASFR.git
```
navigate to project root directory:  
```shell
cd ASFR/
```
install all dependencies using python package manager:
```shell
python -m pip install -r requirements.txt
```
create a directory named **train_images** and put all your images in it:  
```shell
mkdir train_images
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

In the next step you should **load** , **encode** and **save** your encoding values; to do so 
press **load**, **encode** and **save** buttons in order.

Congratulations, now you can press **start** button and program starts the recognition process.  

**Note:** the **stop** button stops the recognition process and if you press it twice, it resets video capture window.

## License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for more details.

[github-profile]: https://github.com/EverLookNeverSee
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
[contributors]: https://github.com/EverLookNeverSee/ASFR/graphs/contributors