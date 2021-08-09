"""
@Author: Rikesh Chhetri
@Date: 2021-08-07 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-08-07 07:03:30
@Title : Program Aim to send stock data from producer to consumer and store into to hdfs
"""
from kafka import KafkaConsumer
import pydoop.hdfs as hdfs
import subprocess
consumer = KafkaConsumer('testtopic')
hdfs.mkdir('hdfs://localhost:9000/stocksdatakafka')
file = '/home/rikesh/data.txt'
args_list = [ 'hdfs', 'dfs', '-put',file, '/stocksdatakafka']
print('Running system command: {}'.format(' '.join(args_list)))
proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc.communicate()
hdfs_path = 'hdfs://localhost:9000/stocksdatakafka/data.txt'


for message in consumer:
    values = message.value.decode('utf-8')
    with hdfs.open(hdfs_path, 'at') as f:
        f.write(f"{values}\n")
        
        
       
        

    










