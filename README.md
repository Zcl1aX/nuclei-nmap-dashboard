# nmap-did-what and nuclei dashboard

**nmap-did-what** is a Grafana docker container and a Python script to parse Nmap XML output to an SQLite database. The SQLite database is used as a datasource within Grafana to view the Nmap scan details in a dashboard.

Full Tutorial for nmap part is available here - [Nmap Dashboard using Grafana](https://hackertarget.com/nmap-dashboard-with-grafana/)

![Grafana Dashboard](https://hackertarget.com/images/nmap-grafana-dashboard.webp)

## Overview

The project consists of two main components:

1. A Python script that parses Nmap XML output and Nuclei json output and stores the data in an SQLite database.
2. A Grafana Docker container with a pre-configured dashboard for visualizing the Nmap scan and Nuclei scan data.


## Usage

To get started with nmap-did-what, ensure you have Docker and Docker Compose installed on your system.

Follow these steps to deploy the environment:

1. **Clone the repository**

```
git clone https://github.com/Zcl1aX/nuclei-nmap-dashboard.git
```

2. **Parse Nmap XML output and Nuclei scan**

Run the `nmap-to-sqlite.py` script to parse your Nmap XML output and store the data in an SQLite database and run `nuclei-to-sqlite.py` to scan and parse nuclei scan data:

```
cd nuclei-nmap-dashboard/data/
python nmap-to-sqlite.py nmap_output.xml
python nuclei-to-sqlite.py
```

3. **Start the Grafana Container**

Use Docker Compose to start the Grafana container:

```
cd nuclei-nmap-dashboard
docker-compose up -d
```

4. **Access Grafana**

Once the container is up and running, access the Grafana dashboard through your web browser:

```
http://localhost:3000
```

Use the default Grafana credentials (admin/admin) unless changed in the configuration. The Nmap dashboard should be loaded with the data from your Nmap scans.

Multiple scans can be reviewed within the DB and the Nmap Dashboard time filters can be used to the view the scan information based on the time stamps from the scans.

## Customization

- Modify the `nmap-to-sqlite.py` script to extract additional information from the Nmap XML output or to change the structure of the SQLite database.
- Custom Dashboard are easy to implement, simply adjust the Grafana dashboard to your requirements. Export the JSON of the Dashboard and replace the default Dashboard or create additional dashboard. The ability to spin up a Grafana Docker container with a prebuilt Dashboard is a nice feature.
- Automation is possible, as you can simply run **nmap** with a cron job, parse the XML with **nmap-to-sqlite.py** and the updated DB will have the newly acquired scan information.

