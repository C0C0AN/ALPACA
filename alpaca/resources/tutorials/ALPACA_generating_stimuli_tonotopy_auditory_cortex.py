# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Automatic Locazation and Parcellation of Auditory Cortex Areas
## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(ALPACA)
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/ALPACA_logo.png" alt="alpaca logo" width="370" height="250" border="10">
# ## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To burst or not to burst -<br/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generating stimuli to be used in experiments focusing the <br/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;localisation, structure and function of the auditory cortex

# ### This notebook deals with the generation of stimuli frequently used in studies focusing the [tonotopic organization of the auditory cortex](https://en.wikipedia.org/wiki/Tonotopy). More precisely, this notebook will show you how one type of stimuli and the respective paradigm included in the ALPACA toolbox was choosen and created.

# As you may know, a broad range of stimuli have been used to functionally localize the auditory cortex and further investigate it's structure, organization and function (you can find a very good overview article [here](https://doi.org/10.1016/j.heares.2013.07.016)). Throughout the last few years, two specific types of stimuli became more and more established: [natural sounds](https://en.wikipedia.org/wiki/Natural_sounds) and [pure tones (bursts)](https://en.wikipedia.org/wiki/Musical_tone#Pure_tone).
# The ALPACA toolbox uses both of them. As the first type of stimuli is reused from previous works (e.g. [here](https://doi.org/10.1073/pnas.1617622114) and [here](https://doi.org/10.1523/JNEUROSCI.1388-12.2012)) and is provided within a [data set release](http://datadryad.org/resource/doi:10.5061/dryad.np4hs), this notebook will focus on the latter.

# ### pure tones (bursts): same same, but different, but still the same?

# One would think that pure tones (bursts) aren't worth any detailed focus, as they appear to be simple, straight forward and not too diverse. But the truth is, that a fast majority of studies neither used the same pure tones (bursts) nor the same experimental paradigm. Therefore, spending some time thinking about the very specific type is more than worth it.
# After reading quite some [articles](https://github.com/PeerHerholz/open_science_fellowship_project/blob/master/open%20lab%20notebook/articles_list_auditory_cortex.md), some properties emerged as quite important:
# * _stimuli_
#     * specific frequencies
#     * how many frequencies
#     * spacing between frequencies
#     * repetition
#
#
# * _paradigm_
#     * ascending & descending vs. random trails
#     * MRI sequence (e.g. sparse sampling, etc.)
#     * duration
#     * task
#
# ALPACA decided to go for a mixture regarding these two points between studies by [Schoenwiesner et al. (2014)](https://doi.org/10.1093/cercor/bhu124) and [De Martino et al. (2014)](https://doi.org/10.1002/mrm.25408) as they show robust and convincing results that tackle some possible problems from older research work :
#
# * _stimuli_ (completed based on [Schoenwiesner et al. (2014)](https://doi.org/10.1093/cercor/bhu124))
#     * [pure tone](https://en.wikipedia.org/wiki/Musical_tone#Pure_tone) bursts, centered around 8 nominal, [logarithmically scaled frequencies](http://www.phon.ox.ac.uk/jcoleman/LOGARITH.htm) (200, 338.8, 573.8, 971.9, 1646.2, 2788.4, 4723.1 and 8000 Hz), 24.4-kHz sampling rate, 24-bit amplitude resolution &rarr; coverage of [normal human hearing](https://en.wikipedia.org/wiki/Hearing_range#Humans) and [cochlear](https://en.wikipedia.org/wiki/Cochlea)/[auditory cortex](https://en.wikipedia.org/wiki/Auditory_cortex) [bandwidths](https://en.wikipedia.org/wiki/Critical_band)
#     * specific frequencies varied in a range of 1 [semitone](https://en.wikipedia.org/wiki/Semitone) centered around the nominal frequency &rarr; prevent response adaption, large enough to be audible, but small enough to be processed in the [same channel](https://www.sciencedirect.com/science/article/pii/037859559090170T?via%3Dihub)
#     * each burst 187.5 ms in length, plus 20 ms [squared-cosine](https://en.wikipedia.org/wiki/Trigonometric_functions#Sine.2C_cosine.2C_and_tangent) [onset and offset ramps](https://www.audiologyonline.com/ask-the-experts/what-is-tone-burst-ramping-11939), presented every 250 ms for 4 seconds (one trial) &rarr; increase signal & prevent onset distortions
#     * present on background noise with [equivalent rectangular bandwith](https://en.wikipedia.org/wiki/Equivalent_rectangular_bandwidth) &rarr; minimize variation inf hearing tresholds between frequencies and participants <br/ >
#
#
# * _paradigm_ (based partly on [Schoenwiesner et al. (2014)](https://doi.org/10.1093/cercor/bhu124) (1) and partly on [De Martino et al. (2014)](https://doi.org/10.1002/mrm.25408) (2))
#     * random trial order &rarr; balanced transition probabillity (from (1))
#     * 20 trials × 8 frequencies + 160 baseline trials + 4 initial dummy trials &rarr; 324 trials in total (from (1))
#     * split into 4 runs &rarr; to enable all planned analysis as good as possible
#     * passive listening task (from (1))
#     * [multiband acquisition scheme](http://mriquestions.com/simultaneous-multi-slice.html) (from (2))
#

# ### my name is burst, pure tone burst

# Now, finally, let's get to work and create the above described stimuli. As for most things, first: there's a python package that will help you greatly and second: someone already did something comparable, so we don't have to start from scratch when generating pure tone bursts. An amazing resource that helps you getting started to work with any kind of audio stimuli / files for nearly every purpose is the [awesome-python-scientific-audio repository on github](https://github.com/faroit/awesome-python-scientific-audio). It's a list of python packages organized based on types of applications / analyses within audio research and is very comprehensive. Furthermore, it contains other useful resources such as [tutorials](https://github.com/faroit/awesome-python-scientific-audio#tutorials), [books](https://github.com/faroit/awesome-python-scientific-audio#books), [articles](https://github.com/faroit/awesome-python-scientific-audio#scientific-papers) and [much more](https://github.com/faroit/awesome-python-scientific-audio#other-resources).
