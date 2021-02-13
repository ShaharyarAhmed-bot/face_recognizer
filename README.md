# SPOTT

Under construction! Alpha release

Developed by Shaharyar Ahmed(c) 2020

## Setup
Make sure you have anaconda (https://www.anaconda.com/) installed then do the following

`conda create -n envname python=3.8` 

replace envname with anyname you want

`conda activate envname`

Then go to https://pypi.org/project/spott/ and download the latest version of the package using pip

## Examples of How To Use (Buggy Alpha Version)

Face Recognition on an image

```python
import spott

recognizer = spott.Recognizer(known_faces_dir = "directory location here", tolerance = 0.6, frame_thickness = 3, font_thickness = 2, model = "hog or cnn or sift")

recognizer.init()
recognizer.recognize_pic(unknown_faces_dir = "directory location here")
```

Live Face Recognition

```python
import spott

recognizer = spott.Recognizer(known_faces_dir = "directory location here", tolerance = 0.6, frame_thickness = 3, font_thickness = 2, model = "hog or cnn or sift")

recognizer.init()
recognizer.live_feed()
```

Report any bugs to my email shaharyar.ahmed1121@gmail.com or create a new issue