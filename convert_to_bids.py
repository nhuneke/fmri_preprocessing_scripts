"""
@author: nathanhuneke

This script converts dicoms to nifti in BIDS format.

Define:
- source_dir: directory containing dicoms
- config_file: path to dcm2bids config file
- bids_output_dir: path to output directory for BIDS files

Run this script from the adhd-rest folder

"""

import os
import glob
import subprocess
import sys

# Define paths
source_dir = 'dicoms'                       # Directory containing dicom folders
config_file = 'bids/code/bids_config-1-30.json'  # Path to dcm2bids config file
bids_output_dir = 'bids'                     # Output directory for BIDS files
participant = sys.argv[1]                    # Participant defined by bash argument

participant_source = os.path.join(source_dir, f"BADHD{participant}fMRI")
    
# Construct dcm2bids command
command = [
    'dcm2bids',
    '-d', participant_source,
    '-p', participant,
    '-c', config_file,
    '-o', bids_output_dir,
    '--forceDcm2niix'
    ]
    
# Run the command
try:
	print(f"Converting {participant} to BIDS format...")
	subprocess.run(command, check=True)
    print(f"{participant} successfully converted.")
except subprocess.CalledProcessError as e:
    print(f"Error converting {participant}: {e}")