% Facts and rule to check whether a bird can fly
bird(sparrow).
bird(pigeon).
bird(eagle).
bird(ostrich).
bird(penguin).

cannot_fly(ostrich).
cannot_fly(penguin).

can_fly(Bird) :-
    bird(Bird),
    \+ cannot_fly(Bird).

% Queries:
% ?- can_fly(sparrow).
% ?- can_fly(penguin).
% ?- can_fly(WhichBird).
