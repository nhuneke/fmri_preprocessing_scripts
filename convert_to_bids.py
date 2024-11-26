"""
@author: nathanhuneke

This script converts xnat-retrieved dicoms to nifti in BIDS format.

Define:
- source_dir: directory containing original dicoms
- config_file: path to dcm2bids config file
- bids_output_dir: path to output directory for BIDS files

"""

import os
import glob
import subprocess

# Define paths
source_dir = 'source'                       # Directory containing participant folders
config_file = 'code/PEBBAL2_BIDS_config.json'  # Path to dcm2bids config file
bids_output_dir = 'bids'                     # Output directory for BIDS files

# Get sorted list of participant IDs from directories in the source directory
participants = sorted([d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))])

# Loop through each participant
for participant in participants:
    # Define the path pattern for scans directory (expanding to actual paths)
    participant_source_pattern = os.path.join(source_dir, participant, '*', '*', 'scans')
    scan_dirs = glob.glob(participant_source_pattern)  # Expand the pattern to match directories

    # Ensure there is at least one matching scans directory
    if not scan_dirs:
        print(f"No scans directory found for {participant}. Skipping.")
        continue

    # Use the first matching scans directory
    participant_source = scan_dirs[0]
    
    # Define the output path in the BIDS directory, matching the 'sub-<id>' format
    participant_bids = os.path.join(bids_output_dir, f"sub-{participant}")
    
    # Check if participant directory already exists in the BIDS output directory
    if os.path.isdir(participant_bids):
        print(f"Skipping {participant}: already converted to BIDS.")
        continue  # Skip to the next participant
    
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

print("All participants processed.")