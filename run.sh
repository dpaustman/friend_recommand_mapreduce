$HADOOP_HOME/bin/hdfs dfs -rm -r /hw1/largeoutput
$HADOOP_HOME/bin/Hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar \
-D mapred.reduce.tasks=20 \
-D mapred.map.tasks=20 \
-input "/hw1/LargeDataset.txt" \
-output "/hw1/largeoutput" \
-mapper /home/houxinyu1116/hadooptest/hadoop-2.7.4/largedata/mapper.py \
-reducer /home/houxinyu1116/hadooptest/hadoop-2.7.4/largedata/reducer.py \
-file /home/houxinyu1116/hadooptest/hadoop-2.7.4/largedata/mapper.py \
-file /home/houxinyu1116/hadooptest/hadoop-2.7.4/largedata/reducer.py

