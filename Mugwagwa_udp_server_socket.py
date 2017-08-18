#!/usr/bin/env python3
#encoding: UTF-8

#My name is Charles Mugwagwa. This is an implementation of a udp server socket that provides capitals of diff countries.

from socket import *
file = open('geo_world.txt','r')
capitals_dic = {}
print("Reading a file...")
for line in file:        
        line = line.split('-')
        country, capital = line[0].strip(),line[1].strip()        
        capitals_dic[country] = capital        
file.close()

HOST = "localhost"
PORT = 4300
if __name__ == "__main__":        
        server_socket = socket(AF_INET, SOCK_DGRAM)
        server_socket.bind((HOST, PORT))        
        print("Listening on %s:%d" % (HOST, PORT))      
        
        (msg, client_addr) = server_socket.recvfrom(5000)
        print("Connected: "+str(client_addr[0]))        
        while True:
                print("User query: "+msg.decode('utf-8'))
                if msg.decode('utf-8') in capitals_dic.keys():
                        server_socket.sendto(("+"+capitals_dic[msg.decode('utf-8')]).encode('utf-8'), client_addr)###if not there??
                else:
                        outmsg = "- There is no such country"
                        server_socket.sendto(outmsg.encode('utf-8'),client_addr)                
                (msg, client_addr) = server_socket.recvfrom(5000)
        print("Disconnected: "+client_addr[0])
        server_socket.close()        