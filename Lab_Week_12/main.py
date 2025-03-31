from mammal import Mammal
from person import Person
from puma import Puma
from tick import Tick

# Create a generic mammal
m = Mammal(age=5)
m.speak()
print()

# Create a person
p = Person(name="Alice", age=30, height=165)
p.speak()
p.heart.beat()
print(p)
print()

# Create a tick
t = Tick()
t.suck_blood()
print()

# Create a puma with a tick
pu = Puma(age=4, tick=t)
pu.speak()
pu.tick.suck_blood()