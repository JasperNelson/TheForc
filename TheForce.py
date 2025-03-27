# Script to auto block IP's that are sniffing our "honey" ports. 
import socket
import subprocess
import time

def listen( SockNum:int=22) -> str:
    SockNum
    instance=socket.create_server(("",SockNum), family=socket.AF_INET, backlog=None)        
    client_conn, client_address = instance.accept()
    instance.send(
b"""⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠿⠛⠛⠋⠉⠉⠛⠛⠛⠻⢽⣦⣄⡀⠀⠀⠀⠀⠀⠀
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
    print(client_address)
    return(client_address)

while True:
    listen()
    time.sleep(100)
