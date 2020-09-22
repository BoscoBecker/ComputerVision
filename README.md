## Aprendizado de visão computacional real-time usando OPENCV e Python
A ideia é usar o OPENCV para reconhecer rosto, sorriso e olhos usando a webcam do seu notebook.

![Screenshot](image/screenshotCV.png)

*Me desculpem pela imagem não tão linda LOL*



# Motivação

O intuito da apicação é entender como funciona o OPENCV e Visão computacional(Computer Vision)usando Python.

## Requisitos
   - [OpenCV 3.0](http://opencv.org/)
   - [Python > 3.5](https://www.python.org/downloads/)
   - [Haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)


# Executando o projeto
```
python appComputerVision.py
```

## Nota
- OpenCV 3.1 might crash on OSX after a while, so that's why I had to switch to version 3.0. See open issue and solution [here](https://github.com/opencv/opencv/issues/5874).
- Moving the `.read()` part of the video stream in a multiple child processes did not work. However, it was possible to move it to a separate thread.


## Maquina usada para o desenvolvimento
* Processador: AMD 1.0 Ghz
* Memoria RAM : 6.0 
* OS WIndows 10 Pro 64 Bits

Make with love - @boscobecker
