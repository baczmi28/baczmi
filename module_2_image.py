# ================================================
#           MODULE 2 - IMAGE TOOLS
# ================================================

import os                        # pliki i ścieżki
import requests                  # internet

from PIL import Image            # obraz
from PIL.ExifTags import TAGS    # nazwy metadanych EXIF

# ================================================
#   POBIERANIE OBRAZU Z INTERNETU / HUGGING FACE
# ================================================

def download_image():
    print()
    print("=" * 50)
    print("POBIERANIE OBRAZU Z INTERNETU")
    print("=" * 50)

    url = input("Podaj bezpośredni URL obrazu z Hugging Face: ")

    file_name = input("Podaj nazwę pliku, np. obraz.jpg: ")

    try:
        response = requests.get(url)

        # Sprawdzamy, czy pobieranie zakończyło się powodzeniem
        if response.status_code == 200:

            # Otwieramy nowy plik w trybie zapisu binarnego
            with open(file_name, "wb") as file:     # write binary
                file.write(response.content)

            print()
            print("Obraz został pobrany.")
            print("Zapisano jako: ", file_name)

            return file_name

        else:
            print("Błąd pobierania obrazu.")
            print("Kod odpowiedzi: ", response.status_code)

            return None

    except requests.RequestException:
        print("Wystąpił błąd podczas połączenia z internetem.")
        return None


# ================================================
#           WCZYTANIE OBRAZU Z KOMPUTERA
# ================================================

def load_local_image():
    print()
    print("=" * 50)
    print("OBRAZ Z KOMPUTERA")
    print("=" * 50)

    file_path = input("Podaj ścieżkę do obrazu: ")

    # Sprawdzamy, czy podany plik istnieje
    if os.path.isfile(file_path):
        return file_path

    else:
        print("Nie znaleziono podanego pliku.")
        return None


# ================================================
# PODSTAWOWE INFORMACJE O OBRAZIE
# ================================================

def show_image_info(file_path):

    try:
        image = Image.open(file_path)

        print()
        print("=" * 50)
        print("INFORMACJE O OBRAZIE")
        print("=" * 50)

        print("Nazwa pliku:", os.path.basename(file_path))
        print("Format:", image.format)
        print("Szerokość:", image.width, "px")
        print("Wysokość:", image.height, "px")
        print("Tryb kolorów:", image.mode)
        print("Rozmiar pliku:", os.path.getsize(file_path), "bajtów")

    except Exception as error:
        print("Nie udało się odczytać obrazu.")
        print("Błąd:", error)


# ================================================
# METADANE EXIF
# ================================================

def show_metadata(file_path):

    try:
        image = Image.open(file_path)

        exif_data = image.getexif()

        print()
        print("=" * 50)
        print("METADANE EXIF")
        print("=" * 50)

        # Sprawdzamy, czy obraz posiada dane EXIF
        if len(exif_data) == 0:
            print("Obraz nie posiada danych EXIF.")
            return

        # Przechodzimy przez wszystkie znalezione metadane
        for tag_id, value in exif_data.items():

            tag_name = TAGS.get(tag_id, tag_id)

            print(tag_name, ":", value)

    except Exception as error:
        print("Nie udało się odczytać metadanych.")
        print("Błąd:", error)


# ================================================
# ODCZYT I ZAPIS BINARNY
# ================================================

def save_binary(file_path):

    try:
        # rb = read binary
        # Odczytujemy cały obraz jako dane binarne
        with open(file_path, "rb") as file:
            binary_data = file.read()

        binary_file = file_path + ".bin"

        # wb = write binary
        # Zapisujemy dane do nowego pliku binarnego
        with open(binary_file, "wb") as file:
            file.write(binary_data)

        print()
        print("=" * 50)
        print("ZAPIS BINARNY")
        print("=" * 50)

        print("Liczba odczytanych bajtów:", len(binary_data))
        print("Dane binarne zapisano jako:")
        print(binary_file)

    except Exception as error:
        print("Nie udało się zapisać obrazu binarnie.")
        print("Błąd:", error)

# ================================================
# GŁÓWNA FUNKCJA MODUŁU IMAGE TOOLS
# ================================================

def image_module():

    while True:

        print()
        print("=" * 50)
        print("IMAGE TOOLS")
        print("=" * 50)

        print("[1] Pobierz obraz z Hugging Face / URL")
        print("[2] Wczytaj obraz z komputera")
        print("[0] Powrót do menu głównego")

        print()

        choice = input("Wybierz opcję: ")

        # ----------------------------------------
        # OBRAZ Z INTERNETU
        # ----------------------------------------

        if choice == "1":

            file_path = download_image()

            if file_path is not None:
                show_image_info(file_path)
                show_metadata(file_path)
                save_binary(file_path)

            input("\nNaciśnij ENTER, aby kontynuować...")


        # ----------------------------------------
        # OBRAZ LOKALNY
        # ----------------------------------------

        elif choice == "2":

            file_path = load_local_image()

            if file_path is not None:
                show_image_info(file_path)
                show_metadata(file_path)
                save_binary(file_path)

            input("\nNaciśnij ENTER, aby kontynuować...")


        # ----------------------------------------
        # POWRÓT
        # ----------------------------------------

        elif choice == "0":
            break


        # ----------------------------------------
        # BŁĘDNY WYBÓR
        # ----------------------------------------

        else:
            print("BŁĄD: Nieprawidłowa opcja.")
            print("Wybierz 0, 1 lub 2.")

            input("\nNaciśnij ENTER, aby spróbować ponownie...")