import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# faker
import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fake_generator = Faker()
topics = ['Search', 'Social', 'Markerplace', 'News', 'Game']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for entry
        top = add_topic()

        # create fake data entry
        fake_url = fake_generator.url()
        fake_date = fake_generator.date()
        fake_name = fake_generator.company()

        # create webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        
        
        # create fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('populate script')
    populate(20)
    print('populate complete')

