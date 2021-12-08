from django.forms import (Form, CharField)


class AtzimjuForma(Form):
    vārds = CharField()
    atzīmes = CharField()
