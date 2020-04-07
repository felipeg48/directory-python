import requests


def get_person_by_email(email):
    person = requests.get('http://localhost:5000/persons/' + email)
    return person.json()


def save_person(name, email, phone):
    person = requests.post('http://localhost:5000/persons',json={'name':name,'email':email,'phone':phone})
    return person.json()


def delete_person_by_email(email):
    person = requests.delete('http://localhost:5000/persons/' + email)
    return person.json()


def get_all_persons():
    persons = requests.get('http://localhost:5000/')
    return persons.json()


