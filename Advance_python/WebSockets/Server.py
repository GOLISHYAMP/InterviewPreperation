import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = {}  # Dictionary to store client connections


def broadcast_message(sender_addr, message):
    """Broadcast the message to all connected clients except the sender."""
    for addr, conn in clients.items():
        if addr != sender_addr:  # Do not send to the sender
            try:
                conn.send(message.encode(FORMAT))
            except Exception as e:
                print(f"[ERROR] Could not send message to {addr}: {e}")
                conn.close()
                del clients[addr]


def handle_client(conn, addr):
    """Handle communication with a single client."""
    print(f"[NEW CONNECTION] {addr} connected.")
    clients[addr] = conn  # Add the client to the list

    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)

                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    print(f"[DISCONNECT] {addr} disconnected.")
                else:
                    print(f"[{addr}] {msg}")
                    broadcast_message(addr, f"[{addr}] {msg}")  # Broadcast message
        except Exception as e:
            print(f"[ERROR] {addr} disconnected unexpectedly: {e}")
            break

    conn.close()
    del clients[addr]  # Remove the client from the list


def start():
    """Start the server to accept connections."""
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    print("[STARTING] Server is starting...")
    try:
        start()
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Server is shutting down...")
    finally:
        server.close()
