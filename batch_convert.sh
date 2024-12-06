#!/bin/bash

set -e
set -u

subs=("32" "34" "35" "36" "37" "38" "39")

for id in "${subs[@]}" ; do
	code/convert_to_bids.py $id
done

echo "Conversion to nifti completed successfully"
