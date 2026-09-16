# ================================================
#           MODULE 5 - NETWORK SCANNER
# ================================================

from scapy.all import IP, ICMP, sr1
import ipaddress
import time


# ================================================
#           ROZPOZNAWANIE SYSTEMU PO TTL
# ================================================

def recognize_system(ttl):

    if ttl >= 200:
        return "Prawdopodobnie urządzenie sieciowe"

    elif ttl >= 100:
        return "Prawdopodobnie Windows"

    elif ttl >= 50:
        return "Linux / Unix lub urządzenie sieciowe"

    else:
        return "System nieznany"

# ================================================
#               SKANOWANIE SIECI
# ================================================

def scan_network(network):

    print()
    print("=" * 50)
    print("SKANOWANIE SIECI")
    print("=" * 50)

    # Zamiana np. 172.20.10.0/28 na zakres adresów
    network_range = ipaddress.ip_network(network, strict=False)

    found = 0

    # Sprawdzamy każdy możliwy adres hosta
    for ip in network_range.hosts():

        ip = str(ip)

        print("Sprawdzam:", ip)

        packet = IP(dst=ip) / ICMP()

        start_time = time.perf_counter()

        response = sr1(
            packet,
            timeout=1,
            verbose=False
        )

        end_time = time.perf_counter()

        if response is not None:

            found += 1

            response_time = (end_time - start_time) * 1000

            ttl = response.ttl

            system = recognize_system(ttl)

            print()
            print("AKTYWNY HOST")
            print("IP:", ip)
            print("TTL:", ttl)
            print("Czas odpowiedzi:", round(response_time, 2), "ms")
            print("System:", system)
            print("-" * 50)

    if found == 0:
        print()
        print("Nie znaleziono hostów odpowiadających na ICMP.")


# ================================================
#               GŁÓWNA FUNKCJA
# ================================================

def network_scanner_module():

    print()
    print("=" * 50)
    print("NETWORK SCANNER")
    print("=" * 50)

    network = input(
        "Podaj adres sieci: "
    )

    scan_network(network)

    input("\nNaciśnij ENTER, aby wrócić do menu")