#!/usr/bin/env python
import matplotlib.pyplot as plt

from classes.class_secant import Secant_Method
from classes.class_numerov import Numerov_Method
from classes.class_simpson import Simpson_Method


'''
Potential function of the quantum system.
---------------------------------------------------------
'''


def v(x):
    'potential for hydrogen atom'
    l = 0.0

    return -1.0/x + l * (l + 1.0)/(x*x)


'''
Help function to discretization of the analytical form
---------------------------------------------------------
'''


def anal_disc():
    'Discretization of the analytical form will be done'
    initial = 0.01
    h = 0.01

    x = []
    y = []

    while initial <= 20:
        x.append(initial)
        y.append(v(initial))
        initial += h

    return x, y


'''
Function used to normalized the wavefunction.
---------------------------------------------------------
'''


def normalized(u):
    'Normalization to the wavefunction'

    result = integration.simpson(u)

    for i in range(len(u)):
        u[i] = u[i] / result

    return u


'''
Function used to calculate the probability
'''


def probability(u):
    y = []
    for i in range(len(u)):
        y.append(u[i] * u[i])

    return y


'''
Function used to make list of the eigenenery to plot.
---------------------------------------------------------
'''


def eigen(x, l):
    'Making the list of an eigenvalue for plotting'
    y = []
    for i in range(len(x)):
        y.append(l)

    return y


'''
Function used to add eigenfunction with eigenenergy.
---------------------------------------------------------
'''


def mixfunction(u, el):
    'For nice visualization adding eigenfunction with eigenvalue'
    y = []
    for i in range(len(u)):
        y.append(u[i]+el[i])
    return y


'''
Stepping into the main program.
---------------------------------------------------------
'''


'Plotting potential'
x, v_x = anal_disc()
plt.plot(x, v_x, 'k')


'Calling Numerov Method for the potential v(x)'
wavefunction = Numerov_Method(x, v_x)

'Calling Secant method for the function $numerov$'
find = Secant_Method(wavefunction.numerov)

'Calling Simpson Method to integrate'
integration = Simpson_Method()

'Initial guess for eigen value'
l = -10

title = 'Eigenvalue(s) = '

while l < 0:
    'Searching for the eigenvalue.'
    l = find.secant(l)

    title = title + str("%.2f" % round(l, 2)) + ', '

    'Calculating the eigenfunction.'
    x, u = wavefunction.numerov(l)

    'Normalizing the eigenfunction'
    u = normalized(u)

    'Probability of eigenfunction'
    u = probability(u)

    'list to plot eigenvalue'
    el = eigen(x, l)

    'Adding eigenvalue and normalized wavefunction'
    n_u = mixfunction(u, el)

    plt.plot(x, n_u, 'g')
    plt.plot(x, el, 'r')

    'for loop'
    l += 0.3

'Plotting graph'
plt.figure(1)
plt.xlabel('Position x')
plt.ylabel('Magnitude')
plt.title(title)
plt.legend(['$V(x)$', 'p(x)', '$E_n$'], loc=4)
plt.axis([0, 20, -1, 0.5])

plt.show()
