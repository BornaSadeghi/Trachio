import matplotlib.pyplot as plt
import wavio
from os import listdir
from os.path import isfile, join
import numpy as np
import pandas as pd
from pydub import AudioSegment

def wav_to_jpg(in_filename, out_filename):
    # read wav file
    samples = wavio.read(in_filename).data
    # convert to mono
    samples = samples.sum(axis=1)


    # Plot the signal read from wav file

    fig = plt.figure(frameon=False)
    fig.set_size_inches(2,1)

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    ax.specgram(samples,Fs=48000)

    fig.savefig(out_filename)
    plt.close()

# wav_to_jpg("uploads/Intro.wav", "spectrogram.jpg")
def preprocess_dataset():
    mypath = "Respiratory_Sound_Database/audio_and_txt_files/"
    filenames = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and f.endswith('.wav'))]
    patient_diagnostics = pd.read_csv("Respiratory_Sound_Database/patient_diagnosis.csv", header=None)

    i=1
    for filename in filenames:
        # get the patient id
        patient_id = int(filename[:3])

        # get the patient diagnosis
        patient_diagnosis = patient_diagnostics[patient_diagnostics[0] == patient_id][1].values[0].lower()

        out_file = "dataset/%s/%s-%d.jpg"%(patient_diagnosis, patient_diagnosis, i)

        print("Should be saving %s into %s"%(mypath+filename, out_file))

        wav_to_jpg(mypath+filename, out_file)
        i+=1

def split_wav(filename, out_dir):
    pass

# print(filenames)

# patient_diagnostics.values[patient index][patient property]
# where patient property is 0:id, 1:diagnosis