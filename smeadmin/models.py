from django.db.models import Model, CharField, TextField


class CarnetDAdresse(Model):
    name = CharField(max_length=100)
    address = TextField(max_length=250)

    def __str__(self):
        return self.name

