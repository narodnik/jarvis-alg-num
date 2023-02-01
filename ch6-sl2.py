import math, pygame, time
from sympy import *

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
stopped = False

font = pygame.font.SysFont('dejavusans', 50, bold=True)

a, b, c = symbols("a b c")
operations = []
current_matrix = Matrix([[1, 0], [0, 1]])

T = Matrix([
    [1, 1],
    [0, 1]
])

S = Matrix([
    [ 0, 1],
    [-1, 0]
])

powers = "⁰¹²³⁴⁵⁶⁷⁸⁹"

coeff_a = a
coeff_b = b
coeff_c = c

value_a = 7
value_b = -10
value_c = 4

# sage: var("a b c x y")
# (a, b, c, x, y)
# sage: T = matrix([[1, 1], [0, 1]])
# sage: S = matrix([[0, 1], [-1, 0]])
# sage: S^-1 * vector([x, y])
# (-y, x)
# sage: f = a*x^2 + b*x*y + c*y^2
# sage: f(x=-y, y=x).expand()
# c*x^2 - b*x*y + a*y^2
# sage: S * vector([x, y])
# (y, -x)
# sage: f(x=y, y=-x).expand()
# c*x^2 - b*x*y + a*y^2
# sage: T^-1 * vector([x, y])
# (x - y, y)
# sage: f(x=(x - y), y=y).expand()
# a*x^2 - 2*a*x*y + b*x*y + a*y^2 - b*y^2 + c*y^2
# sage: T * vector([x, y])
# (x + y, y)
# sage: f(x=(x + y), y=y).expand()
# a*x^2 + 2*a*x*y + b*x*y + a*y^2 + b*y^2 + c*y^2

while not stopped:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Received quit!")
            stopped = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if event.mod & pygame.KMOD_SHIFT:
                    current_matrix = S**-1 @ current_matrix
                    # (a, b, c) -> (c, -b, a)
                    old_a, old_b, old_c = coeff_a, coeff_b, coeff_c
                    coeff_a = old_c
                    coeff_b = -old_b
                    coeff_c = old_a
                    if not operations:
                        operations.append(["S⁻¹", 1])
                    elif operations[-1][0] == "S⁻¹":
                        operations[-1][1] += 1
                    elif operations[-1][0] == "S":
                        if operations[-1][1] == 1:
                            operations.pop()
                        else:
                            operations[-1][1] -= 1
                    else:
                        operations.append(["S⁻¹", 1])
                else:
                    current_matrix = S @ current_matrix
                    # (a, b, c) -> (c, -b, a)
                    old_a, old_b, old_c = coeff_a, coeff_b, coeff_c
                    coeff_a = old_c
                    coeff_b = -old_b
                    coeff_c = old_a
                    if not operations:
                        operations.append(["S", 1])
                    elif operations[-1][0] == "S":
                        operations[-1][1] += 1
                    elif operations[-1][0] == "S⁻¹":
                        if operations[-1][1] == 1:
                            operations.pop()
                        else:
                            operations[-1][1] -= 1
                    else:
                        operations.append(["S", 1])
            elif event.key == pygame.K_t:
                if event.mod & pygame.KMOD_SHIFT:
                    current_matrix = T**-1 @ current_matrix
                    # (a, b, c) -> (a, b - 2a, a - b + c)
                    old_a, old_b, old_c = coeff_a, coeff_b, coeff_c
                    coeff_a = old_a
                    coeff_b = old_b - 2*old_a
                    coeff_c = old_a - old_b + old_c
                    if not operations:
                        operations.append(["T⁻¹", 1])
                    elif operations[-1][0] == "T⁻¹":
                        operations[-1][1] += 1
                    elif operations[-1][0] == "T":
                        if operations[-1][1] == 1:
                            operations.pop()
                        else:
                            operations[-1][1] -= 1
                    else:
                        operations.append(["T⁻¹", 1])
                else:
                    current_matrix = T @ current_matrix
                    # (a, b, c) -> (a, b + 2a, a + b + c)
                    old_a, old_b, old_c = coeff_a, coeff_b, coeff_c
                    coeff_a = old_a
                    coeff_b = old_b + 2*old_a
                    coeff_c = old_a + old_b + old_c
                    if not operations:
                        operations.append(["T", 1])
                    elif operations[-1][0] == "T":
                        operations[-1][1] += 1
                    elif operations[-1][0] == "T⁻¹":
                        if operations[-1][1] == 1:
                            operations.pop()
                        else:
                            operations[-1][1] -= 1
                    else:
                        operations.append(["T", 1])
            elif event.key == pygame.K_BACKSPACE:
                if operations:
                    if operations[-1][1] == 1:
                        operations.pop()
                    else:
                        operations[-1][1] -= 1
                coeff_a = a
                coeff_b = b
                coeff_c = c
                current_matrix = Matrix([[1, 0], [0, 1]])
                for op_name, count in operations:
                    match op_name:
                        case "S⁻¹":
                            M = S**-count
                            # (a, b, c) -> (c, -b, a)
                            old_a, old_b, old_c = coeff_a, coeff_b, coeff_c
                            coeff_a = old_c
                            coeff_b = -old_b
                            coeff_c = old_a
                        case "S":
                            M = S**count
                            # (a, b, c) -> (c, -b, a)
                            old_a, old_b, old_c = coeff_a, coeff_b, coeff_c
                            coeff_a = old_c
                            coeff_b = -old_b
                            coeff_c = old_a
                        case "T⁻¹":
                            M = T**-count
                            # (a, b, c) -> (a, b - 2a, a - b + c)
                            old_a, old_b, old_c = coeff_a, coeff_b, coeff_c
                            coeff_a = old_a
                            coeff_b = old_b - 2*old_a
                            coeff_c = old_a - old_b + old_c
                        case "T":
                            M = T**count
                            # (a, b, c) -> (a, b + 2a, a + b + c)
                            old_a, old_b, old_c = coeff_a, coeff_b, coeff_c
                            coeff_a = old_a
                            coeff_b = old_b + 2*old_a
                            coeff_c = old_a + old_b + old_c
                    current_matrix = M @ current_matrix

    op_str = ""
    for i, (op_name, count) in enumerate(operations):
        match op_name:
            case "S⁻¹":
                op_prefix = "S⁻"
            case "S":
                op_prefix = "S"
            case "T⁻¹":
                op_prefix = "T⁻"
            case "T":
                op_prefix = "T"
        if count == 1 and op_name in ("S", "T"):
            op_name = op_prefix
        else:
            digits = str(count)
            power_conv = "".join(powers[int(c)] for c in digits)
            op_name = op_prefix + power_conv
        if i != 0:
            op_str = " " + op_str
        op_str = op_name + op_str
    if not operations:
        op_str = "I"
    #print(op_str)

    dim = screen.get_rect()
    w, h = dim.w, dim.h

    screen.fill(pygame.Color("black"))

    scale = h/4
    origin_x = w/2
    origin_y = h/2
    pygame.draw.line(screen, (100, 100, 100),
                     (origin_x, 0), (origin_x, h), 2)
    pygame.draw.line(screen, (100, 100, 100),
                     (0, origin_y), (w, origin_y), 2)

    origin = Matrix([origin_x, origin_y])
    # Note: y axis is flipped in pygame
    scalem = Matrix([[scale, 0], [0, -scale]])

    # red: (0, 0) -> (1, 0)
    x1, y1 = scalem*(current_matrix @ Matrix([0, 0])) + origin
    x2, y2 = scalem*(current_matrix @ Matrix([1, 0])) + origin
    pygame.draw.line(screen, (255, 0, 0),
                     (int(x1), int(y1)), (int(x2), int(y2)), 2)

    # green: (1, 0) -> (1, 1)
    x1, y1 = scalem*(current_matrix @ Matrix([1, 0])) + origin
    x2, y2 = scalem*(current_matrix @ Matrix([1, 1])) + origin
    pygame.draw.line(screen, (0, 255, 0),
                     (int(x1), int(y1)), (int(x2), int(y2)), 2)

    # blue: (1, 1) -> (0, 1)
    x1, y1 = scalem*(current_matrix @ Matrix([1, 1])) + origin
    x2, y2 = scalem*(current_matrix @ Matrix([0, 1])) + origin
    pygame.draw.line(screen, (0, 0, 255),
                     (int(x1), int(y1)), (int(x2), int(y2)), 2)

    # purple: (0, 1) -> (0, 0)
    x1, y1 = scalem*(current_matrix @ Matrix([0, 1])) + origin
    x2, y2 = scalem*(current_matrix @ Matrix([0, 0])) + origin
    pygame.draw.line(screen, (255, 0, 255),
                     (int(x1), int(y1)), (int(x2), int(y2)), 2)

    text = font.render(f"{op_str}", True, (255, 255, 255))
    screen.blit(text, (100, 100))
    p, q = current_matrix[0], current_matrix[1]
    text = font.render(f"({p} {q})", True, (255, 255, 255))
    screen.blit(text, (w - 400, 100))
    r, s = current_matrix[2], current_matrix[3]
    text = font.render(f"({r} {s})", True, (255, 255, 255))
    screen.blit(text, (w - 400, 180))

    form_symbolic = f"({coeff_a}, {coeff_b}, {coeff_c})"
    form_symbolic = form_symbolic.replace("*", " ")
    text = font.render(form_symbolic, True, (255, 255, 255))
    screen.blit(text, (w - text.get_rect().w - 100, 300))

    eval_a = coeff_a.subs({a: value_a, b: value_b, c: value_c})
    eval_b = coeff_b.subs({a: value_a, b: value_b, c: value_c})
    eval_c = coeff_c.subs({a: value_a, b: value_b, c: value_c})
    form_eval = f"({eval_a}, {eval_b}, {eval_c})"
    text = font.render(form_eval, True, (255, 255, 255))
    screen.blit(text, (w - text.get_rect().w - 100, 380))

    pygame.display.flip()
    time.sleep(0.1)

