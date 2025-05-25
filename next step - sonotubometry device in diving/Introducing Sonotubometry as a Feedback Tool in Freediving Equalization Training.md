# Introducing Sonotubometry as a Feedback Tool in Freediving Equalization Training: A Pilot Study

## 1. Introduction

Equalization is a vital skill in freediving, necessary to prevent barotrauma and to enable safe descent. Traditional instruction relies heavily on subjective sensation and verbal feedback, which makes skill acquisition inconsistent. This pilot project investigates the potential of **sonotubometry**—an acoustic technique used in ENT medicine—to provide **objective feedback** on Eustachian tube opening during equalization training.

## 2. Background

Equalization techniques such as Frenzel, Valsalva, and Mouthfill require precise control of upper airway structures. However, students often struggle due to a lack of internal feedback. **Sonotubometry** works by transmitting a tone (e.g., 7kHz) through the nostril and detecting its presence in the external ear canal—indicating an open Eustachian tube. This technique has not yet been applied in freediving coaching.

## 3. Method

### Participants
- The author (AIDA instructor candidate) and optionally 1–2 peers

### Equipment
- 7kHz sine wave tone generator (PC or phone)
- Nasal cannula or earbud speaker to deliver tone
- Lavalier or MEMS microphone placed near the external ear canal
- Audacity or Python script to capture and visualize the signal

### Protocol
1. Play continuous tone through the nostril
2. Attempt equalization (Frenzel, Valsalva, etc.)
3. Record the audio from the ear canal microphone
4. Analyze signal spikes at 7kHz as indicators of tube opening
5. Record subjective feedback (“Did you feel the pop?”)

## 4. Results

| Technique | Subjective Opening | 7kHz Signal Spike | Notes |
|----------|--------------------|-------------------|-------|
| Frenzel  | Yes                | Yes               | Consistent |
| Valsalva | No                 | No                | Air blocked |
| Swallow  | Sometimes          | Weak              | Inconsistent |

- FFT plots showed distinct energy spikes in successful equalizations
- Some side differences noted (left easier than right)
- Subjective feedback aligned well with signal data

## 5. Discussion

- Even a simple DIY setup was able to detect successful Eustachian tube openings
- Objective feedback gave confidence in technique
- Potential to assist instructors in verifying student progress
- Portable and low-cost, ideal for use in workshops

## 6. Conclusion

Sonotubometry offers a promising supplement to traditional freediving equalization instruction. The ability to *see* whether an equalization attempt succeeded could accelerate learning and reduce injury risk. Future development should aim to simplify, miniaturize, and validate the tool for broader use.

## 7. Future Work

To progress this into a full academic study or conference paper:
- Increase sample size and participant diversity
- Compare signal characteristics across equalization techniques
- Measure training improvements over time with and without feedback
- Explore underwater-compatible versions for real-time monitoring
- Submit findings to a conference such as EUBS, DAN, or ECSS

## 8. References

- AIDA Education Manual (2023)
- van der Avoort, S.J. et al. “Sonotubometry: A State-of-the-Art Review.” Otol Neurotol, 2005.
- Pyne, J. M. et al. “Transmission of a Novel Sonotubometry Acoustic Click Stimulus…” (2017)

