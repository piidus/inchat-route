import socket
import threading

class Connection:
    ip =  '103.172.92.27' #'192.168.0.100'
    port = 9998
    def __init__(self, user,ip_addr = ip, port=port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip_addr, port))
        self.user_name = user.encode('utf-8')
        self.sock.send(self.user_name)
        # receive_thread = threading.Thread(target=receive_messages, args=(self.sock,))
        # receive_thread.start()
   

    def message_sent(self,receiver, message):
        full_message = f"{receiver}: {message}"
        self.sock.send(full_message.encode('utf-8'))
        print('[SEND MESSAGE]', message)
    
    def receive(self):
        print('received from server in coonnection')
        return self.sock.recv(1024).decode('utf-8')

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\nReceived: {message}")
        except ConnectionResetError:
            break

def main(username:str):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('103.172.92.27', 9998))
    
    # username = input("Enter your username: ")
    client.send(username.encode('utf-8'))
    
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    
    while True:
        recipient = input("Enter recipient username: ")
        message = input("Enter message: ")
        full_message = f"{recipient}: {message}"
        client.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    main(username="admin")