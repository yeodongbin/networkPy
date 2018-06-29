import socketserver
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('client connection : {0}'.format(self.client_address[0]))
        sock = self.request

        rbuff = sock.recv(1024)
        received = str(rbuff, encoding="utf-8")
        print('receive : {0}'.format(received))
        sock.close()

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('{0} <Bind IP>'.format(sys.argv[0]))
        sys.exit()

    bindIP = sys.argv[1]
    bindPort = 5425

    server = socketserver.TCPServer((bindIP, bindPort), MyTCPHandler)

    print('Server Start')
    server.serve.forever()



