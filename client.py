import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 5665))
print("Connected to server. Type 'bye' to exit.")

while True:
    # Send message to server
    message = input("You: ")
    client_socket.send(message.encode())
    if message.lower() == "bye":
        break
        
    # Receive message from server
    server_message = client_socket.recv(1024).decode()
    if server_message.lower() == "bye":
        print("Server ended the chat.")
        break
    print("Server:", server_message)

client_socket.close()   
