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

import numpy as np

# =============================================================================
# User inputs
NR_CATEG = 7  # Number of categories
NR_SOUND_CATEG = 24  # Number of sounds per category
NR_SOUND_CATEG_PER_RUN = 6  # Number of sounds per category per run

# =============================================================================
# Parameters

# Total number of sounds
nr_sound = NR_CATEG*NR_SOUND_CATEG
# Number of sounds per run
nr_sound_per_run = NR_CATEG * NR_SOUND_CATEG_PER_RUN
# Number of runs to complete a full set
nr_run = nr_sound/nr_sound_per_run
# Number of sounds per categtory per run
nr_sound_per_categ_per_run = NR_SOUND_CATEG / NR_SOUND_CATEG_PER_RUN

# =============================================================================
# Generate protocol
temp1 = []
temp2 = [[], [], [], []]

# Generate ordered arrays
for i in range(0, nr_sound_per_categ_per_run):
    blocks = []
    for j in range(0, NR_CATEG):
        # NOTE: Assumes 0 is dedicated for silent stimulus.
        for k in range(1, NR_SOUND_CATEG_PER_RUN + 1):
            x = k + NR_SOUND_CATEG * j + NR_SOUND_CATEG_PER_RUN * i
            blocks = np.append(blocks, [x])
    temp1.append(blocks.astype(int))

# Randomize ordered arrays
print('-'*79)
for i in range(0, nr_run):
    i_array = temp1[i]

    print('SUBSET:{}\n\nOrdered:\n{}'.format(i+1, i_array))

    idx = np.arange(1, nr_sound_per_run + 1)  # index
    newArr, prevRndList = [], []
    prevRnd = -1  # just initialize
    iterCount = 0  # Count iterations for report at the end.

    # NOTE: I don't see what/why is happening here, need to comment better.
    while True:
        # Random number
        rnd_0 = np.floor((np.random.random_sample(1) * nr_sound_per_run))
        rnd = np.floor(rnd_0 / NR_SOUND_CATEG_PER_RUN)

        if rnd != prevRnd:
            if rnd_0 not in prevRndList:
                # Correct occurence, append to list
                newArr = np.append(newArr, i_array[int(rnd_0)])
                # Note down the used index
                prevRndList = np.append(prevRndList, rnd_0)

                if newArr.size == i_array.size:  # When enough entries reached
                    break

        prevRnd = np.copy(rnd)
        iterCount += 1

    newArr = newArr.astype(int)

    print('\nRandomized:\n{}\n\nIteration count:{}'.format(newArr, iterCount))
    print('-'*79)

# =============================================================================
# Insert rests

# =============================================================================
# Export protocol
