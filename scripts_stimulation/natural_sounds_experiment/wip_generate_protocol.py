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
# User input

NR_CATEG = 6  # Total number of categories
NR_SOUND_PER_CATEG = 48  # Number of sounds per category
NR_RUN = 8  # Number of runs to present full set of sounds once

# =============================================================================
# Derived parameters

# Total number of sounds
NR_SOUND = NR_CATEG * NR_SOUND_PER_CATEG
if NR_SOUND % NR_RUN != 0:  # TODO: Swap with try/except?
    print('Number of runs cant divide total nr. sounds!')
# Number of sounds per categtory per run
NR_SOUND_PER_CATEG_PER_RUN = NR_SOUND_PER_CATEG / NR_RUN
# Number of sounds per run
NR_SOUND_PER_RUN = NR_CATEG * NR_SOUND_PER_CATEG_PER_RUN

# =============================================================================
# Generate stimulus presentation order

# Create ordered list of integers representing different sounds
temp1 = np.arange(NR_SOUND)
# Add 1 because 0 will represent silence (NOTE: Might change slience to -1)
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

# Print before after
for i in range(NR_RUN):
    print('SUBSET:{}\n'.format(i))
    print('Before (ordered):\n{}\n'.format(np.sort(temp2[i, :])))
    print('After (permuted):\n{}\n'.format(temp2[i, :]))
    print('-'*79)

# =============================================================================
# Insert rests

# =============================================================================
# Export protocol
