% Greedy Best First Search using heuristic values
:- use_module(library(pairs)).

edge(a, b). edge(a, c). edge(b, d). edge(b, e).
edge(c, f). edge(e, g). edge(f, g).
heuristic(a, 7). heuristic(b, 6). heuristic(c, 4).
heuristic(d, 5). heuristic(e, 2). heuristic(f, 3).
heuristic(g, 0).

best_first(Start, Goal, Path) :-
    search([[Start]], Goal, ReversePath),
    reverse(ReversePath, Path).

search([[Goal|Rest]|_], Goal, [Goal|Rest]).
search([[Node|Path]|Queue], Goal, Result) :-
    findall([Next,Node|Path],
            (edge(Node, Next), \+ member(Next, [Node|Path])),
            Children),
    append(Queue, Children, Combined),
    sort_by_heuristic(Combined, Sorted),
    search(Sorted, Goal, Result).

sort_by_heuristic(Paths, Sorted) :-
    findall(H-Path,
            (member(Path, Paths), Path = [Node|_], heuristic(Node, H)),
            Pairs),
    keysort(Pairs, Ordered),
    pairs_values(Ordered, Sorted).

% Query: ?- best_first(a, g, Path).
