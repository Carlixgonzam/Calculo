#El siguiente programa me ayuda a determinar que tipo de sustitucion debo usar para calcular las integrales
#Además, el tipo de procedimiento que debo seguir para resolver la integral
#Autora Carla González Mina

import sympy as sp

def analizar_integrando():
    """
    Función para mostrar el integrando ingresado de forma simbólica utilizando sympy.
    Se asume que la entrada es correcta.
    """
    x = sp.symbols('x')
    integrando_str = input("Ingrese el integrando en términos de x: ")
    integrando = sp.sympify(integrando_str)
    print("\nEl integrando ingresado es:")
    sp.init_printing(use_unicode=True)
    sp.pretty_print(integrando)

def menu_raiz():
    print("\n--- Integrales que contienen una raíz cuadrada ---")
    print("Seleccione la forma de la raíz:")
    print("  1. √(a² - x²)")
    print("  2. √(a² + x²)")
    print("  3. √(x² - a²)")
    print("  4. √(ax² + bx + c)  (se requiere completar el cuadrado)")
    opcion = input("Ingrese 1, 2, 3 o 4: ").strip()
    
    if opcion == "1":
        print("\nSugerencia: Utilice la sustitución trigonométrica:")
        print("        x = a*sin(u)")
        print("Procedimiento:")
        print("  1. Reemplace x por a*sin(u), de donde dx = a*cos(u) du.")
        print("  2. Sustituya en la integral y use la identidad sin²(u) + cos²(u) = 1 para simplificar.")
        print("  3. Integre con respecto a u y regrese a la variable x mediante u = arcsin(x/a).")
        
    elif opcion == "2":
        print("\nSugerencia: Utilice la sustitución trigonométrica:")
        print("        x = a*tan(u)")
        print("Procedimiento:")
        print("  1. Reemplace x por a*tan(u), de donde dx = a*sec²(u) du.")
        print("  2. Sustituya en la integral y use la identidad 1 + tan²(u) = sec²(u) para simplificar.")
        print("  3. Integre con respecto a u y regrese a la variable x mediante u = arctan(x/a).")
        
    elif opcion == "3":
        print("\nSugerencia: Utilice la sustitución trigonométrica:")
        print("        x = a*sec(u)")
        print("Procedimiento:")
        print("  1. Reemplace x por a*sec(u), de donde dx = a*sec(u)*tan(u) du.")
        print("  2. Sustituya en la integral y use la identidad sec²(u) - 1 = tan²(u) para simplificar.")
        print("  3. Integre con respecto a u y regrese a la variable x mediante u = arcsec(x/a).")
        
    elif opcion == "4":
        print("\nSugerencia:")
        print("  1. Complete el cuadrado en la expresión ax² + bx + c para reescribirla en la forma:")
        print("        a(x - h)² + k")
        print("  2. Según el signo de k:")
        print("       - Si k < 0, se obtiene una forma similar a a² - (x-h)² y se puede usar x - h = a*sin(u).")
        print("       - Si k > 0, se obtiene una forma similar a (x-h)² + a² y se puede usar x - h = a*tan(u).")
        print("  3. Sustituya en la integral, integre y regrese a la variable original.")
        
    else:
        print("Opción no válida. Por favor, ejecute nuevamente el programa y seleccione una opción correcta.")

def menu_trig():
    print("\n--- Integrales que involucran funciones trigonométricas ---")
    print("Seleccione el caso:")
    print("  1. Exponente impar en sen(x) o cos(x)")
    print("  2. Exponentes pares en sen(x) y cos(x) (aplique identidades trigonométricas)")
    opcion = input("Ingrese 1 o 2: ").strip()
    
    if opcion == "1":
        print("\nSugerencia:")
        print("  - Si el exponente de sen(x) es impar, extraiga un factor de sen(x) y use la sustitución u = cos(x).")
        print("  - Si el exponente de cos(x) es impar, extraiga un factor de cos(x) y use la sustitución u = sen(x).")
        print("Procedimiento:")
        print("  1. Factorice el término impar y exprese el resto en función del otro usando la identidad sen²(x) + cos²(x) = 1.")
        print("  2. Realice la sustitución correspondiente y obtenga una integral en u.")
        print("  3. Integre y regrese a la variable original.")
        
    elif opcion == "2":
        print("\nSugerencia:")
        print("  Utilice identidades trigonométricas (como sen²(x) = 1 - cos²(x) o fórmulas de ángulo doble) para reducir los exponentes,")
        print("  y posteriormente, si es posible, aplique una sustitución para integrar la expresión resultante.")
    else:
        print("Opción no válida. Por favor, ejecute nuevamente el programa y seleccione una opción correcta.")

def main():
    print("Bienvenida, Carla.")
    print("Este programa le ayudará a determinar el tipo de sustitución o procedimiento a utilizar para resolver integrales,")
    print("guiándose en distintos casos similares a los ejercicios de la 7ª edición de Stewart.\n")
    
    print("Seleccione la categoría de la integral que desea analizar:")
    print("  1. Integral que contiene una raíz cuadrada.")
    print("  2. Integral de una función compuesta (f(g(x)) donde g′(x) aparece).")
    print("  3. Integral de un producto en el que aparece la derivada de una función (f′(x)·[f(x)]ⁿ).")
    print("  4. Integral que involucra funciones trigonométricas.")
    print("  5. Integral que requiere completar el cuadrado en una expresión cuadrática.")
    print("  6. Otro caso (se recomienda analizar la integral de forma individual).")
    
    opcion = input("Ingrese el número correspondiente a la categoría de la integral: ").strip()
    
    if opcion == "1":
        menu_raiz()
    elif opcion == "2":
        print("\n--- Integral de función compuesta ---")
        print("Sugerencia: Utilice la sustitución u = g(x), donde g(x) es la función interna de f(g(x)).")
        print("Procedimiento:")
        print("  1. Identifique g(x) dentro de f(g(x)).")
        print("  2. Calcule du = g′(x) dx.")
        print("  3. Sustituya en la integral para obtener una integral en función de u.")
        print("  4. Integre y regrese a la variable original mediante u = g(x).")
    elif opcion == "3":
        print("\n--- Integral de la forma f′(x)·[f(x)]ⁿ ---")
        print("Sugerencia: Use la sustitución u = f(x).")
        print("Procedimiento:")
        print("  1. Sea u = f(x), de modo que du = f′(x) dx.")
        print("  2. La integral se transforma en ∫ uⁿ du, la cual es directa de integrar.")
        print("  3. Una vez integrada, reemplace u por f(x).")
    elif opcion == "4":
        menu_trig()
    elif opcion == "5":
        print("\n--- Integral que requiere completar el cuadrado ---")
        print("Sugerencia:")
        print("  1. Reescriba la expresión cuadrática ax² + bx + c en la forma a(x - h)² + k completando el cuadrado.")
        print("  2. Según el valor de k:")
        print("       - Si k < 0, la expresión puede tomar la forma a² - (x-h)² y se usa la sustitución x - h = a*sin(u).")
        print("       - Si k > 0, la expresión puede tomar la forma (x-h)² + a² y se usa la sustitución x - h = a*tan(u).")
        print("  3. Realice la sustitución en la integral, integre y luego regrese a la variable original.")
    elif opcion == "6":
        print("\nSe recomienda analizar la integral de forma individual para identificar la mejor sustitución o método de integración.")
    else:
        print("Opción no válida. Por favor, ejecute nuevamente el programa y seleccione una opción correcta.")
    
    opcion_analisis = input("\n¿Desea ingresar el integrando para mostrar su forma simbólica? (si/no): ").strip().lower()
    if opcion_analisis in ["si", "s"]:
        analizar_integrando()

if __name__ == '__main__':
    main()
