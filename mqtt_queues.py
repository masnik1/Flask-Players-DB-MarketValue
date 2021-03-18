import pika

def send_message_to_checker(message, queue):

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue)

    channel.basic_publish(exchange='',
                      routing_key=queue,
                      body=message)
    connection.close()

