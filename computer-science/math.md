### Moving Average:
SMA
EMA
https://en.wikipedia.org/wiki/Moving_average
sample average VS population average
    https://en.wikipedia.org/wiki/Bessel%27s_correction
### Moving Standard Deviation
直接使用方差公式推导（Running Standard Deviation
    http://www.taylortree.com/2010/11/running-variance.html
    http://www.taylortree.com/2010/06/running-simple-moving-average-sma.html
    http://stackoverflow.com/questions/14635735/how-to-efficiently-calculate-a-moving-standard-deviation
计算moving Variance，然后得到Sdv
    https://en.wikipedia.org/wiki/Variance
    https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance
    使用Online algorithm和Welford
计算Sdv，使用EMA求周期内的均值
    比如30分钟内sdv，以1分钟粒度，求每分钟的sdv，使用EMA算法计算均值

### concepts
In probability and statistics, a `probability mass function (pmf)` is a function that gives the probability that a `discrete random variable` is exactly equal to some value.

A probability mass function differs from a `probability density function (pdf)` in that the latter is associated with continuous rather than discrete random variables; the values of the `probability density function` are not probabilities as such: a pdf must be integrated over an interval to yield a probability.

The `mode` of a set of data values is the value that appears most often. It is the value `x` at which its probability mass function takes its maximum value.
A `mode` of a `continuous probability distribution` is often considered to be any value `x` at which its `probability density function` has a locally maximum value, so any peak is a mode

In mathematics, a `moment` is a specific quantitative measure, used in both mechanics and statistics, of the shape of a set of points.

Given random variables X, Y, ..., that are defined on a probability space, the `joint probability distribution` for X, Y, ... is a probability distribution that gives the probability that each of X, Y, ... falls in any particular range or discrete set of values specified for that variable. In the case of only two random variables, this is called a `bivariate distribution`, but the concept generalizes to any number of random variables, giving a `multivariate distribution`.

A `sigmoid function` is a mathematical function having a characteristic `"S"-shaped curve` or `sigmoid curve`. Often, sigmoid function refers to the special case of the `logistic function`.
A `logistic function` or `logistic curve` is a common "S" shape (sigmoid curve)

A square matrix that is not invertible is called `singular` or `degenerate`. 
