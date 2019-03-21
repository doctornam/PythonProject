import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(("localhost", 5700))
    sock.listen(1)
    conn, addr = sock.accept()
    msg = conn.recv(1024)
    print("서버받음: {}".format(msg))
    conn.sendall(msg)
    conn.close()

