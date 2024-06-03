# Passwort-Generator und -Hasher

Dieses Python-Programm generiert eine vorgegebene Anzahl von zufälligen Passwörtern, verschlüsselt diese mit bcrypt und speichert sowohl die Klartext- als auch die verschlüsselten Passwörter in separaten Dateien.

## Funktionsweise

1. Generierung von zufälligen Passwörtern.
2. Verschlüsselung dieser Passwörter mit bcrypt.
3. Speicherung der Klartext-Passwörter in einer `.txt`-Datei.
4. Speicherung der verschlüsselten Passwörter in einer `.env`-Datei.

## Installation

1. Klone das Repository:
    ```bash
    git clone https://github.com/KiloanTV/PasswordHasher2.0.git
    ```

2. Wechsel in das Projektverzeichnis:
    ```bash
    cd PasswortHasher2.0
    ```

3. Installiere die benötigten Python-Bibliotheken:
    ```bash
    pip install bcrypt
    ```

## Nutzung

1. Passe die Parameter für die Anzahl der Passwörter und die Länge der Passwörter nach Bedarf an:
    ```python
    num_passwords = 100
    password_length = 12
    ```

2. Führe das Skript aus:
    ```bash
    python advanced_passwortgenerator2.0.py
    ```

3. Nach der Ausführung werden zwei Dateien erstellt:
    - `plain.txt`: Enthält die generierten Klartext-Passwörter.
    - `hashed.env`: Enthält die verschlüsselten Passwörter.

## Code

```python
import bcrypt
import os
import random
import string

# Anzahl der Passwörter, die generiert werden sollen
num_passwords = 100

# Länge der zufälligen Passwörter
password_length = 12

# Dateinamen
plain_passwords_file = "plain.txt"
hashed_passwords_file = "hashed.env"

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
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE](LICENSE) Datei für weitere Informationen.