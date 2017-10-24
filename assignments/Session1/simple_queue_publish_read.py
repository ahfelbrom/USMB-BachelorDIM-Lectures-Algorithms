# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:25:02 2017

@author: bouleta

script used to publish / read in clouamqp following the command we use
"""

import pika
import argparse

parser = argparse.ArgumentParser(description='-read for read')
parser.add_argument('-read',
                    dest='reader',
                    action='store_true',
                    help='Activate the read mode')
args = parser.parse_args()
read = args.reader
amqp_url = 'amqp://mchgowzq:gTrpIbR5nfC3qW7YyJ1x6-hpwcFLoW7-@lark.rmq.cloudamqp.com/mchgowzq'
params = pika.URLParameters(amqp_url)
params.socket_timeout = 5
    
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='presentation')

i = 0
def callback(ch, method, properties, body):
    ##
    # Function used for the callback of the read method 
    # @param the chanel
    # @param the method used
    # @param the properties sent
    # @param the body of the message in queue
    global i
    i = i+1
    print("{0} received %r".format(i) % body)

if(read):
        channel.basic_consume(callback,
                              queue='presentation',
                              no_ack=True)
        print(" [*] Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()
else:
   channel.basic_publish(exchange='',
                         routing_key='presentation',
                         body='AaAaAaAaA')
   print(" [x] Sent 'Hello World!'")
   connection.close()