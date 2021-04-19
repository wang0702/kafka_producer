# kafka_producer

## 环境配置
参考https://kafka.apachecn.org/quickstart.html
启动zookeeper服务器和kafka服务器，配置本地端口

`pip3 install kafka-python`

## 环境启动
`python producer.py`

## 说明
每秒生成一个1至1000的随机点，key为timestamp
