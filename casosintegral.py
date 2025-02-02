#El siguiente programa me ayuda a determinar que tipo de sustitucion debo usar para calcular las integrales
#Además, el tipo de procedimiento que debo seguir para resolver la integral
#Autora Carla González Mina

import sympy as sp

# Definición de los símbolos globales
x = sp.symbols('x')
sp.init_printing(use_unicode=True)

# Integración para integrales con √(a² - x²)
def integrate_sqrt_minus():
    print("\n[Integración con √(a² - x²)]")
    print("Se usará la sustitución: x = a*sin(θ)")
    print("Utilice la identidad: sin²(θ) + cos²(θ) = 1, que implica:")
    print("  √(a² - x²) = √(a² - a² sin²(θ)) = a*cos(θ)")
    
    integrand_str = input("Ingrese la función integranda en términos de x: ")
    a_val_str = input("Ingrese el valor de a (constante): ")
    
    integrand = sp.sympify(integrand_str)
    a_val = sp.sympify(a_val_str)
    
    u = sp.symbols('u')
    # Sustitución: x = a*sin(u)  ⇒  dx = a*cos(u) du
    substitution = a_val * sp.sin(u)
    dx_sub = a_val * sp.cos(u)
    
    # Se sustituye en la integral
    integrand_u = integrand.subs(x, substitution) * dx_sub
    integral_u = sp.integrate(integrand_u, u)
    # Regreso a la variable x: u = arcsin(x/a)
    result = sp.simplify(integral_u.subs(u, sp.asin(x / a_val)))
    
    print("\nEl resultado de la integración es:")
    sp.pretty_print(result)

# Integración para integrales con √(a² + x²)
def integrate_sqrt_plus():
    print("\n[Integración con √(a² + x²)]")
    print("Se usará la sustitución: x = a*tan(θ)")
    print("Utilice la identidad: 1 + tan²(θ) = sec²(θ), que implica:")
    print("  √(a² + x²) = √(a² + a² tan²(θ)) = a*sec(θ)")
    
    integrand_str = input("Ingrese la función integranda en términos de x: ")
    a_val_str = input("Ingrese el valor de a (constante): ")
    
    integrand = sp.sympify(integrand_str)
    a_val = sp.sympify(a_val_str)
    
    u = sp.symbols('u')
    # Sustitución: x = a*tan(u)  ⇒  dx = a*sec²(u) du
    substitution = a_val * sp.tan(u)
    dx_sub = a_val * sp.sec(u)**2
    
    integrand_u = integrand.subs(x, substitution) * dx_sub
    integral_u = sp.integrate(integrand_u, u)
    # Regreso a x: u = arctan(x/a)
    result = sp.simplify(integral_u.subs(u, sp.atan(x / a_val)))
    
    print("\nEl resultado de la integración es:")
    sp.pretty_print(result)

#  Integración para integrales con √(x² - a²)
def integrate_sqrt_x2_minus():
    print("\n[Integración con √(x² - a²)]")
    print("Se usará la sustitución: x = a*sec(θ)")
    print("Utilice la identidad: sec²(θ) - 1 = tan²(θ), que implica:")
    print("  √(x² - a²) = √(a² sec²(θ) - a²) = a*tan(θ)")
    
    integrand_str = input("Ingrese la función integranda en términos de x: ")
    a_val_str = input("Ingrese el valor de a (constante): ")
    
    integrand = sp.sympify(integrand_str)
    a_val = sp.sympify(a_val_str)
    
    u = sp.symbols('u')
    # Sustitución: x = a*sec(u)  ⇒  dx = a*sec(u)*tan(u) du
    substitution = a_val * sp.sec(u)
    dx_sub = a_val * sp.sec(u) * sp.tan(u)
    
    integrand_u = integrand.subs(x, substitution) * dx_sub
    integral_u = sp.integrate(integrand_u, u)
    # Regreso a x: se utiliza que cos(u) = a/x  ⇒  u = acos(a/x)
    result = sp.simplify(integral_u.subs(u, sp.acos(a_val / x)))
    
    print("\nEl resultado de la integración es:")
    sp.pretty_print(result)

# 4. Integración para integrales con √(a*x² + b*x + c) (completar el cuadrado)
def integrate_sqrt_quadratic():
    print("\n[Integración con √(a*x² + b*x + c)]")
    print("Se completará el cuadrado y se aplicará la sustitución trigonométrica correspondiente.")
    integrand_str = input("Ingrese la función integranda en términos de x (que contenga √(a*x² + b*x + c)): ")
    a_const_str = input("Ingrese el valor de a (constante): ")
    b_const_str = input("Ingrese el valor de b: ")
    c_const_str = input("Ingrese el valor de c: ")
    
    integrand = sp.sympify(integrand_str)
    a_const = sp.sympify(a_const_str)
    b_const = sp.sympify(b_const_str)
    c_const = sp.sympify(c_const_str)
    
    # Completamos el cuadrado: a*x² + b*x + c = a*(x + b/(2a))² + (c - b²/(4a))
    h = -b_const / (2 * a_const)
    k = c_const - b_const**2 / (4 * a_const)
    print(f"\nSe completa el cuadrado: x = u + ({h}), de forma que la expresión se transforma en:")
    print(f"  a*u² + ({k})")
    
    u = sp.symbols('u')
    if k < 0:
        print("Como k < 0, se sugiere la sustitución: u = √(-k/a) * sin(θ)")
        print("Utilice la identidad: sin²(θ) + cos²(θ) = 1")
        theta = sp.symbols('theta')
        substitution_u = sp.sqrt(-k / a_const) * sp.sin(theta)
        du_sub = sp.sqrt(-k / a_const) * sp.cos(theta)
        # x = u + h
        x_sub = substitution_u + h
        dx_sub = du_sub
        integrand_theta = integrand.subs(x, x_sub) * dx_sub
        integral_theta = sp.integrate(integrand_theta, theta)
        # Regreso: θ = arcsin((x-h)*√(a/(-k)))
        result = sp.simplify(integral_theta.subs(theta, sp.asin((x - h) * sp.sqrt(a_const / (-k)))))
    else:
        print("Como k ≥ 0, se sugiere la sustitución: u = √(k/a) * tan(θ)")
        print("Utilice la identidad: 1 + tan²(θ) = sec²(θ)")
        theta = sp.symbols('theta')
        substitution_u = sp.sqrt(k / a_const) * sp.tan(theta)
        du_sub = sp.sqrt(k / a_const) * sp.sec(theta)**2
        x_sub = substitution_u + h
        dx_sub = du_sub
        integrand_theta = integrand.subs(x, x_sub) * dx_sub
        integral_theta = sp.integrate(integrand_theta, theta)
        # Regreso: θ = arctan((x-h)*√(a/k))
        result = sp.simplify(integral_theta.subs(theta, sp.atan((x - h) * sp.sqrt(a_const / k))))
    
    print("\nEl resultado de la integración es:")
    sp.pretty_print(result)

# 5. Integración de una función compuesta de la forma f(g(x))*g'(x)
def integrate_composite():
    print("\n[Integración de función compuesta f(g(x))*g'(x)]")
    print("Se aplicará la sustitución: u = g(x)")
    integrand_str = input("Ingrese la función integranda en términos de x (debe ser de la forma f(g(x))*g'(x)): ")
    g_str = input("Ingrese la función interna g(x): ")
    
    integrand = sp.sympify(integrand_str)
    g_expr = sp.sympify(g_str)
    
    # Se asume que la integral tiene la forma f(g(x))*g'(x)
    gprime = sp.diff(g_expr, x)
    f_expr = sp.simplify(integrand / gprime)
    
    u = sp.symbols('u')
    # Se reemplaza g(x) por u en f(g(x))
    f_u = f_expr.subs(g_expr, u)
    F_u = sp.integrate(f_u, u)
    # Regreso: u = g(x)
    result = sp.simplify(F_u.subs(u, g_expr))
    
    print("\nEl resultado de la integración es:")
    sp.pretty_print(result)

# 6. Integración de la forma f'(x)*[f(x)]ⁿ
def integrate_derivative_power():
    print("\n[Integración de f'(x)*[f(x)]ⁿ]")
    f_str = input("Ingrese la función f(x): ")
    n_str = input("Ingrese el exponente n: ")
    
    f_expr = sp.sympify(f_str)
    n_val = sp.sympify(n_str)
    
    # Se usa la sustitución u = f(x); la integral se reduce a ∫ uⁿ du
    if n_val != -1:
        result = sp.simplify(f_expr**(n_val + 1) / (n_val + 1))
    else:
        result = sp.simplify(sp.log(sp.Abs(f_expr)))
    
    print("\nEl resultado de la integración es:")
    sp.pretty_print(result)

# 7. Integración de funciones trigonométricas
def integrate_trig():
    print("\n[Integración de funciones trigonométricas]")
    print("Recuerde utilizar identidades trigonométricas tales como:")
    print("  - sin²(x) + cos²(x) = 1")
    print("  - sin(2x) = 2*sin(x)*cos(x)")
    print("  - cos(2x) = 2*cos²(x) - 1  ó  1 - 2*sin²(x)")
    
    integrand_str = input("Ingrese la función integranda en términos de x (por ejemplo, con sin(x) y cos(x)): ")
    integrand = sp.sympify(integrand_str)
    result = sp.simplify(sp.integrate(integrand, x))
    
    print("\nEl resultado de la integración es:")
    sp.pretty_print(result)

# 8. Integración general (otro caso)
def integrate_general():
    print("\n[Integración general]")
    integrand_str = input("Ingrese la función integranda en términos de x: ")
    integrand = sp.sympify(integrand_str)
    result = sp.simplify(sp.integrate(integrand, x))
    
    print("\nEl resultado de la integración es:")
    sp.pretty_print(result)

# Diccionario que asocia cada caso a su descripción y función correspondiente
cases = {
    "1": {"description": "Integral con √(a² - x²)", "func": integrate_sqrt_minus},
    "2": {"description": "Integral con √(a² + x²)", "func": integrate_sqrt_plus},
    "3": {"description": "Integral con √(x² - a²)", "func": integrate_sqrt_x2_minus},
    "4": {"description": "Integral con √(a*x² + b*x + c) (completar el cuadrado)", "func": integrate_sqrt_quadratic},
    "5": {"description": "Integral de función compuesta f(g(x))*g'(x)", "func": integrate_composite},
    "6": {"description": "Integral de f'(x)*[f(x)]ⁿ", "func": integrate_derivative_power},
    "7": {"description": "Integral con funciones trigonométricas", "func": integrate_trig},
    "8": {"description": "Otro caso (integración general)", "func": integrate_general}
}

def main():
    print("Bienvenida, Carla.")
    print("Este programa resuelve integrales aplicando diversas sustituciones y sugiere las identidades trigonométricas correspondientes.")
    print("Seleccione la categoría de la integral que desea resolver:")
    
    for key, info in cases.items():
        print(f"  {key}. {info['description']}")
        
    opcion = input("Ingrese el número correspondiente a su opción: ").strip()
    
    if opcion in cases:
        cases[opcion]["func"]()
    else:
        print("Opción no válida. Por favor, reinicie el programa y seleccione una opción correcta.")

if __name__ == '__main__':
    main()