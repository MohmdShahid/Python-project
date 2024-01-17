import socket

IP_ADDRESS = '192.168.253.146'
# PORT = 139

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    # try:
    #     s.connect((IP_ADDRESS,PORT))
    #     print(f'port {PORT} is open and listining')
    # except:
    #     print(f'Failed to connect to port {PORT}')

    # PORT SCANNER WHICH IS CLOSED OR OPEN
    for port in range(100,150):
        try:
            s.connect((IP_ADDRESS, port))
            print(f'port {port} is open and listining')
        except:
            print(f'port {port} is closed')
