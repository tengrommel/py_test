#!/usr/bin/env python
# coding:utf-8
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明 channel
channel.queue_declare(queue='hello')
# 发布信息 'Hello World'
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()