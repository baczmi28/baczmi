# ================================================
#               MODULE 3 - TO-DO
# ================================================

from colorama import Fore, Style, init
# Fore - zmienia kolor tekstu
# Back - zmienia kolor tła za tekstem
# Style - zmienia styl czcionki


# Uruchomienie kolorów w terminalu
init(autoreset=True)


# ================================================
#              WYŚWIETLANIE LISTY ZADAŃ
# ================================================

def show_tasks(tasks):
    print()
    print(Fore.BLUE + "=" * 50)
    print(Fore.BLUE + "LISTA ZADAŃ")
    print(Fore.BLUE + "=" * 50)

    if not tasks:
        print(Fore.YELLOW + "Brak zadań.")
        return

    print()
    print("[1] Widok listy")
    print("[2] Widok tabeli")

    view = input("Wybierz sposób wyświetlania: ")

    # --------------------------------------------
    #                WIDOK LISTY
    # --------------------------------------------

    if view == "1":

        print()

        for number, task in enumerate(tasks, start=1):

            if task["done"]:
                print(Fore.GREEN + f"{number}. [✓] {task['text']}")

            else:
                print(Fore.YELLOW + f"{number}. [ ] {task['text']}")

    # --------------------------------------------
    #               WIDOK TABELI
    # --------------------------------------------

    elif view == "2":

        print()
        print("-" * 60)
        print("ID | ZADANIE | STATUS")
        print("-" * 60)

        for number, task in enumerate(tasks, start=1):

            if task["done"]:
                status = "WYKONANE"
                color = Fore.GREEN

            else:
                status = "DO ZROBIENIA"
                color = Fore.YELLOW

            print(
                color
                + f"{number:<5}{task['text']:<35}{status:<20}"
            )

        print("-" * 60)

    else:
        print(Fore.RED + "Nieprawidłowy wybór.")


# ================================================
#               DODAWANIE ZADANIA
# ================================================

def add_task(tasks):
    print()
    print(Fore.BLUE + "=" * 50)
    print(Fore.BLUE + "                 DODAJ ZADANIE")
    print(Fore.BLUE + "=" * 50)

    text = input("Wpisz nowe zadanie: ").strip()

    if text == "":
        print(Fore.RED + "Zadanie nie może być puste.")
        return

    new_task = {
        "text": text,
        "done": False
    }

    tasks.append(new_task)

    print(Fore.GREEN + "Zadanie zostało dodane.")


# ================================================
#       OZNACZANIE ZADANIA JAKO WYKONANE
# ================================================

def complete_task(tasks):
    print()

    if len(tasks) == 0:
        print(Fore.YELLOW + "Brak zadań do oznaczenia.")
        return

    show_tasks(tasks)

    try:
        number = int(
            input("\nPodaj numer wykonanego zadania: ")
        )

        if number < 1 or number > len(tasks):
            print(Fore.RED + "Nie ma zadania o takim numerze.")
            return

        tasks[number - 1]["done"] = True

        print(Fore.GREEN + "Zadanie oznaczono jako wykonane.")

    except ValueError:
        print(Fore.RED + "Musisz podać liczbę.")


# ================================================
#                 USUWANIE ZADANIA
# ================================================

def delete_task(tasks):
    print()

    if len(tasks) == 0:
        print(Fore.YELLOW + "Brak zadań do usunięcia.")
        return

    show_tasks(tasks)

    try:
        number = int(
            input("\nPodaj numer zadania do usunięcia: ")
        )

        if number < 1 or number > len(tasks):
            print(Fore.RED + "Nie ma zadania o takim numerze.")
            return

        deleted_task = tasks.pop(number - 1)

        print(
            Fore.RED
            + "Usunięto zadanie: "
            + deleted_task["text"]
        )

    except ValueError:
        print(Fore.RED + "Musisz podać liczbę.")


# ================================================
#          STATYSTYKI I PROSTE OBLICZENIA
# ================================================

def show_statistics(tasks):
    print()
    print(Fore.BLUE + "=" * 50)
    print(Fore.BLUE + "                 STATYSTYKI")
    print(Fore.BLUE + "=" * 50)

    all_tasks = len(tasks)

    if all_tasks == 0:
        print(Fore.YELLOW + "Brak zadań do analizy.")
        return

    done_tasks = 0

    for task in tasks:
        if task["done"]:
            done_tasks += 1

    remaining_tasks = all_tasks - done_tasks

    percentage = done_tasks / all_tasks * 100

    print("Wszystkie zadania:", all_tasks)
    print("Wykonane:", done_tasks)
    print("Pozostałe:", remaining_tasks)
    print("Procent wykonania:", round(percentage, 1), "%")

    print()

    # Pasek postępu
    progress = int(percentage / 10)

    print(
        Fore.GREEN
        + "█" * progress
        + Fore.WHITE
        + "░" * (10 - progress)
    )


# ================================================
#              GŁÓWNE MENU MODUŁU TO-DO
# ================================================

def todo_module():
    tasks = []

    while True:

        print()
        print(Fore.BLUE + "=" * 50)
        print(Fore.BLUE + "TO-DO")
        print(Fore.BLUE + "=" * 50)

        print(Fore.YELLOW + "[1] Pokaż zadania")
        print(Fore.GREEN + "[2] Dodaj zadanie")
        print(Fore.BLUE + "[3] Oznacz jako wykonane")
        print(Fore.RED + "[4] Usuń zadanie")
        print(Fore.MAGENTA + "[5] Statystyki")
        print("[0] Powrót do menu głównego")

        print()

        choice = input("Wybierz opcję: ")

        if choice == "1":
            show_tasks(tasks)
            input("\nNaciśnij ENTER, aby kontynuować...")

        elif choice == "2":
            add_task(tasks)
            input("\nNaciśnij ENTER, aby kontynuować...")

        elif choice == "3":
            complete_task(tasks)
            input("\nNaciśnij ENTER, aby kontynuować...")

        elif choice == "4":
            delete_task(tasks)
            input("\nNaciśnij ENTER, aby kontynuować...")

        elif choice == "5":
            show_statistics(tasks)
            input("\nNaciśnij ENTER, aby kontynuować...")

        elif choice == "0":
            break

        else:
            print(Fore.RED + "BŁĄD: Wybierz liczbę od 0 do 5.")
            input("\nNaciśnij ENTER, aby spróbować ponownie...")