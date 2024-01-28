#!/bin/bash

#run python script to convert mp4 to wav
python3 video2wav.py

# Directory containing the audio files
audio_dir="audio"

# Get the absolute path of the audio directory
audio_dir_abs=$(realpath "$audio_dir")

# Iterate over all .wav files in the directory
for audio_file in "$audio_dir"/*.wav
do
    # Reset the timer
    SECONDS=0

    # Extract the base name of the file (without directory path and extension)
    audio_name=$(basename "$audio_file" .wav)

    # Create a new directory for this audio file
    output_dir="transcripts/$audio_name"
    mkdir -p "$output_dir"

    # Get the absolute path of the output directory
    output_dir_abs=$(realpath "$output_dir")

    echo "Running whisper on $audio_file"

    # Run the whisper command on the audio file and output to the new directory
    # Edit this to your config
    whisper "$audio_file" --fp16 False --language English --model tiny > "$output_dir_abs/$audio_name.txt"

    echo "Done - took $SECONDS seconds"
done