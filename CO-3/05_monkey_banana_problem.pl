% Simplified Monkey and Banana planning problem
% State: state(MonkeyPosition, BoxPosition, MonkeyOnBox, HasBanana)
move(state(at_door, at_window, no, no),
     walk_to_window,
     state(at_window, at_window, no, no)).
move(state(at_window, at_window, no, no),
     push_box_to_middle,
     state(at_middle, at_middle, no, no)).
move(state(at_middle, at_middle, no, no),
     climb_box,
     state(at_middle, at_middle, yes, no)).
move(state(at_middle, at_middle, yes, no),
     grasp_banana,
     state(at_middle, at_middle, yes, yes)).

solve(State, []) :- State = state(_, _, _, yes).
solve(State, [Action|Rest]) :-
    move(State, Action, Next),
    solve(Next, Rest).

% Query: ?- solve(state(at_door, at_window, no, no), Plan).
