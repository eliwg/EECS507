#!/bin/bash
#pwd


echo "single step (s) or triplet (t)?" 
read grouping


# Define the target directory
directory="data/raw"

# Check if the target is not a directory
if [ ! -d "$directory" ]; then
  exit 1
fi

# Run FootStepSplicer.py with all of raw data as arg
for file in "$directory"/*; do
  if [ -f "$file" ]; then
    echo "Getting footsteps from $file" >> Footstep_Identification/footstep_splicing_inf.txt
    case $grouping in
      "s")
        python3  Footstep_Identification/FootStepSplicer.py -i "$file" >> Footstep_Identification/footstep_splicing_inf.txt
        ;;
      "t")
        python3  Footstep_Identification/FootStepSplicer_to_3s.py -i "$file" >> Footstep_Identification/footstep_splicing_inf.txt
        ;;
      "c")
        python3  Footstep_Identification/FootStepSplicer_to_3s_clean.py -i "$file" >> Footstep_Identification/footstep_splicing_inf.txt
        ;;
      *)
        echo "grouping not recognize. options: t or s or c"
        exit 1
        ;;
    esac
  fi
done