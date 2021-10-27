DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    
    all_python_devs_filter = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs_filter = list(map(lambda worker: worker['name'],all_python_devs_filter))
    
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    all_platzi_workers_filters = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers_filters = list(map(lambda worker: worker['name'],all_platzi_workers_filters))
    
    adults = [worker['name'] for worker in DATA if worker['age'] >= 18]

    adults_filter = list(filter(lambda worker: worker['age'] >= 18, DATA ))
    adults_filter = list(map(lambda worker: worker['name'], adults_filter))
    
    old_people = [{**worker, **{'old':worker['age'] > 70}} for worker in DATA]
    
    old_people_map = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))

    print ('All python developers: ')
    for worker in all_python_devs:
        print(worker)

    print ('\nAll python developers using high order functions: ')
    for worker in all_python_devs_filter:
        print(worker)

    print ('\nAll platzi workers: ')
    for worker in all_platzi_workers:
        print(worker)

    print ('\nAll platzi workers using high order functions: ')
    for worker in all_platzi_workers_filters:
        print(worker)

    print ('\nAdults: ')
    for worker in adults:
        print(worker)

    print ('\nAdults using high order functions: ')
    for worker in adults_filter:
        print(worker)

    print('\nOld into the dictionary')
    for worker in old_people:
        print(worker)

    print('\nOld into the dictionary using high order functions')
    for worker in old_people_map:
        print(worker)


if __name__ == "__main__":
    run()