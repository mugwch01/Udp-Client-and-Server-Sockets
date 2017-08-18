#My name is Charles Mugwagwa. This is an implementation of a udp client socket that uses
#the services of the udp server socket that translates country names to their capitals

from socket import *

Server_addr = "localhost"
Server_port = 4300

if __name__ == '__main__':
    client_socket = socket(AF_INET, SOCK_DGRAM)   
    print("You are connected to the GEO101 server")
    message = input('Enter a country or "BYE" to quit: ')   
    while message != 'BYE':
        print(message)           
        client_socket.sendto(message.encode('utf-8'),(Server_addr,Server_port))
        Response_message, Server_addr2 = client_socket.recvfrom(5000)
        print(Response_message.decode('utf-8'))
        message = input('Enter another country or "BYE" to quit: ')           
    print("BYE!")
    client_socket.close()