import sympy as sp

def integrar_por_partes(expr, var, u=None, dv=None):
    """
    Realiza la integración por partes de una expresión dada.
    
    :param expr: Expresión simbólica a integrar.
    :param var: Variable de integración.
    :param u: (Opcional) Parte elegida como u.
    :param dv: (Opcional) Parte elegida como dv.
    :return: Resultado de la integral.
    """
    if u is None or dv is None:
        # Si no se especifican u y dv, se elige automáticamente
        # Priorizamos: logaritmos > potencias > trigonométricas > exponenciales
        if expr.has(sp.log(var)):
            u = sp.log(var)
            dv = expr / u
        elif expr.has(var):
            u = var
            dv = expr / u
        elif expr.has(sp.exp(var)):
            u = sp.exp(var)
            dv = expr / u
        elif expr.has(sp.sin(var)) or expr.has(sp.cos(var)):
            u = expr
            dv = 1  # dv = dx

    # Derivo u para obtener du
    du = sp.diff(u, var)
    # Integro dv para obtener v
    v = sp.integrate(dv, var)

    #fórmula de integración por partes
    integral_resultado = u * v - sp.integrate(v * du, var)

    return integral_resultado.simplify()

#variable simbólica
x = sp.Symbol('x')

#  ∫ x * e^x dx
expr = x * sp.exp(x)

resultado = integrar_por_partes(expr, x)
print(f"Integral de {expr}:")
print(resultado)