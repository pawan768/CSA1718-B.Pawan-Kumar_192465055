% Simple rule-based medical diagnosis demonstration.
% Not a substitute for professional diagnosis.
symptom(fever, flu).
symptom(cough, flu).
symptom(body_pain, flu).
symptom(sneezing, common_cold).
symptom(runny_nose, common_cold).
symptom(headache, migraine).
symptom(light_sensitivity, migraine).

diagnosis(Disease, Symptom) :-
    symptom(Symptom, Disease).

% Queries:
% ?- diagnosis(Disease, fever).
% ?- diagnosis(Disease, cough).
% Seek medical care for concerning or persistent symptoms.
