# 🎭 OSC-Based Multimedia Show Control System

> Synchronizing audio playback and lighting control using  
> **Python + REAPER + grandMA3 onPC**

---

# 🚀 Project Overview

This project demonstrates a lightweight multimedia show control system using:

- 🎵 REAPER for audio playback
- 💡 grandMA3 onPC for lighting control
- 🐍 Python for automation and OSC communication

The system automates:
- audio playback
- timeline navigation
- lighting cue execution
- sequential show blocks

using **OSC (Open Sound Control)** over localhost.

---

# 🖥️ System Architecture

```mermaid
flowchart TD

    A[🐍 Python Script]

    A -->|OSC Commands| B[🎵 REAPER]
    A -->|OSC Commands| C[💡 grandMA3 onPC]

    B --> D[▶️ Playback Control]
    B --> E[📍 Marker Navigation]

    C --> F[💡 Cue Triggering]
    C --> G[🎬 Sequence Control]
```

---

# 🌐 Communication Flow

```mermaid
sequenceDiagram

    participant Python as 🐍 Python Script
    participant REAPER as 🎵 REAPER
    participant GMA3 as 💡 grandMA3

    Python->>REAPER: Stop Playback
    Python->>REAPER: Jump to Marker
    Python->>REAPER: Start Playback

    loop Cue Sequence
        Python->>GMA3: Goto Cue X Sequence 1
    end
```

---

# ✨ Core Features

## 🎵 REAPER Integration

The script can:

- ▶️ Start playback
- ⏹️ Stop playback
- 📍 Jump to timeline markers

using REAPER OSC action commands.

Example:

```python
reaper.send_message("/action/1007", 1.0)
```

---

## 💡 grandMA3 Cue Control

Lighting cues are triggered directly through OSC commands:

```text
Goto Cue X Sequence 1
```

Example:

```python
gma3.send_message("/gma3/cmd", "Goto Cue 5 Sequence 1")
```

---

# 🧩 Block-Based Show Programming

The show is divided into programmable blocks.

Each block contains:
- 📍 REAPER marker
- 💡 starting cue
- 💡 ending cue
- ⏱️ duration

Example:

```python
ShowBlock(
    marker=1,
    start_cue=1,
    end_cue=5,
    duration=2
)
```

---

# 🛠️ Software Stack

| Software | Purpose |
|---|---|
| 🎵 REAPER | Audio playback and timeline control |
| 💡 grandMA3 onPC | Lighting cue execution |
| 🐍 Python | Automation and scripting |
| 📡 python-osc | OSC networking library |

---

# 📚 Python Library

## 📡 python-osc

Used for communication between:
- REAPER
- grandMA3
- Python

Install using:

```bash
pip install python-osc
```

---

# 🧠 Code Structure

```mermaid
flowchart TD

    A[⚙️ Configuration]

    A --> B[🌐 OSC Clients]

    B --> C[🧱 ShowBlock Dataclass]

    C --> D[🎵 REAPER Functions]
    C --> E[💡 grandMA3 Functions]

    D --> F[⚡ Show Engine]
    E --> F

    F --> G[🎬 Main Show Execution]
```

---

# 🎬 Example Show Flow

```mermaid
timeline
    title 🎭 Show Timeline

    Block 1 : 📍 Marker 1
            : 💡 Cue 1 → 5
            : ⏱️ 2 Seconds

    Block 2 : 📍 Marker 2
            : 💡 Cue 6 → 10
            : ⏱️ 2 Seconds

    Block 3 : 📍 Marker 3
            : 💡 Cue 11 → 15
            : ⏱️ 5 Seconds
```

---

# ⚡ Show Execution Flow

```mermaid
flowchart LR

    A[⏹️ Stop REAPER]
        --> B[📍 Jump to Marker]

    B --> C[▶️ Start Playback]

    C --> D[💡 Trigger Cue Sequence]

    D --> E[⏱️ Delay Between Cues]

    E --> F[🎬 Next Cue]
```

---

# ✅ Advantages

## ⚡ Simple Architecture

Uses:
- one laptop
- localhost networking
- lightweight automation

This reduces:
- hardware complexity
- setup time
- synchronization delay

---

## 🚀 Fast Development Workflow

The block structure allows:
- rapid testing
- quick cue adjustments
- modular show programming

---

## 🎛️ Flexible Control

Lighting and audio can be modified independently while maintaining synchronized playback.

---

# ⚠️ Current Limitations

The current system uses:

```python
time.sleep()
```

for timing control.

This can introduce:
- ⌛ timing drift
- 🖥️ OS scheduling delay
- ⚠️ non-frame-accurate synchronization

For professional-grade synchronization:
- MIDI Timecode (MTC)
- SMPTE Timecode

would provide significantly higher precision.

---

# 🔮 Future Improvements

```mermaid
mindmap
  root((🔮 Future Improvements))

    🎞️ Timecode Sync
      MIDI Timecode
      SMPTE Integration

    🌌 Spatial Audio
      L-ISA Integration
      Object Automation

    🖥️ UI Development
      Control Dashboard
      Real-Time Monitoring

    ⚡ Performance
      Async OSC
      Recovery Handling
      Emergency Stop
```

---

# 🏁 Conclusion

This project demonstrates a compact OSC-based multimedia show control workflow integrating:

- 🎵 REAPER
- 💡 grandMA3 onPC
- 🐍 Python automation

The system provides:
- synchronized playback
- automated lighting control
- scalable show sequencing
- efficient multimedia integration

suitable for:
- 🎓 educational showcases
- 🎭 multimedia performances
- 🧪 experimental installations
- 🎬 small-scale live productions