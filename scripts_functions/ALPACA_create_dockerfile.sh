# Generate Dockerfile.
docker run --rm kaczmarj/neurodocker:master generate \
-b neurodebian:stretch-non-free -p apt \
--afni version=latest \
--ants version=2.2.0 \
--c3d version=1.0.0 \
--freesurfer version=6.0.0 min=true \
--fsl version=5.0.10 \
--install git nano swig graphviz gcc g++ tree git-annex-standalone\
--user alpaca \
--miniconda env_name=alpaca \
            conda_install="python=2.7 numpy pandas traits jupyter jupyterlab matplotlib scikit-image scikit-learn seaborn vtk" \
            pip_install="nipype nipy rdflib mne mayavi nilearn datalad ipywidgets pythreejs nibabel pymvpa2 PySurfer pybids pygraphviz" \
            activate=true \
--user alpaca \
--workdir /home/alpaca \
--no-check-urls > Dockerfile

# Build Docker image using the saved Dockerfile.
docker build -t alpaca -f Dockerfile .



