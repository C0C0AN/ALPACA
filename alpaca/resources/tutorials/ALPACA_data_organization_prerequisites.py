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
#     display_name: Bash
#     language: bash
#     name: bash
# ---

# # &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Automatic Locazation and Parcellation of Auditory Cortex Areas
## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(ALPACA)
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/ALPACA_logo.png" alt="alpaca logo" width="370" height="250" border="10">
# ## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data organization & prerequisites

# ### This notebook will provide you with information regarding data organization and prerequisites necessary to run the ALPACA toolbox. However, as the tools presented here are highly recommended in state of the art neuroinformatics and aren't specific for the ALPACA toolbox, they're also useful for any other neuroimaging related application intended to be comprehensive, robust, reproducible and openly shared.
#
# ### More precisely, it'll contain the following sections:
#
# ##### - sidequest: [docker](https://www.docker.com)
#
# ### - data organization using the [Brain Imaging Data Structure (BIDS)](http://bids.neuroimaging.io)
#
# ### - data quality control & assurance using [MRIQC](https://mriqc.readthedocs.io/en/latest/)
#
# ### - structural image processing using [mindboggle](http://www.mindboggle.info)

# Before we actually start, let me pump the breaks right here and open a sidequest that is not only important for this tutorial notebook and the toolbox, but also will change your (neuroscience-programming-related) life completely.
# Picture the following scenario (which we all been in at least a couple of times): you want to use some function, code, scripts, etc. that someone put out there or a colleague shared with you. Usually and depending on the specific case, that comes with certain requirements you have to meet, or more precisely certain dependencies the respective function, code, scripts, etc. builds upon and needs to work properly. Even worse: sometimes you even need a specific OS. Depending on you, your set of skills and your set up this results (quite often) in anger, wasted time and drinks. Well, no more! How you ask? By using a pretty amazing thingy called docker:
#
# ##### sidequest: [docker](https://www.docker.com)
#
# **Note**: *This section heavily uses information & parts from the [docker notebook in Michael Notter's nipype tutorial](https://miykael.github.io/nipype_tutorial/notebooks/introduction_docker.html). If you find anything that is not referenced correctly or at all, I'm truly sorry, but please let me know, so that I can give appropriate credit.*

# <img src="../img/logoDocker.png" alt="Drawing" style="width: 400px;"/>

# [Docker](https://www.docker.com/) is an open-source project that automates the deployment of applications inside software containers. Those containers wrap up a piece of software in a complete filesystem that contains everything it needs to run: code, system tools, software libraries, such as [Python](https://www.python.org), neuroimaging related software such as [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSL), [AFNI](https://afni.nimh.nih.gov), [SPM](http://www.fil.ion.ucl.ac.uk/spm/), [FreeSurfer](https://surfer.nmr.mgh.harvard.edu), [ANTs](http://stnava.github.io/ANTs/) and pretty much any other open source software or tools. This guarantees that it will always run the same, regardless of the environment it is running in. As this notebook will just briefly talk about docker and it's application, make sure you go through this very nice and comprehensive [introduction to docker](http://nipy.org/workshops/2017-03-boston/lectures/lesson-container/#1).
#
# Wondering why we're actually talking about this (I mean besides the already mentioned advantages)? Well, as ALPACA is commited and interested in open and reproducible (neuro-)science, the toolbox itself will be in a docker container one day and everything we focus on here will highly depend on / make us of docker. Additionally, and I can't stress this enough, it's incredibly useful. Now, let's check some basic docker commands:

# ##### Install docker
# Before you can do anything, you first need to install [docker](https://www.docker.com/) on your system.
# The installation process differes per system. Luckily, the docker homepage has nice instructions for...
#
# - [Ubuntu](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) or [Debian](https://docs.docker.com/engine/installation/linux/docker-ce/debian/)
# - [Windows 7/8/9/10](https://docs.docker.com/toolbox/toolbox_install_windows/) or [Windows 10Pro](https://docs.docker.com/docker-for-windows/install/)
# - [OS X (from El Capitan 10.11 on)](https://docs.docker.com/docker-for-mac/install/) or [OS X (before El Capitan 10.11)](https://docs.docker.com/toolbox/toolbox_install_mac/)
#
# Once Docker is installed, open up a terminal and test it works properly with the command:

docker run hello-world

# **Note**: Linux users might need to use `sudo` to run `docker` commands or follow [post-installation steps](https://docs.docker.com/engine/installation/linux/linux-postinstall/).
#
# ##### Pulling and checking available docker images
# You can download various docker images from [docker hub](https://hub.docker.com), which always works like this:
#
# `docker pull docker_id/docker_image:version` , e.g. `docker pull peerherholz/ALPACA:latest`
#
# **Note**: you don't have to include `:version` if you're not looking for a specific version. When not including it, `:latest` is set by default.
#
# Once it's done or whenever you want, you can check available images on your system:

docker images

# ##### How to run docker images
# After installing docker on your system, making sure that the hello-world example was running and pulling one or the other docker image you would like to use, you are good to go and actually run a docker image. The exact implementation of that is a bit different for Windows user, but the general commands look similar. The standard version goes something like this:
#
# `docker run -it --rm -p 8888:8888 docker_id/docker_image command`
#
# However, if you want use stuff (notebooks, code, scripts, etc.) which are not included in the respective docker image, but should run within it's environment, access process or save local or remote data, you can also mount your  directories, e.g.:
#
# `docker run -it --rm -v /path/to/resources/:/home/resources -v /path/to/data/:/home/data -v /path/to/output/:/home/output -p 8888:8888 docker_id/docker_image command`
#
#
# But what do those flags mean?
#
# - the `-it` flag tells docker that it should open an interactive container instance
# - the `--rm` flag tells docker that the container should automatically be removed after we close docker
# - the `-p` flag specifies which port we want to make available for docker
# - the `-v` flag tells docker which folders should be mount to make them accesible inside the container. Here:   /path/to/resources is your local directory where you stored notebooks, functions, scripts. /path/to/data/ is a directory where you stored your data, and /path/to/output can be an empty directory that will be used for output. - The second part of the `-v` flag (here: /home/resources, /data or /output) specifies under which path the mounted folders can be found inside the container. Important: To use the resource, data, output or any other folder, you first need to create them on your local system!
# - `docker_id/docker_image` tells docker which image you want to run
# - `command` tells docker, that you want to directly run a certain command within the container

# ##### Docker tips and tricks
# ###### Access docker container with bash
# You can access a docker container directly with bash or ipython by adding it to the end of your command, i.e.:
#
# `docker run -it --rm -v /path/to/resources/:/home/resources -v /path/to/data/:/home/data -v /path/to/output/:/home/output -p 8888:8888 docker_id/docker_image bash`
#
# `docker run -it --rm -v /path/to/resources/:/home/resources -v /path/to/data/:/home/data -v /path/to/output/:/home/output -p 8888:8888 docker_id/docker_image ipython`
#
#
# This also works with other software commands, such as bet etc.
#
# ###### Stop Docker Container
# To stop a running docker container, either close the docker running  terminal or select the terminal and press the `Ctrl-C` shortcut multiple times.

# ###### List all installed docker images
# To see a list of all installed docker images use:
#
#

docker images

# ###### Delete a specific docker image
# To delete a specific docker image, first use the `docker images` command to list all installed containers and than use the `IMAGE ID` and the `rmi` instruction to delete the container:

docker rmi -f IMAGE ID

# ###### Export and import a docker image
# If you don't want to depend on a internet connection, you can also export an already downloaded docker image and than later on import it on another PC. To do so, use the following two commands:
#
# - export docker image docker_id/docker_image
#
# `docker save -o docker_image.tar docker_id/docker_image`
#
# - import docker image on another PC
#
# `docker load --input docker_image.tar`
#
# It might be possible that you run into administrator privileges isssues because you ran your docker command with `sudo`. This means that other users don't have access rights to `docker_image.tar`. To avoid this, just change the rights of `docker_image.tar` with the command:
#
# `sudo chmod 777 docker_image.tar`
#
# For more information check the [already mentioned introduction](http://nipy.org/workshops/2017-03-boston/lectures/lesson-container/#1) or Michael Notter's [introduction to docker notebook](https://miykael.github.io/nipype_tutorial/notebooks/introduction_docker.html).

# ### After our short sidequest into the world of docker, let's start with something which is as basic as it's important: the structure of your data.

# ## Data organization using [BIDS](http://bids.neuroimaging.io)
#
# **Note**: *This section heavily uses information & parts from the [BIDS website](http://bids.neuroimaging.io), [openfmri](https://openfmri.org), the [BIDS paper in Nature Scientific Data](https://doi.org/10.1038/sdata.2016.44) and the [BIDS notebook in Michael Notter's nipype tutorial](https://miykael.github.io/nipype_tutorial/notebooks/introduction_dataset.html). If you find anything that is not referenced correctly or at all, I'm truly sorry, but please let me know, so that I can give appropriate credit.*

# The ALPACA toolbox assumes or let's say works best when your data is structured according to the Brain Imaging Data Structure (BIDS). BIDS is a simple and intuitive way to organize and describe your neuroimaging and behavioral data. Neuroimaging experiments result in complicated data that can be arranged in many different ways. So far there is no consensus how to organize and share data obtained in neuroimaging experiments. BIDS tackles this problem by suggesting a new standard for the arrangement of neuroimaging datasets.
#
# The idea of BIDS is that the file and folder names follow a strict set of rules (graphic taken from [here](https://www.nature.com/articles/sdata201644/figures/1)):
#
# <img src="../img/bids.png" alt="Drawing" style="width: 800px;"/>
#
#

# BIDS basically describes how you should organize and structure your data, which not only helps you, but also others when sharing your data (which is also eased up). This also allows hassle free applications of other workflows and pipelines which can work with BIDS datasets, increases reproducibility and simplifies collaboration. Once ALPACA has grown up and became super fluffy it is intended to also run as a [BIDS app](http://bids-apps.neuroimaging.io), meaning that you'll be able to run the whole toolbox (or just the parts you want) within one line of code and without any software-installation-related stress. Pretty cool, eh? To do so, BIDS and the here mentioned prerequisites are necessary...just to convince you even more to start using BIDS.

# ##### How to convert datasets into BIDS?

# At this point you might ask yourself: nice stuff, but how do I get my dataset into BIDS? Well, this depends on how your data is currently organized and which file format it is in. If you already have converted your data from [dicom](https://en.wikipedia.org/wiki/DICOM) to [nifti](www.nifti.nimh.nih.gov/) the easist way would be to write a small bash/python/matlab/etc. script that reorganizes you files into BIDS. However, if you still have your files in dicom, it's recommend to convert them again using certain tools, like those which are listed [here](https://neurostars.org/t/convert-data-to-bids-format/720), as they allow you to extract more metadata than is usually present in your niftis and also already organize your dataset into BIDS. As there are quite a few out there, I would recommend checking their respective github sites, play around a bit and decide for one that works well for you.
#
# As an example, for me this is [heudiconv](https://github.com/nipy/heudiconv), which can also be run via [docker](https://hub.docker.com/r/nipy/heudiconv/).
# To familiarize yourself with heudiconv, check the additional information and tutorials on it's [github page](https://github.com/nipy/heudiconv). If you want to use heudiconv via docker:
#
# 1. get it by running &nbsp;&nbsp; `docker pull nipy/heudiconv` &nbsp;&nbsp; in your terminal
# 2. check this [introduction](http://nipy.org/workshops/2017-03-boston/lectures/bids-heudiconv/#1)

# ##### Almost there
#
# Got your dataset in BIDS? Coolio! Only two more things you should do before you start working on it!
# I guess you know the saying "sharing is caring", eh? Like mentioned before, in the context of BIDS / neuroimaging this means sharing your data publicly and freely with others, so that the whole field and world can benefit from it. That's one part of "caring", with the other being "caring" about privacy protection. More precisely, protecting the privacy of the individuals that have been scanned. Besides being self-evident, all major neuroimaging data sharing initiatives and platforms require [_anonymization_](https://open-brain-consent.readthedocs.io/en/stable/anon_tools.html). There are different tools which can be used for that. Have a look at the [respective section of the Open Brain Consent docs](https://open-brain-consent.readthedocs.io/en/stable/anon_tools.html) for some examples. However, you have to decide on one and as you can see below, they tend to perform very differently (graphic taken from [BIDSonym](https://peerherholz.github.io/BIDSonym/)):
# <img src="https://raw.githubusercontent.com/PeerHerholz/BIDSonym/master/img/bidsonym_example.png" alt="Drawing" style="width: 800px;"/>


# To keep the momentum going and in the spirit of what we've talked about above, we're going to use [BIDSOnym](https://peerherholz.github.io/BIDSonym/) as it supports the most frequently used `de-facing` tools and additionally also takes care of potentially sensitive information in the image headers and meta-data.
#
#
# Here's how you get the [BIDSonym Docker image](https://hub.docker.com/r/peerherholz/bidsonym):

docker pull peerherholz/bidsonym

# Let's assume you want to apply it to the data of the participant with the id `01` who has T1w and T2w anatomical data using [pydeface](https://github.com/poldracklab/pydeface/) to deface the images. Additionally you want to check and delete certain meta-data fields, create a brainmask for quality-control purposes using [FSL's BET](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET) and keep the original, non-anonymized data in case something goes wrong. Here's your command:

 sudo docker run -it --rm \
 -v /home/peerherholz/Desktop/bidsonym/example_data/:/bids_dataset \
 peerherholz/bidsonym /bids_dataset participant --participant_label 01 \
 --deid pydeface --del_meta 'InstitutionAddress' --deface_t2w \
 --del_nodeface no_del --brainextraction bet --bet_frac 0.5 --participant_label 01 \

# De-identified all participants in your BIDS dataset? Awesome! At this point, so before start working with and/or sharing your dataset, you might want to make sure that everything is correct, nothing's missing and you're good to go. But don't worry, you don't have to go through your whole dataset checking every folder and file. As we're in the realm of robust, reproducible and automated processing there's, of course, a tool for that. It's called [bids-validator](https://github.com/INCF/bids-validator) and can be applied in multipe ways:
#
# - web browser version:
#
#   - in google Chrome (currently the only supported browser) go to the [bids-validator website](http://incf.github.io/bids-validator/)
#   - select the folder containing your BIDS dataset
#   - check the output and, if erros/problems appear (e.g. missing files), resolve them and run it again
#
#
# - docker version:
#
#   - get the [docker image](https://hub.docker.com/r/bids/validator/)
#   - run it on your BIDS dataset, by providing the respective path
#   - check the output and, if erros/problems appear (e.g. missing files), resolve them and run it again

docker pull bids/validator

docker run -ti --rm -v /path/to/BIDS/dataset:/data:ro bids/validator /data

# ##### How to make use of it

# Besides the already mentioned advantages there are a lot of tools which are intended to and ease up the work with BIDS datasets. A very good example is [pybids](https://github.com/INCF/pybids), which is incredibly useful for any kind of interaction with [BIDS](http://bids.neuroimaging.io) datasets, e.g. within a nice & reproducible [nipype](https://github.com/nipy/nipype) [workflow](http://nbviewer.jupyter.org/github/nipy/workshops/blob/master/170327-nipype/notebooks/basic-bids/basic_data_input_bids.ipynb). Make sure to also have a look at [bidsutils](https://github.com/INCF/bidsutils). Furthermore, you should also check the already mentioned [BIDS apps](http://bids-apps.neuroimaging.io). These are "portable neuroimaging pipelines that understand BIDS datasets". More precisely, [BIDS apps](http://bids-apps.neuroimaging.io/about/) are neuroimaging pipelines / workflows for a [huge variety of analyses](http://bids-apps.neuroimaging.io/apps/) packed in a docker image that will work / run out of the box given a [BIDS dataset](https://www.nature.com/articles/sdata201644) as input. It won't get any more comfortable (okay, maybe with [openneuro.org](https://openneuro.org)).
#
# That being said, let's actually work with BIDS and BIDS apps to get some data ready for ALPACA.
#
# **Note**: if you decide to use any of the mentioned tools please show credit by citing them: [BIDS](https://doi.org/doi:10.1038/sdata.2016.44), [BIDS apps](https://doi.org/10.1371/journal.pcbi.1005209), [heudiconv](https://github.com/nipy/heudiconv), [mri_deface](https://doi.org/10.1002/hbm.20312), [pydeface](https://github.com/poldracklab/pydeface) and [bids-valditor](http://incf.github.io/bids-validator/).

# ## data quality control & assurance using [MRIQC](https://poldracklab.github.io/mriqc/)

# **Note**: _This section heavily uses information & parts from the [MRIQC website](https://poldracklab.github.io/mriqc/), [MRIQC readthedocs page](http://mriqc.readthedocs.io/en/latest/) and [MRIQC paper in PLOS ONE](https://doi.org/10.1371/journal.pone.0184661). If you find anything that is not referenced correctly or at all, I'm truly sorry, but please let me know, so that I can give appropriate credit._
#
#
# Assuming your data is in BIDS format, de-identified and the BIDS validator had nothing to complain, it's time to let the games begin. Along the initial steps of analyzing neuroimaging data (or basically any other data as well) some sort of data quality control should be done. This is important, as checking for [artifacts](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4340093/), [inhomogeneities](http://www.mr-tip.com/serv1.php?type=db1&dbs=Inhomogeneity) or any other kind of data corruption can prevent effects of the mentioned possible problems on your analyses and results. An example is depicted below (modified from Esteban O, Birman D, Schaer M, Koyejo OO, Poldrack RA, Gorgolewski KJ (2017) MRIQC: Advancing the automatic prediction of image quality in MRI from unseen sites. PLoS ONE 12(9): e0184661. https://doi.org/10.1371/journal.pone.0184661):
#
#
# <img src="../img/artifact_example_MRIQC.png" alt="Drawing" style="width: 600px;"/>
#
#
#
# As visual inspections can become quite time consuming and demanding in the age of big (neuroimaging) data and [inter-rater reliability](https://en.wikipedia.org/wiki/Inter-rater_reliability) shows quite some variability, automated quality assessments come in handy. Over the years some toolboxes were developed which all compute a broad amount of image quality metrics. Among those and very recommendable are [QAP](http://preprocessed-connectomes-project.org/quality-assessment-protocol/) and [MRIQC](http://mriqc.readthedocs.io/en/latest/). As the latter builds upon the first and is already provided as a docker image, this notebook will focus on [MRIQC](http://mriqc.readthedocs.io/en/latest/).

# ##### What exactly is [MRIQC](http://mriqc.readthedocs.io/en/latest/)?
#
# MRI Quality Control Tool (MRIQC) is tool for automated quality assessment which it does by extracting (image) quality measures. The [introduction page of MRIQC](http://mriqc.readthedocs.io/en/latest/about.html) provides a comprehensive overview of it's functions and properties:
#
# MRIQC is an open-source project, developed under the following software engineering principles:
#
# 1. Modularity and integrability: MRIQC implements a [nipype](http://nipype.readthedocs.io/en/latest/) [workflow](http://miykael.github.io/nipype-beginner-s-guide/firstSteps.html#important-building-blocks) to integrate modular sub-workflows that rely upon third party software toolboxes such as [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki), [ANTs](http://stnava.github.io/ANTs/) and [AFNI](https://afni.nimh.nih.gov).
# 2. Minimal preprocessing: the MRIQC workflows should be as minimal as possible to estimate the IQMs on the original data or their minimally processed derivatives.
# 3. Interoperability and standards: MRIQC follows the the [brain imaging data structure (BIDS)](http://bids.neuroimaging.io), and it adopts the [BIDS-App](http://bids-apps.neuroimaging.io) standard.
# 4. Reliability and robustness: the software undergoes frequent vetting sprints by testing its robustness against data variability (acquisition parameters, physiological differences, etc.) using images from [OpenfMRI](https://openfmri.org). Its reliability is permanently checked and maintained with [CircleCI](https://circleci.com/gh/poldracklab/mriqc).
#
# MRIQC is part of the MRI image analysis and reproducibility platform offered by the [CRN](http://reproducibility.stanford.edu). This pipeline derives from, and is heavily influenced by, the [PCP Quality Assessment Protocol](http://preprocessed-connectomes-project.org/quality-assessment-protocol/).

# ##### How to get and run [MRIQC](https://mriqc.readthedocs.io/en/latest/install.html)
#
# At this point you can probably guess the next few lines...yup, there are different ways of getting / running MRIQC: via [pip](https://github.com/poldracklab/mriqc), [docker](https://hub.docker.com/r/bids/mriqc/) or [openneuro.org](https://openneuro.org). Please be aware, that as MRIQC is a [BIDS app](http://bids-apps.neuroimaging.io) it assumes that your dataset is in BIDS format. But as already mentioned, if you followed the notebook till here and the [bids-validator](https://github.com/INCF/bids-validator) had nothing to complain, you're good to go.

# - run MRIQC on [openneuro.org](https://openneuro.org)
#
#   - don't want to deal with any sort of installation, don't have reasonable computing power or just want
#     to try MRIQC before actually deciding on running it &rarr; [openneuro.rg](https://openneuro.org) is the way to go
#   - go to [www.openneuro.org](https://openneuro.org) and sign in
#   - select the MRIQC pipeline and select the folder of the BIDS dataset on your local machine
#   - wait for the magic to happen
#   - check and download the output

# - run MRIQC with [docker](https://hub.docker.com/r/poldracklab/mriqc/)
#
#   - get the MRIQC docker image via

docker pull poldracklab/mriqc

#    - check if the MRIQC docker images works properly (if so, the last line of the output should show the current version of mriqc)

docker run -it poldracklab/mriqc:latest -v

#   - run MRIQC docker image on the participant level using the following command:
#
#   `docker run -it --rm -v /path/to/BIDS/dataset:/data:ro -v /path/to/output/folder:/out poldracklab/mriqc:latest /data /out participant --participant_label participant labels`
#
#   for example on participants 001, 002 & 003:
#
#   `docker run -it --rm -v /Users/peer/ALPACA:/data:ro -v /Users/peer/ALPACA/output:/out poldracklab/mriqc:latest /data /out participant --participant_label 001 002 003`

docker run -it --rm -v /path/to/BIDS/dataset:/data:ro -v /path/to/output/folder:/out poldracklab/mriqc:latest /data /out participant --participant_label participant labels

#    - run MRIQC docker image on the group level & generate a report based on previously processed participants using the following command:
#
#    `docker run -it --rm -v /path/to/BIDS/dataset:/data:ro -v /path/to/output/folder:/out poldracklab/mriqc:latest /data /out group`
#
#    for example on the BIDS input from above:
#
#    `docker run -it --rm -v /Users/peer/ALPACA:/data:ro -v /Users/peer/ALPACA/output:/out poldracklab/mriqc:latest /data /out group`
#

docker run -it --rm -v /path/to/BIDS/dataset:/data:ro -v /path/to/output/folder:/out poldracklab/mriqc:latest /data /out group

# - get / run MRIQC via pip / as a python module
#
#   - only supports python 3
#   - not recommend, but if you really want / need it, here you go
#   - get the necessary dependencies: [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki), [AFNI](https://afni.nimh.nih.gov) & [ANTs](http://stnava.github.io/ANTs/) &rarr; if you're on a linux distribution this is comparably easy:
#
#     - get the [NeuroDebian repository](http://neuro.debian.net) (if you already have it, awesome, skip to "get the system dependencies")
#       &rarr; go [here](http://neuro.debian.net/#get-neurodebian), select your operating system and the server you want to use, choose the option "All software", run the resulting two lines of command, e.g.

wget -O- http://neuro.debian.net/lists/xenial.de-md.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
sudo apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9

#         - update your operating system via:

sudo apt-get update

#         - get the system dependencies

sudo apt-get install fsl afni ants
sudo ln -sf /usr/lib/ants/N4BiasFieldCorrection /usr/local/bin/

#         - make sure that the respective binaries are added to $PATH
#         - get MRIQC via pip

pip install -r https://raw.githubusercontent.com/poldracklab/mriqc/master/requirements.txt
pip install git+https://github.com/poldracklab/mriqc.git

#    - run MRIQC on the participant level using the following command:
#
#      `mriqc /path/to/BIDS/dataset/ /path/to/output/folder/ participant --participant-label participant labels --verbose`
#
#      for example on participants 01, 02 & 03:
#
#      `mriqc /Users/peer/ALPACA/ /Users/peer/ALPACA/output participant --participant-label 01 02 03 --verbose`
#

mriqc /path/to/BIDS/dataset/ /path/to/output/folder/ participant --participant-label participant labels --verbose

#   - run MRIQC on the group level & generate a report based on previously processed participants using the following command:
#
#   `mriqc path/to/BIDS/dataset/ /path/to/output/folder/ group`
#
#   for example on the BIDS input from above:
#
#   `mriqc /Users/peer/ALPACA/ /Users/peer/ALPACA/output group`

mriqc path/to/BIDS/dataset/ /path/to/output/folder/ group

# ##### What's happening when running MRIQC ?
#
# As said before, MRIQC computes a broad range of [image quality metrics (IQM)](https://mriqc.readthedocs.io/en/latest/measures.html#qap) within two main workflows: [IQMs for structural](https://mriqc.readthedocs.io/en/latest/iqms/t1w.html) and [IQMs for functional images](https://mriqc.readthedocs.io/en/latest/iqms/bold.html).

#    - [IQMs for structural images](https://mriqc.readthedocs.io/en/latest/iqms/t1w.html)
#
#      - include the following four types of IQMs
#        - [measures based on noise measurements](https://mriqc.readthedocs.io/en/latest/iqms/t1w.html#measures-based-on-noise-measurements)
#        - [measures based on information theory](https://mriqc.readthedocs.io/en/latest/iqms/t1w.html#measures-based-on-information-theory)
#        - [measures targeting specific artifacts](https://mriqc.readthedocs.io/en/latest/iqms/t1w.html#measures-targeting-specific-artifacts)
#        - [other measures](https://mriqc.readthedocs.io/en/latest/iqms/t1w.html#other-measures)
#
#      - the workflow for computing [anatomical IQMs](https://mriqc.readthedocs.io/en/latest/workflows.html#the-anatomical-workflow) is depicted below
#
#   <img src="../img/anatomical_workflow_source.png" alt="Drawing" style="width: 700px;"/>

# - [IQMs for functional images](http://mriqc.readthedocs.io/en/latest/iqms/bold.html)
#
#   - include the following three types of IQMs
#
#     - [measures for the structural information](http://mriqc.readthedocs.io/en/latest/iqms/bold.html#measures-for-the-structural-information)
#     - [measures for the temporal information](http://mriqc.readthedocs.io/en/latest/iqms/bold.html#measures-for-the-temporal-information)
#     - [measures for artifacts and other](http://mriqc.readthedocs.io/en/latest/iqms/bold.html#measures-for-artifacts-and-other)
#
#    - the workflow for computing [functional IQMs](https://mriqc.readthedocs.io/en/latest/workflows.html#the-functional-workflow) is depicted below
#
#       <img src="../img/functional_workflow_source.png" alt="Drawing" style="width: 700px;"/>
#

# ##### What's the output of MRIQC ?

# MRIQC will provide you with a lot of different and detailed information, depending on input and level.
# Assuming you run the complete MRIQC pipeline for structural & functional images, on the participant & group level, your output will look like depicted below.
#
# In general the output of MRIQC is organized in [reports](https://mriqc.readthedocs.io/en/latest/reports.html#module-mriqc.reports).
#
# On the participant level:
#
# - report structural images (per participant)
# - report functional images (per participant)
#
# On the group level:
# - output group level
#
# The participant level reports are organized comparably across modalities such that they are displayed on a generated html page and tripartite: summary, visual/verbose reports, metadata. The summary contains important information: date & time of execution, MRIQC version, participant identifier and the extracted [IQMs](https://mriqc.readthedocs.io/en/latest/measures.html). The visual/verbose reports display mosaic views of supporting information. Finally, the metadata section contains any metadata that was found in the BIDS dataset. Looks have a look on the participant level reports first.
#
# For [structural images](https://mriqc.readthedocs.io/en/latest/reports/smri.html#) this looks as follows:

# - [summary structural image](https://mriqc.readthedocs.io/en/latest/reports/smri.html#summary)
#
# <img src="../img/MRIQC_example_summary_anatomical.png" alt="Drawing" style="width: 300px;"/>
#

# - [visual/verbose reports](https://mriqc.readthedocs.io/en/latest/reports/smri.html#visual-reports)
#
# <img src="../img/MRIQC_example_anatomical.png" alt="Drawing" style="width: 700px;"/>
#

# Comparably for [functional images](https://mriqc.readthedocs.io/en/latest/reports/bold.html):

# - [summary functional images](https://mriqc.readthedocs.io/en/latest/reports/bold.html#summary)
#
# <img src="../img/MRIQC_example_summary_functional.png" alt="Drawing" style="width: 400px;"/>

# - [visual/verbose reports](https://mriqc.readthedocs.io/en/latest/reports/bold.html#visual-reports)
#
# <img src="../img/MRIQC_example_functional.png" alt="Drawing" style="width: 700px;"/>

# The corresponding values, all [IQMs](https://mriqc.readthedocs.io/en/latest/measures.html) are also written out in [json files](https://en.wikipedia.org/wiki/JSON) and are collected in [.csv tables](https://en.wikipedia.org/wiki/Comma-separated_values). Before we continue, make sure to also check complete example outputs (html pages) for structural and functional images which can be found [here](http://web.stanford.edu/group/poldracklab/mriqc/reports/sub-51296_T1w.html) and [here](http://web.stanford.edu/group/poldracklab/mriqc/reports/sub-50013_task-rest_bold.html). Pretty comprehensive, eh? Well, that's just the first level. Let's check the group reports which build upon everything we just saw.

# - [group reports](https://mriqc.readthedocs.io/en/latest/reports/group.html)

# After processing all [participants](http://localhost:8888/notebooks/google_drive/ALPACA/tutorials/ALPACA_data_organization_prerequisites.ipynb#How-to-get-and-run-MRIQC) in your dataset and run the [group analyses](http://localhost:8888/notebooks/google_drive/ALPACA/tutorials/ALPACA_data_organization_prerequisites.ipynb#How-to-get-and-run-MRIQC) you can check the corresponding output which will include on strip-plot per [IQM](https://mriqc.readthedocs.io/en/latest/measures.html). As mentioned, they build upon the participant level results (aka the .csv tables). To familiarize yourself with this kinda data and plots check the examples given at the [MRIQC website](https://poldracklab.github.io/mriqc/) based on [ABIDE dataset](http://fcon_1000.projects.nitrc.org/indi/abide/).
#
#   - [structural group report](http://web.stanford.edu/group/poldracklab/mriqc/reports/anat_group.html)

# <img src="../img/MRIQC_example_group_anatomical.png" alt="Drawing" style="width: 700px;"/>

# - [functional group report](http://web.stanford.edu/group/poldracklab/mriqc/reports/func_group.html)

# <img src="../img/MRIQC_example_group_functional.png" alt="Drawing" style="width: 700px;"/>

# A very neat feature of these strip-plots is that they are interactive, such that you can (in the html version) click on certain dots/points/samples to get the corresponding individual report. With that it's easy and straight forward to identify outliers in your dataset and subsequently spend a closer look on them.

# ##### MRIQC - to data quality and beyond

# So, what to do with all this comprehensive quality related information? Besides being amazed and overwhelmed by this incredibly useful open source tool, you should definitely make us of it's output. E.g. check overall quality and stability, control for outliers, etc. . You can do this visually, or, of course, with regard to reproducibility, at least for structural images, using a high end function that's already included in MRIQC. More precisely, MRIQC comes with a [already included, defined and pre-trained classifier](https://mriqc.readthedocs.io/en/latest/classifier.html) to predict if certain samples in a dataset should be accepted or rejected. This is based on a [random forrest classifier](https://mriqc.readthedocs.io/en/latest/cv/base.html#the-random-forests-classifier-in-mriqc) which was trained on a combination of the [ABIDE](http://fcon_1000.projects.nitrc.org/indi/abide/) and
# [UCLA Consortium for Neuropsychiatric Phenomics LA5c Study](https://openfmri.org/dataset/ds000030/) datasets and will perform a binary classification into the already mentioned labels accepted or rejected. Everything the respective funtion needs as an input to run is the output of the group level analyses of MRIQC. Hence, it's as easy as:

mriqc_clf --load-classifier -X outputofmriqcgrouplevel.csv -o classifieroutput.csv

# For further information, e.g. on [building your own classifier](https://mriqc.readthedocs.io/en/latest/cv/base.html#building-your-custom-classifier) or the function in general, check the [respective website](https://mriqc.readthedocs.io/en/latest/classifier.html). For a nice overview, [a poster, from the 2017 OHBM](https://mriqc.readthedocs.io/en/latest/index.html), introducing this approach is depicted below. If you use MRIQC please show credit by using the following [citation](https://mriqc.readthedocs.io/en/latest/about.html#citation):
#
# Esteban O, Birman D, Schaer M, Koyejo OO, Poldrack RA, Gorgolewski KJ; MRIQC: Advancing the Automatic Prediction of Image Quality in MRI from Unseen Sites; PLOS ONE 12(9):e0184661; [doi:10.1371/journal.pone.0184661](https://doi.org/10.1371/journal.pone.0184661).
#
#

# <img src="../img/MRIQC_ohbm_poster.png" alt="Drawing" style="width: 700px;"/>

# After [running MRIQC](http://localhost:8888/notebooks/google_drive/ALPACA/tutorials/ALPACA_data_organization_prerequisites.ipynb#How-to-get-and-run-MRIQC), [checking and evaluating it's output (visually or via the classifier)](http://localhost:8888/notebooks/google_drive/ALPACA/tutorials/ALPACA_data_organization_prerequisites.ipynb#What's-the-output-of-MRIQC-?), in combination with everything that we talked about before ([docker](http://localhost:8888/notebooks/google_drive/ALPACA/tutorials/ALPACA_data_organization_prerequisites.ipynb#sidequest:-docker) & [BIDS](http://localhost:8888/notebooks/google_drive/ALPACA/tutorials/ALPACA_data_organization_prerequisites.ipynb#data-quality-control-&-assurance-using-MRIQC)), you already have a very solid and pretty awesome data structure and processing pipeline, that helped you preparing your data in a state-of-the-art way for subsequent analyses. For example using [BIDS apps](http://bids-apps.neuroimaging.io). But as neuroimaging analyses and workflows are at least as diverse as the field itself, this notebook will just focus on a very easy to apply, comprehensive, open & reproducible one that works well with BIDS datasets and is useful for nearly any study, for example also the ALPACA toolbox. It's an extensive pipeline for structural image processing and called [mindboggle](http://www.mindboggle.info).

# ## structural image processing using [mindboggle](http://www.mindboggle.info)

# **Note**: as this part of the notebook contains processing steps that are computationally very demanding and take (depending on your system) several hours, it is not recommend to run them in this notebook, but on powerful machines and make us of the output here. This especially means [FreeSurfer](https://surfer.nmr.mgh.harvard.edu) and [ANTs](http://stnava.github.io/ANTs/). However, for the sake of completeness the respective commands and functions will still be included here. More over, the parts dealing with installation and setup can be used.
#
# *This section heavily uses information & parts from the [mindboggle website](http://www.mindboggle.info), [mindboggle github page](https://github.com/nipy/mindboggle), [mindboggle tutorial jupyter notebook](https://github.com/nipy/mindboggle/blob/master/docs/mindboggle_tutorial.ipynb) and [mindboggle paper in PLOS computational biology](https://doi.org/10.1371/journal.pcbi.1005350). If you find anything that is not referenced correctly or at all, I'm truly sorry, but please let me know, so that I can give appropriate credit.*
#
# <img src="../img/mindboggle_logo.jpg" alt="Drawing" style="width: 200px;"/>

# Most neuroimaging pipelines / workflows, like the ALPACA toolbox, incoporate structural images at some point. Either as a sole focus or within a multi-modal way, e.g. together with functional images for coregistration. There is, of course, a huge varierity for both, the first and the latter. But why not use a pipeline that includes both and covers the vast majority of possible use cases and subsequent analyses? Can't think of any reason? Me neither! Hence, let me introduce you to [mindboggle](http://www.mindboggle.info). As mentioned before, [mindboggle](http://www.mindboggle.info) is a very easy to apply, comprehensive, open & reproducible software package/pipeline for structural image processing. In it's full extent it includes [FreeSurfer](https://surfer.nmr.mgh.harvard.edu), [ANTs](http://stnava.github.io/ANTs/) and [mindboggle itself](https://github.com/nipy/mindboggle), with the latter building upon the first two. Running the complete [mindboggle](http://www.mindboggle.info) workflow will provide you with e.g. [segmentations](http://mindhive.mit.edu/node/106), [surface reconstruction](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferAnalysisPipelineOverview#TheSurface-basedStream) and [in-depth subtle measures of label, feature and shape information in volume, surface and tabular data](http://mindboggle.readthedocs.io/en/latest/#appendix-output). For the latter you'll additionally also get [vertex-wise summary statistics like median, mean, skew, SD, etc.](http://mindboggle.readthedocs.io/en/latest/#appendix-processing) .

# In detail, the complete mindboggle pipeline consits of the following steps (additional information will be given along the way):
#
# - running [FreeSurfer's recon-all](http://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferAnalysisPipelineOverview)
# - running [ANTs antsCorticalThickness.sh](https://github.com/ntustison/KapowskiChronicles/blob/master/paper2.pdf?raw=true)
# - running [mindboggle](http://mindboggle.readthedocs.io/en/latest/#appendix-processing)

# ##### gimme, gimme, gimme...[mindboggle](http://mindboggle.readthedocs.io/en/latest/#installation)

# The same procedure as in every installation related part of this notebook: there are several ways of getting and installing the respective software package. Even though, the following section contains every possible way, it's (also as usual) recommended to obtain and use mindboggle within a docker container (as the [general version](https://hub.docker.com/r/nipy/mindboggle/) or the [BIDS app](https://github.com/BIDS-Apps/mindboggle).

# - mindboogle on [openeuro.org](https://openneuro.org)
#
#   - if you want to try mindboggle before actually installing it
#   - if you don't have a powerful machine or server system at hand
#   - go to [openneuro.org](https://openneuro.org)
#   - select `mindboggle` from the available pipelines
#   - provide the path to the dataset you want to analyze in BIDS format on your local machine
#   - wait for the magic to happen
#   - check and get your output

# - get mindboggle via [docker](https://hub.docker.com/r/nipy/mindboggle/)
#     - get the mindboggle docker image via

docker pull nipy/mindboggle

#    - check if you can access and run the container via
#      - setting a path within the variable 'HOST' to access inputs/outputs on your local machine, e.g. `HOST=/path/to/inputsoutputs/on/local/machine`
#      - setting a path within the varibale `DOCK` from the container to `HOST`, `DOCK=/home/jovyan/work` (you should set DOCK like that)
#      - mount these two
#      - setting the container's bash shell as an entry point, including `--entrypoint /bin/bash` when starting the container

# +
HOST=/path/to/inputsoutputs/on/local/machine
DOCK=/home/jovyan/work

docker run --rm -ti -v $HOST:$DOCK --entrypoint /bin/bash nipy/mindboggle
# -

# - after that you should see a typically looking bash prompt, including the user name & path set in DOCK:

# <img src="../img/mindboggle_bash_entry_example.png" alt="Drawing" style="width: 600px;"/>

# - get the [mindboggle BIDS app](https://github.com/BIDS-Apps/mindboggle) via

docker pull bids/mindboggle

# - check if you can access and the run the container via
#     - setting a path to your BIDS dataset
#     - setting a path to the data directory within the container
#     - mount these two
#     - setting the container's bash shell as an entry point, including `--entrypoint /bin/bash` when starting the container

docker run -ti -v /path/to/BIDS/dataset/on/local/machine:/home/jovyan/work/data --entrypoint /bin/bash bids/mindboggle

# - after that you should see a typically looking bash prompt, including the user name & path set in the docker command (like in the example above)

# - get [mindboggle](https://github.com/nipy/mindboggle) via git (not recommend):
#
#   - install dependencies: [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall), [ANTs](http://miykael.github.io/nipype-beginner-s-guide/installation.html#ants)
#   - install necessary python dependencies listed in the [mindboggle environment.yml](https://github.com/nipy/mindboggle/blob/master/environment.yml) and [mindboggle docker](https://github.com/nipy/mindboggle/tree/master/install) files on [github](https://github.com/nipy/mindboggle)
#   - catch mindboggle and install it using:

git clone https://github.com/nipy/mindboggle
cd mindboggle
python setup.py install

# By now you might be tired of this, but: in terms of open and reproducible neuroscience it's strongly recommended to use one of the docker variants. Based on that the following section "mindboggle to the rescue" will only focus on the different docker variants.

# ##### mindboggle to the rescue

# Paying close attention to the previous part, explaining how to get mindboggle, you probably recognized that there is not one, but two different ways of running mindboggle within a docker container: the ["classic" mindboggle docker image](https://hub.docker.com/r/nipy/mindboggle/) and the [mindboggle BIDS app](https://hub.docker.com/r/bids/mindboggle/). Subsequently, both will be discussed in more detail.

# _the ["classic" mindboggle docker image](https://hub.docker.com/r/nipy/mindboggle/)_
#
# the ["classic" mindboggle docker image](https://hub.docker.com/r/nipy/mindboggle/) can be run in two different ways: either as a single command which will automatically process the structural images through the whole pipeline, including: [FreeSurfer's recon-all](https://surfer.nmr.mgh.harvard.edu/fswiki/recon-all),[ANTs' antsCorticalThickness](https://github.com/ANTsX/ANTs/wiki/antsCorticalThickness-and-antsLongitudinalCorticalThickness-output) and [mindboggle](https://github.com/nipy/mindboggle/blob/master/mindboggle/mindboggle). However, as this is automated default settings are used and only some can be changed. If you want to create a very specific pipeline including specific flags / options you can also run the pipeline command by command. The intitial setup is identical:
#
# - set necessary environment variables (comparable as you did for [testing the images](http://localhost:8888/notebooks/ALPACA_data_organization_prerequisites.ipynb#gimme,-gimme,-gimme...mindboggle)) which will be mounted and/or passed to the commands:
#

HOST=/path/to/inputsoutputs/on/local/machine # to access inputs/outputs on your local machine
DOCK=/home/jovyan/work                       # path from container to host
OUT=/path/to/output/folder                   # path the output folder (only if you want to use a different output folder, which is $DOCK/mindboggle123_output/)
IMAGE=/path/to/structural/image              # path to structural image you want to process
ID=ID_for_image                              # Id for structural image you want to process (e.g. sub-01)

# - to run the complete mindboggle pipeline within one command:

docker run --rm -ti -v $HOST:$DOCK nipy/mindboggle $IMAGE --id $ID --out $OUT

# With that, you've run the complete mindboggle pipeline within one command. Now, continuing with separate commands.

# - to run mindboggle using separate commands:
#
#   - enter the container's bash shell:

docker run --rm -ti -v $HOST:$DOCK --entrypoint /bin/bash nipy/mindboggle

# - from within the container's bash shell start the mindboggle pipeline with running FreeSurfer's recon-all:

# +
FREESURFER_OUT=$DOCK/freesurfer_subjects               # define a FreeSurfer output directory

recon-all -all -i $IMAGE -s $ID -sd $FREESURFER_OUT    # run FreeSurfer's complete recon-all on the image defined above, using the set ID and output directory
# -

# - continue with running ANTs' antsCorticalThickness on the same IMAGE and ID as above, additionally specifying an output directory and templates to use within the process:

# +
ANTS_OUT=$DOCK/ants_subjects                                     # define an ANTs output directory
TEMPLATE=/opt/data/OASIS-30_Atropos_template                     # define the path to the template to be used

antsCorticalThickness.sh -d 3 -a $IMAGE -o $ANTS_OUT/$ID/ants \  # run ANTs' antsCorticalThickness on the $Image and $ID as above
  -e $TEMPLATE/T_template0.nii.gz \                              # specify necessary templates for e.g. cerebellum, etc.
  -t $TEMPLATE/T_template0_BrainCerebellum.nii.gz \
  -m $TEMPLATE/T_template0_BrainCerebellumProbabilityMask.nii.gz \
  -f $TEMPLATE/T_template0_BrainCerebellumExtractionMask.nii.gz \
  -p $TEMPLATE/Priors2/priors%d.nii.gz
# -

# - subsequently, you can run the actual mindboggle command using the previously processed data:

# +
FREESURFER_SUBJECT=$FREESURFER_OUT/$ID # set FreeSurfer path and ID
ANTS_SUBJECT=$ANTS_OUT/$ID             # set ANTs path and ID

mindboggle $FREESURFER_SUBJECT --out $OUT \               # run mindboggle on data processed by FreeSurfer, saving results in $OUT
    --ants $ANTS_SUBJECT/antsBrainSegmentation.nii.gz \   # also include ANTs results
    --roygbiv                                             # output to visualize surface data with roygbiv
# -

# With that, you've run the complete mindboggle pipeline using separate commands from within the container's bash shell.
#
# After talking about the two different ways of running the mindboggle pipeline within the classical container, we'll focus on the other containerized version of mindboggle which is the mindboggle BIDS app.

# the [mindboggle BIDS app](https://hub.docker.com/r/bids/mindboggle/)
#
# the [mindboggle BIDS app](https://hub.docker.com/r/bids/mindboggle/) works as you would expect it, aka like any other [BIDS app](https://github.com/BIDS-Apps/example): you basically just need your data set in BIDS format and you're ready to go. Regarding the mindboggle BIDS app you have the same options of running mindboggle as when using the classic container. However, the exact calls / command lines differ with regard to input arguments and data structure.

# - running the mindboggle BIDS app as one command:

docker run -ti -v /path/to/BIDS/dataset:/home/jovyan/work/data bids/mindboggle /home/jovyan/work/data /home/jovyan/work/data/derivatives/ participant_id

# - you only have to change the `path to the BIDS data set` you want to process and `participant_id` to the BIDS participant id (e.g. sub-01)
# - the output of the mindboggle BIDS app will be stored in `/path/to/BIDS/dataset/derivatives/mindboggle`

# - running the mindboggle BIDS app using separate commands:
#
#     - enter the container's bash shell:

 docker run -ti -v /path/to/BIDS/dataset:/home/jovyan/work/data --entrypoint /bin/bash bids/mindboggle

# - apply the same steps as within the [classic mindboggle docker container](http://localhost:8888/notebooks/ALPACA_data_organization_prerequisites.ipynb#mindboggle-to-the-rescue)

# If you use mindboggle please show credit by using the following [citation](http://www.mindboggle.info/#citing-mindboggle):
#
# Klein A, Ghosh SS, Bao FS, Giard J, Hame Y, Stavsky E, Lee N, Rossa B, Reuter M, Neto EC, Keshavan A. (2017) Mindboggling morphometry of human brains.
# PLoS Computational Biology 13(3): e1005350. [https://doi.org/10.1371/journal.pcbi.1005350](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005350)

# ## How do you go on from here, when in your heart, you begin to understand, there is no going back?

# This was quite a ride, eh? Assuming you've followed the whole notebook, you invested a decent amount of time, work and (based on my lack of skills) frustration. Thank you for that. I hope, that, along the way, you had the chance to get to know and familiarize yourself with the awesome tools covered in this notebook. The same accounts for a possible adaption in your own workflows. But, after all this, we do we actually have and why is it important / how does ALPACA make use of it?

# - your data in [BIDS format](http://bids.neuroimaging.io)
#   - easy to understand data structure & machine readability a lot of tools already make us of (e.g. BIDS apps)
#   - zipped files, functional data in 4D instead of 3D, which speeds up computation and saves disk space big time
#   - a lot of meta data which is usually lost and/or ignored
#   - ready to share with colleagues and/or openly (e.g. on [openfmri](https://openfmri.org)) without the need to explain everything or and/or adapt scripts/functions/pipelines (except for the input path)
#
#   --> ALPACA makes use of all the things mentiond above.

# - data quality control via [mriqc](https://mriqc.readthedocs.io/en/latest/index.html)
#   - a huge variety of image quality metrics for structural and functional images
#   - respective metrics in .csv files and easy-to-check html-versions, for both single participants and the whole data set
#   - possibility to apply a pre-trained classifier to label data as either "accept" or "reject" (or define/train a new classifier)
#   - investigate and check data for artifacts that might influence subsequent analyses and therefore results
#
#   --> ALPACA is kinda strict about things, including data quality (as you should be too). Hence, it doesn't like to use data below a certain quality status to &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prevent the mentioned possible problems. So, if possible, only use data that the mriqc classifier label "accept" for further analyses in ALPACA. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Additionally, it wants to have a look on and document quality metrics that result out of a defined mri sequence to allow further enhacements in &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auditory neuroscience (e.g. influence of sparse sampling, headphones, etc.).

# - structural image processing using [mindboggle](http://www.mindboggle.info)
#   - FreeSurfer
#     - segmentation
#     - surface reconstruction
#     - labelling / parcellations
#     - values (e.g. cortical thickness per label / parcellation)
#   - ANTs
#     - segmentation
#     - labelling / parcellation
#     - values (e.g. cortical thickness per label / parcellation)
#   - mindboggle
#     - hybrid FreeSurfer / ANTs segmentation
#     - number-labeled surfaces and volumes
#     - surfaces with features: sulci, fundi
#     - surfaces with shape measures (per vertex)
#     - tables of shape measures (per label/feature/vertex)
#
#   --> ALPACA highly profits from the mindboggle pipeline. For example, the structural pipeline of ALPACA uses the FreeSurfer & ANTs segmentations &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and labels / parcellations for the generation of ROIs in volume and surface format in native & reference space. Additionally, those outputs are used &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to transform ROIs from divers atlases into participant's native space. Furthermore, they are also very important in ALPACA's functional pipeline, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. during coregistration, normalization and volume/surface based 1st level statistics. The diverse and in depth measures also provide amazing &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;details with regard to structure-function relationships (e.g. correlations of structural properties with functional profiles) and also enhance the fine &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grained analyses of the auditory cortex in general, as well as the possible influence of certain factors like age, musical training, etc. .

# - all of the above
#
#   - easy to implement and run
#   - automated
#   - standardized
#   - open source
#   - transparent
#   - reproducible

# At this point there's nothing left to say accept: thank you for your interest and effort. I truly hope that you'll benefit from this notebook one way or the other.
#
# If you have any questions, please don't hesitate to contact me.
#
# _Have a good one & mahalo!_
