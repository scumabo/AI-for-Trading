# Introduction to Neural Networks
## **AND, OR, XOR** using neural networks

1. AND
![](2020-03-22-22-26-21.png)

2. OR
![](2020-03-22-22-27-54.png)

3. XOR
![](2020-03-22-22-28-41.png)
![](2020-03-22-22-30-35.png)

## Intuition: find the binary classification line.

Points correctly classified are good. Points are misclassified want the line to move closer to them. 

To move a line closer to a point, we just need to modify the line equation's coefficient by subtracting the points coordinates (with bias 1) (TODO: math?). We need to use a learning rate to control the speed of the line moving to the point.

![](2020-03-22-22-42-46.png)

Algorithm:

![](2020-03-22-23-34-34.png)

