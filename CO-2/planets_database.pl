% Planets database
planet(mercury, terrestrial, 0.39).
planet(venus, terrestrial, 0.72).
planet(earth, terrestrial, 1.00).
planet(mars, terrestrial, 1.52).
planet(jupiter, gas_giant, 5.20).
planet(saturn, gas_giant, 9.58).
planet(uranus, ice_giant, 19.2).
planet(neptune, ice_giant, 30.1).

% Second argument is planet type; third is approximate distance from Sun in AU.
% Query: ?- planet(Name, Type, Distance).
% Query: ?- planet(Name, gas_giant, _).
