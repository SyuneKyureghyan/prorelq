import socket
import sys

def scan_ports(target_ip, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET-y ip-n stugelu hamar e, SICET_STREAM y henc TCP-ov kapi hamar
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port)) #stugum e (SYN/ACK-ov) porty bac e te voch
        if result == 0:
            print(f"Port {port} is open") 
        sock.close()

if len(sys.argv) != 2:
    print("Usage: python3 your_script.py <target_ip>")
    sys.exit(1)

target_ip = sys.argv[1]
ports_to_scan = range(1, 65000)

print(f"Scanning ports on {target_ip}")
scan_ports(target_ip, ports_to_scan)
