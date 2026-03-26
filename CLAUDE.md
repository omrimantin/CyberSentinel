# CyberSentinel — Claude Code Guide

## Project Overview
Distributed real-time security monitoring platform (academic project).
- **server/** — central server: multi-client TCP socket, live tkinter dashboard, SQLite logs
- **agent/** — runs on each monitored machine: process/network/file/camera monitors, each in its own thread
- **shared/** — AES-128 encryption + JSON message protocol shared by both sides

## Architecture Rules
- Every monitor class extends `threading.Thread` with `daemon=True`
- All agent→server communication must be AES-encrypted via `shared/encryptor.py`
- Messages follow the protocol in `shared/protocol.py` (JSON with `type` + `payload` keys)
- The server must support multiple simultaneous agents (one thread per client)

## Code Style
- Python 3.10+
- Class-based OOP — no standalone scripts with logic outside classes
- Keep monitors independent: each monitor only calls `alert_callback(alert_type, details_dict)`
- No global state; pass dependencies via `__init__`

## Key Classes (to be implemented)
| Class | File | Responsibility |
|---|---|---|
| `Encryptor` | shared/encryptor.py | AES-128 CBC encrypt/decrypt |
| `Server` | server/server.py | Multi-client TCP server |
| `ClientHandler` | server/server.py | One thread per connected agent |
| `Dashboard` | server/dashboard.py | tkinter live event table |
| `LogDB` | server/db.py | SQLite log storage |
| `Agent` | agent/agent.py | Connects to server, starts all monitors |
| `ProcessMonitor` | agent/process_monitor.py | Detects suspicious processes |
| `NetworkMonitor` | agent/network_monitor.py | Detects suspicious connections |
| `FileMonitor` | agent/file_monitor.py | Detects critical file changes |
| `CameraMonitor` | agent/camera_monitor.py | Motion detection via webcam (opencv) |

## Dependencies
```
pycryptodome   # AES encryption
psutil         # process + network monitoring
opencv-python  # camera access
```

## Academic Requirements Checklist
- [x] OOP — 10+ classes
- [x] Sockets — multi-client TCP server
- [x] Threads — each monitor + each client handler is a separate thread
- [x] Hardware access — webcam (cv2), process list (psutil), filesystem
- [x] Encryption — AES-128 on all traffic
- [x] Interactive GUI — tkinter dashboard with live updates

## GitHub
https://github.com/omrimantin/CyberSentinel
