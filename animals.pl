% Facts: Direct size comparisons
bigger(elephant, horse).
bigger(horse, donkey).
bigger(donkey, dog).
bigger(donkey, monkey).

% Rules: How to infer 'is_bigger' relationships

% Rule 1: Direct relationship implies 'is_bigger'
is_bigger(X, Y) :-
    bigger(X, Y).

% Rule 2: Transitive relationship
% X is bigger than Y if X is directly bigger than some Z,
% and Z is (recursively) bigger than Y.
is_bigger(X, Y) :-
    bigger(X, Z),
    is_bigger(Z, Y).
