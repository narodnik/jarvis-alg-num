import os

unicode_table = {
    "α": "\\alpha",
    "ά": "{\\alpha'}",
    "ω": "\\omega",
}

def asciify(latex):
    ascii_latex = ""
    for char in latex:
        if char in unicode_table:
            ascii_latex += unicode_table[char]
        else:
            ascii_latex += char
    return ascii_latex

def render_latex(latex):
    latex = asciify(latex)
    os.system(f'latex2sixel "\\${latex}\\$"')

# Plot lattices
# nth degree polynomials

