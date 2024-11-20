# Audio-amplitude-based-LED-controller

# Audio Signal Normalization and Intensity Extraction

## Overview

This project extracts and normalizes the left-channel audio signal from a `.wav` file. The normalized intensity values are computed in batches of 4 samples and saved to a text file for further analysis or use in audio-based applications.

---

## Features

- **Waveform Analysis:**
  - Reads the left channel from a stereo `.wav` file.
  - Normalizes the audio signal to the range `[0, 1]`.

- **Batch Processing:**
  - Divides the audio signal into batches of 4 samples.
  - Computes the average intensity for each batch.

- **Output Storage:**
  - Saves the normalized intensity values to `normalized_intensity_values.txt`.

---

## Requirements

- Python 3.8 or above
- Libraries:
  - `numpy`: For efficient numerical computations.
  - `wave`: For handling `.wav` audio files.

---

## Setup and Usage

1. Place your `.wav` file in the same directory as the script and name it `music.wav`.

2. Run the script:
   ```bash
   python audio_normalizer.py


How It Works
Read the Audio File:

The script reads a stereo .wav file using Python's wave module.
The left-channel signal is extracted and converted to a numpy array.
Normalization:

The signal is normalized to the range [0, 1] using min-max scaling.
Batch Processing:

The signal is divided into batches of 4 samples.
The average intensity of each batch is computed and normalized.
Output:

The normalized intensity values are written to normalized_intensity_values.txt.
Contributing
Feel free to fork this repository and suggest improvements or new features. Bug reports and feature requests are welcome via issues.
