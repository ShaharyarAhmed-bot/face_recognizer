from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))


VERSION = '0.0.1'
DESCRIPTION = 'Face Recognizer'
LONG_DESCRIPTION = 'A package that allows developers to do face recognition in a few lines of code'

# Setting up
setup(
    name="face_recognizer",
    version=VERSION,
    author="Shaharyar Ahmed",
    author_email="<shaharyar.ahmed1121@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['face-recognition', 'opencv-contrib-python'],
    keywords=['python', 'face-recognition', 'opencv'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)