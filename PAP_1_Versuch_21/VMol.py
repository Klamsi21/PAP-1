import numpy as np

def VMol(pL, T, dpL, dT):
    V0 = 22.414
    p0 = 760
    T0 = 273.15
    dpd = 0.63

    p = 0.75*pL- 0.9*19.82

    dp= np.sqrt((0.75*dpL)**2 + (0.9*dpd)**2)
    print(f"{p} \pm {dp}")
    V = p0/p * T/T0 *V0

    error = np.sqrt((p0/p * dT/T0 *V0)**2 + (p0/(p**2) * T/T0 *V0*0.75*dp)**2)

    return V, error

print(VMol(1009, (23+273.15), 0.2, 0.5))

def n(Vm, dVm, V, dV):
    n = V/Vm
    error = np.sqrt((1/Vm * dV)**2 + ((V/(Vm**2))*dVm)**2)

    return n, error

print(n(25.00, 0.04, (0.0226- 0.0013), 0.00014))

def F(n, I, t, dn, dI, dt):
    z= 4
    F = (I*t)/(z*n)

    dF = np.sqrt(
        ((I)/(z*n)*dt)**2
        + ((t)/(z*n)*dI)**2
        + ((t*I)/(z*(n**2))*dn)**2
    )

    return F, dF

print(F(8.52*10**(-4), 0.56, 605.3, 0.06*10**(-4), 0.03, 0.3))