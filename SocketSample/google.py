import socket

ip = socket.gethostbyname("google.com")
print("구글 아이피:{}".format(ip))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, 80))

s = "GET / HTTP/1.1\n\n"
sock.send(s.encode())
recv = sock.recv(4096)
print(recv)