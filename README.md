# Gesture-Customization-and-recognition
This project is used to detect static hand signs. Hand signs are fed in to the model which are usually a component of sign language or a static gesture. The model can predict the hand signs by using the webcam. There are similar words done previsouly(https://www.youtube.com/watch?v=pDXdlXlaCco), but they relied on image processing and CNNs to predict the gesture. The major disadvantages with this approach are:
1. Image sensitive to background
2. High computational power
3. There can be a lag between the image procuring and detection when deployed, due to higher computational time.

Instead, Google's mediapipe library(https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqblMwVmp2ZXFPQzdLLUF5VkJINGYwd093Vm5Dd3xBQ3Jtc0trelhYelBUdjgxRXh1UEYzZWg5NFBFd253X2gxNkZjTHBFQ2IyQXBIcmxTSkdsWDctczVFdVZ3M1FhQ1ZRbFNtZXFVang5b1RPZHpnaDBwSm1ENV9Bbkx3cDlQWGFILWMzTXRMNmM1c3JWVVVITUNoOA&q=https%3A%2F%2Fgithub.com%2Fkinivi%2Fhand-gesture-recognition-mediapipe&v=a99p_fAr6e4) can be used to detect the key hand coordinates and these coordinates can be processed and fed to an ANN. Therefore, it solves the above disadvantages.
This project can become an interface of communication for the deaf and dumb community.

Gesture Customization:
This set of code helps to customize static hand gestures by the webcam and save the data using OpenCV. 

Gesture Model:
This is an ANN model that trains on the data which is saved during customizing the hand sign.

Gesture Prediction:
Live hand gestures can be recognised through the webcam. This can be deployed into a mobile application and data can be extracted from the mobile camera.
