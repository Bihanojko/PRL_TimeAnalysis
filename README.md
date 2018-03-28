# PRL_TimeAnalysis
Test script for PRL project 1 time complexity analysis

Usage:
1. Add "time" to test.sh
Change: mpirun --prefix OpenMPI -np $2 mss 
To: time mpirun --prefix OpenMPI -np $2 mss

2. Put TimeAnalysis.py into the same folder as test.sh

3. Run using: python3 TimeAnalysis.py

4. In TimeAnalysis.py, change line 8 for different count of experiments per testing set and change line 9 for different type of time measurement

Output format:
{length_of_sequence}; {number_of_processors}; {elapsed_time}\n
