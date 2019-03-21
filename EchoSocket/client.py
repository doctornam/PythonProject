import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("localhost", 5700))
    data = input("입력하세요:")
    sock.sendall(data.encode())
    response = str(sock.recv(1024), "utf-8")
    print("클라이언트 받음: {}".format(response))
