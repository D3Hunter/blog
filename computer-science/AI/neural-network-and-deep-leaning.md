 In the conventional approach to programming, we tell the computer what to do, breaking big problems up into many small, precisely defined tasks that the computer can easily perform. By contrast, in a neural network we don't tell the computer how to solve our problem. Instead, it learns from observational data, figuring out its own solution to the problem at hand.

two important types of artificial neuron (the perceptron and the sigmoid neuron)
A perceptron takes several binary inputs, x1,x2,…x1,x2,…, and produces a single binary output:
A way you can think about the perceptron is that it's a device that makes decisions by weighing up evidence.
`perceptron's bias`: b = −threshold.
it's conventional to draw an extra layer of perceptrons - the input layer - to encode the inputs: This notation for `input perceptrons`, in which we have an output, but no inputs
a network of perceptrons can be used to simulate a circuit containing many `NAND` gates. And because `NAND` gates are universal for computation, it follows that `perceptrons are also universal for computation`.
`Sigmoid neurons` are similar to perceptrons, but modified so that small changes in their weights and bias cause only a small change in their output.
Indeed, it's the smoothness of the `σ function` that is the crucial fact, not its detailed form.
`Δoutput` is a linear function of the changes `Δwj` and `Δb` in the weights and bias.
`σ function` is one of activation functions

- input layer
- output layer
- hidden layer: not input nor output
for historical reasons, such multiple layer networks are sometimes called `multilayer perceptrons` or `MLPs`, despite being made up of sigmoid neurons, not perceptrons. 
neural networks where the output from one layer is used as input to the next layer. Such networks are called `feedforward neural networks`.
neural networks in which feedback loops are possible. These models are called `recurrent neural networks`.
- Loops don't cause problems in such a model, since a neuron's output only affects its input at some later time, not instantaneously.

`cost function`: Sometimes referred to as a `loss or objective function`.

gradient descent
`stochastic gradient descent` can be used to speed up learning.

until we've exhausted the training inputs, which is said to complete an `epoch` of training. At that point we start over with a new training epoch.
η is a small, positive parameter (known as the `learning rate`)

`hyper-parameters` of the neural network - things like the `learning rate`, and so on
The lesson to take away from this is that debugging a neural network is not trivial
sophisticated algorithm ≤ simple learning algorithm + good training data.
∇C is called the `gradient vector`

`backpropagation`：a fast algorithm for computing such gradients

In any case, σ is commonly-used in work on neural nets, and is the `activation function` we'll use most often in this book.