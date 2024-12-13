#!/bin/bash

# From adhd-rest/ command is "bash bids/code/fmri_preprocessing_scripts/preprocess.sh".

set -e -u

subs=("32" "34" "35" "36" "37" "38" "39")

for label in "${subs[@]}" ; do

	echo "Preprocessing ${label}"

	# Run MRIQC
	##### Change paths #####
	docker run -it --rm -v /local/scratch/cs1n24/adhd-rest/bids:/data:ro \
		-v /local/scratch/adhd-rest/derivatives:/out \
		nipreps/mriqc:latest \
		/data /out participant --participant-label $label

	# Do fmriprep preprocessing
	##### Change paths #####
	fmriprep-docker ./bids  ./derivatives \
		participant --participant-label $label \
		--fs-no-reconall \
		--user $( id -u ) \
		--skip-bids-validation \
		--fs-license-file /local/software/freesurfer/license.txt

	echo "Preprocessing for ${label} complete."
done

echo "All subjects pre-processed"