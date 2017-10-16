# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:11:16 2017

@author: bouleta
"""

import pika

amqp_url = 'amqp://mchgowzq:gTrpIbR5nfC3qW7YyJ1x6-hpwcFLoW7-@lark.rmq.cloudamqp.com/mchgowzq'
params = pika.URLParameters(amqp_url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue = 'presentation')
channel.basic_publish( exchange = '',
                       routing_key = 'presentation',
                       body = 'mon penis bien profond dans ton nez')
print('[x] Sent message :)')
connection.close()