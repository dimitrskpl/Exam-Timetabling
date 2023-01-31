# exam-timetabling

Exam timetabling is a difficult Constraint-Satisfaction problem regarding the planning of the examination of specific subjects on specific days and hours during an examination period. The aim of this project is the modeling and solving of a relatively simple version of this problem using Constraint-Satisfaction algorithms. The problem to be solved is defined as follows:

We have to prepare the schedule of the next exam for the subjects of our department. Subjects are given in the 'Subjects Details.csv' file. The constraints of the problem are:

* The examination period lasts 21 consecutive days (exams on the weekend too).
* Each subjects is examined for 3 hours.
* On each day of the examination period there are 3 time periods during
which a subject can be examined (9-12, 12-3 and 3-6).
* There is only one room available for the exam, where all the students can fit
for each of the courses (therefore, there cannot be two or more subjects examined on the same day and time).
* Subjects of the same year should be examined on different days.
* There are some subjects that have a laboratory (see archive). For these subjects, the lab exam should follow after the exam of the theory (e.g. 12-3 Artificial Intelligence Theory, 3-6 Artificial Intelligence Laboratory). The examination of a laboratory is done by the subject's teacher.
* Some of the subjects are considered difficult (see archive). The exams of difficult subjects must be at least 2 days apart from each other for the convenience of students.
* Subjects of the same teacher must be examined on different days.

For this project I use the algorithms FC, MAC, MinConflicts, while I use the heuristic MRV rule for the dynamic arrangement of the variables and the heuristic dom/wdeg rule described in the article F. Boussemart, F. Hemery, C. Lecoutre and L. Sais. Boosting Systematic Search by Weighting Constraints. Proc. of ECAI 2004, pages 146–150, available on the website http://www.frontiersinai.com/ecai/ecai2004/ecai04/pdf/p0146.pdf for the arrangement of the values.

My implementation is based on the Python code, available on the website  https://github.com/aimacode/aima-python/blob/master/csp.py .

## Algorithms Comparison

| Aglorithms Combination | Assignments | Execution Time | Constraints Checks |
| --- | --- | --- | --- |
| Dom/wdeg - MAC | 38 | 1.2651739120483398 | 969327 |   
| Dom/wdeg - FC | 38 | 0.06960821151733398 | 162327 | 
| MRV - MAC | 38 | 1.1617200374603271 | 967680 |
| MRV - FC | 38 | 0.06492090225219727 | 161212 | 
| MIN CONFLICTS | 38 | 0.046045541763305664 | 86099 | 

The metrics for the comparison of the combinations of the algorithms are the number of assignments, the execution time and the number of constraints checks. For the current CSP prolblem MRV and Dom/wdeg have similar efficiency, but in general Dom/wdeg is more efficient in cases of domains wiped out, which help the algorithm to better estimate the variables. Comparing FC with MAC it is known that FC is based on the following condition: For each variable in which no value has been assigned there is at least one value of its domain which is consistent with the values that have been asigned in other variables, while MAC uses the concept of the edge. After every assignement all the edges of the graph are checked for their consistency. Additionally, in the current problem the number of edges are n^2, where n is the number of variables (subjects). This fact makes it reasonable for the MAC to have greater number of constraints checks and greater execution time. For the number of assignement we know that MAC<=FC which is true for the current instance. For a different modeling or for smaller exam duration MAC would propably make fewer assignments. MIN-CONFLICT seems to be the most efficient algorithm for this problem. The performance of this algorithm depends on the form of the constraints, which seems to contribute positively. In general it is kwown that MIN CONFLICT is highly efficient for many CSP.
