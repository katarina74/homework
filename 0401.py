import random

class Warrior:
    
    health=0
    name=""
    power=0

    def __init__(self,name):
        self.name=name
        self.power=random.randint(20,30)
        self.health=random.randint(100,150)
        
    def getHealthAndPower(self):
        return (self.power, self.health)
    
    def takeDamage(self,power):
        self.health-=power
        if self.health<=0:
            print(self.name," получил ",power," урона и погиб.")
        else:
            print(self.name," получил ",power," урона. ","Осталось ",self.health, " здоровья.")

class WarriorWithShield(Warrior):

    shield=0

    def __init__(self,name):
        Warrior.__init__(self,name)
        shield=random.randint(5,10)
    
    def takeDamage(self,power):
        self.health=self.health-power+self.shield
        if self.health<=0:
            print(self.name," получил ",power," урона и погиб.")
        else:
            print(self.name," получил ",power," урона. ","Осталось ",self.health, " здоровья.")


class Expert(Warrior):

    def getHealthAndPower(self):
        if random.random()<0.2:
            return (self.power*2, self.health)
        else:
            return (self.power, self.health)
    
# три воина
warrior1 = Warrior("Petya")
warrior2 = WarriorWithShield("Dima")
warrior3 = Expert("Serega")

print("атака воина 1: ", warrior1.getHealthAndPower()[0])
print("атака воина 2: ", warrior2.getHealthAndPower()[0])
print("атака воина 3: ", warrior3.getHealthAndPower()[0])

#битва двух воинов
while True:
    if warrior2.getHealthAndPower()[1]>0:
        warrior1.takeDamage(warrior2.getHealthAndPower()[0])
    else:
        print(warrior1.name, " won")
        break
    if warrior1.getHealthAndPower()[1]>0:
        warrior2.takeDamage(warrior1.getHealthAndPower()[0])
    else:
        print(warrior2.name, " won")
        break
# битва двух армий
army1=[warrior1,warrior2,warrior3,warrior4,warrior5,warrior6,warrior7,warrior8,warrior9,warrior10]=[Warrior("Petya"),Warrior("Petr"),Warrior("Petrucho"),Warrior("Petrovich"),WarriorWithShield("Dima"),WarriorWithShield("Dmitriy"),WarriorWithShield("Dimasik"),WarriorWithShield("Dimon"),Expert("Serega"),Expert("Seregey")]
army2=[warrior11,warrior12,warrior13,warrior14,warrior15,warrior16,warrior17,warrior18,warrior19,warrior20]=[Warrior("Petya1"),Warrior("Petr1"),Warrior("Petrucho1"),Warrior("Petrovich1"),WarriorWithShield("Dima1"),WarriorWithShield("Dmitriy1"),WarriorWithShield("Dimasik1"),WarriorWithShield("Dimon1"),Expert("Serega1"),Expert("Seregey1")]

i=0
while True:
    
    i+=1
    i1=random.randint(0,max(len(army1)-1,0))
    i2=random.randint(0,max(len(army2)-1,0))
    
    if army1!=[] and army2!=[]:
        if 1%2==1:
            army2[i2].takeDamage(army1[i1].getHealthAndPower()[0])
            if army2[i2].getHealthAndPower()[1]<0:
                del army2[i2]
        else:
            army1[i1].takeDamage(army2[i2].getHealthAndPower()[0])
            if army1[i1].getHealthAndPower()[1]<0:
                del army1[i1]
    else:
        if army1==[]:
            print("army2 won")
        else:
            print("army1 won")
        break
