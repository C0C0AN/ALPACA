"""Generate stimulus presentation protocol for natural sounds experiment.

Work in progress. Not intended for use.

Notes
-----
TODO: Add rest/silence conditions.
TODO: Add description of randomization scheme here.

References
----------
TODO: Add references for the randomization scheme here.

"""

from __future__ import division
import os
import csv
import time
import numpy as np

# =============================================================================
# User input

NR_CATEG = 6  # Total number of categories
NR_SOUND_PER_CATEG = 48  # Number of sounds per category
NR_RUN = 8  # Number of runs to present full set of sounds once
OUT_DIR = '/home/faruk/Git/alpaca/scripts_stimulation/natural_sounds_experiment/protocols'

# Enter durations in units of measurements
DUR_STIM = 1
DUR_OFFSET = 5
DUR_REST = 2

# Identifiers for experiment states
ID_REST = 0
ID_OFFSET = -1

# =============================================================================
# Derived parameters

# Total number of sounds
NR_SOUND = NR_CATEG * NR_SOUND_PER_CATEG
if NR_SOUND % NR_RUN != 0:  # TODO: Swap with try/except?
    print('Number of runs cant divide total nr. sounds!')
# Number of sounds per categtory per run
NR_SOUND_PER_CATEG_PER_RUN = NR_SOUND_PER_CATEG // NR_RUN
# Number of sounds per run
NR_SOUND_PER_RUN = NR_CATEG * NR_SOUND_PER_CATEG_PER_RUN

# =============================================================================
# Generate stimulus presentation order

# Create ordered list of integers representing different sounds
temp1 = np.arange(NR_SOUND)
# Add 1 because 0 will represent silence (NOTE: Might bind to user input)
temp1 += 1
# Arange rows for sound indices, columns for category indices
temp1 = temp1.reshape(NR_CATEG, NR_SOUND_PER_CATEG)
# Randomize sound order within category
temp2 = np.copy(temp1)
for i in range(NR_CATEG):
    temp2[i, :] = np.random.permutation(temp1[i, :])
# Divide into runs (run x category x sound index)
temp2 = temp2.reshape(NR_CATEG, NR_RUN, NR_SOUND_PER_CATEG_PER_RUN)
temp2 = np.transpose(temp2, [1, 0, 2])
temp2 = temp2.reshape(NR_RUN, NR_SOUND_PER_RUN)

# Randomize ordered arrays
for i in range(NR_RUN):
    temp2[i, :] = np.random.permutation(temp2[i, :])

# # Print before after
# for i in range(NR_RUN):
#     print('SUBSET:{}\n'.format(i))
#     print('Before (ordered):\n{}\n'.format(np.sort(temp2[i, :])))
#     print('After (permuted):\n{}\n'.format(temp2[i, :]))
#     print('-'*79)

# Insert rests
stim = np.ones([NR_RUN, NR_SOUND_PER_RUN*2]) * ID_REST
stim[:, 1::2] = temp2

# Insert offsets
stim = np.insert(stim, [0, stim.shape[1]], ID_OFFSET, axis=1)
stim = stim.astype(int)

# =============================================================================
# Insert attention task trials
# TODO

# =============================================================================
# Insert durations
# TODO: Add jitter to rests
dur = np.zeros(stim.shape, dtype=int)
dur[:, 2::2] = DUR_STIM
dur[:, 1:-1:2] = DUR_REST
dur[:, [0, -1]] = DUR_OFFSET

onset = np.cumsum(dur, axis=1)

# =============================================================================
# Export run protocols
date = time.strftime("%Y_%m_%d_%H_%M", time.localtime())
out_name = 'protocol_TEST_{}'.format(date)
out_path = os.path.join(OUT_DIR, out_name)

# Literal identifiers
stim_id = stim.astype(str)
stim_id[stim_id == str(ID_REST)] = 'rest'
stim_id[stim_id == str(ID_OFFSET)] = 'offset'

# TODO: Put stimulus file names here
temp_id1 = stim_id != 'rest'
temp_id2 = stim_id != 'offset'
stim_id[temp_id1 * temp_id2] = 'placeholder.wav'

for i in range(NR_RUN):
    out_run = '{}_run{}.tsv'.format(out_path, i+1)
    file = open(out_run, 'w')
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(['onset', 'duration', 'trial_type', 'identifier'])
    for j in range(stim.shape[1]):
        writer.writerow([onset[i, j], dur[i, j], stim_id[i, j], stim[i, j]])
    file.close()
