import socket

HOST = '127.0.0.1'
PORT = 65432

print('------------------ Client ------------------')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        filename = input('Enter file to request from server: ')

        if not filename:
            break

        sock.sendall(bytes(filename, 'utf-8'))
        print(f'Sent: {filename}')

        data = sock.recv(1024).decode('utf-8')
        print(f'Received: {data}')
        print()
