planet(mercury, rocky, 0.39, small, hot).
planet(venus, rocky, 0.72, small, very_hot).
planet(earth, rocky, 1.00, medium, moderate).
planet(mars, rocky, 1.52, small, cold).
planet(jupiter, gas_giant, 5.20, large, very_cold).
planet(saturn, gas_giant, 9.58, large, very_cold).
planet(uranus, ice_giant, 19.22, medium, very_cold).
planet(neptune, ice_giant, 30.05, medium, very_cold).

habitable(Planet) :-
    planet(Planet, rocky, _, medium, moderate).

gas_giant(Planet) :-
    planet(Planet, gas_giant, _, _, _).

ice_giant(Planet) :-
    planet(Planet, ice_giant, _, _, _).