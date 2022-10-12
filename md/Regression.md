# Regression

## three steps of regression

1. **define a model**

   > model = a set of function
   >
   > > for example
   > >
   > > > select Linear Model -- y = b + w * x
   > > >
   > > > a set of function just like y~1~ = 11.0 + 5.5 * x , y~2~ = 2.0 + 4.3 * x ，......
   
2. **goodness of function**

​		compute Loss Fuction L(f) = L(features) using Training data

3. **select the best f***

   test the average error by using Testing data



## Regression application in Pokemon

### How to predict the possible CP after evolution

0. **collect ten sets of data** $\rightarrow$ think factors may influence of CP : X~cp~, X~W~, X~Species~, X~h~...... 

1. **linear model y~cp~ = b + w $\times$ x~cp~**

> attention : upper label is one sample class, lower label is one feature of sample 

2. **goodness**

​	Loss function
$$
L(f) = L(w, b) =
	\sum\limits_{n=1}^{10}(\hat{y}^{n}-(b+w\times x_{cp}^{n}))^{2} \\
$$
​							$\Downarrow$ **but how to find the best w,b in f* ? (L only measure  the goodness)**

----

#### Gradient Descent(find the best f* in Linear Model)

+ randomly initiate w~0~, b~0~
+ compute $\frac{\partial L}{\partial w} _{w=w_{0}}$,  $\frac{\partial L}{\partial b} _{b=b_{0}}$

+ update $w_{1} = w_{0}-\frac{\partial L}{\partial w} _{w=w_{0}}$ , $b_{1} = b_{0}-\frac{\partial L}{\partial b} _{b=b_{0}}$

> **why subtract the partial?**
>
> A : you need to choose the direction that L is smaller, so when $\frac{\partial L}{\partial w} _{w=w_{0}}<0$ , you should increase w but $\frac{\partial L}{\partial w} _{w=w_{0}} < 0$ why you subtract

+ loop third step until find the **local optimal**

==!! local optimal is not global optimal, but in Linear Model local == global==

----

3. **find the best f***

​	compute average error in Testing datas

4. **improve the f**

+ redesign model 

​		When degree of f is higher, the average error of Traing datas is lower but the average error of Testing datas may like lower before and upper later(**overfitting**). So **choose the suitable degree** is vital.

+ consider more features 

  Species, Weight......

  too much features also cause overfitting......so suitable

  

## coding gradient descent



