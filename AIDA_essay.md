Here’s an **expanded outline** of your paper with detailed subsections, suggested content for each, and where to justify key arguments with supporting evidence or figures. This structure will strengthen your narrative, improve clarity, and help align with short paper requirements like IEEE EMBC or UbiComp/ISWC Demo tracks.

---

## **Title**

*A Dry-Land Sonotubometry-Based Assessment Tool for Ear Equalisation Training in Freediving: A Proof-of-Concept Study*

---

## **Abstract** (150–250 words)

* One-sentence background: why ear equalisation matters in freediving
* Gap: lack of dry-land, objective feedback tools
* Solution: your low-cost, sonotubometry-based prototype
* Validation: tested with two users, successfully detected events
* Impact: paves the way for safer, more efficient equalisation training

---

## **Keywords**

*Sonotubometry, Ear Equalisation, Freediving, Eustachian Tube, Training Tool*

---

## **1. Introduction**
1. Background and Importance
Equalising middle ear pressure via the Eustachian tube (ET) is essential for all forms of diving (SCUBA and freediving).

Failure to equalise can cause barotrauma, hearing loss, vertigo, or chronic ear conditions — especially during descent.

2. Equalisation Techniques and Training Methods
Divers are taught to equalise using techniques such as:

Valsalva, Frenzel, BTV (hands-free), and Mouthfill (for deep freediving).

Dry-land training tools include:

Balloon-based trainers (e.g., Otovent)

Digital nasal pressure sensors (e.g., EQ Tool by UBA)

Instructor observation, focusing on technique coordination.

3. Limitation in Existing Approaches
Existing tools and training methods only confirm the attempt or technique quality.

However, they do not verify whether the ET actually opens or if middle ear pressure is equalised.

This limitation:

Increases injury risk in beginners.

Creates a gap in objective, physiological feedback.

Is especially problematic for those with undetected ET dysfunction.

4. Clinical Evaluation Methods: Effective but Inaccessible
Tools like sonotubometry, tympanometry, and tubomanometry can detect ET opening.

Yet these are typically:

Clinical-use only (costly, non-portable, and require training).

Not usable by divers for dry-land self-training or real-time assessment.

5. Gap and Unmet Need
There is no accessible and affordable tool that directly measures ET tube opening during equalisation in a dry-land setting.

This impedes:

Safe learning for novice divers.

Screening for ET dysfunction before diving.

Feedback integration with existing equalisation trainers.

6. Our Contribution
We propose a feasibility prototype of a diver-friendly ET opening detection system using sonotubometry.

Our system:

Uses a simple DIY setup with a microphone and speaker.

Enables objective feedback on ET opening during equalisation attempts.

Demonstrates technical feasibility as a low-cost, practical extension to existing dry-land training.

7. Paper Overview
We first review related tools and assessment methods.

Then present the prototype design, validation process, and test results.

Finally, we discuss limitations and opportunities for integration into diver training and screening.

---

Let me know if you'd like this converted into a written introduction paragraph or expanded into presentation slides.



## **2. Related Work**

### 2.1 Commercial Equalisation Tools

| Device                       | Purpose                   | Objective? | Real-time? | Notes                     |
| ---------------------------- | ------------------------- | ---------- | ---------- | ------------------------- |
| Octopus Equalisation Trainer | Air delivery drill        | ✗          | ✗          | Balloon-based             |
| C4 Freediving EQ Tool        | Tongue/palate training    | ✗          | ✗          | No feedback               |
| Kogan Ear Pressure Device    | OTC relief for discomfort | ✗          | ✗          | Not training-focused      |
| **UBA EQ Tool Pro**          | ✅ Captures signal via mic | Partial    | Partial    | No public validation data |

* Add product URLs and screenshots (if permitted)
* Mention the **lack of ET opening detection** or real-time feedback

### 2.2 Clinical Assessment Techniques

| Method             | Invasive | Real-time | ET Direct? | Portable | Training Use |
| ------------------ | -------- | --------- | ---------- | -------- | ------------ |
| Tympanometry       | ✗        | ✗         | ✗          | ✗        | ✗            |
| Video Otoscopy     | ✗        | ✗         | ✗          | ✗        | ✗            |
| Nasopharyngoscopy  | ✓        | ✓         | ✓          | ✗        | ✗            |
| Sonotubometry      | ✗        | ✓         | ✓          | ⚠        | ⚠            |
| **Your prototype** | ✗        | ✓         | ✓          | ✅        | ✅            |

* Use uploaded review content here to give 1–2 lines per method
* Highlight how your tool builds on sonotubometry while being miniaturised and portable

---

## **3. System Design**

### 3.1 Hardware Architecture

* Speaker (tone source in nasal cavity)
* In-ear microphone (signal receiver)
* ESP32/MCU with ADC and USB
* 3D printed ear mold for consistency
* Optional: diagram of device structure

### 3.2 Software and Signal Processing

* Tone generation (6–8 kHz)
* Continuous sampling of mic signal
* Real-time FFT
* Envelope tracking and gain change detection
* Threshold logic for ET opening event
* Optional: software stack diagram or flowchart

### 3.3 Design Considerations

* Why ear canal mic was chosen
* Trade-offs between latency, accuracy, comfort
* Handling noise, jaw movement artifacts

---

## **4. Preliminary Evaluation**

### 4.1 Experimental Protocol

* Environment: quiet room, seated users
* Instructions: attempt equalisation (Frenzel/Valsalva)
* Conditions: successful attempts vs control (no effort)
* Metrics: amplitude gain, spectrum peak shift

### 4.2 Results

* Time-aligned spectrograms
* Plots of amplitude before/after equalisation
* Annotation of “detected events”
* Optional: quantitative table of event detection success (e.g., 7/10 attempts)

### 4.3 Observed Limitations

* Inconsistent probe placement
* Artifacts from jaw motion
* Fit issues with ear tip
* Signal drift from poor seal

---

## **5. Discussion and Limitations**

### 5.1 Insights

* Gain changes are visible and match user feedback
* Promising as real-time training feedback
* Can suggest partial vs full ET opening, but not quantify

### 5.2 Limitations

* Small sample size (n = 2)
* No gold standard for ground truth
* Not yet tested in larger cohorts
* False positives possible from motion or poor fit

### 5.3 Comparison to Other Methods

* More direct than acoustic reflectometry
* More portable than clinical sonotubometry
* Lower cost than consumer electronics

---

## **6. Conclusion and Future Work**

* We present a novel, low-cost dry-land tool for EQ training
* Successfully detects equalisation events in real time
* Applicable to both beginners and instructors
* Future steps:

  * Field validation with instructors
  * Improved UI for user feedback
  * Integration with apps or log systems

---

## **References**

* Cite review papers (Edmonds, sonotubometry studies)
* Product manuals or websites (UBA EQ Tool, Octopus)
* Clinical method validation papers (e.g. tympanometry, otoscopy)

