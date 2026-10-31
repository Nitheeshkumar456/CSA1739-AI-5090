bird(parrot).
bird(eagle).
bird(penguin).
bird(ostrich).

can_fly(parrot).
can_fly(eagle).

cannot_fly(penguin).
cannot_fly(ostrich).

fly(X) :-
    bird(X),
    can_fly(X).

fly(X) :-
    bird(X),
    cannot_fly(X),
    fail.