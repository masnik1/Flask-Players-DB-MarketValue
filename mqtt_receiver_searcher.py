import pika, sys, os
from sql_data import insert_players_values

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='check_player')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        body = body.decode("utf-8")
        name = body.split(',')[0]
        age = body.split(',')[1]
        club = body.split(',')[2]
        position = body.split(',')[3]
        market_value = body.split(',')[4]
        insert_players_values(name, age, club, position, market_value)
       
    channel.basic_consume(queue='check_player', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)