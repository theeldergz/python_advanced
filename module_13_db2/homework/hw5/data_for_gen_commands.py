import random

COUNTRIES = (
    'Russia', 'France', 'USA', 'Argentina', 'England', 'Belgium', 'Bulgaria',
    'Spain', 'Sweden', 'Switzerland', 'Iran', 'Australia', 'Netherlands',
    'Brazil', 'Italy', 'Colombia', 'Morocco', 'Germany', 'Senegal', 'Japan'
)

COMMAND_LVL_LIST = ('Weak', 'Middle', 'Middle', 'Strong')


def gen_command_template() -> list:
    command_country = random.choice(COUNTRIES)
    command_name: str = command_country + f' {random.randint(1, 100)}'

    result = [command_name, command_country]

    return result


def gen_group() -> list:
    commands = [gen_command_template() for _ in range(4)]
    for i in range(len(COMMAND_LVL_LIST)):
        commands[i].append(COMMAND_LVL_LIST[i])

    return commands



