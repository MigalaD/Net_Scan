import psutil
import time

# Tworzenie listy aktualnych połączeń
current_connections = psutil.net_connections()

while True:
    # Sprawdzenie aktualnych połączeń
    new_connections = psutil.net_connections()

    # Przeszukanie nowych połączeń i sprawdzenie, czy nie są one już na liście aktualnych połączeń
    for conn in new_connections:
        if conn not in current_connections:
            # Jeśli znaleziono nowe połączenie, wyświetlenie informacji o nim
            print(f"Nowe połączenie: {conn}")

    # Zaktualizowanie listy aktualnych połączeń
    current_connections = new_connections

    # Poczekanie kilka sekund przed ponownym sprawdzeniem połączeń
    time.sleep(5)
