import bcrypt
import os
import random
import string

# Anzahl der Passwörter, die generiert werden sollen
num_passwords = 100

# Länge der zufälligen Passwörter
password_length = 12

# Dateinamen
plain_passwords_file = "plain_server3.txt"
hashed_passwords_file = "hashed_server3.env"

# Listen, um die Passwörter zu speichern
plain_passwords = []
hashed_passwords = []

# Funktion zur Generierung eines zufälligen Passworts
def generate_random_password():
    print("generate next passwort")
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(password_length))

# Generiere und verschlüssele die Passwörter
for i in range(1, num_passwords + 1):
    print("encrypt next passwort!")
    plain_password = generate_random_password()
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    plain_passwords.append(f"PASSWORD_{i}={plain_password}")
    hashed_passwords.append(f"PASSWORD_{i}={hashed_password}")

# Schreibe die unverschlüsselten Passwörter in die .env-Datei
with open(plain_passwords_file, 'w') as f:
    print("write the clear text...")
    f.write('\n'.join(plain_passwords))

# Schreibe die verschlüsselten Passwörter in die Textdatei
with open(hashed_passwords_file, 'w') as f:
    print("write the hashed passwort...")
    f.write('\n'.join(hashed_passwords))

print(f"{num_passwords} Passwörter wurden generiert und in '{plain_passwords_file}' und '{hashed_passwords_file}' gespeichert.")