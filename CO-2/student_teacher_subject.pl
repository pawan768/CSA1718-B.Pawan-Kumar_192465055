% Student-Teacher-Subject database
student(101, 'Anu').
student(102, 'Bala').
teacher(t1, 'Dr_Ravi').
teacher(t2, 'Ms_Priya').
subject(s1, 'Artificial_Intelligence').
subject(s2, 'Database_Systems').
handles(t1, s1).
handles(t2, s2).
enrolled(101, s1).
enrolled(102, s2).

student_subject_teacher(StudentName, SubjectName, TeacherName) :-
    student(Id, StudentName),
    enrolled(Id, SubjectId),
    subject(SubjectId, SubjectName),
    handles(TeacherId, SubjectId),
    teacher(TeacherId, TeacherName).

% Query: ?- student_subject_teacher(Student, Subject, Teacher).
