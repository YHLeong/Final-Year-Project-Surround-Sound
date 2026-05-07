# Final Year Project - Surround Sound Show Control System

## Overview

This project is a Python-based show control system developed as part of my Final Year Project to demonstrate real-time synchronization between immersive surround sound playback and professional lighting control systems.

The system integrates:
- :contentReference[oaicite:0]{index=0} for multi-track surround sound playback
- :contentReference[oaicite:1]{index=1} for lighting cue execution
- OSC (Open Sound Control) over UDP networking
- Python automation and timing logic

The objective of the project was to explore how modern AV and entertainment systems can be centrally automated using software-based control architecture similar to professional live production environments.

---

# Project Goals

This project was designed to demonstrate the following technical capabilities:

- Real-time communication between multiple professional systems
- Audio and lighting synchronization
- Automation using Python scripting
- Network-based show control
- Understanding of OSC protocol implementation
- Timing and event sequencing
- Integration of professional AV technologies
- System-level thinking for immersive multimedia environments

---

# Technical Skills Demonstrated

## Software Development

- Python programming
- Function-based architecture
- Modular system design
- Network communication
- Real-time event sequencing
- Timing synchronization logic
- Command abstraction
- Structured code organization

---

## Audio Engineering Integration

Using :contentReference[oaicite:2]{index=2}, the system controls:
- playback transport
- timeline markers
- synchronized multi-track audio playback

The project demonstrates an understanding of:
- DAW automation
- OSC device control
- surround sound workflow integration
- playback synchronization

---

## Lighting Control Integration

Using :contentReference[oaicite:3]{index=3}, the system remotely executes:
- cue changes
- timed lighting sequences
- automated playback-triggered events

The implementation demonstrates:
- lighting console networking
- OSC-based command execution
- show sequencing logic
- cue automation workflow

---

## Networking and Protocol Knowledge

The system uses OSC (Open Sound Control) over UDP networking.

Key concepts implemented:
- IP-based communication
- UDP packet transmission
- OSC message formatting
- Device-to-device communication
- Low-latency control systems

This reflects practical understanding of protocols commonly used in:
- live events
- theatre systems
- immersive installations
- broadcast environments
- AV-over-IP ecosystems

---

# How the System Works

The Python application acts as the central show controller.

It communicates with both:
- :contentReference[oaicite:4]{index=4}
- :contentReference[oaicite:5]{index=5}

using OSC messages sent over the network.

---

# System Architecture

```text
Python Show Controller
        │
        ├── OSC UDP → REAPER
        │       ├── Stop Playback
        │       ├── Jump Timeline Marker
        │       └── Start Playback
        │
        └── OSC UDP → grandMA3
                └── Trigger Lighting Cues
```

---

# Code Workflow Breakdown

## 1. Establish OSC Connections

The script first creates OSC clients for both systems.

```python
REAPER_IP = "127.0.0.1"
REAPER_PORT = 8001

GMA3_IP = "127.0.0.1"
GMA3_PORT = 8000
```

This allows Python to send network commands directly to:
- REAPER
- grandMA3

---

## 2. REAPER Playback Control

The script remotely controls REAPER transport functions.

### Play

```python
reaper.send_message("/action/1007", 1.0)
```

### Stop

```python
reaper.send_message("/action/1016", 1.0)
```

### Jump to Marker

```python
/action/40161
```

These commands automate:
- playback start
- playback stop
- timeline navigation

without requiring manual user interaction.

---

# Why This Matters

This demonstrates:
- external software control
- protocol-level integration
- automation engineering
- understanding of DAW command systems

---

# 3. grandMA3 Cue Automation

Lighting cues are triggered automatically using OSC command execution.

Example:

```python
command = f"Goto Cue {cue_number} Sequence 1"
```

This dynamically generates lighting commands such as:

```text
Goto Cue 5 Sequence 1
```

which are transmitted directly to the lighting console.

---

# Why This Matters

This demonstrates:
- automation of professional lighting systems
- real-time command generation
- dynamic cue control
- integration between audio and lighting systems

---

# 4. Synchronization Engine

The core system logic is handled by:

```python
run_block()
```

This function:
1. Stops playback
2. Jumps to a timeline marker
3. Starts playback
4. Executes lighting cues sequentially
5. Maintains timing between events

---

# Timing Logic

Cue timing is calculated dynamically:

```python
cue_delay = duration / total_cues
```

Example:
- 5 cues
- 2 second duration

Result:
- 0.4 second interval between cues

---

# Why This Matters

This demonstrates understanding of:
- event scheduling
- synchronization logic
- real-time automation
- timed execution systems

which are critical concepts in:
- live show control
- broadcast automation
- immersive AV systems
- themed entertainment technology

---

# Example Show Sequence

```python
run_block(
    marker=1,
    start_cue=1,
    end_cue=5,
    duration=2
)
```

Execution flow:

```text
1. Stop REAPER
2. Jump to Marker 1
3. Start Playback
4. Trigger Cue 1
5. Trigger Cue 2
6. Trigger Cue 3
7. Trigger Cue 4
8. Trigger Cue 5
```

---

# Engineering Concepts Applied

## Real-Time Systems

The project implements:
- timed execution
- event sequencing
- low-latency communication

---

## Automation Systems

The project automates:
- playback transport
- cue sequencing
- synchronized execution

without manual operation.

---

## System Integration

The project combines multiple professional systems into one unified control workflow.

This reflects real-world AV engineering practices where:
- audio
- lighting
- video
- networking
- control systems

must operate together reliably.

---

# Challenges Solved During Development

During development, several engineering challenges were addressed:

- OSC communication setup
- Port routing and device networking
- Synchronization timing
- Command sequencing reliability
- Cross-platform software communication
- Automation workflow testing
- Real-time execution stability

This required troubleshooting across:
- software
- networking
- timing systems
- AV integration workflows

---

# Future Improvements

Potential future development includes:
- SMPTE timecode integration
- GUI-based control interface
- Dynamic JSON show files
- Async event processing
- Multi-device synchronization
- AV-over-IP routing
- Real-time monitoring dashboard
- Error handling and recovery systems

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Automation logic |
| python-osc | OSC communication |
| OSC Protocol | Show control messaging |
| UDP Networking | Real-time communication |
| :contentReference[oaicite:6]{index=6} | Surround sound playback |
| :contentReference[oaicite:7]{index=7} | Lighting control |

---

# Project Significance

This project demonstrates practical skills in:
- software development
- automation engineering
- professional AV integration
- networking
- multimedia system control
- real-time systems design

The implementation reflects how software engineering principles can be applied within professional entertainment and AV technology environments to create synchronized immersive experiences.