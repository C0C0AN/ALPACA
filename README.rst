===============================
ALPACA
===============================

.. image:: https://img.shields.io/travis/C0C0AN/ALPACA.svg
        :target: https://travis-ci.org/C0C0AN/ALPACA

.. image:: https://img.shields.io/pypi/v/ALPACA.svg
        :target: https://pypi.python.org/pypi/ALPACA
        
.. image:: https://img.shields.io/github/issues-pr/C0C0AN/ALPACA.svg
    :alt: PRs
    :target: https://github.com/C0C0AN/ALPACA/pulls/

.. image:: https://img.shields.io/github/contributors/C0C0AN/ALPACA.svg
    :alt: Contributors
    :target: https://GitHub.com/C0C0AN/ALPACA/graphs/contributors/

.. image:: https://github-basic-badges.herokuapp.com/commits/C0C0AN/ALPACA.svg
    :alt: Commits
    :target: https://github.com/C0C0AN/ALPACA/commits/master

.. image:: http://hits.dwyl.io/C0C0AN/ALPACA.svg
    :alt: Hits
    :target: http://hits.dwyl.io/C0C0AN/ALPACA

.. image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
    :alt: License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. image:: alpaca/resources/img/ALPACA_logo.png
    :align: center
    :scale: 30 %
    :alt: alpaca_logo

Description
-----------
ALPACA is a toolbox (and hopefully soon BIDS app) for the localization and parcellation of human auditory cortex areas. In more detail, it includes an anatomical and a functional processing pipeline (implemented in `nipype <https://nipype.readthedocs.io/en/latest/>`_) that can be run alone or in combination. While the first just needs an anatomical image and takes advantage of `FreeSurfer <https://surfer.nmr.mgh.harvard.edu>`_ and `ANTs <http://stnava.github.io/ANTs/>`_, effectively mapping a user specified `list of auditory cortex regions <https://github.com/C0C0AN/ALPACA/tree/master/resources/regions_of_interest>`_ from template to native space, the latter makes use of `different classic tonotopy experiments that also come with the toolbox <https://github.com/C0C0AN/ALPACA/tree/master/scripts_stimulation>`_ and therefore requires functional data. Furthermore, it includes a `set of tutorials <https://github.com/C0C0AN/ALPACA/tree/master/resources/tutorials>`_, ranging from data management and preparation over stimulus generation to ROI extraction. Beside being a hopefully helpful tool, ALPACA also intends to further increase standardization and reproducibility, by e.g., uploading anonymized results to an interactive online repository, allowing for large scale meta-analysis.

Documentation
-------------
A documentation is currently in the works and will be available soon. Sorry for any inconvenience this might cause.
(COMING SOON!) https://peerherholz.github.io/alpaca.

How to report errors
--------------------
Running into any bugs :beetle:? Check out the `open issues <https://github.com/C0C0AN/ALPACA/issues>`_ to see if we're already working on it. If not, open up a new issue and we will check it out when we can!

How to contribute
-----------------
Thank you for considering contributing to our project! Before getting involved, please review our `Code of Conduct <https://github.com/C0C0AN/ALPACA/blob/master/CODE_OF_CONDUCT.md>`_. Next, you can review  `open issues <https://github.com/C0C0AN/ALPACA/issues>`_ that we are looking for help with. If you submit a new pull request please be as detailed as possible in your comments. Please also have a look at our `contribution guidelines <https://github.com/C0C0AN/ALPACA/blob/master/CONTRIBUTING.md>`_.

Acknowledgements
----------------
If you intend to or already used ALPACA, we would be very happy if you cite this github repo, till we have "something" out there!


Please feel free to contact me wrt any question or idea via mail (herholz dot peer at gmail dot com), twitter (`@peerherholz <https://twitter.com/peerherholz?lang=eng>`_), the brainhack slack team (@peerherholz) or the project channel (#alpaca). 

The ALPACA project logo was made using an amazing freely available alpaca picture from `Max Pixel <http://maxpixel.freegreatpicture.com/Pako-Mammal-Wool-Vicugna-Pacos-Alpaca-Wool-Alpaca-814953>`_ and (cytoarchitectonic) auditory cortex ROIs from `Morosan et al. <https://www.ncbi.nlm.nih.gov/pubmed/11305897>`_ overlaid on the right hemisphere of `FreeSurfer's fsaverage brain <https://surfer.nmr.mgh.harvard.edu>`_. No alpacas were harmed during the creation of this logo. 

Support
-------
This work is supported in part by funding provided by `Brain Canada <https://braincanada.ca/>`_, in partnership with `Health Canada <https://www.canada.ca/en/health-canada.html>`_, for the `Canadian Open Neuroscience Platform initiative <https://conp.ca/>`_.

.. image:: https://conp.ca/wp-content/uploads/elementor/thumbs/logo-2-o5e91uhlc138896v1b03o2dg8nwvxyv3pssdrkjv5a.png
    :alt: logo_conp
    :target: https://conp.ca/
