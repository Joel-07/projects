import random
from string import ascii_lowercase, ascii_uppercase, digits
l1 = []
a = "[@_!#$%^&*()<>?/|}{~:]"
l1.extend(random.sample(ascii_uppercase, 4)+random.sample(ascii_lowercase,
          4)+random.sample(a, 2)+random.sample(digits, 2))
random.shuffle(l1)
print("".join(l1))
