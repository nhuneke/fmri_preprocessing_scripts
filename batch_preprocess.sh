#!/bin/bash

set -e
set -u

subs=("32" "34" "35" "36" "37" "38" "39")

for id in "${subs[@]}" ; do
	subj="sub-$id"
	code/preprocess.sh ${subj}
done

echo "Batch pre-processing completed successfully"
