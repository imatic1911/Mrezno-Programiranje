import socket

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "www.google.com"
        port = 80
        client_socket.settimeout(10)  # Postavi vremensko ograničenje na 10 sekundi
        client_socket.connect((host, port))
        print("Socket konekcija prema {} na portu {} je uspješno uspostavljena.".format(host, port))
        client_socket.close()
    except Exception as e:
        print("Došlo je do pogreške prilikom uspostavljanja konekcije:", e)

if __name__ == "__main__":
    main()
