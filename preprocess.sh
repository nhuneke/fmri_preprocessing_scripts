#!/bin/bash

# Command is "bash code/preprocess.sh sub-ID".

set -e -u

subj="$1"
prefix="sub-"
label=${subj/#$prefix}

echo "Preprocessing ${subj}"

# Run MRIQC
##### Change paths #####
docker run -it --rm -v /local/scratch/nh6g15/datasets/roar_preproc/raw:/data:ro -v /local/scratch/nh6g15/datasets/roar_bids_qc/derivatives:/out nipreps/mriqc:latest /data /out participant --participant-label $label

# Do fmriprep preprocessing
##### Change paths #####
fmriprep-docker ./raw  ./${sub} \
	participant --participant-label ${label} \
	--fs-no-reconall \
	--user $( id -u ) \
	--skip-bids-validation \
	--fs-license-file /local/software/freesurfer/license.txt

echo "Preprocessing for ${subj} complete."
