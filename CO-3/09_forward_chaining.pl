% Forward chaining: repeatedly derive new facts from rules
:- dynamic derived/1.

fact(rain).
fact(has_umbrella).

rule(wet_ground, [rain]).
rule(can_go_out, [has_umbrella]).
rule(stay_inside, [rain, no_umbrella]).

known(Fact) :- fact(Fact).
known(Fact) :- derived(Fact).

run_forward_chaining :-
    retractall(derived(_)),
    repeat,
    findall(X, (rule(X, Conditions),
                forall(member(C, Conditions), known(C)),
                \+ fact(X), \+ derived(X)), New),
    add_new(New),
    New = [], !.

add_new([]).
add_new([X|Xs]) :-
    (derived(X) -> true ; assertz(derived(X))),
    add_new(Xs).

% Query: ?- run_forward_chaining.
% Then: ?- known(wet_ground).
