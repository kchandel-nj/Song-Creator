# Libraries
from Note import Note

# File meant to test the Note class

a4 = Note("A", 4)
print(a4.frequency)
print(a4)
a5 = Note("A", 5)
print(a5.frequency)
a6 = Note("A", 6)
print(a6.frequency)
a3 = Note("A", 3)
print(a3.frequency)
a2 = Note("A", 2)
print(a2.frequency)

as4 = a4.halfStepUp()
print(as4.frequency)
print(as4)
b4 = as4.halfStepUp()
print(b4)
c4 = b4.halfStepUp()
print(c4)

g4 = Note("G", 4)
print(g4)
print(g4.halfStepUp())
print(g4.halfStepUp().halfStepUp())

name = "A"
name = chr(ord(name[0]) - 1)
print(name) # @

# Recall A4
print(a4.frequency)
print(a4.halfStepDown())
print(a4.halfStepDown().frequency)
print(a4.halfStepDown().halfStepDown())
print(a4.halfStepDown().halfStepDown().frequency)

# Check equality methods
print(a4 == Note("A", 4))
print(a4.__eq__(Note("A", 4)))

print(a4 < a4.halfStepDown())
print(a4 > a4.halfStepDown())

print(a4 < a4.halfStepUp())
print(a4 > a4.halfStepUp())