import json


class Dumn:
    def __init__(self):
        self.name = 'popa'
        self.gugu = 4


def save_progress():
    a = Dumn()
    b = Dumn()
    
    trunk_template = [a.name,b.gugu]
    
    access_template = [a.name,b.gugu]
    
    to_json_1 = {'trunk': trunk_template, 'access': access_template}
    to_json_2 = {'trunk': trunk_template, 'access': access_template}
    
    with open('test.json', 'w') as f:
        f.write(json.dumps(to_json_1))
        f.write('\n')
        f.write(json.dumps(to_json_2))
    
    with open('test.json') as f:
        print(f.read())