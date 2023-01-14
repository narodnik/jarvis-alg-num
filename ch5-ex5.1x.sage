def find_prime_ideals(p):
    assert is_prime(p)
    F.<X> = GF(p)[]
    K.<γ> = F.quo(X^3 - 2)
    ideals = []
    if len(factor(X^3 - 2)) == 1:
        return [f"⟨{p}⟩"]
    for g_X, ramification in factor(X^3 - 2):
        g_γ = g_X(γ)
        if ramification > 1:
            ideals.append(f"⟨{p}, {g_γ}⟩^{ramification}")
        else:
            ideals.append(f"⟨{p}, {g_γ}⟩")
        #ideals.append((g_X(γ), ramification))
    return ideals

print("⟨5⟩  =", " ".join(find_prime_ideals(5)))
print("⟨7⟩  =", " ".join(find_prime_ideals(7)))
print("⟨31⟩ =", " ".join(find_prime_ideals(31)))

F.<X> = GF(5)[]
K.<γ> = F.quo(X^3 - 2)
assert (γ + 2)*(γ^2 + 3*γ + 4) == 0
F.<X> = GF(31)[]
K.<γ> = F.quo(X^3 - 2)
assert (γ + 11)*(γ + 24)*(γ + 27) == 0

