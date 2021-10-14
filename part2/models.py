from django.db import models
from typing import List


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    is_favorite = models.BooleanField(help_text="True mean's favorite, False mean's not favorite")


def create_contact(name:str,  email:str, phone:str, is_favorite:bool):
    new_contact = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    new_contact.save()
    return new_contact


def all_contacts():
    return Contact.objects.all()

def favorite_contacts() :
    return Contact.objects.filter(is_favorite=True)


def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except Contact.DoesNotExist:
        return None

def delete_contact(name):
    contact = find_contact_by_name(name)
    contact.delete()
    

def update_contact_email(name, email):
    contact = find_contact_by_name(name=name)
    contact.email = email
    contact.save()

# def update_contact_email(name, email):
#     Contact.objects.filter(name=name).update(email=email)