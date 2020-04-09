# Random Forests (Ensembling)

![](images/2020-03-30-19-32-27.png)

![](images/2020-03-30-19-32-49.png)

![](images/2020-03-30-19-35-52.png)

![](images/2020-03-30-19-38-05.png)

![](images/2020-03-30-19-39-35.png)

## Out-of-Bag Estimation

I can be shown that for bagging (or bootstrapping), each tree will uses around 2/3 of the original observations. Therefore, for each observation, it will not be used to train 1/3 of the trees in the forest. We can use the 1/3 of the tree to predict the observation and aggregate all prediction scores. The out-of-bag error can be calculated by aggregating over the entire data set.

![](2020-04-09-14-36-36.png)
![](2020-04-09-14-37-12.png)
![](2020-04-09-14-37-36.png)
![](2020-04-09-14-37-58.png)
![](2020-04-09-14-38-22.png)