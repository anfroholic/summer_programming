con_conner = {
    'name': 'conner',
    'flush': .7,
    'munch': 24
}

fake_conner = {
    'name': 'fake connor',
    'flush': .17,
    'munch': 29
}

izzy = {
    'name': 'izzy',
    'light': {
        'state': True,
        'pin': 1
    }
}

wally = {
    'name': 'wally',
    'eva': {
        'name': 'eva',
        'state': False,
        'pin': 0
    },
    'motors': [
        {'name': 'Mr_Louie', 'can_id': 3},
        {'name': 'Sir_Louie', 'can_id': 4},
        {'name': 'Mrs_Rodger', 'can_id': 5},
        {'name': 'Jr_Rodger', 'can_id': 6}
    ]
}

driver = {}



# agents = {
#    'conner ': {
#         'self': conner,
#         'outputs': []
#     }
#
# }

# self.agents_dict['conner']['self'].check()s