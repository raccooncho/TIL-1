class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = level * 100
        self.power = level * 20 
        self.sp = 3

    def set_hp(self, point):
        self.hp += point

    def check_status(self):
        if self.hp > 0:
            return True
        else:
            return False
    
    def basic_attack(self, enemy):
        enemy.set_hp(-user.power)

    def critical_attack(self, enemy):
        if self.sp > 0:
            enemy.set_hp(-user.power * 1.5)
            self.sp -= 1
        else:
            print('you have no skill point for critical attack')
            print('use basic attack')
            enemy.set_hp(-user.power)

    def check_hp(self):
        return self.hp

    def level_up(self):
        self.level += 1
    


e1 = Pokemon('Enemy_1', 1)
e2 = Pokemon('Enemy_2', 10)
e3 = Pokemon('Enemy_3', 20)

#game start
start = input('Do you want to start the game? [y/n]')
if start == 'n':
    print('You have no choice! let\'s go to the Pokemon world!')
else:
    print('Ok! Let\s go to the Pokemon world!')
print()

# set id of user
print('you got a pokemon')
print('I think it needs a name')
print('please give me a idea of it')
id = input('What is the name of your Pokemon?')
if id == 'Mu':
    user = Pokemon(id, 999)
else:
    user = Pokemon(id, 1)

# meet Enemy_1
while user.level < 10:
    print(f'you met "{e1.name}"!')
    print()
    while user.check_status() and e1.check_status():
        print('please choose attack type')
        print('1) basic attack')
        print(f'2) critical attack - left[{user.sp}]')
        attack_type = input()
        print()    
        if attack_type == '1': #basic attack
            user.basic_attack(e1)
            print(f'you attack the {e1.name} and it got a {user.power} damege')
            print(f'{user.name} : {user.hp}')
            print(f'{e1.name} : {e1.hp}')
            print()
        else: #critical attack
            user.critical_attack(e1) 
            if user.sp > 0:                
                print(f'you attack the {e1.name} and it got a {user.power * 1.5} damege')
            else:                
                print(f'you attack the {e1.name} and it got a {user.power} damege')
            print(f'{user.name} : {user.hp}')
            print(f'{e1.name} : {e1.hp}')
            print()
        e1.basic_attack(user)  #enemy attack uesr
        print(f'{e1.name} attacks you!')
        print(f'{user.name} : {user.hp}')
        print(f'{e1.name} : {e1.hp}')
        print()
    if not user.check_status():
        print(f'{user.name} lose OTL ')
        print()
    elif not e1.check_status():
        print(f'{user.name} win! :-) ')
        print()
    user.level_up()
    print(f'{user.name} level up ! it becomes {user.level}', end='\n\n')
    user.hp = user.level * 100
    e1.hp = e1.level * 100
    user.sp = 3

# enemy_2 coming soon