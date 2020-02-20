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
# ## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;create the ALPACA docker container

# ### This notebook will show you how to create the ALPACA docker container used to apply the toolbox, including short explanations of the respective packages and software. Furthermore, it'll also give a brief introduction into docker itself, as well as the process of generating, building and managing docker containers.
# Please note that this notebook won't work on on [binder](https://mybinder.org/) as it includes commands to create and build a Docker image and the same holds true when you run it within the ALPACA Docker or Singularity image. It thus only runs locally. Furterhmore, to not be dependent on adding the bash kernel, every cell starts with `%%bash` to allow the execution of
# bash commands in a jupyter notebook running a python kernel.

# ### docker - reproducibility in a container

# *This section is taken from the [ALPACA - data organization and prerequisites notebook](ALPACA_data_organization_prerequisites.ipynb).*

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
# To stop a running docker container, either close the docker running  terminal or select the terminal and press the `Ctrl-C` shortcut twice.

# ###### List all installed docker images
# To see a list of all installed docker images use:
#

# `docker images`

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
#
# After learning a little bit about docker, let's actually create and build a container.

# ### creating & building docker containers - there and back again

# You might think: do I really need to know this and why is it important anyway? Well, besides a bunch of points, here are two very obvious and major points: reproducibility and sharing/standardization. Focusing the first, the [introduction section](#docker---reproducibility-in-a-container) already briefly mentioned that through the possibility of wrapping up entire systems/setups, docker is a great tool with regard to reproducibility. More precisely, you can provide the exact same setup you used for a certain analysis or even study together with the respective so that others (fellow researchers, reviewers, your friends and family, etc.) can reproduce your results or apply your work to new data with ease. Along many positive effects this also boosts your integrity, big time. Focusing the latter, docker also helps you collaborating with peeps and to establish standards, increasing your impact tremendously. If you've developed a great and robust pipeline, why not share it with others so that they can benefit from it as well? Maybe you'll also be able to support the further standardization of neuroinformatics related applications (in terms of state of the art and best practise, of course), like e.g. [BIDS apps](http://bids-apps.neuroimaging.io) do. After all we're all in this together and for (neuro-)science, not for our egos.

# ##### Dockerception

# There are actually a lot of amazing resources on how to create, build and ship docker containers. From the [documentation on the docker website](https://docs.docker.com/engine/reference/commandline/create/) and [guides](https://deis.com/blog/2015/creating-sharing-first-docker-image/) to even [youtube videos](https://www.youtube.com/watch?v=K6WER0oI-qs). This already seems quite comprehensive and helpful, eh? But wait for it: the neuroscience community is actually lucky enough that there's a docker image that creates docker images for neuroscience related applications, so basically, dockerception! It's called [neurodocker](https://www.youtube.com/watch?v=K6WER0oI-qs) and is nothing but off the charts. As it makes the creation of docker images for reproducible neuroscience reproducible and because it's super straightforward, ALPACA also uses [neurodocker](ttps://www.youtube.com/watch?v=K6WER0oI-qs).
#
# As usally, at first you need to pull the image:

sudo docker pull kaczmarj/neurodocker

# neurodocker supports a vast variety of neuroinformatics related applications and software. For a comprehensive overview make sure to check the [respective sections on it's github page](https://github.com/kaczmarj/neurodocker#supported-software). The basic functionality is as with any other docker image: you need to run it with certain options / specifications.
#
# The run command itself should already look familiar to you:
# `sudo docker run --rm kaczmarj/neurodocker`
#
# What follows aren't mounts of data paths or functions, but all the applications, packages and software you want to include in your docker image. Furthermore, also settings with regard to the container's architecture, where the docker file should be saved, etc. For the ALPACA toolbox this looks like this:

docker run --rm kaczmarj/neurodocker:master generate -b neurodebian:stretch-non-free -p apt \
--install git nano num-utils gcc g++ curl build-essential graphviz gcc g++ tree git-annex-standalone\
--user=alpaca \
--miniconda env_name=alpaca \
            conda_install="python=3.7 notebook ipython numpy pandas traits jupyter jupyterlab matplotlib scikit-image scikit-learn seaborn vtk" \
            pip_install="ipywidgets ipyevents jupytext nilearn nistats nibabel jupytext nipype nipy rdflib mne mayavi nilearn datalad ipywidgets pythreejs nibabel pymvpa2 PySurfer pybids pygraphviz datalad" \
            activate=true \
--run 'mkdir -p ~/.jupyter && echo c.NotebookApp.ip = \"0.0.0.0\" > ~/.jupyter/jupyter_notebook_config.py' \
--entrypoint="/neurodocker/startup.sh"
--cmd jupyter notebook


# This might look confusing and overwhelming at first glance, but don't worry, we're gonna dissect the parts:

# As mentioned, the run command itself should already look familiar to you:
#
# `sudo docker run --rm kaczmarj/neurodocker`
#
# This just tells docker that we want to run the image `kaczmarj/neurodocker` with root privileges and that it should automatically be removed after closing docker (check the corresponding [section](#How-to-run-docker-images) in this notebook).
#
# Subsequently, we tell neurodocker which applications, packages and software we want to include in our container, starting with a minimal neurodebian system and the package manager `apt`:
#
# `-b neurodebian:stretch-non-free -p apt \`
#

# Continuing with neuroimaging related software packages:
#
# `--afni version=latest \`
#
# `--ants version=2.2.0 \`
#
# `--c3d version=1.0.0 \`
#
# `--freesurfer version=6.0.0 min=true \`
#
# `--fsl version=5.0.10 \`
#
# *What are these and how does ALPACA make use of it?*:
#
# - [afni](https://afni.nimh.nih.gov) &rarr; preprocessing (e.g. despiking) and surface based analyses
# - [ants](http://stnava.github.io/ANTs/) &rarr; registrations & transformations
# - [c3d](https://sourceforge.net/projects/c3d/)  &rarr; converting of file formats
# - [freesurfer](https://surfer.nmr.mgh.harvard.edu) &rarr; registrations & conversions
# - [fsl](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSL)  &rarr; preprocessing (e.g. motion correction) and statistics

# After that, some useful applications:
#
# `--install git nano swig graphviz\`
#
# *What are these and how does ALPACA make use of it?*:
#
# - [git](https://git-scm.com) &rarr; version control for all types of data
# - [nano](https://en.wikipedia.org/wiki/GNU_nanohttps://en.wikipedia.org/wiki/SWIG) &rarr; basic text editor to checkt scripts, etc.
# - [graphviz](https://www.graphviz.org) &rarr; graph visualization (needed for nipype)
# - [gcc](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) &rarr; C compiler for GNU
# - [g++](https://www.cprogramming.com/g++.html) &rarr; C++ compiler for GNU
# - [tree](http://manpages.ubuntu.com/manpages/trusty/man1/tree.1.html) &rarr; recursive directory listing program
# - [git-annex-standalone](https://git-annex.branchable.com) &rarr; file managing with git

# Now to the real fun, a python distribution including a variety of packages:
#
# `--user alpaca \`
#
# `--miniconda env_name=alpaca \`
#
#   `conda_install="python=2.7 numpy pandas traits jupyter jupyterlab matplotlib scikit-image scikit-learn seaborn
# vtk" \`
#
#   `pip_install="nipype rdflib nipy mne mayavi nilearn datalad nibabel pymvpa2 PySurfer pybids pygraphviz" \`
#
#    `activate=true \`
#
# *What are these and how does ALPACA make use of it?*:
#
# - create an environment named "alpaca" using [miniconda](https://conda.io/docs/glossary.html#miniconda-glossary)
# - use [conda](https://conda.io/docs/glossary.html#conda-glossary) to install python packages
# - [python 2.7](https://www.python.org/download/releases/2.7/) &rarr; python 2 version as basis for toolbox (needed by certain packages like e.g. pymvpa2)
# - [numpy](http://www.numpy.org) &rarr; scientific computing, reading, manipulation & writing of images (through nibabel & nilearn)
# - [pandas](https://pandas.pydata.org) &rarr; data munging, preparation and analyses
# - [traits](https://pypi.python.org/pypi/traits) &rarr; adding characteristics to python object attributes (important for nipype)
# - [jupyter](http://jupyter.org) &rarr; spin-off of [ipython](https://en.wikipedia.org/wiki/IPython) enabling the application of [notebooks](https://en.wikipedia.org/wiki/IPython#Notebook) like this one (or the other interactive tutorials of the ALPACA toolbox)
# - [jupyterlab](https://github.com/jupyterlab/jupyterlab) &rarr; further extends the functionality of jupyter notebooks
# - [matplotlib](https://matplotlib.org) &rarr; 2 D plotting library used for the generation and adjustment of graphics
# - [scikit-image](http://scikit-image.org) &rarr; image processing
# - [scikit-learn](http://scikit-learn.org/stable/index.html) &rarr; workhorse for anything related to machine learning  analyses (e.g. through nilearn & pymvpa2)
# - [seaborn](https://seaborn.pydata.org/index.html) &rarr; generation of statistical graphics
# - [vtk](https://pypi.python.org/pypi/vtk) &rarr; 3 D graphics, image processing & visualization
# - [nipype](http://nipype.readthedocs.io/en/latest/) &rarr; interface to neuroimaging software, fascilitates interaction between them, used to create processing workflows
# - [rdflib](https://github.com/RDFLib/rdflib) &rarr; representation of information in graphs
# - [nipy](http://nipy.org/nipy/) &rarr; analyses of neuroimaging data
# - [mne](https://martinos.org/mne/stable/index.html) &rarr; exploring, analyzing & visualizing of eeg data
# - [mayavi](http://docs.enthought.com/mayavi/mayavi/) &rarr; 3 D data visualization & plotting (mainly within mne)
# - [nilearn](http://nilearn.github.io/index.html) &rarr; statistical learning on, reading, manipulating & writing of neuroimaging data, plotting
# - [datalad](http://datalad.org) &rarr; manage, download, upload data
# - [nibabel](http://nipy.org/nibabel/) &rarr; read, write access to neuroimaging data (through e.g. nilearn)
# - [pymvpa2](http://www.pymvpa.org) &rarr; statistical learning analyses on neuroimaging data
# - [PySurfer](https://pysurfer.github.io) &rarr; visualization of cortical surface representations of neuroimaging data
# - [pybids](https://github.com/INCF/pybids) &rarr; interactions with data sets in BIDS format
# - [pygraphviz](https://pygraphviz.github.io) &rarr; python interface to graphviz

# Last but not least, indicate the user working directory within the container:
#
# `--user alpaca \`
#
# `--workdir /home/alpaca \`

# We're gonna finish with providing an output path and name for the dockerfile:
#
# `--no-check-urls > Dockerfile`

# With that we created our Dockerfile containing all information necessary. It should be saved in whatever directory you run the code from above. Subsequently, we need to actually build our docker image to be able to run and ship it.

# ##### build me up dockercup

# Building the docker image is comparably easy, straightforward and done in one line:

docker build -t alpaca -f Dockerfile .

# A bit more in depth, we're starting with telling (kindly asking) docker to build a docker image based on the subsequent specifications (arguments and options):
#
# ``docker build``

# This is followed by providing a name (and optionally a tag if you want) for our docker image, naming ours "alpaca"
#
# ``-t alpaca``
#
# **hint**: the docker build command only accepts all non-capital names. If you want to additionally provide a tag, you should use the following scheme: `name:tag`, e.g. `-t alpaca:firstdraft` . This is very important in terms of enabling a good and comprehnsible version control of your docker image.

# After that, you (hopefully) can relax and enjoy the magic happen. Depending on your machine and the specific Dockerfile, creating a docker image can take a while. So, don't worry if it takes more than a couple of minutes. The terminal output will actually give information on what's currently happening and allows
