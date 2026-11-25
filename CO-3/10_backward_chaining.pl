% Backward chaining: prove a goal from facts and rules
fact(sunlight).
fact(water).
fact(soil).

rule(grows, [sunlight, water, soil]).
rule(healthy_plant, [grows]).

prove(Goal) :- fact(Goal).
prove(Goal) :-
    rule(Goal, Conditions),
    prove_all(Conditions).

prove_all([]).
prove_all([Goal|Rest]) :-
    prove(Goal),
    prove_all(Rest).

% Queries: ?- prove(grows).
% ?- prove(healthy_plant).
% ?- prove(can_fly).
