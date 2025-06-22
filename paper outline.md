好的，下面是你所要求的结构化**IEEE EMBC Short Paper Outline**，基于你提供的结构框架进行完整组织，适合撰写一篇4页论文初稿（IEEE double column格式）。

---

# 📄 Paper Title (暂定)

**"A Dry-Land Sonotubometry-Based Assessment Tool for Ear Equalisation Training in Freediving: A Proof-of-Concept Study"**

---

## 📑 Structured Outline

---

### **Abstract**

(*结构化摘要，约200字*)

* **Background**: Ear equalisation is essential in freediving to prevent discomfort and barotrauma.
* **Need**: Current training lacks objective dry-land tools to assess if a diver has performed equalisation correctly.
* **Method**: We propose a non-invasive assessment tool using sonotubometry to detect Eustachian tube openings during equalisation maneuvers.
* **Results**: A simple prototype was developed and tested on two users. The system successfully captured air conduction changes during Frenzel manoeuvres, with identifiable waveforms and frequency shifts.
* **Conclusion**: This proof-of-concept system demonstrates the potential for a portable, real-time equalisation trainer. Future work will expand the system’s robustness and user testing.

---

### **1. Introduction**

* Ear equalisation (Frenzel, Valsalva) is a critical technique in freediving.
* Inadequate equalisation can cause failed dives and middle ear barotrauma.
* Current training lacks an objective tool to verify proper equalisation on land.
* Underwater testing can cause stress, reducing learning effectiveness.
* **Our contribution**:

  * A low-cost dry-land sonotubometry prototype.
  * Demonstration of signal detection during equalisation.
  * Discussion of potential for training integration.

---

### **2. Related Work**

#### 2.1 Clinical Assessment Techniques

| Method                   | Invasiveness | Real-time? | Active? | Suitability for training |
| ------------------------ | ------------ | ---------- | ------- | ------------------------ |
| Tympanometry             | No           | ❌          | ❌       | ❌                        |
| Nasopharyngoscopy        | Yes          | ✅          | ✅       | ❌                        |
| Acoustic Reflectometry   | No           | ❌          | ❌       | ❌                        |
| Sonotubometry (clinical) | No           | ✅          | ✅       | ⚠️（设备复杂）                 |

#### 2.2 Sonotubometry in Literature

* Used in ENT to detect tube patency, but not commonly used in training.
* Prior work shows it correlates with active equalisation maneuvers.

#### 2.3 Training Gaps

* Diving instructors rely on sound/feel – subjective and error-prone.
* No dry-land system currently available for structured training.

---

### **3. System Design**

#### 3.1 Hardware Overview

* Sound source: miniature speaker delivering narrowband noise (e.g., 6–8 kHz).
* Receiver: in-ear microphone (MEMS or electret) records transmission.
* Enclosure: 3D-printed headset for positioning on nose and ear.

#### 3.2 Signal Processing Pipeline

* Input: continuous tone or broadband chirp.
* Signal recorded during equalisation attempts.
* FFT + amplitude envelope tracking used to detect Eustachian opening.
* Detection thresholding based on RMS gain change or frequency shift.

*(插入系统框图 + 信号处理流程图)*

---

### **4. Preliminary Evaluation**

#### 4.1 Method

* 2 test users performed repeated Frenzel and non-equalisation maneuvers.
* Signals collected in quiet room, compared with user-reported success.

#### 4.2 Results

* **Frenzel attempt**: identified air conduction change – waveform peak + gain increase
* **No attempt**: stable waveform, no change in response
* FFT shows reproducible signal change in mid-frequencies (7 kHz region)

*(插入图表：波形图，频谱变化前后对比)*

#### 4.3 Failure Analysis

* Some false positives when jaw motion occurred
* Earbud fit affects detection stability

---

### **5. Discussion & Limitations**

* Prototype confirms feasibility, but:

  * Sensitivity to ear fit and user movement
  * No ground-truth sensor for Eustachian opening
  * Small sample size (2 users)

* Compared to ENT-grade sonotubometry:

  * Simpler, portable, real-time
  * Lacks clinical calibration

* Could supplement coaching by providing repeatable dry-land assessment

---

### **6. Conclusion & Future Work**

* We demonstrated a portable dry-land system for detecting ear equalisation using acoustic methods.
* Results show initial feasibility with minimal equipment.
* Future work:

  * Improve hardware robustness and feedback system
  * Validate across more users with instructor feedback
  * Integrate real-time feedback UI for training sessions
  * Consider underwater adaptation for further research

---

### **References**

(参考文献示例，按 IEEE 格式编号)
\[1] Swarts, J. D., et al. “Eustachian tube function tests: a review.” *Otolaryngology—Head and Neck Surgery*, 2013.
\[2] Virtanen, H., et al. “Sonotubometry in assessing Eustachian tube function.” *Acta Otolaryngol.*, 2003.
\[3] Asenov, F., et al. “A new approach to non-invasive sonotubometry.” *Journal of Laryngology & Otology*, 2015.
\[4] DAN: “Understanding Equalisation and Ear Injuries.”

---

如果你愿意，我可以基于这个大纲直接帮你撰写论文初稿（LaTeX 格式或 Word 格式都可以），并协助图表绘制与内容润色。你想继续往哪个方向推进？是否要先写 Abstract + Introduction 段落？
