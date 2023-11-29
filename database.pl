person(john, date(1990, 5, 12)).
person(jane, date(1995, 2, 28)).
person(bob, date(1985, 11, 3)).
person(susan, date(1978, 7, 19)).


dob(Name, DateOfBirth) :- person(Name, DateOfBirth).
