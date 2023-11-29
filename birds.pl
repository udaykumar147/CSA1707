bird(robin, red_breast, woodland).
bird(sparrow, brown, urban).
bird(blue_jay, blue, woodland).
bird(penguin, black_and_white, polar).

% Rules to query information
color_of_bird(Bird, Color) :-
    bird(Bird, Color, _).

habitat_of_bird(Bird, Habitat) :-
    bird(Bird, _, Habitat).