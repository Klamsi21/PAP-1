from math import sqrt, pi
fall = [10.760, 11.040, 10.930, 11.740, 12.290]
steig = [18.590, 20.560, 21.860, 18.270, 20.650]

def v(zeiten: list[float]) -> list[float]:
    result = []
    for zeit in zeiten:
        result.append(5*10**(-4)/zeit)
    return result

def r0(velocities: list[float]) -> list[float]:
    result = []
    eta = 1.81*10**(-5)
    g = 9.81
    rho = 872.2-1.29
    for v in velocities:
        r= sqrt(
            (9* eta* v)/
            (2*rho*g)
            )
        result.append(r)

    return result

def f(radien: list[float]) -> list[float]:
    b = 7.78 * 10**(-3)
    p = 101450
    result = []
    for r in radien:
        result.append(1/(1+ b/(r*p)))
    return result


def q(v_fall: list[float], v_steig: list[float], r0: list[float], f: list[float]):

    rho = 872.2-1.29
    eta = 1.81*10**(-5)
    g = 9.81
    U = 495
    d = 0.006
    result = []

    for i in range(len(v_fall)):
        q = (v_fall[i]+ v_steig[i])*sqrt((9*v_fall[i]*(f[i]*eta)**3)/(2*rho*g))*(6*pi*d)/U

        result.append(q)
    return result

vs = v(steig)
vf = v(fall)
r0 = r0(vf)
f = f(r0)
q= q(vf, vs, r0, f)

print(vs)
print(vf)
print(r0)
print(f)
print(q)