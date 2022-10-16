# Deep Learning

很热门--google很多应用

## DL的起起伏伏

1958：Perceptron(linear model)--海军项目提出

1969：Perceptron有限制--被遮盖部分但是可以分辨哪些卡车哪些是tank??原来是因为data中卡车和坦克拍摄**亮度**不同  ***Perceptron臭掉***

1980s：**Multi-layer** perceptron（Neural network）--合并多个linear model,和今天的DNN没什么区别

1986：超过3层hidden layer就没有用了

1989：一层hidden layer就足够了  ***Multi-layer perceptron臭掉***

2006：**RBM initialization**--突破，用RBM初始化的Multi-layer perceptron，很复杂然鹅没什么用，但是激起大家的兴趣去研究  ***石头汤***

2009：**GPU**加速

2011：语音识别中DL技术很受欢迎

2012：赢了图像识别的比赛，开始受欢迎

## DL三步骤

1. define a set of function == neural network structure

----

### **Neuron Network**

一个神经元就是一个function，每个都有自己的weight和bias，输入一个向量，输出一个向量

多个连接的神经网络就是一个function set

![image-20221016154534699](.\images\image-20221016154534699.png)

![image-20221016155433578](.\images\image-20221016155433578.png)

上图每个layer的一个nueron会传给下一个layer的每个neuron值，然后下层layer每个neuron合并接收到上层每个neuron的值继续往前传  ***从后往前***

### **Deep == 很多hidden layer**

但是很多基于neuron network的都称自己为deep learning，即使只有一层

### feedforward neural network的矩阵操作

![image-20221016160541772](.\images\image-20221016160541772.png)

+ 首先，把输入的vector乘以一层layer的nueron权重再加上bias
+ 接着用某种func(比如说sigamo function)对结果再进行处理，产生新的vector继续往后传

![image-20221016161117934](.\images\image-20221016161117934.png)

矩阵运算用gpu优化

实际上中间的hidden layerS可以看成用来提取出input中最好的feature再进入output的多类分类器进行分类  ***hidden layers更新feature***

### Example application

数字辨识

![image-20221016163920307](.\images\image-20221016163920307.png)

将每个像素存入vector，记录特征（比如涂黑的是1，没有是0。。。），然后通过neural network（比如feedforward network）提取特征输出所有类别的可能性，得出结果

### ==Question==

怎么决定layer和neuron的数目？

A：直觉、经验、试验

自动确定network structure?

A：有

### DL和non-DL

+ non-DL需要feature transform（问题是如何找到比较好的feature）

+ DL需要design neural network（问题变成如何设计神经网络）

+ **但是**DL对输入的数据没有很大要求，扔进去就可以训练

+ 像语音、影像识别很难去定义出好的feature，因此用不同的network让他自己去找出好的feature是比较容易的

+ 在NLP问题上目前没有很明显的进步，但是长久来看还是有帮助的，可以帮人们找到没有发现的feature等等

----



2. goodness

定义loss

![image-20221016212943761](.\images\image-20221016212943761.png)

C^n^表示y^n^与$\head{y}^{n}$间的距离

![image-20221016165914077](.\images\image-20221016165914077.png)

找最好的w,--Gradient Descent

![image-20221016170118430](.\images\image-20221016170118430.png)

算微分的好方法--backpropagation一些工具tensorflow...

![image-20221016213744986](.\images\image-20221016213744986.png)

因此我们不用关注Total loss对每个参数的偏微分，只需要关注每个数据loss的偏微分

![image-20221016214118848](.\images\image-20221016214118848.png)

![image-20221016215035218](.\images\image-20221016215035218.png)

3. best f*

![image-20221016170604142](.\images\image-20221016170604142.png)