# task 3
class PokemonBasic:

  def __init__(self, name = 'Default', hp = 0, weakness = 'None', type = 'Unknown'):
    self.name = name
    self.hit_point = hp
    self.weakness = weakness
    self.type = type

  def get_type(self):
    return 'Main type: ' + self.type

  def get_move(self):
    return 'Basic move: ' + 'Quick Attack'

  def __str__(self):
    return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness


# WRITE FROM HERE

class PokemonExtra(PokemonBasic):
    def __init__(self,name="Default",hp=0,weak=None,type=None,sec=None,*ex_mov):
        super().__init__(name,hp,weak,type)
        self.sec=sec
        self.ex_mov=ex_mov
        self.l_move=list(self.ex_mov)
        self.mov1=[]
        self.mov2=""
        for i in self.ex_mov:
            self.mov1=list(i)
        self.mov2+=" , ".join(self.mov1)
    def get_move(self):
        if len(self.ex_mov)==0:
            return "Basic move: Quick Attack"
        else:
            return f"Basic move: Quick Attack \nOther move: {self.mov2}"
    def get_type(self):
        if self.sec==None:
            return f"Main type: {self.type}, Secondary type:{self.sec}"

print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())

print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())

print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())
