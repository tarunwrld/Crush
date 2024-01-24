import socket
import threading

# HOST= socket.gethostbyname(socket.gethostname())
HOST = '127.0.0.1'
# HOST ='122.162.145.251'
# # port = 55555
PORT = 1384
# # Replace "your_dynamic_dns_link.example.com" with your actual dynamic DNS hostname
# HOST = "212.ip.ply.gg"
# PORT = 1384

# # Resolve the hostname to its corresponding IP address
# try:
#     ip_address = socket.gethostbyname(HOST)
#     print("Resolved IP address:", ip_address)
# except socket.gaierror:
#     print("Unable to resolve the hostname.")
#     # exit()

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []
# Sending Messages To All Connected Clients
# def broadcast(message):
#     for client in clients:
#         client.send(message)
def broadcast(message):
    for client in clients:
        if isinstance(client, socket.socket):
            client.send(message)

# Handling Messages From Clients
def handle_connection(client):
    stop = False
    while not stop:
        try:
            # Check if the socket is still open
            if client.fileno() == -1:
                stop = True
                break
            
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"{nickname} left the chat!!".encode('utf-8'))
            client.close()
            stop = True


# def handle_connection(client):
#     stop = False
#     while not stop:
#         try:
#             # Broadcasting Messages
#             message = client.recv(1024)
#             broadcast(message)
#         except:
#             # Removing And Closing Clients
#             index = clients.index(client)
#             nicknames.pop(clients.index(client))
#             # clients.remove(client)
#             nickname = nicknames[index]
#             nickname.remove(nickname)
#             broadcast(f"{nickname} left the chat!!".encode('utf-8'))
#             stop = True

def main():
    print("#######################- ...SERVER IS RUNNING... -#######################")
    while True:
        client, addr = server.accept()
        print("Connected with {}".format(str(addr)))
        # print(f"connected to {addr}")

        client.send("NICK".encode('utf-8'))

        nickname = client.recv(2048).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print("Nickname is {}".format(nickname))
        # print(f"Nickname is {nickname}")

        broadcast("{} joined!".format(nickname).encode('ascii'))
        # broadcast(f"{nickname} joined the chat!!")

        client.send("You are now connected!!".encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle_connection, args=(client,))
        thread.start()

if __name__ == '__main__':
    main()

