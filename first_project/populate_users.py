import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

from first_app.models import User
from faker import Faker

fake_generator = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fake_generator.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]

        fake_email = fake_generator.email()

        #new db entry
        user = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]

if __name__ == '__main__':
    print('start')
    populate(20)
    print('end')        