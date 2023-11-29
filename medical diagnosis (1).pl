symptom(john, fever).
symptom(john, cough).
symptom(john, headache).
symptom(john, runny_nose).
symptom(jane, fever).
symptom(jane, cough).
symptom(jane, sore_throat).
symptom(jane, body_ache).

disease(influenza) :-
    symptom(X, fever),
    symptom(X, cough),
    symptom(X, headache),
    symptom(X, runny_nose).
disease(cold) :-
    symptom(X, headache),
    symptom(X, sneezing),
    symptom(X, sore_throat),
    symptom(X, chills),
    symptom(X, runny_nose).
disease(measles) :-
    symptom(X, fever),
    symptom(X, cough),
    symptom(X, conjunctivitis),
    symptom(X, rash).

diagnosis(Patient, Disease) :-
    disease(Disease),
    symptom(Patient, Symptom),
    symptom(Patient, Symptom2),
    Symptom \= Symptom2,
    symptom(Patient, Symptom3),
    Symptom \= Symptom3,
    Symptom2 \= Symptom3.

?- diagnosis(jane, Disease).
