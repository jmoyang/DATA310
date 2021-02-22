# Informal Reponse 3 (Feb. 21st) 

#### Modify the existing filter and if needed the associated weight in order to apply your new filters to the image 3 times. 
<img src="0x-4x0.png" width="500" height="400">

1. filter = [ [0, 1, 0], [1, -4, 1], [0, 1, 0]] 
* Changed the filters so it will have zeros on the four corners. It seems like it really emphasized rectangular shapes in the photo rather than emphasizing a single line, horizontally or vertically. It is a weird medium of a result created by a filter with vertical/horizontal emphasis.

<img src="02.png" width="500" height="400">

2. filter = [ [0, 2, -2], [-2, 0, 2], [2, -2, 0]]
* Changed the filters to have zeros go across the 3X3X3 matrix diagonally. As the image shows, the filter has put a great emphasis on diagonal line going from top left to the right bottom corner.  

<img src="03.png" width="500" height="400">

3. filter = [ [1, -1, 0], [2, -1, -1], [2, -1, -1]]
