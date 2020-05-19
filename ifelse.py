#!/usr/bin/env python3.8

user = {'admin': False, 'active': False , 'name': 'Kevin' }

if user['active'] and user['admin']:
    print(f"ACTIVE - (ADMIN) {user['name']}")
elif user['admin'] and not user['active']:
    print(f"(ADMIN) {user['name']}")
elif user['active'] and not user['admin']:
    print(f"ACTIVE - {user['name']}")
else:
    print(f"{user['name']}")
