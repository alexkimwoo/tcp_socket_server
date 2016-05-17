#=======================================================================================================================
"""SOCKET SERVER V0.1"""
__author__      = "alexkimwoo"
__copyright__   = "Copyright 2016, Alex Kim Woo"

"""
CALL PROGRAM EXAMPLE
#=======================================================================================================================
import socket_server
import datetime
import time
import thread
#=======================================================================================================================
value = 0
#=======================================================================================================================
def now():
    return datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')
#=======================================================================================================================
def count():
    global value
    value += 1
    return value
#=======================================================================================================================
def server_business(name, delay):

    while True:

        rules = {'ping': 'pong', 'time': now(), 'r': count()}
        b = socket_server.Business(rules)

        resp_ping = b.process_data('ping')
        resp_time = b.process_data('time')
        resp_r = b.process_data('r')

        rules_result = (['ping', resp_ping],['time', resp_time],['r', str(resp_r)])
        b.refresh_data(rules_result)
        time.sleep(delay)

#=======================================================================================================================
try:
    thread.start_new_thread(server_business, ("SERVER_BUSINESS", 0.5, ) )
except Exception,err:
    print '%s' % str(err)
#=======================================================================================================================
socket_server.myServer(port=9000)
#=======================================================================================================================
while True:
   pass

"""
#=======================================================================================================================
try:
    import sys, os, time, datetime
    import thread
    import ConfigParser
    import SocketServer
    import threading
except Exception,import_lib_err:
    print 'IMPORT LIBRARIES FAILED . ERROR => %s' % import_lib_err
    exit()
    quit()
#=======================================================================================================================
server_responses = ()
#=======================================================================================================================
def now():
    return datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')
#=======================================================================================================================
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        global server_responses

        name = "SOCKET_SERVER"
        client = '%s:%s' % (self.client_address[0], self.client_address[1])
        print '[%s] %s | NEW CLIENT CONNECTED: %s' % (now(),name,client)
        start_time = datetime.datetime.today()

        while True:
            try:
                data = self.request.recv(100).strip()
                if not data:
                    print '[%s] %s | CONNECTION CLOSED: %s' % (now(),name,client)
                    break
                resp = 'null'
                resp_to_client = server_responses

                #print resp_to_client

                for n in resp_to_client:
                    if data == n[0]:
                        resp = n[1]
                        break
                    resp = '<%s> NO RESPONSE' % data

                if not resp:
                    break

                curr_time = datetime.datetime.today()
                delta = curr_time - start_time

                try:
                    resp2 = resp.replace('\r\n','')
                except:
                    resp2 = resp

                print '[%s] %s | CLIENT: %s (%s DAYS %.2d:%.2d:%.2d) - < RECEIVED: %s  >> RESPONSE: %s >' % (now(),name,client,delta.days,delta.seconds//3600,(delta.seconds//60)%60, delta.seconds%60, data, resp2)

                self.request.sendall(resp)

            except Exception,err:
                print '[%s] %s | CONECTION FAILED. ERROR => %s' % (now(),name,err)
                break

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
#=======================================================================================================================
class Business:
    server_business = {}
    def __init__(self, business):   #contrutor
        self.server_business = business

    def process_data(self,k):
        return self.server_business.get(k)

    def refresh_data(self,responses):
        global server_responses
        server_responses = responses
#=======================================================================================================================
class myServer:

    def __init__(self,port):

        HOST, PORT = '0.0.0.0', port
        server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
        ip, port = server.server_address

        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print '[%s] SOCKET_SERVER | SERVER STARTED (%s:%s)' % (now(),ip, port)

        try:
            while True:
                pass
        except KeyboardInterrupt:
            print '%s SOCKET_SERVER | SERVER CLOSED (%s:%s)' % (now(),ip, port)
            server.shutdown()
            server.server_close()

            try:
                sys.exit(0)
                exit()
                quit()
            except SystemExit:
                os._exit(0)
#=======================================================================================================================


