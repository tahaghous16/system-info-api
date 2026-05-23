# Linux Command Executor API

## Project Overview
A FastAPI project that executes predefined Linux commands and returns outputs in JSON format.

## Features
- System uptime API
- Disk usage API
- Memory usage API
- Current user API
- Health check endpoint
- Error handling

## Technologies Used
- Python
- FastAPI
- Uvicorn
- Linux Commands

## API Endpoints

| Endpoint | Description |
|---|---|
| /health | Health check |
| /system/uptime | System uptime |
| /system/disk | Disk usage |
| /system/memory | Memory usage |
| /system/user | Current user |

## Run Project

```bash
uvicorn main:app --reload
-