% Family tree facts
parent(john, mary).
parent(john, peter).
parent(mary, alice).
parent(peter, david).
parent(susan, mary).

male(john).
male(peter).
male(david).
female(susan).
female(mary).
female(alice).

father(F, C) :- parent(F, C), male(F).
mother(M, C) :- parent(M, C), female(M).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
grandparent(G, C) :- parent(G, P), parent(P, C).
ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(A, X), ancestor(X, D).

% Queries: ?- father(john, mary).
% ?- grandparent(john, alice).
% ?- ancestor(john, Who).
