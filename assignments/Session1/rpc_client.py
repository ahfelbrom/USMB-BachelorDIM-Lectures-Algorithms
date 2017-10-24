# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:37:33 2017

@author: bouleta

script used as a client in the cloudAMQP following the rpc method
"""

import pika
import uuid
import msgpack 
import msgpack_numpy as m 
import numpy

corr_id = str(uuid.uuid4())

def on_response(ch, method, properties, body):
    ##
    # Function used for the callback of the read method 
    # @param the chanel
    # @param the method used
    # @param the properties sent
    # @param the body of the message in queue
    if (properties.correlation_id == corr_id):
        print(body)
    else:
        raise Exception('l\'id de correlation est différent')


amqp_url = 'amqp://mchgowzq:gTrpIbR5nfC3qW7YyJ1x6-hpwcFLoW7-@lark.rmq.cloudamqp.com/mchgowzq'
params = pika.URLParameters(amqp_url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()

message = numpy.random.random((20,30)) 
request_msg = msgpack.packb(message,default = m.encode) 

result = channel.queue_declare(exclusive=True)
callback_queue = result.method.queue


channel.basic_publish(exchange='',
                           routing_key='rpc_queue',
                           properties=pika.BasicProperties(
                                 reply_to = callback_queue,
                                 correlation_id = corr_id,),
                                 body=str(request_msg))
print('[x] Sent message :)')

# wait for requests
channel.basic_consume(on_response, queue=callback_queue, no_ack=True)

channel.start_consuming()

connection.close()