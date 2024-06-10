#!/bin/bash
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
-input ./join_input \
-output ./join_output \
-mapper ./joinmap.py \
-reducer ./joinreduce.py
