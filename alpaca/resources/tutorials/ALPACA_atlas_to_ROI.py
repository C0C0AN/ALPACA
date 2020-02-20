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
# ## &nbsp;&nbsp;&nbsp;extracting (auditory cortex) regions of interest (ROIs) from atlases of the human brain

# ### This notebook will focus on how to extract regions of interest from atlases of the human. As ALPACA is all about the [auditory cortex](https://en.wikipedia.org/wiki/Auditory_cortex), all examples will be used to extract [regions of interest](https://en.wikipedia.org/wiki/Region_of_interest#Medical_imaging) within the auditory cortex . Given that most atlases of the human brain are in a [reference space, e.g. the mni space](http://www.lead-dbs.org/?p=1241), a section of the notebook will also show how to transform regions of interest from reference to a participants respective native space. Comparable to other notebooks of the ALPACA toolbox, the methods and analyses steps described here are easy to adapt for other, more general purposes than "just" auditory neuroscience related topics.

# ### Around the brain in 80 atlases

# You might ask yourself "What's with all that talking about atlases? What's actually an atlas of the human brain?". So, to enable the best possible understanding and to bring everyone (nearly) on the same page, the first section of this notebook will give a brief overview of atlases of the human brain.
