import random
import string

length = 12
characters = string.ascii_letters + string.digits

password = ''.join(random.choice(characters) for i in range(length))

print("Password kamu:", password)
