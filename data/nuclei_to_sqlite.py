import sqlite3
import json
import os
from datetime import datetime



def parse_nuclei_json(conn):

    file_path = '/home/user/project/nuclei_scan/result.out'

    with open(file_path, 'r') as file:
        data = json.load(file)

    scan = {}
    scan['port'] = 0
    scan['ip'] = '0'
    scan['extracted'] = '0'
    scan['remediation'] = '0'
    scan['description'] = '0'

    for l in data:
        scan['signature'] = str(l['info']['name'])
        scan['hostname'] = str(l['host'])

        if 'port' in l.keys():
            scan['port'] = int(l['port'])

        if 'ip' in l.keys():
            scan['ip'] = str(l['ip'])

        ltimestamp = l['timestamp']
        scan['timestamp'] = datetime.timestamp(datetime.fromisoformat(ltimestamp[:19]))*1000
        scan['severity'] = str(l['info']['severity'])

        if 'extracted-results' in l.keys():
            scan['extracted'] = str(l['extracted-results'])

        if 'remediation' in l['info'].keys():    
            scan['remediation'] = str(l['info']['remediation'])

        if 'description' in l['info'].keys():    
            scan['description'] = str(l['info']['description'])


        c = conn.cursor()
        
        c.execute("INSERT INTO scans (ip, hostname, port, signature, description, severity, extracted, remediation, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (scan['ip'], scan['hostname'], scan['port'], scan['signature'], scan['description'], scan['severity'], scan['extracted'], scan['remediation'], scan['timestamp']))
    
        conn.commit()

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    
    c.execute('''CREATE TABLE IF NOT EXISTS scans
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 ip TEXT,
                 hostname TEXT,
                 port INTEGER,
                 signature TEXT,
                 description TEXT,
                 severity TEXT,
                 extracted TEXT,
                 remediation TEXT,
                 timestamp INTEGER)''')


    
    conn.commit()
    return conn


def main():

    db_name = '/home/user/project/nmap-did-what/data/nuclei_results.db'

    os.system("docker run -v /home/user/project/nuclei_scan:/app/template  projectdiscovery/nuclei:latest -ni -l /app/template/target_list.txt  -je /app/template/result.out")

    conn = create_database(db_name)
    parse_nuclei_json(conn)

    conn.close()

if __name__ == '__main__':
    main()
