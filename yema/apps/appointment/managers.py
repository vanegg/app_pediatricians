from django.db import models

class AppointmentManager(models.Manager):
    def create(self, validated_data):
      print('Manager')
      print(validated_data)
    #     # crear un patient si no existe. 
    #   #validar hora de 8 a 8 
    #   validar horas cerradas
    #     # do something with the book
    #     return appointment