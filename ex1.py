import subprocess
import re
import time

logfile_path = "/var/log/auth.log"
threshold = 3
ban_duration = "1m"

ip_count = {}
ip_banned = {}

#subprocess.run-y command line- hraman ashxatacnelu hamar e
def block_ip(ip):
    if ip not in ip_banned:
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
        print(f"Blocked IP: {ip}")
        ip_banned[ip] = True

# .* nshanakum e vor aystex mtnelu e kamayakan erkarutyamb ev kamayakan simvolnerov string isk (mijiny amen "[0-9]+"-y nshanakum e vor aystex linelu e mekic avel simvolner 0-9 ascii-i simvolnerov, isk "\."-y dnelu hamar e (pakagceri mijinn ynknum e group-i mej yst hertakanutyan))
#ete "search" funkciayov inch-vpr ban gtnvel e uremn group(i)-i mijiny kveragrvi ip-in, heto teci kunena qanakneri stugum tarorinak kerpov
def parse_log(logline):
    match = re.search(r"Failed password for .* from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", logline)
    if match:
        ip = match.group(1)
        if ip in ip_count:
            ip_count[ip] += 1
            if ip_count[ip] >= threshold:
                block_ip(ip)
        else:
            ip_count[ip] = 1

with open(logfile_path, "r") as logfile:
    for line in logfile:
        parse_log(line)

try:
    while True:
        with open(logfile_path, "r") as logfile:
            logfile.seek(0, 2)  # ijnum e fayli verj
            for line in logfile:
                parse_log(line)
        time.sleep(10)
except KeyboardInterrupt:
    print("Script terminated.")
