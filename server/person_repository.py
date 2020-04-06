persons = [
    {
        'email': 'jeni@email.com',
        'name': 'Jeni Yanez',
        'phone': '1-800-AWESOME'
    },
    {
        'email': 'carlos@email.com',
        'name': 'Carlos Yanez',
        'phone': '1-800-AWESOME'
    },
    {
        'email': 'john@email.com',
        'name': 'Jonh Yanez',
        'phone': '1-800-AWESOME'
    }
]


def get_all_persons():
    return persons


def add_person(person):
    new_person = {
        'email': person['email'],
        'name': person['name'],
        'phone': person['phone']
    }
    uperson = update_person(person)
    if uperson is None:
        persons.append(new_person)
        return new_person
    return uperson

def find_person_by_email(email):
    person = [person for person in persons if person['email'] == email]
    if len(person) == 0:
        return None
    return person[0]


def update_person(person):
    uperson = find_person_by_email(person['email'])
    if uperson is not None:
        new_person = {
            'email': person['email'],
            'name': person['name'],
            'phone': person['phone']
        }
        persons[persons.index(uperson)] = new_person
        return new_person

    return None

def remove_person(email):
    person = find_person_by_email(email)
    if person is None:
        return None
    persons.remove(person)
    return person
