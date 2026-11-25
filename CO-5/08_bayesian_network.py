# Small Bayesian network: Rain -> Wet Grass
# Uses conditional probability enumeration without external libraries.
p_rain = 0.2
p_wet_given_rain = 0.9
p_wet_given_no_rain = 0.1

p_wet = (p_wet_given_rain * p_rain) + (p_wet_given_no_rain * (1 - p_rain))
p_rain_and_wet = p_wet_given_rain * p_rain
p_rain_given_wet = p_rain_and_wet / p_wet

print("P(Rain) =", p_rain)
print("P(Wet grass) =", round(p_wet, 3))
print("P(Rain | Wet grass) =", round(p_rain_given_wet, 3))
