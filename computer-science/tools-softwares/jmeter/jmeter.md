A `test plan` describes a series of steps JMeter will execute when run.
`Thread group` elements are the beginning points of any test plan.
The controls for a thread group allow you to:
- Set the number of threads
- Set the ramp-up period
- Set the number of times to execute the test
Start with Ramp-up = number of threads and adjust up or down as needed.
By default, the thread group is configured to loop once through its elements.

JMeter has two types of Controllers: Samplers and Logical Controllers.
- Samplers tell JMeter to send requests to a server.
- Logic Controllers let you customize the logic that JMeter uses to decide when to send requests.

The Test Fragment element is purely for code re-use within Test Plans
Listeners provide access to the information JMeter gathers about the test cases while JMeter runs.

By default, a JMeter thread executes samplers in sequence without pausing. We recommend that you specify a delay by adding one of the available timers to your Thread Group.
Assertions allow you to assert facts about responses received from the server being tested.

Execution order
- Configuration elements
- Pre-Processors
- Timers
- Sampler
- Post-Processors (unless SampleResult is null)
- Assertions (unless SampleResult is null)
- Listeners (unless SampleResult is null)

The JMeter test tree contains elements that are both hierarchical and ordered. Some elements in the test trees are strictly hierarchical (Listeners, Config Elements, Post-Processors, Pre-Processors, Assertions, Timers), and some are primarily ordered (controllers, samplers).

### 注意事项
压测时tomcat的maxThreads要>=jmeter线程数num_threads, 否则很容易因为超时出错，实际测试发现maxThreads >= 2 * num_threads时（根据测试结果得到的一个大概的估计），max response time会下降，具体原因待研究

### perfmon
perfmon抓取保存的数据在elapse列中，且数值都乘了1000

### 把采集到的性能数据存储，使用Grafana展现
JMeter’s Backend Listener allows to plug an external database to store test results and performance metrics.
Grafana: Grafana is an open-source platform for time series analytics, which allows you to create real-time graphs based on time series data,

### performance test
- Collecting
- Aggregating
- Visualizing
- Interpreting
- Analyzing
- Reporting

