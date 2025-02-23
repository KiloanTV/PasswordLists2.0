# Passwort-Generator

Dieses Python-Programm generiert eine vorgegebene Anzahl von zufälligen Passwörtern und speichert diese in einer .env-Datei.

## Funktionsweise

1. Generierung von zufälligen Passwörtern
2. Speicherung der Passwörter in einer `.env`-Datei

## Installation

1. Klone das Repository:
    ```bash
    git clone https://github.com/KiloanTV/PasswordHasher2.0.git
    ```

2. Wechsel in das Projektverzeichnis:
    ```bash
    cd PasswortHasher2.0
    ```

## Nutzung

1. Passe die Parameter für die Anzahl der Passwörter und die Länge der Passwörter nach Bedarf an:
    ```python
    num_passwords = 100
    password_length = 12
    ```

2. Führe das Skript aus:
    ```bash
    python generator.py
    ```

3. Nach der Ausführung wird eine Datei erstellt:
    - `passwords.env`: Enthält die generierten Passwörter

## Code

```python
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
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE](LICENSE) Datei für weitere Informationen.