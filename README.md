
# Azure Secure Web Application Deployment

A hands-on Microsoft Azure project demonstrating the deployment of a secure, multi-tier web application using Azure Virtual Machines, Virtual Networks, Network Security Groups, an Internal Load Balancer, Nginx, and Python Flask.

## Project Overview

This project implements a frontend and backend architecture on Microsoft Azure.

The frontend runs Nginx on an Ubuntu virtual machine. Nginx acts as a reverse proxy and forwards API requests to an Azure Standard Internal Load Balancer.

The internal load balancer distributes traffic across two backend Ubuntu virtual machines running a Python Flask application.

The backend virtual machines do not have public IP addresses. Access to backend services is controlled through Network Security Groups.

## Key Objectives

- Deploy and configure Linux virtual machines on Azure.
- Design a Virtual Network with separate frontend and backend subnets.
- Configure Network Security Groups to control network traffic.
- Deploy Nginx as a frontend web server and reverse proxy.
- Deploy a Python Flask API on backend virtual machines.
- Configure an Azure Standard Internal Load Balancer.
- Configure HTTP health probes.
- Test backend availability and failure recovery.
- Configure systemd to manage backend application services.

## Azure Environment

| Component | Configuration |
|---|---|
| Cloud Provider | Microsoft Azure |
| Region | Central India |
| Resource Group | `rg-azure-secure-web` |
| Virtual Network | `vnet-secure-web` |
| VNet Address Space | `10.10.0.0/16` |
| Frontend Subnet | `10.10.1.0/24` |
| Backend Subnet | `10.10.2.0/24` |
| Operating System | Ubuntu Server 24.04 LTS |
| Frontend Web Server | Nginx |
| Backend Framework | Python Flask |
| Load Balancer | Standard Internal Load Balancer |
