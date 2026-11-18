# Azure Secure Web Application - Infrastructure Notes

## Azure Environment
- Resource Group: rg-azure-secure-web
- Region: Central India
- VNet: vnet-secure-web
- Address Space: 10.10.0.0/16

## Subnets
- Frontend: snet-frontend - 10.10.1.0/24
- Backend: snet-backend - 10.10.2.0/24

## Virtual Machines
- Frontend: vm-frontend-01
- Backend 01: vm-backend-01 - 10.10.2.4
- Backend 02: vm-backend-02 - 10.10.2.5
- Operating System: Ubuntu Server 24.04 LTS
- Backend VMs have no public IP addresses.

## Network Security Groups
### Frontend NSG
- SSH TCP/22: Allowed from administrator public IP (/32)
- HTTP TCP/80: Allowed from Any

### Backend NSG
- SSH TCP/22: Allowed from frontend subnet (10.10.1.0/24)
- Application TCP/8080: Allowed from frontend subnet (10.10.1.0/24)

## Load Balancer
- Name: lb-backend-internal
- SKU: Standard
- Type: Internal
- Frontend Private IP: 10.10.2.10
- Backend Pool: bp-backend-vms
- Members: vm-backend-01, vm-backend-02
- Probe: HTTP TCP/8080, path /health
- Load Balancing Rule: TCP/8080 -> TCP/8080

## Application Architecture
- Frontend: Nginx on Ubuntu
- Backend: Python Flask
- Backend application port: 8080
- Nginx reverse proxy: /api/ -> Internal Load Balancer
- Application service: backend-app.service
- Process recovery: systemd Restart=always

## Tests Performed
- Public frontend access
- Nginx reverse proxy
- Backend connectivity
- Load balancing across backend VMs
- Health probe verification
- Backend application failure and failover
- Backend application recovery
- systemd automatic startup
- systemd process recovery using SIGKILL

## Future Improvements
- HTTPS with TLS
- Gunicorn instead of Flask development server
- Terraform infrastructure as code
- More granular backend access restrictions
- Azure Monitor and Log Analytics
