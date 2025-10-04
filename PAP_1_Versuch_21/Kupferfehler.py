import numpy as np

def error(I, t, m, dI, dt, dm):
    z= 2
    M = 63.546
    F = ((I*t)/(z*m))*M
    term1 = ((t)/(z*m))*M*dI
    term2 = ((I)/(z*m))*M*dt
    term3 = ((I*t)/(z*m**2))*M*dm

    return F, np.sqrt(term1**2 + term2**2 + term3**2)


print(error(0.51, 1800, (0.3021), 0.03, 3, 0.0014))