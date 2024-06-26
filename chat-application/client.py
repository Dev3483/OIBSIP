import socket
import threading


HOST = '127.0.0.1'  # Localhost
PORT = 12345


def receive_messages(client_socket):
    """Receive messages from the server and display them."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\n{message}")
        except:
            print("An error occurred while receiving the message.")
            client_socket.close()
            break


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Connected to the server. You can start sending messages.")

    # Start a thread to receive messages from the server
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        try:
            message = input("")
            if message:
                client_socket.send(message.encode('utf-8'))
        except:
            print("An error occurred while sending the message.")
            client_socket.close()
            break


if __name__ == "__main__":
    main()
# this is client side python