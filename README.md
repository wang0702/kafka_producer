# kafka_producer

## 环境配置
参考https://kafka.apachecn.org/quickstart.html
启动zookeeper服务器和kafka服务器，配置本地端口

`pip3 install kafka-python`

## 环境启动
`python producer.py`

## 说明
每秒生成一个1至1000的随机点，key为timestamp

后期会用kafka输出到flink进行进一步聚合计算，并将结果导入Redis中进行持久化操作。

利用Ray分布式计算对Redis中的结果进行机器学习拟合计算，输出各项指标。（练手项目）