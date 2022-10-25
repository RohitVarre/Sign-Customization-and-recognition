# Gesture-Customization-and-recognition
The goal of this project is to detect static hand signs. A machine learning model is designd to detect live hand signs using the webcamera. These signs are usually static gestures or a part of sign language. There are similar words done previsouly(https://www.youtube.com/watch?v=pDXdlXlaCco), but they relied on image processing and CNNs to predict the gesture. The major disadvantages with this approach are:
1. Image sensitivity to background
2. High computational power
3. Possible lag between the image procuring and detection when deployed, due to higher computational time.

Instead, Google's mediapipe library(https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqblMwVmp2ZXFPQzdLLUF5VkJINGYwd093Vm5Dd3xBQ3Jtc0trelhYelBUdjgxRXh1UEYzZWg5NFBFd253X2gxNkZjTHBFQ2IyQXBIcmxTSkdsWDctczVFdVZ3M1FhQ1ZRbFNtZXFVang5b1RPZHpnaDBwSm1ENV9Bbkx3cDlQWGFILWMzTXRMNmM1c3JWVVVITUNoOA&q=https%3A%2F%2Fgithub.com%2Fkinivi%2Fhand-gesture-recognition-mediapipe&v=a99p_fAr6e4) can be used to detect the key palm coordinates very efficiently and these coordinates can be processed and fed to an ANN. Therefore, it overcomes the above shortcomings.
This project has the potential to become an interface of communication for the deaf and dumb community with the normal world. 

It can be divided in to three subparts:

Gesture Customization:
This set of code helps to customize static hand gestures and save the data using OpenCV. The data comprises of the x and y coordinates of various key points on a palm. These coordinates are preprocessed and stored to train the model.

Gesture Model:
This is an ANN model that trains on the data which is saved by the gesture customization code. 

Gesture Prediction:
Live hand gestures are recognised through the webcam. The webcam captures the live coordinates of the hand and feeds it to the ANN model which recognises the handsigns. This can be deployed into a web or mobile application and data can be extracted from the mobile camera.
