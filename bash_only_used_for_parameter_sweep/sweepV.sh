#!/bin/bash

# sweepV.sh - Bash script for running parameter sweep and automation (using von Neumann movement)

# Cite: COMP 1005. 2022. “Lecture Slides” Lecture 8, COMP1005 Fundamentals of Programming, Semester 2, 2022.
# Cite: COMP 1005. 2022. “dosage_sweep.sh” Practical 8, COMP1005 Fundamentals of Programming, Semester 2, 2022.
# Cite: COMP 1005. 2022. “Practical 8 Walkthrough Video” Blackboard iLecture, COMP1005 Fundamentals of Programming, Semester 2, 2022.


exp_dir=Swamp_von_Neumann_`date "+%Y-%m-%d_%H-%M-%S"` # directory name's formatting (date)

mkdir $exp_dir # create a directory
cp swamp.py $exp_dir # copy all necessary files for the script to run, into the directory
cp swampLife.py $exp_dir
cp terrain.csv $exp_dir
cp sweepV.sh $exp_dir # copy the drive script(.sh), into the directory
cd $exp_dir # change into the directory

# duck
low_duck=$1 # start value 
hi_duck=$2 # stop value
step_duck=$3 # step value

# newt
low_newt=$4 # start value 
hi_newt=$5 # stop value
step_newt=$6 # step value

# shrimp
low_shrimp=$7 # start value 
hi_shrimp=$8 # stop value
step_shrimp=$9 # step value

# alga
low_alga=${10} # start value 
hi_alga=${11} # stop value
step_alga=${12} # step value

# rock
low_rock=${13} # start value 
hi_rock=${14} # stop value
step_rock=${15} # step value

# timestep
low_time=${16} # start value 
hi_time=${17} # stop value
step_time=${18} # step value

# "for" loop for the parameter sweep (6 loops, one nested inside another, to get all the possible combination)
for d in `seq $low_duck $step_duck $hi_duck`;
do
    for n in `seq $low_newt $step_newt $hi_newt`;
    do
        for s in `seq $low_shrimp $step_shrimp $hi_shrimp`;
        do
	    for a in `seq $low_alga $step_alga $hi_alga`;
	    do
	        for c in `seq $low_rock $step_rock $hi_rock`;
	        do
		    for t in `seq $low_time $step_time $hi_time`;
		    do
			echo "Experiment: " $d $n $s $a $c $t
			outfile="Swamp_von_Neumann_Duck"$d"_Newt"$n"_Shrimp"$s"_Alga"$a"_Rock"$c"_Timesteps"$t".txt" # create & format the output file's name
			python3 swampLife.py V $d $n $s $a $c $t > $outfile # redirect the output into the output file(.txt)
		    done
		done
	    done
	done
    done
done
