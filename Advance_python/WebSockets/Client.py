import socket
import threading

PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "192.168.0.103" # Replace with server IP
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_message(msg):
    """Send a message to the server."""
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def receive_messages():
    """Continuously listen for messages from the server."""
    while True:
        try:
            message = client.recv(2048).decode(FORMAT)
            print(message)
        except Exception as e:
            print(f"[ERROR] Connection lost: {e}")
            break


# Start a thread to listen for incoming messages
receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

print("Type your messages below. Type 'exit' to exit.")
while True:
    message = input()
    if message == 'exit':
        send_message(DISCONNECT_MESSAGE)
        break
    send_message(message)


client.close()
