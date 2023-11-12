import random

class Organism:
    def init_org(self, HP=None, damage=None, speed=None, vid=None, protivnik=None ):
        self.HP=HP
        self.damage=damage
        self.speed=speed
        self.alive=True
        self.vid=vid
        self.stat=0
        self.protivnik=protivnik
    def alive(self):
        if self.HP<=0:
            self.alive=False
    def eat(self):
        self.random_cube=random.randint(1,3)
        if self.random_cube==3:
            self.speedRand=random.randint(1,50)
            if self.speedRand>=50:
                self.golod=100
class Lizard(Organism):
    def __init__(self):
        self.init_org(HP=200, speed=random.randint(1,5), damage=random.randint(1,5), vid="Lizard")
        self.speed+=7
        self.damage-=5
class Volk(Organism):            #Брат брату брат, если ты своему брату не брат, то твой брат тебе не брат, АУФ    *Безумно можно быть пееервым*
    def __init__(self):
        self.init_org(HP=200, speed=random.randint(1,5), damage=random.randint(1,5),vid="Volf")
        self.speed-=5
        self.damage+=5


auf=Volk()
geko=Lizard()

def battle(User, Vrag):
    atack=random.randint(1,20)+User.damage
    vragKD=15+Vrag.speed
    if atack>=vragKD:
        Vrag.HP -= random.randint(1, 20)+User.damage
        print("По ",str(Vrag.vid)," попали!")
        print("HP",str(Vrag.vid)," = ",str(Vrag.HP))
    else:
        print("По ",str(Vrag.vid)," Промахнулись!")
        print("HP",str(Vrag.vid)," = ",str(Vrag.HP))
i=1
while(i>0):
    battle(User=geko, Vrag=auf)
    if auf.HP<0:
        print("Ящер окаянный победил!")
        break
    input("Нажмите enter для продолжения!")
    battle(User=auf, Vrag=geko)
    if geko.HP<0:
        print("Волк пацанский победил!")
        break
    input("Нажмите enter для продолжения!")
input()
