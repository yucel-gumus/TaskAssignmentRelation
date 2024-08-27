from django.core.management.base import BaseCommand
from tasks.models import Person, Task, PersonTaskAssignment
from django.utils import timezone
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Örnek Data Ekleme'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20): 
            Person.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name()
            )
            Task.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.text()
            )

        persons = Person.objects.all()
        tasks = Task.objects.all()

        for _ in range(200):
            PersonTaskAssignment.objects.create(
                person=random.choice(persons),
                task=random.choice(tasks),
                frequency=random.randint(1, 10),
                last_completion_time=fake.date_time_this_decade()
            )

        self.stdout.write(self.style.SUCCESS('Data Ekleme Başarılı'))
