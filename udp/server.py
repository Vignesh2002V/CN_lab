import socket

HOST = '127.0.0.1'
PORT = 65432

print('------------------ Server ------------------')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        if not data:
            break

        filename = data.decode('utf-8')
        print(f'Received Filename: {filename} From: {addr}')

        try:
            with open(filename, 'r') as f:
                data = f.read()
            data = bytes(data, 'utf-8')
        except:
            data = bytes(f'File {filename} not found', 'utf-8')

        sock.sendto(data, addr)
        print(f'Sent: {data} To: {addr}')
        print()
