import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to an IP or port
server_socket.bind(("localhost", 5665))

# Listen for connection
server_socket.listen(1)
print("Server is listening on port 5665...")

# Accept a conversation
conn, addr = server_socket.accept()
print(f"Connected by{addr}")

while True:
    # Receive message from client
    client_message = conn.recv(1204).decode()
    if client_message.lower() == "bye":
        print("Client ended the chat.")
        break
    print("Client:", client_message)

    # Send message to client
    server_message = input("You: ")
    conn.send(server_message.encode())
    if server_message.lower() == "bye":
        break

conn.close()
server_socket.close()