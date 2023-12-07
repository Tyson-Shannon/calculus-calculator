#Math calculations and output
#pip install sympy
import sympy
import math

#takes function y and sets limit for symbol to value
def limit(y, symbol, value, historyBox, tk):
    x = sympy.Symbol(symbol)
    historyBox.insert(tk.END, "A: "+str(sympy.limit(y, x, value))+"\n")

#takes derivative of function with respect to symbol
def der(f, symbol, historyBox, tk):
    x = sympy.Symbol(symbol)
    historyBox.insert(tk.END, "A: "+str(sympy.Derivative(f, x).doit())+"\n")

#takes differential of function with respect to symbol
def dif(f, symbol, historyBox, tk):
    x = sympy.Symbol(symbol)
    historyBox.insert(tk.END, "A: "+str(sympy.diff(f, x))+"\n")

#indefinite integrate a function with respect to symbol
def integrate1(f, symbol, historyBox, tk):
    x = sympy.Symbol(symbol)
    historyBox.insert(tk.END, "A: "+str(sympy.integrate(f, x))+"\n")

#definite integrate a function with respect to symbole with lower limit and upper limit
def integrate2(f, symbol, lower, upper, historyBox, tk):
    x = sympy.Symbol(symbol)
    historyBox.insert(tk.END, "A: "+str(sympy.integrate(f, (x, lower, upper)))+"\n")

#washer is integrate(a, b) pi(f^2-g^2) 
def washer(f, g, symbol, lower, upper, historyBox, tk):
    x = sympy.Symbol(symbol)
    expr = "("+f+")**2-("+g+")**2"
    historyBox.insert(tk.END, "A: PI*"+str(sympy.integrate(expr, (x, lower, upper)))+"\n")
