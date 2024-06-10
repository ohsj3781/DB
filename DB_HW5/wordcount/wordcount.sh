#!/bin/bash
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
-input ./wordcount_input \
-output ./wordcount_output \
-mapper ./map.py \
-reducer ./reduce.py \
> output.txt
