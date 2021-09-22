#create a function that finds acceleration given velocities and time
def accelEqn(Vi,Vf,t):
    return (Vf - Vi) / t

#create a function that finds final velocity when time is unknown
def finalVEqn(Vi, a, d):
    return (Vi ** 2) + (2 * a * d)

#create a function that finds distance when we don't know final velocity
def distanceNoVel (Vi, a, t):
    return (Vi * t) + ((a * (t ** 2)) / 2)

#create a function that finds distance when you dont know acceleration
def distanceNoAccel(Vf, Vi, t):
    return ((Vf + Vi) / 2) * t