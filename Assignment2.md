# Assingment 2 (Feb. 8th)

### 1) Trainning vs Testing Label
* The training data and labels are used to train the programs to determine the characteristics of the material, which in Maroney's case is shoes. Therefore, the training images are used to train the program and the testing images are used to test the program to make sure the program knows what makes the image an imgae of a shoe or not. Also, there is no point of showing the same images to the program to test, because the program already knows that the images used during training are shoes (images from testing should be different from training). 

### 2) Layers in fashion MNIST
* ".Flatten" takes the rectangular shape of the data, the 28 by 28 image and flatten that to a one dimensional array that can be processed in the next layer. ".relu" function states that if the output of the function is 0, set it to 0 because negative outputs can skew the results downward and it cancels out the positive outputs elsewhere. ".softmax" helps you find the most likely candidate, it is usually on the very last layer. ".softmax" function sets the greatest probability as 1 and rest to 0, allowing the user to just find the value 1 as the candidate for the accurate result, rather than comparing the probability. There are 10 neurons in the third and last layer because there are 10 pieces of clothing in the data set. Therefore, the job of the each of the neuron layers are to calculate the probability that a piece of clothing is for that particular class or category. 

### 3) Optimizer and Loss Function
* The outputs from all the neurons are added up (for all training sets, 60K in this case). Then the loss function calculates how 'bad' or how 'good' those answers are and the optimizer tweaks the random parameters (m and c in the example on video) to run the neurons again. Overtime, values within the neurons will change for the datat outputs are fit as accuratly as possible to the training labels. 

### 4) Handwriting 
* What is the shape of the images training set?
  * The shape of the imgages training set is 28X28 gray scale images in 10 classes.
* What is the length of the labels training set?
  * 60,000 training set images.
* What is the shape of the images test set?
  * There 10,000 of 28X28 images as a test set.

* Estimate 
  * [0.07451967895030975, 0.9771999716758728] The return was .977 or 97.7%, which means that the program is getting the test data correct at 97% accuracy. 
  
### 5) np.argmax()
  * Using np.argmax() on the predictions output, the number with the highest probability form the test labels dataset was "1". 
  
### 6) Plot image and histogram
