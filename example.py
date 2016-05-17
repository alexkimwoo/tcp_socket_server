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














# import datetime
# import time
# #--------------------------------------------------------------------------------------
# class Server:
#     d = {}
#     def __init__(self, dic):   #contrutor
#         d = dic
#
#     def processa(self, k):   # o loop recebendo a mensagem
#         return d.get(k)
#
# #--------------------------------------------------------------------------------------
#
# def now():
#     return datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')
#
# value = 0
#
# def count():
#     global value
#     value += 1
#     return value
# #--------------------------------------------------------------------------------------
# d = {'ping': 'pong', 'time': now(), 'r': count()}
# s = Server(d)
#
# while True:
#     d = {'ping': 'pong', 'time': now(), 'r': count()}
#     print s.processa('ping')
#     print s.processa('time')
#     print s.processa('r')
#     time.sleep(1)
#=======================================================================================================================