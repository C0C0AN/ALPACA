# ALPACA_inverse_transform_ROIs.py
# This script performs an inverse transformation (from MNI reference to participant's native space) of auditory cortex
# ROIs extracted from publicly available atlases.
# It assumes that mindboggle and the preprocessing workflow were already run as it heavily makes use of it's outputs.
# All ROIs will be transformed in volume and surface format.
# -*- coding: utf-8 -*-

# Ver. 1 - 10/2017 - Peer Herholz (herholz dot peer at gmail dot com)

##### Import important modules #####

from os.path import join as opj
from nipype.interfaces.ants import ApplyTransforms
from nipype.interfaces.freesurfer import FSCommand, Binarize, Label2Label
from nipype.interfaces.utility import Function, IdentityInterface, Merge
from nipype.interfaces.io import SelectFiles, FreeSurferSource, DataSink
from nipype.pipeline.engine import Workflow, Node, MapNode

##### Specify interface behaviors #####

# FreeSurfer - Specify the location of the freesurfer folder
fs_dir = '../resources/example_data/derivatives/mindboggle/freesurfer_subjects'
FSCommand.set_default_subjects_dir(fs_dir)

##### Specify important variables #####

experiment_dir = '../resources/example_data' # location of experiment folder
input_dir_preproc = '../resources/example_data/derivatives/preprocessing/output_prepro_ALPACA' # name of preprocessing output folder
input_dir_reg = '../resources/example_data/derivatives/preprocessing/output_prepro_ALPACA/output_registration_ALPACA' # name of registration output folder
input_dir_ROI = '../resources/regions_of_interest' # location of ROI folder

input_dir_source = '/usr/local/freesurfer/subjects'
source_id = ['fsaverage'] # name of the surface subject/space the to be transformed ROIs are in

subject_list = ['sub-01'] # create the subject_list variable

output_dir = 'output_inverse_transform_ROIs_ALPACA'  # name of norm output folder
working_dir = 'workingdir_inverse_transform_ROIs_ALPACA'  # name of norm working directory


##### Create & specify nodes to be used and connected during the normalization pipeline #####

# Concatenate BBRegister's and ANTS' transforms into a list
merge = Node(Merge(2), iterfield=['in2'], name='mergexfm')

# Binarize node - binarizes mask again after transformation
binarize_post2ant = MapNode(Binarize(min=0.1),iterfield=['in_file'],
                    name='binarize_post2ant')

binarize_pt2pp = binarize_post2ant.clone('binarize_pt2pp')

# FreeSurferSource - Data grabber specific for FreeSurfer data
fssource_lh = Node(FreeSurferSource(subjects_dir=fs_dir, hemi='lh'),
                run_without_submitting=True,
                name='fssource_lh')

fssource_rh = Node(FreeSurferSource(subjects_dir=fs_dir, hemi='rh'),
                run_without_submitting=True,
                name='fssource_rh')

# Transform the volumetric ROIs to the target space
inverse_transform_mni_volume_post2ant = MapNode(ApplyTransforms(args='--float',
                                  input_image_type=3,
                                  interpolation='Linear',
                                  invert_transform_flags=[False, False],
                                  num_threads=1,
                                  terminal_output='file'),
                  name='inverse_transform_mni_volume_post2ants', iterfield=['input_image'])

inverse_transform_mni_volume_pt2pp = inverse_transform_mni_volume_post2ant.clone('inverse_transform_mni_volume_pt2pp')

# setlabel2label output file name - there might be a bug in nipype's label2label interface, should be checked from time to time and if resolved adapted the workflow accordingly 
def set_output_name(label):
    output_name = label + '_converted.label'
    
    return output_name
    
# set output name - set label specific output name
set_output_name_lh_post2ant = MapNode(Function(input_names=['label'],
                               output_names=['output_name'],
                               function=set_output_name),
                               iterfield=['label'],
                      name='set_output_name_lh_post2ant')

set_output_name_rh_post2ant= set_output_name_lh_post2ant.clone(name='set_output_name_rh_post2ant')

set_output_name_lh_pt2pp = set_output_name_lh_post2ant.clone(name='set_output_name_lh_pt2pp')

set_output_name_rh_pt2pp = set_output_name_lh_post2ant.clone(name='set_output_name_rh_pt2pp')

# Transform the surface ROIs to the target space
inverse_transform_mni_surface_lh_post2ant = MapNode(Label2Label(hemisphere = 'lh',
                                                                subjects_dir=fs_dir,
                                                                copy_inputs=True), 
                                                                iterfield=['source_label', 'out_file'], 
                                                                name = 'inverse_transform_mni_surface_lh_post2ant')

inverse_transform_mni_surface_rh_post2ant = MapNode(Label2Label(hemisphere = 'rh',
                                                                subjects_dir=fs_dir
                                                                ), 
                                                                iterfield = ['source_label', 'out_file'], 
                                                                name = 'inverse_transform_mni_surface_rh_post2ant')

inverse_transform_mni_surface_lh_pt2pp = MapNode(Label2Label(hemisphere = 'lh',
                                                               subjects_dir=fs_dir
                                                               ), 
                                                                iterfield = ['source_label', 'out_file'], 
                                                                name = 'inverse_transform_mni_surface_lh_pt2pp')

inverse_transform_mni_surface_rh_pt2pp = MapNode(Label2Label(hemisphere = 'rh',
                                                                subjects_dir=fs_dir
                                                                ), 
                                                                iterfield = ['source_label', 'out_file'], 
                                                                name = 'inverse_transform_mni_surface_rh_pt2pp')

# Initiation of the inverse transform ROIs workflow
inverse_ROI_flow = Workflow(name='inverse_ROI_flow')
inverse_ROI_flow.base_dir = opj(experiment_dir, working_dir)


##### Specify input and output stream #####

##### establish input and output streams by connecting Infosource, SelectFiles and DataSink to the main workflow #####

# Infosource - a function free node to iterate over the list of subject names
infosource = Node(IdentityInterface(fields=['subject_id',
                                            'source_subject']),
                  name="infosource")
infosource.iterables = [('subject_id', subject_list),
                        ('source_subject', source_id)]

# SelectFiles - to grab the data (alternativ to DataGrabber)
reg_file = opj(input_dir_reg, 'bbregister', '{subject_id}', 'mean*.mat')
inverse_transform_composite = opj(input_dir_reg, 'antsreg', '{subject_id}', 'transformInverseComposite.h5')
convert2itk = opj(input_dir_reg, 'convert2itk', '{subject_id}', 'affine.txt')
target = opj(input_dir_preproc, 'realign', '{subject_id}', 'mean*merged.nii')
mni_volume_post2ant = opj(input_dir_ROI, 'mni152_posterior2anterior/*.nii.gz')
mni_volume_pt2pp = opj(input_dir_ROI, 'mni152_te11-te10-te12-pt-pp/*.nii.gz')
mni_surface_lh_post2ant = opj(input_dir_ROI, 'surf_posterior2anterior/lh*.label')
mni_surface_rh_post2ant = opj(input_dir_ROI, 'surf_posterior2anterior/rh*.label')
mni_surface_lh_pt2pp = opj(input_dir_ROI, 'surf_te11-te10-te12-pt-pp/lh*.label')
mni_surface_rh_pt2pp = opj(input_dir_ROI, 'surf_te11-te10-te12-pt-pp/rh*.label')
source_subject_white_lh = opj(input_dir_source, '{source_subject}', 'surf/lh.white')
source_subject_sphere_lh = opj(input_dir_source, '{source_subject}', 'surf/lh.sphere.reg')
source_subject_white_rh = opj(input_dir_source, '{source_subject}', 'surf/rh.white')
source_subject_sphere_rh = opj(input_dir_source, '{source_subject}', 'surf/rh.sphere.reg')


templates = {'reg_file' : reg_file,
             'inverse_transform_composite' : inverse_transform_composite,
             'convert2itk' : convert2itk,
             'target': target,
             'mni_volume_post2ant': mni_volume_post2ant,
             'mni_volume_pt2pp' : mni_volume_pt2pp,
             'mni_surface_lh_post2ant' : mni_surface_lh_post2ant,
             'mni_surface_rh_post2ant' : mni_surface_rh_post2ant,
             'mni_surface_lh_pt2pp' : mni_surface_lh_pt2pp,
             'mni_surface_rh_pt2pp' : mni_surface_rh_pt2pp,
             'source_subject_sphere_lh' : source_subject_sphere_lh,
             'source_subject_white_lh' : source_subject_white_lh,
             'source_subject_sphere_rh' : source_subject_sphere_rh,
             'source_subject_white_rh' : source_subject_white_rh,
            }

selectfiles = Node(SelectFiles(templates,
                               base_directory=experiment_dir),
                   name="selectfiles")

# Datasink - creates output folder for important outputs
datasink = Node(DataSink(base_directory=experiment_dir,
                         container=output_dir),
                name="datasink")

# Use the following DataSink output substitutions
substitutions = [('_subject_id_', ''),
                 ('_apply2con', 'apply2con'),
                 ('_warpall', 'warpall'),
                 ('_mask_', ''),
                 ('_source_subject_', '')]
datasink.inputs.substitutions = substitutions

# Connect SelectFiles and DataSink to the workflow
inverse_ROI_flow.connect([(infosource, selectfiles, [('subject_id', 'subject_id'),
                                                          ('source_subject', 'source_subject')]),
                  (selectfiles, merge, [('convert2itk', 'in2')]),
                  (selectfiles, merge, [('inverse_transform_composite', 'in1')]),                  
                  (infosource, fssource_lh, [('subject_id', 'subject_id')]),
                  (infosource, fssource_rh, [('subject_id', 'subject_id')]),                       
                  (selectfiles, inverse_transform_mni_volume_post2ant, [('mni_volume_post2ant', 'input_image')]),
                  (selectfiles, inverse_transform_mni_volume_post2ant, [('target', 'reference_image')]),
                  (selectfiles, inverse_transform_mni_volume_pt2pp, [('mni_volume_pt2pp', 'input_image')]),
                  (selectfiles, inverse_transform_mni_volume_pt2pp, [('target', 'reference_image')]),
                  (merge, inverse_transform_mni_volume_post2ant, [('out', 'transforms')]),
                  (merge, inverse_transform_mni_volume_pt2pp, [('out', 'transforms')]),
                  (inverse_transform_mni_volume_post2ant, binarize_post2ant, [('output_image', 'in_file')]),
                  (inverse_transform_mni_volume_pt2pp, binarize_pt2pp, [('output_image', 'in_file')]),                 
                  (selectfiles, set_output_name_lh_post2ant, [('mni_surface_lh_post2ant', 'label')]),
                  (set_output_name_lh_post2ant, inverse_transform_mni_surface_lh_post2ant, [('output_name', 'out_file')]),
                  (infosource, inverse_transform_mni_surface_lh_post2ant, [('subject_id', 'subject_id')]),
                  (fssource_lh, inverse_transform_mni_surface_lh_post2ant, [('sphere_reg', 'sphere_reg')]),
                  (fssource_lh, inverse_transform_mni_surface_lh_post2ant, [('white', 'white')]),
                  (infosource, inverse_transform_mni_surface_lh_post2ant, [('source_subject', 'source_subject')]),
                  (selectfiles, inverse_transform_mni_surface_lh_post2ant, [('source_subject_white_lh', 'source_white')]),
                  (selectfiles, inverse_transform_mni_surface_lh_post2ant, [('source_subject_sphere_lh', 'source_sphere_reg')]),                 
                  (selectfiles, inverse_transform_mni_surface_lh_post2ant, [('mni_surface_lh_post2ant', 'source_label')]),               
                  (selectfiles, set_output_name_rh_post2ant, [('mni_surface_rh_post2ant', 'label')]),
                  (set_output_name_rh_post2ant, inverse_transform_mni_surface_rh_post2ant, [('output_name', 'out_file')]),
                  (infosource, inverse_transform_mni_surface_rh_post2ant, [('subject_id', 'subject_id')]),
                  (fssource_rh, inverse_transform_mni_surface_rh_post2ant, [('sphere_reg', 'sphere_reg')]),
                  (fssource_rh, inverse_transform_mni_surface_rh_post2ant, [('white', 'white')]),
                  (infosource, inverse_transform_mni_surface_rh_post2ant, [('source_subject', 'source_subject')]),
                  (selectfiles, inverse_transform_mni_surface_rh_post2ant, [('source_subject_white_rh', 'source_white')]),
                  (selectfiles, inverse_transform_mni_surface_rh_post2ant, [('source_subject_sphere_rh', 'source_sphere_reg')]),                 
                  (selectfiles, inverse_transform_mni_surface_rh_post2ant, [('mni_surface_rh_post2ant', 'source_label')]),               
                  (selectfiles, set_output_name_lh_pt2pp, [('mni_surface_lh_pt2pp', 'label')]),
                  (set_output_name_lh_pt2pp, inverse_transform_mni_surface_lh_pt2pp, [('output_name', 'out_file')]),
                  (infosource, inverse_transform_mni_surface_lh_pt2pp, [('subject_id', 'subject_id')]),
                  (fssource_lh, inverse_transform_mni_surface_lh_pt2pp, [('sphere_reg', 'sphere_reg')]),
                  (fssource_lh, inverse_transform_mni_surface_lh_pt2pp, [('white', 'white')]),
                  (infosource, inverse_transform_mni_surface_lh_pt2pp, [('source_subject', 'source_subject')]),
                  (selectfiles, inverse_transform_mni_surface_lh_pt2pp, [('source_subject_white_lh', 'source_white')]),
                  (selectfiles, inverse_transform_mni_surface_lh_pt2pp, [('source_subject_sphere_lh', 'source_sphere_reg')]),                 
                  (selectfiles, inverse_transform_mni_surface_lh_pt2pp, [('mni_surface_lh_pt2pp', 'source_label')]),
                  (binarize_post2ant, datasink, [('binary_file', 'inverse_transform_mni_volume_post2ant.@warpall')]),
                  (binarize_pt2pp, datasink, [('binary_file', 'inverse_transform_mni_volume_pp2pt.@warpall')]),
                  (inverse_transform_mni_surface_lh_post2ant, datasink, [('out_file', 'inverse_transform_mni_surface_lh_post2ant.@surfacetransform')]),
                  (inverse_transform_mni_surface_rh_post2ant, datasink, [('out_file', 'inverse_transform_mni_surface_rh_post2ant.@surfacetransform')]),
                  (inverse_transform_mni_surface_rh_pt2pp, datasink, [('out_file', 'inverse_transform_mni_surface_lh_pt2pp.@surfacetransform')])
                 ])

#### visualize the pipeline ####

# Create a colored output graph
inverse_ROI_flow.write_graph(graph2use='colored',format='png', simple_form=True)

# Create a detailed output graph
inverse_ROI_flow.write_graph(graph2use='flat',format='png', simple_form=True)

#### run the workflow using multiple cores ####
inverse_ROI_flow.run('MultiProc', plugin_args={'n_procs':4})

