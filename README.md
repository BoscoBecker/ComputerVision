# Computer vision learning using OPENCV and Python

Computer vision, smile and real-time eyes application using OPENCV and Python.
The idea is to recognize faces, a smile or eyes using your notebook's webcam. 

![Screenshot](image/screenshotCV.png)

* I'm sorry for the not-so-cute image😂😂 *

# Motivation 😎

The purpose of the application is to understand how OPENCV and Computer Vision using Python works and of course
learn a little about haarcascade. 

## Requirements 
   - [OpenCV 3.0](http://opencv.org/)
   - [Python > 3.5](https://www.python.org/downloads/)
   - [Haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)


# run the project
```
python appComputerVision.py
```

## Note about new version of OpenCV 3.1
- In OpenCV 3.1 might crash on OSX after a while, so that's why I had to switch to version 3.0. 
See open issue and solution [here](https://github.com/opencv/opencv/issues/5874).

## False Positive
When performing several tests I noticed that when using haarcascade (haarcascade_smile.xml) for smile detection,
I was wearing a NIKE shirt and it was interpreted as a smile, then. . . in short . . . 

 ![Screenshot](image/screenshotCVFalsoPositivo.png)
 
 *Não recomendo usar camisa da NIKE ao tentar detectar sorriso😁 *

## Machine used to develoment
* Processor: AMD 1.0 Ghz (Pretty bad, yeah, I know, Complicated 😢😢)
* RAM Memory: 6.0
* WIndows 10 Pro 64 Bit 

Make with ❤ - @boscobecker
