# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:11:16 2017

@author: bouleta

script used to publish a message in cloudAMQP
"""

import pika
import argparse

parser = argparse.ArgumentParser(description='-concurrency to keep message')
parser.add_argument('-concurrency',
                    dest='reader',
                    action='store_true',
                    help='activate the message keeping')
args = parser.parse_args()
concurrency = args.reader
amqp_url = 'amqp://mchgowzq:gTrpIbR5nfC3qW7YyJ1x6-hpwcFLoW7-@lark.rmq.cloudamqp.com/mchgowzq'
params = pika.URLParameters(amqp_url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue = 'presentation')

if (concurrency):
    for x in range(1000):        
        channel.basic_publish( exchange = '',
                               routing_key = 'presentation',
                               body = 'coucou, j\'aime les chewing-gum',
                               properties=pika.BasicProperties(
                                   delivery_mode = 2
                               ))
        print('[x] Sent message :)')
    connection.close()
else:
    channel.basic_publish( exchange = '',
                           routing_key = 'presentation',
                           body = 'coucou, j\'aime les chewing-gum')
    print('[x] Sent message :)')
    connection.close()