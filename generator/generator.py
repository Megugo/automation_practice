import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')#.seed()
#faker_ru.seed()
def generated_person():
    yield Person(
        full_name= f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}",
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age= random.randint(10,80),
        salary= random.randint(1000,18000),
        department= faker_ru.job(),
        email= faker_ru.email(),
        current_address= faker_ru.address(),
        permanent_address= faker_ru.address()
    )