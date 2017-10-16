# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:25:02 2017

@author: bouleta
"""

import pika

# publish
def publish():
    amqp_url = 'amqp://mchgowzq:gTrpIbR5nfC3qW7YyJ1x6-hpwcFLoW7-@lark.rmq.cloudamqp.com/mchgowzq'
    params = pika.URLParameters(amqp_url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue = 'presentation')
    channel.basic_publish( exchange = '',
                           routing_key = 'presentation',
                           body = 'Hello world ! ')
    print('[x] Sent message :)')
    connection.close()

# read
def read():
    amqp_url = 'amqp://mchgowzq:gTrpIbR5nfC3qW7YyJ1x6-hpwcFLoW7-@lark.rmq.cloudamqp.com/mchgowzq'
    params = pika.URLParameters(amqp_url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue = 'presentation')
    
    def callback(ch, method, properties, body):
        print("[x] received %r" % body)
    
    channel.basic_consume(callback,
                          queue = 'presentation',
                          no_ack = True)
    
    print('[*] Waiting for new messages. To exit, press CTRL+C')
    channel.start_consuming()
    
