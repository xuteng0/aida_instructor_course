# 📑 Sonotubometry Device Setups: Literature Overview

This document summarizes hardware setups used in various sonotubometry research papers to evaluate Eustachian tube (ET) function.

---

## 1. **Asakura et al. (2021) - JASA Express Letters**
**Title:** Evaluation of Eustachian Tube Function Using a Portable Device  
**Link:** https://pubs.aip.org/asa/jel/article/1/6/062001/219604/

### 🔧 Device Setup
- **Sound Source:** Pure-tone stimuli (7.0 & 9.5 kHz)
- **Speaker:** Miniature speaker connected to nasal olive
- **Microphone:** Ear canal MEMS microphone
- **Control Interface:** Android smartphone
- **Features:**
  - Fully portable
  - Battery-operated
  - Measures T_open (open time) and ΔL (sound pressure difference)
- **Purpose:** Real-time, non-clinical assessment of ET function

---

## 2. **Widodo et al. (2021) – Cleft Palate Study**
**Title:** Evaluation of Sonotubometry in Patients with Cleft Palate  
**(Paper referenced via summary search)**

### 🔧 Device Setup
- **Sound Source:** Ear Tone 3A hearing aid speaker
- **Microphone:** Type CM 120 condenser microphone
- **Audio Interface:** SB1140 Creative Sound Blaster USB sound card
- **Calibration:** CS 20 sound level meter
- **Software:** Adobe Audition CS6
- **Computer:** Laptop
- **Setup:**
  - Speaker in nostril
  - Mic in external ear canal
  - Seated in quiet room
- **Outputs:** ET opening count, amplitude, duration

---

## 3. **Di Martino et al. (2007) - Eur Arch ORL**
**Title:** Evaluation of Eustachian Tube Function by Sonotubometry Using 8 kHz  
**Link:** https://link.springer.com/article/10.1007/s00405-006-0172-1

### 🔧 Device Setup
- **Sound Source:** 8 kHz pure-tone
- **Delivery:** Nasal olive + earphone
- **Microphone:** Probe microphone in external ear canal
- **Recording System:** Custom-made sonotubometry unit
- **Measurement Conditions:**
  - Dry swallowing
  - Liquid swallowing
  - Yawning
  - Valsalva
- **Findings:** Positive responses in 55% of trials; various sonotubogram shapes

---

## 4. **van der Avoort et al. (2005) – Otology & Neurotology**
**Title:** Sonotubometry: A State-of-the-Art Review  
**Link:** https://journals.lww.com/otology-neurotology/Abstract/2005/05000/...

### 📝 Notes
- Review article (no specific new hardware)
- Discusses evolution of sonotubometry
- Outlines methodological issues and challenges in reproducibility
- Emphasizes need for standardization, especially in children

---

## 5. **Di Stadio et al. (2023) – Silicone Model Study**
**Title:** Sound and Noise Sources in Sonotubometry  
**Link:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11247061/

### 🔧 Device Setup
- **Model:** 3D-printed silicone ET/nasal cavity with solenoid actuator
- **Sound Source:** White/pink noise, also tested various tones
- **Microphone:** High-fidelity microphone in ear canal
- **Data Acquisition:** High-speed DAQ + STFT analysis
- **Control:** Controlled ET opening with motor trigger
- **Purpose:** Identify noise sources (clicks, swallowing, leakage) and refine algorithm detection

---

## 📌 Summary Table

| Study                         | Signal Type      | Speaker           | Mic Type         | Analysis Platform | Notes                              |
|------------------------------|------------------|-------------------|------------------|-------------------|-------------------------------------|
| Asakura et al. (2021)        | 7.0/9.5 kHz tones | Mini speaker      | MEMS mic         | Android app       | Portable, real-time use             |
| Widodo et al. (2021)         | White noise       | Ear Tone 3A       | CM 120 cond. mic | Adobe Audition    | Used for cleft palate screening     |
| Di Martino et al. (2007)     | 8 kHz tone        | Earphone + olive  | Probe mic        | Custom DAQ        | 55% detection rate                  |
| Di Stadio et al. (2023)      | Broadband         | Speaker to model  | Studio mic       | STFT (Python/Matlab) | Identified noise source patterns |
| van der Avoort et al. (2005) | Review            | Various           | Various          | Literature only   | Clinical analysis and challenges    |

---

## 🛠️ Notes for DIY System

If you're planning to replicate or build a research prototype:
- **Use nasal olive for sealed sound delivery**
- **Pick 7–9.5 kHz tone** for better tube transmission
- **Use MEMS mic or Etymotic ER-7C** for canal recording
- **Process signals with FFT/STFT** for ET opening detection

Let me know if you'd like a schematic or parts list!
