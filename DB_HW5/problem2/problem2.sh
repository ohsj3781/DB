#!/bin/bash
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
-input ./input \
-output ./output \
-mapper ./map.py \
-reducer ./reduce.py\