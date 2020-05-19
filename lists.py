#!/usr/bin/env python3.8

users = [
        {'admin': True, 'active': False , 'name': 'Kevin Bacon' },
        {'admin': False, 'active': True , 'name': 'Jennifer Garner' },
        {'admin': True, 'active': True , 'name': 'Jessica Alba' },
        {'admin': False, 'active': False , 'name': 'Leo Dicaprio' },
        {'admin': True, 'active': False , 'name': 'Elizabeth' },
        {'admin': False, 'active': True , 'name': 'Emma Stone' },
        {'admin': True, 'active': True , 'name': 'Alix' },
        {'admin': False, 'active': False , 'name': 'Alexa' },
        ]

line = 1

for user in users:
    prefix = f"{line} "

    if user['active'] and user['admin']:
        prefix += "ACTIVE - (ADMIN) "
    elif user['admin'] and not user['active']:
        prefix += "(ADMIN) "
    elif user['active'] and not user['admin']:
        prefix += "ACTIVE - "

    print(prefix + user['name'])
    line += 1
