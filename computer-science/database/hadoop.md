## Hadoop vs MPP
https://0x0fff.com/hadoop-vs-mpp/

Given all this information, you can conclude why Hadoop cannot be used as a complete replacement of the traditional enterprise data warehouse, but it can be used as an engine for processing huge amounts data in a distributed way and getting important insights from your data.

## Hadoop
`Hadoop` is not a single technology, it is an ecosystem of related projects, which has its pros and cons.
- The biggest pro is extensibility
- As a con I can put the fact that building the platform of a separate technologies by yourself is a hell lot of work
    - and no one is doing it manually now
    - most of the companies are running pre-built platforms like the ones provided by `Cloudera` and `Hortonworks`.

Hadoop resource manager (YARN) is slower than MPP resource manager and sometimes not that good in managing concurrency.

## SQL interface for Hadoop
- Hive running on MR/Tez/Spark
    - it is an engine that translate SQL queries into MR/Tez/Spark jobs and executes them on the cluster.
    - All the jobs are built on top of the same MapReduce concept and give you good cluster utilization options and good integration with other Hadoop stack.
- SparkSQL
    - SparkSQL is a different beast sitting between the MapReduce and MPP-over-Hadoop approaches
- it might be Impala or HAWQ or IBM BigSQL
    - they are MPP execution engines on top of Hadoop working with the data stored in HDFS.
- it might be something completely different like Splice Machine.

## Architecture
`Simple Coherency Model` is a “`write-once-read-many access model for files`” that HDFS uses to simplify the data model in Hadoop. Once you “put” a file into `HDFS`, you can’t edit it to change the file. You can remove the file but once you write it, that is it.

## 3Vs
3Vs (volume, variety and velocity) are three defining properties or dimensions of big data.
- Volume refers to the amount of data
- variety refers to the number of types of data
- velocity refers to the speed of data processing.

According to the `3Vs model`, the challenges of `big data management` result from the expansion of all three properties, rather than just the volume alone -- the sheer amount of data to be managed.

