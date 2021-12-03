def personal_inf(**kwargs):
    return ' '.join(kwargs.values())

params = {
    'name': input('enter name '),
    'surname': input('enter surname'),
}

print(personal_inf(**params))
