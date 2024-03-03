import pika
from faker import Faker
from models import Contact
from mongoengine import connect
from Web_8.connect import connect


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue')
    number_contacts = 10

    fake = Faker('uk_UA')
    for _ in range(number_contacts):
        full_name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        contact = Contact(full_name=full_name, email=email, phone_number=phone_number)
        contact.save()
        print(f"Contact {full_name} ({email}) successfully added to database")

        message_body = str(contact.id)
        channel.basic_publish(exchange='', routing_key="email_queue", body=message_body)
        print(f"Message for contact {full_name} ({email}) has been added to email_queue")

    connection.close()


if __name__ == '__main__':
    main()
