% Educational diet suggestions based on a selected condition.
% This is a classroom example, not medical advice.
diet(diabetes, 'Balanced meals with controlled portions; limit sugary drinks.').
diet(hypertension, 'Choose lower-sodium foods, vegetables and fruits.').
diet(anemia, 'Include iron-rich foods such as beans and leafy greens.').
diet(obesity, 'Prefer balanced portions, vegetables and minimally processed foods.').

suggest_diet(Disease, Advice) :-
    diet(Disease, Advice).

% Query: ?- suggest_diet(diabetes, Advice).
% Always consult a qualified clinician/dietitian for personal advice.
