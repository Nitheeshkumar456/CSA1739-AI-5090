move(state(floor, middle, onbox),
     state(floor, middle, onbox),
     climb).

move(state(floor, P, onfloor),
     state(floor, P, onbox),
     climb).

move(state(floor, P, onfloor),
     state(floor, Q, onfloor),
     walk(P, Q)) :-
     P \= Q.

move(state(floor, P, onfloor),
     state(onbox, P, onfloor),
     push(P)).

goal(state(_, _, onbox)).

solve(S, []) :-
    goal(S).

solve(S, [M|Moves]) :-
    move(S, S1, M),
    solve(S1, Moves).