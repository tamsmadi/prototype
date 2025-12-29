1-Title: Gesture recognition under different levels of visual degradation

2-Problem Statement:

Retinal impairment patients are facing serious problem with contrast loss, which will cause patients to see everything in monotonic color resulting in lost of eye vision functions. Difficulty in recognition for gestures is another problem they face, they lose the ability to understand gestures 

3-Objective: Evaluate how visual degradation gesture recognition performance and understand concept of degradation aware training

4-Dataset: hand gesture recognition from kaggle [(https://www.kaggle.com/datasets/gti-upm/leapgestrecog)]

the dataset contains 10 different classes totaling of 20000 images 
split ratio was 80% training 10% test and 10% validation

5-Methodology:

A baseline convolution neural network architect was built and compiled.
Applied contrast loss on test set images to evaluate model performance on degraded images, then applied same script on training set to do degradation aware training .
Accuracy was used to evaluate model performance 

6-Experiments:

Fit the model on clean train set and evaluate on clean test set to see performance of baseline architecture on ideal conditions, then did evaluation on degraded test set to see how model perform when distribution shift, then did another fit on mix of different degradation levels images and clean images
