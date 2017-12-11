### Concepts
- `tensor`: The central unit of data in TensorFlow which consists of a set of primitive values shaped into an array of any number of dimensions. A tensor's `rank` is its number of dimensions.
- `node`: takes zero or more tensors as inputs and produces a tensor as an output.
- `session`: encapsulates the control and state of the TensorFlow runtime.
- TensorBoard: a utility that can display a picture of the computational graph.
- placeholder: is a promise to provide a value later.
- A loss function measures how far apart the current model is from the provided data. 
- optimizers that slowly change each variable in order to minimize the loss function.
    - gradient descent
- tf.estimator is a high-level TensorFlow library that simplifies the mechanics of machine learning, including the following:
    - running training loops
    - running evaluation loops
    - managing data sets

`import tensorflow as tf`
MNIST is a simple computer vision dataset.

提出假设模型和优化策略
大量输入训练
依靠优化策略不断逼近并获得稳定
A one-hot vector is a vector which is 0 in most dimensions, and 1 in a single dimension.
### Model
- Softmax Regression.
    - Flattening the data
    - If you want to assign probabilities to an object being one of several different things, softmax is the thing to do, because softmax gives us a list of values between 0 and 1 that add up to 1.
    - first we add up the evidence of our input being in certain classes, 
    - then we convert that evidence into probabilities.
### Nodes
- constant
- operation
- Variable
    - To initialize all the variables in a TensorFlow program, you must explicitly call a special operation as follows:
    - `init = tf.global_variables_initializer()`
    - `sess.run(init)`


You might think of TensorFlow Core programs as consisting of two discrete sections:
- Building the computational graph.
    - A computational graph is a series of TensorFlow operations arranged into a graph of nodes.
- Running the computational graph.
