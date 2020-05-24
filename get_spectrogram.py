import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

def wav_to_jpg(in_filename, out_filename):
    # read wav file
    sample_rate, samples = wavfile.read(in_filename)
    # convert to mono
    samples = samples.sum(axis=1)


    # Plot the signal read from wav file

    fig = plt.figure(frameon=False)
    fig.set_size_inches(2,1)

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    ax.specgram(samples,Fs=sample_rate)

    fig.savefig(out_filename)

# wav_to_jpg("uploads/Intro.wav", "spectrogram.jpg")

# mypath = "/kaggle/input/respiratory-sound-database/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/"
# filenames = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and f.endswith('.wav'))] 