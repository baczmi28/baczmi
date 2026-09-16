# Aktualny standard: NIST SP 800-63B-4 z lipca 2025 r.
# biblioteka secrets - do generowania prawdziwych haseł

# ================================================
#           MODULE 4 - PASSWORD GENERATOR
# ================================================

import string
import secrets

def password_module():

    print()
    print("=" * 50)
    print("PASSWORD GENERATOR")
    print("=" * 50)

    # Użytkownik określa budowę hasła
    lowercase = int(input("Ile małych liter: "))
    uppercase = int(input("Ile dużych liter: "))
    digits = int(input("Ile cyfr: "))
    special = int(input("Ile znaków specjalnych: "))

    # Znaki specjalne, których może używać generator
    special_characters = "!@#$%^&*?"

    # Tutaj będziemy przechowywać wszystkie znaki hasła
    password_characters = []

    # Dodawanie małych liter
    for i in range(lowercase):
        password_characters.append(
            secrets.choice(string.ascii_lowercase)
        )

    # Dodawanie dużych liter
    for i in range(uppercase):
        password_characters.append(
            secrets.choice(string.ascii_uppercase)
        )

    # Dodawanie cyfr
    for i in range(digits):
        password_characters.append(
            secrets.choice(string.digits)
        )

    # Dodawanie znaków specjalnych
    for i in range(special):
        password_characters.append(
            secrets.choice(special_characters)
        )

    # Losowe mieszanie wszystkich znaków
    password = ""

    while password_characters:

        random_index = secrets.randbelow(
            len(password_characters)
        )

        password += password_characters.pop(random_index)

    # Wyświetlenie hasła
    print()
    print("Wygenerowane hasło:")
    print(password)

    print("Długość hasła:", len(password))


    input("\nNaciśnij ENTER, aby wrócić do menu")