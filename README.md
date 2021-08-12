# Kafka_to_Hdfs
# Version used:
* Kafka _2.13-2.8.0
* pydoop 2.0.0
# KAFKA TASK 2: Write python program for producer and consumer and send stock data from producer to consumer and store it to hdfs.

* Step1:
* Create consumer.py and producer.py file and write the following code:

* Producer.py file
*  code is there inside the folder

* Consumer.py file
* code is there inside the folder

* Step2:
# start zookeeper
* bin/zookeeper-server-start.sh config/zookeeper.properties 
* Zookeeper started

# start kafka-server
* sudo bin/kafka-server-start.sh config/server.properties 
* Kafka-server /broker started


* Step3:
* Now execute the consumer.py file from the terminal and start producer .py file 
* It will create stocksdatakafka folder into hdfs and also copy blank data,txt file inside stocksdatakafka folder.
* Now execute producer.py we will get the output in consumer .py file now the program will start to write data into hdfs.

