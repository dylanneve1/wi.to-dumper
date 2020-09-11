import random
import string

letters = string.ascii_lowercase
digits = string.digits
random_code = ( ''.join(random.choice(letters + digits) for i in range(16)) )

print ('https://wi.to/' + random_code)