#Math calculations and output
#pip install sympy
import sympy

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