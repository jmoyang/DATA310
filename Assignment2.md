# Assingment 2 (Feb. 8th)

1) Trainning vs Testing Label
* The training data and labels are used to train the programs to determine the characteristics of the material, which in Maroney's case is shoes. Therefore, the training images are used to train the program and the testing images are used to test the program to make sure the program knows what makes the image an imgae of a shoe or not. Also, there is no point of showing the same images to the program to test, because the program already knows that the images used during training are shoes (images from testing should be different from training). 


2) Layers in fashion MNIST
* ".Flatten" takes the rectangular shape of the data, the 28 by 28 image and flatten that to a one dimensional array that can be processed in the next layer. ".relu" function states that if the output of the function is 0, set it to 0 because negative outputs can skew the results downward and it cancels out the positive outputs elsewhere. There are 10 neurons in the third and last layer because there are 10 pieces of clothing in the data set. Therefore, the job of the each of the neuron layers are to calculate the probability that a piece of clothing is for that particular class or category. 
