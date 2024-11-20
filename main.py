import numpy as np
import wave
import time

filename = "music.wav"
wav_obj = wave.open(filename)
n_samples = wav_obj.getnframes()
sample_freq = wav_obj.getframerate()
t_audio = n_samples / sample_freq

# Calculate Signal Wave
signal_wave = wav_obj.readframes(n_samples)
signal_arr = np.frombuffer(signal_wave, dtype=np.int16)
l_channel = signal_arr[0::2]

# Normalize the audio signal to the range [0, 1]
l_channel_normalized = (l_channel - np.min(l_channel)) / (np.max(l_channel) - np.min(l_channel))
print(l_channel_normalized)

# Open a file for writing normalized intensity values
output_file = open("normalized_intensity_values.txt", "w")

# Batch and average intensity values every 4 samples
batch_size = 4
num_batches = len(l_channel_normalized) // batch_size
for i in range(num_batches):
    start_idx = i * batch_size
    end_idx = (i + 1) * batch_size
    batch_intensity = np.mean(l_channel_normalized[start_idx:end_idx])
    # Normalize the intensity value to the range [0, 1]
    normalized_intensity = (batch_intensity - np.min(l_channel_normalized)) / (np.max(l_channel_normalized) - np.min(l_channel_normalized))
    output_file.write(f"{normalized_intensity}\n")

output_file.close()



