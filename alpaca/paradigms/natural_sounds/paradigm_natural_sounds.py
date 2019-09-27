#!/usr/bin/env python
"""MRI sound stimulus presentation (work in progress).

Notes
-----
Experimental design is similar to [1].

References
----------
[1] Santoro R, et al (2017) Reconstructing the spectrotemporal modulations of
    real-life sounds from fMRI response patterns. PNAS 114(18): 4799-4804.
    <https://doi.org/10.1073/pnas.1617622114>
"""

from __future__ import division
import numpy as np
import os
import time
# import pickle
from psychopy import visual, monitors, core, sound, event, misc
from pprint import pprint

# =============================================================================
# Session parameters
SESSION_ID = 'TEST'
PATH_OUTPUT = 'outputs'

# Run parameters
IDX_RUN = 0  # run index, starts from 0

TR = 2.6  # in seconds, measurement repetition time
TA = 1.4  # in seconds, acquisition time (until silent gap in each measurement)
TSO = 0.1  # in seconds, minimum time after TA until sound presentation
TS = TA + TSO  # stimulus onset in one TR

# Other parameters
FULLSCREEN = False
FILE_PROTOCOLS = 'RUN_PROTOCOLS.pickle'
PATH_STIM = 'stimuli'

SCANNER_TRIGGER_BUTTONS = ['5']
QUIT_BUTTONS = ['escape', 'q']
RESPONSE_BUTTONS = ['1']

IDX_SIL = 0  # silence stimulus index
DATE = time.strftime("%b_%d_%Y_%H_%M", time.localtime())
DEBUG = True
# =============================================================================

# Protocol setup --------------------------------------------------------------
# TODO: Get rid of pickles since they are not recommended anymore
# file = open(FILE_PROTOCOLS, 'rb')
# pickleFile = pickle.load(file)
# file.close()
# blocks = pickleFile['blocks'][IDX_RUN]
# block_durations = pickleFile['blockDur'][IDX_RUN]

# NOTE: Use these arrays for debugging instead of loading from a protocol file
# State identifiers
blocks = np.array(
    [0,   0,  23,   0, 163,   0,  72,   0, 144,   0, 164,   0,  47,
     0, 142,   0,  70,   0, 165,   0,  94,   0,   0,   0,  20,   0,
     141,   0,  24,   0, 166,   0,  96,   0,  43,   0,  45,   0,  69,
     0,  92,   0, 143,   0, 143,   0, 167,   0, 118,   0,  93,   0,
     21,   0,  48,   0, 116,   0, 115,   0, 140,   0, 140,   0,  19,
     0, 120,   0,   0,   0,  22,   0,  91,   0,  71,   0,  95,   0,
     46,   0,   0,   0,  44,   0, 168,   0, 117,   0, 119,   0, 139,
     0,  67,   0,  68,   0,   0])
# State durations in measurement counts
block_durations = np.array(
    [1, 4, 1, 1, 1, 3, 1, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 1,
     3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 3,
     1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 3, 1,
     3, 1, 2, 1, 3, 1, 3, 1, 2, 1, 3, 1, 3, 1, 3, 1, 1, 1, 3, 1, 1, 1, 2,
     1, 1, 1, 6, 1])

# Execution information -------------------------------------------------------
print('{:=^80}'.format(' ' + DATE + ' '))
print('Session ID : {}'.format(SESSION_ID))
print('Run index  : {}'.format(IDX_RUN))
print('Total number of measurements : {}'.format(np.sum(block_durations)))

# Scale block durations from trigger count units to time units
block_durations = block_durations * TR
state_cumsum = np.cumsum(block_durations)
total_time = state_cumsum[-1]
print('Total time                   : {} min {} sec'.format(
    int(total_time // 60), int(total_time % 60)))
if DEBUG:
    print('Debug mode active!')

if os.path.isdir(PATH_OUTPUT):
    print('Output folder already exists.')
else:
    os.mkdir(PATH_OUTPUT)
    print('Output folder is created.')

print('='*80)

# Monitor setup ---------------------------------------------------------------
moni = monitors.Monitor('testMonitor', width=8.2, distance=60)  # cm
win = visual.Window(size=(800, 600), screen=0, winType='pyglet',
                    allowGUI=False, allowStencil=False, fullscr=FULLSCREEN,
                    monitor=moni, color='grey', colorSpace='rgb', units='cm',
                    blendMode='avg')

# Stimulus --------------------------------------------------------------------
sounds = sorted(os.listdir(PATH_STIM))
if DEBUG:
    print('{:-^80}'.format(' Sounds files '))
    pprint(sounds)
    print('{:-^80}'.format(' States '))
    pprint(blocks)
    print('{:-^80}'.format(' State durations (in seconds) '))
    pprint(block_durations)
    print('-'*80)


def set_sound(inputPath, inputSoundName):
    """Lorem ipsum."""
    global outputSetSound
    outputSetSound = sound.Sound(os.path.join(inputPath, inputSoundName),
                                 bits=16, sampleRate=44100)
    return inputSoundName


def render_sound_info(inputSoundNameFromSetSound, i):
    """Lorem ipsum."""
    tDelta = float(np.sum(block_durations[0:i]))
    print('  Sound name              : {}'.format(inputSoundNameFromSetSound))
    if DEBUG:  # This is something I have used to check hickups
        t = clock.getTime() - tDelta
        print('  Time before play command: {0:.3f}'.format(t))
    outputSetSound.play()
    if DEBUG:
        t = clock.getTime() - tDelta
        print('  Time after play command : {0:.3f}'.format(t))
        stimText.setText(inputSoundNameFromSetSound)


# Auditory stimulus name
stimText = visual.TextStim(win=win, color='black', height=0.25)
stimText.setAutoDraw(False)
# Fixation cross
fixation = visual.TextStim(win=win, text='+', pos=[0, 0], color='black',
                           height=0.75)
fixation.setAutoDraw(True)

# Initialize sound module with silence sound (this can prevent initial hickups)
outputSetSound = sound.Sound(value=os.path.join(PATH_STIM, sounds[IDX_SIL]),
                             bits=16, sampleRate=44100)
outputSetSound.play()

# Render ----------------------------------------------------------------------
core.wait(0.5)  # give the system time to settle, recommended by Psychopy devs
clock = core.Clock()

trigTime = []  # trigger time
soundPlay = []  # To note clock time after running .play() command
interruption = False
scannerStartTrigger = True

print('Waiting for scanner trigger...\n')
while scannerStartTrigger:
    for keys in event.getKeys():
        if keys in SCANNER_TRIGGER_BUTTONS:
            scannerStartTrigger = False
            print('{:~^80}'.format(' Experiment has begun '))
        elif keys[0] in QUIT_BUTTONS:
            win.close()
            core.quit()

clock.reset()
i, trigCount, playSwitch = 0, 0, True

while clock.getTime() < total_time:
    print('\nState counter: {}'.format(i))

    while clock.getTime() < state_cumsum[i]:

        # No stimulus
        if clock.getTime() % TR < TS:
            if DEBUG:
                stimText.setText('---NO_STIM---')
            pass

        # Offset
        elif blocks[i] == 999:
            playSwitch = False
            if DEBUG:
                stimText.setText('OFFSET')

        # Rest or silence
        elif blocks[i] == 0:
            playSwitch = False
            if DEBUG:
                stimText.setText('REST/Silence')

        # Sound stimulus
        elif playSwitch is True:
            stimName = set_sound(PATH_STIM, sounds[blocks[i]])
            render_sound_info(stimName, i)
            playSwitch = False
            soundPlay.append([clock.getTime()])

        t = clock.getTime()
        win.flip()

        # handle key presses each frame
        for keys in event.getKeys(timeStamped=True):
            if keys[0] in SCANNER_TRIGGER_BUTTONS:
                trigCount += 1
                trigTime.append([clock.getTime()])
            if keys[0] in QUIT_BUTTONS:
                interruption = True
            if keys[0] in RESPONSE_BUTTONS:
                print('Button press registered : {0:.3f}'.format(
                      clock.getTime()))

        # break out nested loops
        if interruption:
            break

    if interruption:
        print('!!! \nInterrupted! \n!!!')
        break

    if DEBUG:
        print('  Estimated duration      : {0:.3f}'.format(state_cumsum[i]))
        print('  Block completed in      : {0:.3f}'.format(clock.getTime()))
    i += 1
    playSwitch = True

print('Estimated total duration: %f' % total_time)
print('Completed in: %f' % clock.getTime())


# Output ----------------------------------------------------------------------
# TODO: Change the output format to something else, pickles are bad.
output = {'Run_Number': IDX_RUN,
          'blocks': blocks,
          'block_durations': block_durations,
          'Trigger_Time': trigTime,
          'Sound_Play': soundPlay,
          'Interruption': interruption}

out_file_name = '{}-{}.pickle'.format(SESSION_ID, DATE)
misc.toFile(os.path.join(PATH_OUTPUT, out_file_name), output)

print('{:~^80}'.format(' Finished '))
win.close()
core.quit()
