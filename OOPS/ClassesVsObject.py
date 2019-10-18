class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health -= self.damage

me = Fighter("Me")
you = Fighter("You")

me.attack(you)

print (you.health)
print (me.health)