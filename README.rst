===============================
ALPACA
===============================

[![GitHub issues](https://img.shields.io/github/issues/C0C0AN/ALPACA.svg)](https://github.com/C0C0AN/ALPACA/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/C0C0AN/ALPACA.svg)](https://github.com/C0C0AN/ALPACA/pulls/)
[![GitHub contributors](https://img.shields.io/github/contributors/C0C0AN/ALPACA.svg)](https://GitHub.com/PeerHerholz/C0C0AN/ALPACA/contributors/)
[![GitHub Commits](https://github-basic-badges.herokuapp.com/commits/C0C0AN/ALPACA.svg)](https://github.com/C0C0AN/ALPACA/commits/master)
[![GitHub size](https://github-size-badge.herokuapp.com/C0C0AN/ALPACA.svg)](https://github.com/C0C0AN/ALPACA/archive/master.zip)
[![GitHub HitCount](http://hits.dwyl.io/C0C0AN/ALPACA.svg)](http://hits.dwyl.io/C0C0AN/ALPACA)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="alpaca/resources/img/ALPACA_logo.png" alt="alpaca logo" width="470" height="350" border="10">


Description
-----------
ALPACA is a toolbox (and hopefully soon BIDS app) for the localization and parcellation of human auditory cortex areas. In more detail, it includes an anatomical and a functional processing pipeline (implemented in [nipype](https://nipype.readthedocs.io/en/latest/)) that can be run alone or in combination. While the first just needs an anatomical image and takes advantage of [FreeSurfer](https://surfer.nmr.mgh.harvard.edu) and [ANTs](http://stnava.github.io/ANTs/), effectively mapping a user specified [list of auditory cortex regions](https://github.com/C0C0AN/ALPACA/tree/master/resources/regions_of_interest) from template to native space, the latter makes use of [different classic tonotopy experiments (that also come with the toolbox)](https://github.com/C0C0AN/ALPACA/tree/master/scripts_stimulation) and therefore requires functional data. Furthermore, it includes a [set of tutorials](https://github.com/C0C0AN/ALPACA/tree/master/resources/tutorials), ranging from data management and preparation over stimulus generation to ROI extraction. Beside being a hopefully helpful tool, ALPACA also intends to further increase standardization and reproducibility, by e.g., uploading anonymized results to an interactive online repository, allowing for large scale meta-analysis.


<img src="alpaca/resources/img/alpaca_poster_nh18.png" alt="alpaca poster">



Documentation
-------------
A documentation is currently in the works and will be available soon. Sorry for any inconvenience this might cause.
(COMING SOON!) https://peerherholz.github.io/alpaca.

How to report errors
--------------------
Running into any bugs :beetle:? Check out the [open issues](https://github.com/C0C0AN/ALPACA/issues) to see if we're already working on it. If not, open up a new issue and we will check it out when we can!

How to contribute
-----------------
Thank you for considering contributing to our project! Before getting involved, please review our [Code of Conduct](https://github.com/C0C0AN/ALPACA/blob/master/CODE_OF_CONDUCT.md). Next, you can review  [open issues](https://github.com/C0C0AN/ALPACA/issues) that we are looking for help with. If you submit a new pull request please be as detailed as possible in your comments. Please also have a look at our [contribution guidelines](https://github.com/C0C0AN/ALPACA/blob/master/CONTRIBUTING.md).

Acknowledgements
----------------
If you intend to or already used ALPACA, we would be very happy if you cite this github repo, till we have "something" out there!


<sub></sup>Please feel free to contact me wrt any question or idea via mail (herholz dot peer at gmail dot com), twitter ([@peerherholz](https://twitter.com/peerherholz?lang=eng)), the brainhack slack team (@peerherholz) or the project channel (#alpaca). <sup><sub>

<sub><sup>The ALPACA project logo was made using an amazing freely available alpaca picture from [Max Pixel](http://maxpixel.freegreatpicture.com/Pako-Mammal-Wool-Vicugna-Pacos-Alpaca-Wool-Alpaca-814953) and (cytoarchitectonic) auditory cortex ROIs from [Morosan et al.](https://www.ncbi.nlm.nih.gov/pubmed/11305897) overlaid on the right hemisphere of [freesurfer's fsaverage brain](https://surfer.nmr.mgh.harvard.edu). No alpacas were harmed during the creation of this logo. <sup></sub
