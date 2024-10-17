# Riemann Monitoring Example

This project demonstrates how to use the Riemann monitoring system to send and track events for distributed systems. The setup includes running a Riemann server in Docker, sending events from a Python client, and verifying the events in Riemann.

## Prerequisites
- Docker
- Python 3.10+
- Poetry (for Python dependency management)

## 1. Local Testing with Docker

### Step 1: Pull Riemann Docker Image
To set up a local Riemann server for testing, pull the Docker image:

$bash
$ docker pull riemannio/riemann

## Run the Riemann server on port 5555 (you can change the port if want)
$ docker run -d -p 5555:5555 riemannio/riemann

## Install Dependencies

$ poetry install

## Run the Python Monitoring Script

$ poetry run python monitor.py

## Checking Docker Logs
$ docker logs <docker-id>