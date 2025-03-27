# Script to auto block IP's that are sniffing our "honey" ports. 
import socket
import os
import time

def listen( SockNum:int=22) -> str:
    SockNum
    instance=socket.create_server(("",SockNum), family=socket.AF_INET, backlog=None)        
    client_conn, client_address = instance.accept()
    instance.close() # close instance
    return(client_address)

def kick(SockNum:int)->None:
    os.system("conf")
    os.system(f"set firewall ipv4 name foo rule 1 source address{str(SockNum)}")
    os.system("commit")


while True:
    a=listen()
    kick(a)
    time.sleep(100)
    