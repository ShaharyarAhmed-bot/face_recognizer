# face_recognizer

Under construction! Alpha release

Developed by Shaharyar Ahmed(c) 2020

## Examples of How To Use (Buggy Alpha Version)

Face Recognition on an image

```python
import face_recognizer

recognizer = face_recognizer.Recognizer(known_faces_dir = "directory location here", tolerance = 0.6, frame_thickness = 3, font_thickness = 2, model = "hog or cnn or sift")

recognizer.init()
recognizer.recognize_pic(unknown_faces_dir = "directory location here")
```

Live Face Recognition
```python
import face_recognizer

recognizer = face_recognizer.Recognizer(known_faces_dir = "directory location here", tolerance = 0.6, frame_thickness = 3, font_thickness = 2, model = "hog or cnn or sift")

recognizer.init()
recognizer.live_feed()
```
