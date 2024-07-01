import os

nmap_str = 'nmap -sV -F --script=http-title,ssl-cert -oA /home/user/project/nuclei-nmap-dashboard/data/result.xml -iL /home/user/project/nuclei-nmap-dashboard/data/target.list'
convet_str = '/usr/bin/python3 /home/user/project/nuclei-nmap-dashboard/data/nmap-to-sqlite.py /home/user/project/nuclei-nmap-dashboard/data/result.xml'
print("start NMAP scan "+ nmap_str)
os.system(nmap_str)

print("Start convert")
os.system(convet_str)
