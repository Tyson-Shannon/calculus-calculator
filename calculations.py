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

#discx is integrate(a, b) pi(f^2)
def discx(f, symbol, lower, upper, historyBox, tk):
    x = sympy.Symbol(symbol)
    expr = "("+f+")**2"
    historyBox.insert(tk.END, "A: PI*"+str(sympy.integrate(expr, (x, lower, upper)))+"\n")

#discy is integrate(a, b) pi(y)
def discy(f, symbol, lower, upper, historyBox, tk):
    y = sympy.Symbol(symbol)
    historyBox.insert(tk.END, "A: PI*"+str(sympy.integrate(f, (y, lower, upper)))+"\n")

#riemann sums left, middle, and right where n=# of slices on interval [a, b]
def riemannl(f, symbol, a, b, n, historyBox, tk):
    delta = (b-a)/n
    i = a
    rSum = 0
    while(i<b):
        xi = f.replace(symbol, str(i))
        rSum = rSum+(eval(xi)*delta)
        i = i+delta
    historyBox.insert(tk.END, "A: "+str(rSum)+"\n")

def riemannm(f, symbol, a, b, n, historyBox, tk):
    delta = (b-a)/n
    i = a
    rSum = 0
    while(i<b):
        x1 = eval(f.replace(symbol, str(i)))
        x2 = eval(f.replace(symbol, str(i+1)))
        eq = (x1+x2)/2
        rSum = rSum+(eq*delta)
        i = i+delta
    historyBox.insert(tk.END, "A: "+str(rSum)+"\n")

def riemannr(f, symbol, a, b, n, historyBox, tk):
    delta = (b-a)/n
    i = a
    rSum = 0
    while(i<b):
        xi = f.replace(symbol, str(i+1))
        rSum = rSum+(eval(xi)*delta)
        i = i+delta
    historyBox.insert(tk.END, "A: "+str(rSum)+"\n")

#sequences convergent or divergent test where n=starting point
def seq(f, symbol, n, historyBox, tk):
    x = sympy.Symbol(symbol)
    seqLimit = sympy.limit(f, x, float("inf"))
    if (seqLimit == float("inf") or seqLimit == -float("inf")):
        historyBox.insert(tk.END, "A: Diverges to "+str(seqLimit)+"\n")
    elif (seqLimit == sympy.nan):
        historyBox.insert(tk.END, "A: Divergent, limit DNE\n")
    else:
        historyBox.insert(tk.END, "A: Converges to "+str(seqLimit)+"\n")
    
#series convergent or divergent improper integral test where n=starting point
def series(f, symbol, n, historyBox, tk):
    x = sympy.Symbol(symbol)
    serInt = sympy.integrate(f, (x, n, float("inf")))
    if (serInt == float("inf") or serInt == -float("inf")):
        historyBox.insert(tk.END, "A: Diverges to "+str(serInt)+"\n")
    elif (serInt == sympy.nan):
        historyBox.insert(tk.END, "A: Divergent, integral DNE\n")
    else:
        historyBox.insert(tk.END, "A: Converges to "+str(serInt)+"\n")

#arc length is integrate(a, b) sqrt(1+(f')**2)
def arcl(fPrime, symbol, lower, upper, historyBox, tk):
    x = sympy.Symbol(symbol)
    expr = "(1+("+fPrime+")**2)**0.5"
    historyBox.insert(tk.END, "A: "+str(sympy.integrate(expr, (x, lower, upper)))+"\n")
