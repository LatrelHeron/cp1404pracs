"""
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

Tests
line 1: 18, 11, 19
line 2: 3, 3, 3
line 3: 4.784055021044187, 3.4541339522061927, 3.9100796083747524

line 1: smallest 5, largest 19
line 2: smallest 3, largest 9, and no line 2 could not produce a 4
line 3: smallest 2.5, largest 5.5
"""

import random

print(random.randint(0, 101))