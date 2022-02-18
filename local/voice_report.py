#!/usr/bin/env python
# coding: utf-8
import sys
import parselmouth
from parselmouth.praat import call

from glob import glob
import sys

path = sys.argv[1]

filename = path.split('/')[-1]
txtFn = path.split('.')[0]
sys.stdout = open(txtFn, 'w', encoding='utf-8')


def voice_report(filename):
    Sound = parselmouth.Sound(filename)

    # set time range
    intensity = Sound.to_intensity(100)
    start = call(intensity, "Get time from frame number", 1)
    nframes = call(intensity, "Get number of frames")
    end = call(intensity, "Get time from frame number", nframes)

    # set pitch 
    minimum_pitch = 50
    maximum_pitch = 625

    pitch_silence_threshold = 0.03
    pitch_voicing_threshold = 0.45
    pitch_octave_cost = 0.01
    pitch_octave_jump_cost = 0.35
    pitch_voiced_unvoiced_cost = 0.14

    Pitch = call(Sound, "To Pitch (cc)", start, minimum_pitch, 15, "no", pitch_silence_threshold, pitch_voicing_threshold, pitch_octave_cost, pitch_octave_jump_cost, pitch_voiced_unvoiced_cost, maximum_pitch)
    Point_process = call([Sound, Pitch], "To PointProcess (cc)")

    
    # voice_quality settings
    maximum_period_factor = 1.3
    maximum_amplitude_factor = 1.6

    report = call([Sound, Pitch, Point_process],"Voice report...", start, end, minimum_pitch, maximum_pitch, maximum_period_factor, maximum_amplitude_factor, pitch_silence_threshold, pitch_voicing_threshold)
        
    print(report)

    sys.stdout.close()


voice_report(path)
