"""
CP1404 Prac9
Band class
"""


from musician import Musician

class Band:
def __init__(self, name=''):
self.name = name
self.members = []


def add_member(self, musician):
if isinstance(musician, Musician):
self.members.append(musician)
else:
raise TypeError('Band members must be Musician instances')


def __str__(self):
return f"{self.name}: {self.members}"


def play(self):
for m in self.members:
m.play()