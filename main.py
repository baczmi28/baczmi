# ================================================
#               PYTHON MULTITOOL
# ================================================

import module_1_weather
import module_2_image
import module_3_todo
import module_4_password_generator
import module_5_network_scanner


def main_menu():
    print("WYBIERZ OPCJĘ Z MENU:")

    print()
    print("[1] WEATHER")
    print("Informacje o pogodzie")

    print()
    print("[2] IMAGE TOOLS")
    print("Analiza obrazu i metadanych")

    print()
    print("[3] TO-DO")
    print("Lista zadań do zrobienia")

    print()
    print("[4] PASSWORD GENERATOR")
    print("Generator haseł")

    print()
    print("[5] NETWORK SCANNER")
    print("Skanowanie sieci")

    print()
    print("[0] EXIT")


# ================================================
#          MODULE 4 - PASSWORD GENERATOR
# ================================================

def password_module():
    print()
    print("=" * 50)
    print("PASSWORD GENERATOR")
    print("=" * 50)

    input("\nNaciśnij ENTER, aby wrócić do menu")


# ================================================
#           MODULE 5 - NETWORK SCANNER
# ================================================

def network_scanner_module():
    print()
    print("=" * 50)
    print("NETWORK SCANNER")
    print("=" * 50)

    input("\nNaciśnij ENTER, aby wrócić do menu")


# ================================================
#           GŁÓWNA FUNKCJA PROGRAMU
# ================================================

def main():

    while True:

        main_menu()

        choice = input("Wybierz opcję: ")

        if choice == "1":
            module_1_weather.weather_module()

        elif choice == "2":
            module_2_image.image_module()

        elif choice == "3":
            module_3_todo.todo_module()

        elif choice == "4":
            module_4_password_generator.password_module()

        elif choice == "5":
            module_5_network_scanner.network_scanner_module()

        elif choice == "0":
            print("Zamykanie programu")
            break

        else:
            print("BŁĄD: Nieprawidłowa opcja")
            print("Wybierz liczbę od 0 do 5")

            input("\nNaciśnij ENTER, aby spróbować ponownie")


# ================================================
#              URUCHAMIANIE PROGRAMU
# ================================================

if __name__ == "__main__":
    main()
