'''
소켓은 서버와 클라이언트의 역할로 나뉨

서버                                    클라이언트
1. 소켓 생성                            1. 소켓생성
2. 바인딩(bind())                       2. 바인딩 해도 그만 안해도 그만
3. 접속 대기(listen())                  3. 접속 시도(connect())
4. 접속 수락(accept())                  4.
5. 데이터 송/수신 (send()/receive())     5. 데이터 송/수신(send() / receive() )
6. 접속종료(close())                     6. 접속종료 (close())
'''

import socket

print("1. 소켓생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("2. 바인딩")
sock.bind(("", 9700))

print("3. 접속대기")
sock.listen()

print("4. 접속수락")
c_sock, addr = sock.accept()

print("5. 데이터 수신")
read_data = c_sock.recv(1024)

print("수신:{}".format(read_data))

print("6. 접속종료")
c_sock.close()
sock.close()
