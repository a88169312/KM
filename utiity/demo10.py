import ast

x1 = "None"
x2 = "None"
x3 = "None"
y0 = None
print(type(y0), y0)
print(type(x1), x1)
y1 = ast.literal_eval(x1)
print(type(y1), y1)
y2 = None if x2 == "None" else x2
print(type(y2), y2)
y3 = eval(x3)
print(type)