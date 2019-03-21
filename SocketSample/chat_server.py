import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    # 접속 유저 관리
    users = {}

    def sendToAll(self, msg):
        for sock, addr in self.users.values():
            sock.send(msg.encode())

    def deleteUser(self, nickname):
        if nickname not in self.users:
            return
        
        del self.users[nickname]
        self.sendToAll("[{}] 님이 퇴장하셨습니다.".format(nickname))
        print("현재 참여중 {} 명".format(len(self.users)))

    def addUser(self, nickname, c_sock, addr):
        # 이미 등록된 닉네임인 경우
        if nickname in self.users:
            c_sock.send("이미 등록된 닉네임 입니다.\n".encode())
            return None
        # 새로운 유저인경우
        self.users[nickname] = (c_sock, addr)
        self.sendToAll("[{}]님이 입장 했습니다.".format(nickname))
        print("현재 참여중 {} 명".format(len(self.users)))
        return nickname

    def handle(self):
        print("[{}] 접속 연결됨".format(self.client_address[0]))

        while True:
            self.request.send("채팅 닉네임을 입력하세요: ".encode())
            nickname = self.request.recv(1024).decode()
            if self.addUser(nickname, self.request, self.client_address):
                break
        
        while True:
            msg = self.request.recv(1024)
            print(msg)
            if msg.decode() == "/bye":
                self.request.close()
                break
            self.sendToAll("[{}] {}".format(nickname, msg.decode()))
        
        self.deleteUser(nickname)
        print("[{}] 접속종료".format(self.client_address[0]))

class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

chat = ChatServer(("", 9700), MyHandler)
chat.serve_forever()
chat.shutdown()
chat.server_close()