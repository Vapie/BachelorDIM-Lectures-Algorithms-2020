# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:56:03 2020

@author: tapiev
"""

import pika 



count = 0
f = open("P:\\Git_algo\key.txt", "r")
connec_string = f.read()
print(connec_string)
connection = pika.BlockingConnection(pika.URLParameters(connec_string))
channel=connection.channel()
channel.queue_declare(queue='hello')

def callback(ch,method,properties,body):
    print(" [x] Received %r" % body)
    global count
    count +=1
    print("number of received event : " + str(count))
    

channel.basic_consume(queue='hello',
                      on_message_callback = callback,
                      auto_ack=True)
print(' [*] Waiting for messages. o exit press CTRL+C')
channel.start_consuming()