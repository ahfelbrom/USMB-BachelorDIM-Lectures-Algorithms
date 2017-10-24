# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:06:57 2017

@author: bouleta

script used as a server in cloudAMQP following the rpc method
"""

import pika
import msgpack 
import msgpack_numpy as m


def coucou(request_param):
    ##
    # function used to process the message received
    # @param the message received
    # @return the response to be sent to the client
    decoded_message = msgpack.unpackb(request_param,object_hook = m.decode)    
    print(decoded_message)
    return 'fine and you ?'

def on_request(ch, method, properties, body):
    ##
    # Function used for the callback of the read method 
    # @param the chanel
    # @param the method used
    # @param the properties sent
    # @param the body of the message in queue
    request_param = body # retrieve input parameters
    response = coucou(request_param) #process the message
    ch.basic_publish(exchange='', #reply
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id = properties.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag) #acknowledge
    
amqp_url = 'amqp://mchgowzq:gTrpIbR5nfC3qW7YyJ1x6-hpwcFLoW7-@lark.rmq.cloudamqp.com/mchgowzq'
params = pika.URLParameters(amqp_url)
params.socket_timeout = 5

# initiate the connexion and setup the communication channel
connection = pika.BlockingConnection(params) 
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')
# wait for requests
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

channel.start_consuming()