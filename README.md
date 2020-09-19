# Gesture-Customization-and-recognition
This project is used to detect Hand signs. Hand signs are fed in to the model which are usually a component of sign language or a static gestures. The model can predict the hand signs by using the webcam.
This project can help the dumb and deaf people to communicate with others by feeding the necessary information to the model.

Gesture Customization:
This set of code helps to customize static hand gestures and saves the data using OpenCV. This data can be used to train a model to recognize the hand gestures fed to the model.

Gesture Model:
This is a CNN model that trains on the data which is saved during customizing the hand sign. Accuracy of around 99 percent is reached with a very few epochs since a lot a preprocessing is done using OpenCV.

Gesture Prediction:
Live hand gestures can be recognised through the webcam. Mask is used to detect the hand, instead a Cascade from OpenCV modules can also be used to detect the hand.

 
