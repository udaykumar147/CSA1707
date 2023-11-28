male(uday).
male(shiva).
male(ali).
male(pavan).
male(naga).

female(lakshmi).
female(rose).
female(pooja).
female(vinitha).

parent(uday, shiva).
parent(uday, rose).
parent(pooja, mike).
parent(susan, rose).
parent(shiva, ali).
parent(rose, pavan).
parent(rose, vinitha).
parent(ali, naga).
parent(pooja, naga).

father(Father, Child) :-
    male(Father),
    parent(Father, Child).

mother(Mother, Child) :-
    female(Mother),
    parent(Mother, Child).

sibling(Sibling1, Sibling2) :-
    parent(Parent, Sibling1),
    parent(Parent, Sibling2),
    Sibling1 \= Sibling2.

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).