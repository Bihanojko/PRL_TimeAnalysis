# PRL_TimeAnalysis
Test script for PRL project 1 time complexity analysis

Usage:
1. Add "time" to test.sh
Change: mpirun --prefix OpenMPI -np 'proc_numbers' mss 'args'
To: time mpirun --prefix OpenMPI -np 'proc_numbers' mss 'args'

2. Comment all prints in your program (printing is slow and shadows real time)

3. Compile you program

4. Comment out creating and removing numbers file in test.sh

5. Comment out compiling in test.sh

6. Comment out removing binary in test.sh

7. Put TimeAnalysis.py into the same folder as test.sh

8. In TimeAnalysis.py, change line 8 for different count of experiments per testing set and change line 9 for different type of time measurement

9. Run using: python3 TimeAnalysis.py

Output format:
{length_of_sequence} {elapsed_time}\n
