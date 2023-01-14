def fieldify(F, g):
    X = F.gens()[0]
    return sum(F(b)*X^i for b, i in g.coefficients())

def find_prime_ideals(g_X, p):
    assert is_prime(p)

    F.<X> = GF(p)[]
    # Convert to this field
    g_X = fieldify(F, g_X)

    K.<γ> = F.quo(g_X)

    ideals = []
    factors = factor(g_X)
    if len(factors) == 1 and factors[0][1] == 1:
        return [f"⟨{p}⟩"]
    for g_X, ramification in factor(g_X):
        g_γ = g_X(γ)
        if ramification > 1:
            ideals.append(f"⟨{p}, {g_γ}⟩^{ramification}")
        else:
            ideals.append(f"⟨{p}, {g_γ}⟩")
        #ideals.append((g_X(γ), ramification))

    return ideals

var("x")

print("K = ℚ( √[3](2) )")
print("⟨5⟩  ℤ_K =", " ".join(find_prime_ideals(x^3 - 2, 5)))
print("⟨7⟩  ℤ_K =", " ".join(find_prime_ideals(x^3 - 2, 7)))
print("⟨31⟩ ℤ_K =", " ".join(find_prime_ideals(x^3 - 2, 31)))
print()

F.<X> = GF(5)[]
K.<γ> = F.quo(X^3 - 2)
assert (γ + 2)*(γ^2 + 3*γ + 4) == 0
F.<X> = GF(31)[]
K.<γ> = F.quo(X^3 - 2)
assert (γ + 11)*(γ + 24)*(γ + 27) == 0

K.<a> = NumberField(x^2 + 2)
# Δ = (γ1 - γ2)^2 (γ1 - γ3)^2 (γ2 - γ3)^2
γ1 = sqrt(-2)
γ2 = -sqrt(-2)
D_K = (γ1 - γ2)^2
assert D_K == K.discriminant()
print("K = ℚ( √(-2) )")
print(f"D_K = {D_K}")
print("⟨2⟩ ℤ_K =", " ".join(find_prime_ideals(x^2 + 2, 2)))
print()

print("-------------------")

def is_reducible(f):
    R.<X> = ZZ[]
    f = fieldify(R, f)
    ramified_factors = sum(n for _, n in factor(f))
    assert ramified_factors > 0
    return ramified_factors > 1

for i in range(4):
    # Now create a random quadratic field
    # Polynomial must be irreducible
    while True:
        A, B = [ZZ.random_element(0, 20) for _ in range(2)]
        f = x^2 + A*x + B
        if is_reducible(f):
            # Try again since this poly is not irreducible
            continue

        K.<a> = NumberField(f)
        break

    # Δ = (γ1 - γ2)^2 (γ1 - γ3)^2 (γ2 - γ3)^2
    γ1, γ2 = [sol.rhs() for sol in f.solve(x)]
    D_K = (γ1 - γ2)^2
    #assert D_K == K.discriminant()
    print(f"γ^2 + {A} γ + {B} = 0")
    print("K = ℚ(γ)")
    print(f"D_K = {D_K} or {K.discriminant()}")
    for p, _ in factor(int(D_K)):
        print(f"⟨{p}⟩ ℤ_K =", " ".join(find_prime_ideals(f, p)))
    print()

