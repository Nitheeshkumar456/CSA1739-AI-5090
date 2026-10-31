diet(diabetes, 'Avoid sugar and eat vegetables').
diet(obesity, 'Eat fruits and low-fat food').
diet(anemia, 'Eat spinach and iron-rich food').
diet(fever, 'Drink water and eat light food').
diet(hypertension, 'Avoid excess salt and eat fruits').

suggest(X) :-
    diet(X, Y),
    write('Diet Suggestion: '),
    write(Y).