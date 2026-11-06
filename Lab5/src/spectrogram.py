from windowing import hann
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from fft import fft
from cubic_spline import nat_cubic

if __name__ == "__main__":
    # Generate a sample noise signal
    DURATION = 3
    SAMPLE_RATE = 44100

    print("Recording audio, speak now")
    print(f"Duration: {DURATION}s, Sample rate: {SAMPLE_RATE}Hz")
    recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate = SAMPLE_RATE, channels = 1, dtype = 'float32', blocking = True)
    x = recording.flatten()
    print("Recording complete.")

    t_original = np.arange(len(x)) / SAMPLE_RATE
    t_fine = np.linspace(t_original[0], t_original[-1], 10000)
    x_interpolated = nat_cubic(t_original, x, x_eval = t_fine)
    # TODO: Change this code to record an audio sample instead

    # Iterate over the windowed audio and compute power spectrum data
    psds = []
    N = 1024 # samples per chunk of windowed audio
    for chunk in hann(x, N):
        # Compute the fast Fourier transform (FFT) of this chunk
        X = fft(chunk)[0:N//2] # TODO: Use your own FFT instead

        # Compute the power spectral density (PSD) of this chunk
        # PSD is 10*log10 of the square of the real part of the FFT
        psd = 10*np.log10(np.abs(X)**2)
        psds.append(psd)
    psds = np.array(psds).transpose()

    # Plot the PSDs as a spectrogram
    # TODO: Add a subplot showing the interpolated audio waveform (with shared x-axis)
    # TODO: Label and correct the x-axis and y-axis values
    n_time_frames = psds.shape[1]
    time_spectrogram = np.array([(i * (N - 256)) / SAMPLE_RATE for i in range(n_time_frames)])

    fig, (ax_wave, ax_spec) = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw = {'height_ratios':[1, 3]}, sharex=True)

    ax_wave.plot(t_fine, x_interpolated, linewidth = 0.5, color = 'steelblue')
    ax_wave.set_ylabel('Amplitude')
    ax_wave.set_title(f'Interpolated Audio Waveform (Duration: {t_fine[-1]:.2f}s)')
    ax_wave.grid(True, alpha = 0.3)
    ax_wave.set_ylim(-1.2, 1.2)

    freqs = np.linspace(0, SAMPLE_RATE / 2, N // 2)
    im = ax_spec.imshow( psds, aspect = 'auto', origin = 'lower', extent = [time_spectrogram[0], time_spectrogram[-1], freqs[0], freqs[-1]], cmap='viridis')
    ax_spec.set_ylabel('Frequency (Hz)')
    ax_spec.set_xlabel('Time (s)')
    ax_spec.set_title('Power Spectral Density')
    plt.colorbar(im, ax=ax_spec, label='Power (dB)')
    ax_spec.grid(True, alpha = 0.3)

    fig.suptitle(f'Audio Spectrogram ({DURATION}s recording, {SAMPLE_RATE} Hz)', fontsize = 14, fontweight = 'bold')
    fig.tight_layout()
    plt.show()
