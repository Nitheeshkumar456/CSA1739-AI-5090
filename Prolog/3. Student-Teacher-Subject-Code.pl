student(101, ravi).
student(102, priya).

teacher(t1, kumar).
teacher(t2, anitha).

subject(s1, python).
subject(s2, prolog).

handles(t1, s1).
handles(t2, s2).

studies(X, Y) :-
    student(X, _),
    teacher(T, _),
    handles(T, Y).