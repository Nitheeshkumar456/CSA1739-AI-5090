male(ram).
male(kumar).
male(raj).

female(sita).
female(geetha).

parent(ram, kumar).
parent(sita, kumar).
parent(kumar, raj).
parent(geetha, raj).

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.