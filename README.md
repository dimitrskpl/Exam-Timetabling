# exam-timetabling

Exam timetabling is a difficult Constraint-Satisfaction problem regarding the planning of the examination of specific subjects on specific days and hours during an examination period. This project is about the modeling and the solving of a relatively simple version of this problem using Constraint-Satisfaction algorithms. The problem to be solved is defined as follows:

We have to prepare the schedule of the next exam for the subjects of our department. Subjects are given in the 'Subjects Details' file. The constraints of the problem are:

* The examination period lasts 21 consecutive days (exams on the weekend too).
* Each subjects is examined for 3 hours.
* On each day of the examination period there are 3 time periods during
which a subject can be examined (9-12, 12-3 and 3-6).
* There is only one room available for the exam, where all the students can fit
for each of the courses (therefore, there cannot be two or more subjects examined on the same day and time).
* Subjects of the same year should be examined on different days.
*There are some subjects that have a laboratory (see archive). For these subjects, the lab exam should follow after that of theory (e.g. 12-3 Artificial Intelligence Theory, 3-6 Artificial
Intelligence Laboratory). The examination of a laboratory is done by the subject's teacher.
• Some of the subjects are considered difficult (see archive). The exams of difficult subjects must be at least 2 days apart from each other for the convenience of students.
• Subjects of the same teacher must be examined on different days.

For this project I use the algorithms FC, MAC, MinConflicts, while I use the heuristic MRV rule for the dynamic arrangement of the variables and the heuristic dom/wdeg rule described in the article F. Boussemart, F. Hemery, C. Lecoutre and L. Sais. Boosting Systematic Search by Weighting Constraints. Proc. of ECAI 2004, pages 146–150, available on the website http://www.frontiersinai.com/ecai/ecai2004/ecai04/pdf/p0146.pdf for the arrangement of the values.

My impementation is based on the Python code available on the website  https://github.com/aimacode/aima-python/blob/master/csp.py .
