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

We need a continuous and differentiable error function in order to use gradient decent.

![](2020-03-23-09-41-29.png)

We use activation function to let each unit returns continuous probabilities:

![](2020-03-23-10-03-10.png)

### Softmax
Essentially, we want to convert the generated scores (z) to probability range in [0, 1]. Since the z could be negative, we need to apply exponential before normalization.

![](2020-03-23-10-13-50.png)