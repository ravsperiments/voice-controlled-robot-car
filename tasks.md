# 🛠️ Project Tasks

## Phase 0: Hardware Prep
- [x] Reuse Elegoo chassis, L298N, motors
- [x] Purchase ESP32 DevKit
- [x] Purchase INMP441 mic module

## Phase 1: ESP32 Setup
- [ ] Flash ESP32 blink sketch
- [ ] Test motor control with L298N
- [ ] Wire and verify I²S mic capture

## Phase 2: Local Server Setup
- [ ] Install Whisper
- [ ] Create FastAPI upload endpoint
- [ ] Run test transcription
- [ ] Chain to local LLaMA (Ollama or llama.cpp)
- [ ] Return command JSON to ESP32

## Phase 3: Communication
- [ ] ESP32 sends audio buffer to server
- [ ] Parse JSON on ESP32 and control motors
- [ ] Add retry and timeout logic

## Phase 4: Voice Commands
- [ ] Build natural phrase set (e.g., "go left", "spin")
- [ ] Map to structured actions

## Phase 5: Testing & Extensions
- [ ] Voice → Motion loop working
- [ ] Add override via button / web UI
- [ ] Explore ESP32-CAM streaming

