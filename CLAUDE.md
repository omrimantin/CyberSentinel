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

## Shared AES Key
All agents and the server use this hardcoded key:
```
7f026d24873b44fad78c46955d44fea914112f4edb7ba1159b1ce78a784e5959
```

## Progress — What's Done
| Class | File | Status |
|---|---|---|
| `Encryptor` | shared/encryptor.py | ✅ Done |
| `Protocol` | shared/protocol.py | ✅ Done |
| `Server` | server/server.py | ✅ Done — multi-client TCP, AES decrypt, one thread per client |
| `Agent` | agent/agent.py | ✅ Done — connects to server, `send_alert()` encrypts + sends |
| `Dashboard` | server/dashboard.py | ⬜ Next |
| `LogDB` | server/db.py | ⬜ Next |
| `ProcessMonitor` | agent/process_monitor.py | ⬜ Next |
| `NetworkMonitor` | agent/network_monitor.py | ⬜ Next |
| `FileMonitor` | agent/file_monitor.py | ⬜ Next |
| `CameraMonitor` | agent/camera_monitor.py | ⬜ Next |

## What's Next (recommended order)
1. **`server/db.py`** — `LogDB` class, SQLite, saves every received message
2. **`server/dashboard.py`** — tkinter GUI, live event table, reads from LogDB
3. **`agent/process_monitor.py`** — detects suspicious processes (psutil), calls `agent.send_alert()`
4. **`agent/network_monitor.py`** — detects suspicious connections (psutil)
5. **`agent/file_monitor.py`** — detects file changes (hashlib)
6. **`agent/camera_monitor.py`** — motion detection (opencv)
7. **Wire everything together** — Agent starts all monitors, server pipes events to dashboard

## Split of Work
- **omrimantin** → server/ files (db.py, dashboard.py)
- **omri1213** → agent/ monitor files (process, network, file, camera)

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
