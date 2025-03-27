# Script to auto block IP's that are sniffing our "honey" ports. 
import socket
import subprocess
import time

def listen( SockNum:int=22) -> str:
    SockNum
    instance=socket.create_server(("",SockNum), family=socket.AF_INET, backlog=None)        
    client_conn, client_address = instance.accept()
    instance.send(
"""⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠿⠛⠛⠋⠉⠉⠛⠛⠛⠻⢽⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⡾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠻⣖⣄⠀⠀⠀⠀
⠀⠀⢀⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠈⠻⣷⡄⠀⠀
⠀⢠⣾⠋⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣁⠀⠉⠉⠑⠲⣄⡀⠀⠀⠀⠀⠈⢾⣆⠀
⣰⣿⠃⠀⠀⠀⣰⣶⣶⣶⣿⣁⣀⠀⠉⠉⠓⠦⣄⡀⠀⠙⢶⡒⠲⢦⡀⠈⢯⣦
⣿⡇⠀⠀⢀⣴⠃⠀⠀⢹⣏⠉⠉⠉⠙⠲⢤⡀⠈⠱⠆⠀⠀⠙⠂⠀⢳⡀⠘⡿
⣻⠀⠀⣠⡿⠁⡀⠀⠄⣸⢿⡟⠲⠦⣄⡀⠀⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⢷
⣿⠀⣴⡟⡠⢡⢐⢉⣼⣇⡈⠳⣤⣀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢺
⣿⣼⠏⡴⡑⢆⣪⣾⣁⠉⠙⠛⠶⢯⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡥⣻
⣿⣏⡜⣲⡙⣶⠟⣿⣿⣿⣶⣦⣤⣀⡈⠉⠻⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠻
⠹⣿⡜⢦⣽⠏⠀⠘⢿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣙⣲⣤⡄⠀⠀⠀⠀⠀⠀⢘⠀
⠀⠘⢿⣿⠃⠐⠠⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⠀⠀⠀⠀⠀⠀⢨⠀
⠀⠀⠈⠻⣿⣤⠁⠂⠄⡀⠀⠀⠈⠉⠙⠛⠋⠉⠉⢸⣯⢽⣇⠀⠀⠀⠀⠀⡂⢸
⠀⠀⠀⠀⠈⠻⢿⣦⣔⡠⠁⠂⢄⠠⠀⠄⠠⠐⡀⢸⣯⢎⣿⣆⣀⡀⣀⣴⡱⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠛⡽⣷⣾⣦⣤⣥⣬⡤⣵⣶⣾⡿⣟⠊⡙⣒⠛⠓⠉⠀⠀""")
    instance.close() # close instance
    return(client_address)

def kick(SockNum:str)->None:
    print(SockNum)


while True:
    a=listen()
    kick(a)
    time.sleep(100)
