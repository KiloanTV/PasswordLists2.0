import os
import random
import string

# Anzahl der Passwörter, die generiert werden sollen
num_passwords = 100

# Länge der zufälligen Passwörter
password_length = 12

# Dateinamen
passwords_file = "passwords.env"

# Listen, um die Passwörter zu speichern
plain_passwords = []

# Funktion zur Generierung eines zufälligen Passworts
def generate_random_password():
    print(".")
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(password_length))

# Generiere die Passwörter
for i in range(1, num_passwords + 1):
    plain_password = generate_random_password()
    
    plain_passwords.append(f"PASSWORD_{i}={plain_password}")

# Schreibe die Passwörter in die .env-Datei
with open(passwords_file, 'w') as f:
    f.write('\n'.join(plain_passwords)) 

print(f"{num_passwords} Passwörter wurden generiert und in '{passwords_file}' gespeichert.")
