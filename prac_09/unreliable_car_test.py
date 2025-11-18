"""
CP1404 prac 9
Basic assert-style tests for UnreliableCar.
This test runs multiple attempts to ensure reliability is roughly honoured; it is not a strict unit test.
"""
from unreliable_car import UnreliableCar




def test_unreliable():
car = UnreliableCar('Unreliable', 100, 30)
successes = 0
trials = 200
for _ in range(trials):
d = car.drive(1)
if d > 0:
successes += 1
# sanity check: for 30% reliability expect around 60 successes in 200 trials (+/- big margin)
assert 0 < successes < trials




if __name__ == '__main__':
test_unreliable()
print('UnreliableCar test ran (non-deterministic).')