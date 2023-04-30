# Sensor of BAS
This is the sensor of Breach and Attack Simulation tool.  
Sensor is the dockerized application that run using docker-compose in the daemon mode.

## Tech stack
The sensor is written using following technologies:
* Python - Requests, logger
* Modsecurity - the firewall solution, that is being tested in the current config. It is launched in the same network via docker compose under the hood. It is planned to run the sensor as standalone script and provide the IP and Port of firewall to be tested. 

## Flow
To conduct a scan following actions should be performed:
* Run the sensor in the same subnet as scanner
* Ensure that firewall and sensor are running uninterrupted
* Start the scan 
* Recieve results on the CLI of scanner and User Interface 

## Set-up
To set up the application perform following operations:  
* Pull the project from the git
* Start the sensor via:
        * ./run_sensor.sh

