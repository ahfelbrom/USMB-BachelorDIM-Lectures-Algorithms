# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:11:40 2017

@author: bouleta
"""

import pika
import argparse
import time

parser = argparse.ArgumentParser(description='-concurrency to keep message')
parser.add_argument('-concurrency',
                    dest='reader',
                    action='store_true',
                    help='Activate the acknowledging')
args = parser.parse_args()
concurrency = args.reader

amqp_url = 'amqp://mchgowzq:gTrpIbR5nfC3qW7YyJ1x6-hpwcFLoW7-@lark.rmq.cloudamqp.com/mchgowzq'
params = pika.URLParameters(amqp_url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue = 'presentation')
i = 0
def callback(ch, method, properties, body):
    global i
    i = i+1
    print("{0} received %r".format(i) % body)
    if (concurrency):
        channel.basic_ack(delivery_tag = method.delivery_tag)
        time.sleep(0.01)

if (concurrency):
    channel.basic_consume(callback,
                          queue = 'presentation',
                          no_ack = False)
    
    print('[*] Waiting for new messages. To exit, press CTRL+C')
    channel.start_consuming()
else:
    channel.basic_consume(callback,
                          queue = 'presentation',
                          no_ack = True)
    
    print('[*] Waiting for new messages. To exit, press CTRL+C')
    channel.start_consuming()