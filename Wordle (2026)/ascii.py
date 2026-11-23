import os

# Enables ANSI colors in Windows Command Prompt / PowerShell
os.system("")

# Color presets (Background + Text)
YELLOW = "\033[103m\033[30m"  # Bright yellow bg, black text
GOLD = "\033[43m\033[30m"  # Standard yellow bg, black text
CYAN = "\033[106m\033[30m"  # Bright cyan bg, black text
GREEN = "\033[102m\033[30m"  # Bright green bg, black text
RESET = "\033[0m"

import os

# Enables ANSI colors in Windows Command Prompt / PowerShell
os.system("")

def colorize(letter_art, color=YELLOW):
  lines = letter_art.split("\n")
  colored_lines = []
  for line in lines:
    # Only color the inside of the box (lines starting with │)
    if line.startswith("│") and line.endswith("│"):
      inner = line[1:-1]
      colored_lines.append(f"│{color}{inner}{RESET}│")
    else:
      colored_lines.append(line)
  return "\n".join(colored_lines)





a = """\
┌────────────────┐
│       █        │
│      ███       │
│     █  ██      │
│    ▄▀▀▀▀█▄     │
│   ▄█▄  ▄██▄    │
└────────────────┘"""

b = """\
┌────────────────┐
│    ▀██▀▀█▄     │
│     ██   ██    │
│     ██▀▀▀█▄    │
│     ██   ██    │
│    ▄██▄▄▄█▀    │
└────────────────┘"""

c = """\
┌────────────────┐
│    ▄▄█▀▀▀▄█    │
│   ▄█▀     ▀    │
│   ██           │
│   ▀█▄     ▄    │
│    ▀▀█▄▄▄▄▀    │
└────────────────┘"""

d = """\
┌────────────────┐
│    ▀██▀▀█▄     │
│     ██   ██    │
│     ██   ██    │
│     ██   ██    │
│    ▄██▄▄▄█▀    │
└────────────────┘"""

e = """\
┌────────────────┐
│   ▀██▀▀▀▀█     │
│    ██  ▄       │
│    ██▀▀█       │
│    ██          │
│   ▄██▄▄▄▄▄█    │
└────────────────┘"""

f = """\
┌────────────────┐
│    ▀██▀▀▀▀█    │
│     ██  ▄      │
│     ██▀▀█      │
│     ██         │
│    ▄██▄        │
└────────────────┘"""

g = """\
┌────────────────┐
│    ▄▄█▀▀▀▄█    │
│   ▄█▀     ▀    │
│   ██   ▄▄▄▄    │
│   ▀█▄    ██    │
│    ▀▀█▄▄▄▀█    │
└────────────────┘"""

h = """\
┌────────────────┐
│   ▀██▀  ▀██▀   │
│    ██    ██    │
│    ██▀▀▀▀██    │
│    ██    ██    │
│   ▄██▄  ▄██▄   │
└────────────────┘"""

i = """\
┌────────────────┐
│      ▀██▀      │
│       ██       │
│       ██       │
│       ██       │
│      ▄██▄      │
└────────────────┘"""

j = """\
┌────────────────┐
│       ▀██▀     │
│        ██      │
│        ██      │
│        ██      │
│    ██ ▄█▀      │
└────────────────┘"""

k = """\
┌────────────────┐
│    ▀██▀  █▀    │
│     ██ ▄▀      │
│     ██▀█▄      │
│     ██  ██     │
│    ▄██▄ ██▄    │
└────────────────┘"""

l = """\
┌────────────────┐
│   ▀██▀         │
│    ██          │
│    ██          │
│    ██     ▄    │
│   ▄██▄▄▄▄▄█    │
└────────────────┘"""

m = """\
┌────────────────┐
│   ▀██   ██▀    │
│    ███ ███     │
│    █▀█▄▀██     │
│    █ ▀█▀ ██    │
│   ▄█▄ █ ▄██▄   │
└────────────────┘"""

n = """\
┌────────────────┐
│   ▀█▄   ▀█▀    │
│    █▀█   █     │
│    █ ▀█▄ █     │
│    █   ███     │
│   ▄██▄  ▄█▄    │
└────────────────┘"""

o = """\
┌────────────────┐
│    ▄▄█▀▀██     │
│   ▄█▀    ██    │
│   ██     ██    │
│   ▀█▄    ██    │
│    ▀▀█▄▄▄█▀    │
└────────────────┘"""

p = """\
┌────────────────┐
│    ▀██▀▀█▄     │
│     ██   ██    │
│     ██▄▄▄█▀    │
│     ██         │
│    ▄██▄        │
└────────────────┘"""

q = """\
┌────────────────┐
│    ▄▄█▀▀██     │
│   ▄█▀    ██    │
│   ██     ██    │
│   ▀█▄ ▄▀ ▀█    │
│    ▀▀█▄▄▄▀█▄   │
└────────────────┘"""

r = """\
┌────────────────┐
│   ▀██▀▀█▄      │
│    ██   ██     │
│    ██▀▀█▀      │
│    ██  ▀█▄     │
│   ▄██▄  ▄██▄   │
└────────────────┘"""

s = """\
┌────────────────┐
│     ▄█▀▀▀▄█    │
│    ██▄▄  ▀     │
│     ▀▀███▄     │
│    ▄     ██    │
│    █▀▄▄▄▄█▀    │
└────────────────┘"""

t = """\
┌────────────────┐
│    █▀▀██▀▀█    │
│    ▀  ██  ▀    │
│       ██       │
│       ██       │
│      ▄██▄      │
└────────────────┘"""

u = """\
┌────────────────┐
│   ▀██▀  ▀█▀    │
│    ██    █     │
│    ██    █     │
│    ██    █     │
│    ▀█▄▄▀       │
└────────────────┘"""

v = """\
┌────────────────┐
│   ▀██▀  ▀█▀    │
│    ▀█▄  ▄▀     │
│     ██  █      │
│      ███       │
│       █        │
└────────────────┘"""

w = """\
┌────────────────┐
│▀██   ▀██▀  ▀█▀ │
│ ▀█▄ ▄▀ ▀█▄ ▄▀  │
│  ██ █   ██ █   │
│   ███    ███   │
│    █      █    │
└────────────────┘"""

x = """\
┌────────────────┐
│   ▀██▀  ▀█▀    │
│    ▀█▄ ▄▀      │
│      ██        │
│    ▄▀ ▀█▄      │
│   ▄██▄ ▄██▄    │
└────────────────┘"""

y = """\
┌────────────────┐
│   ▀██▀  ▀█▀    │
│    ▀█▄ ▄▀      │
│      ██        │
│      ██        │
│     ▄██▄       │
└────────────────┘"""

z = """\
┌────────────────┐
│   █▀▀▀▀▀██     │
│   ▀    ▄█▀     │
│      ██        │
│    ▄█▀   ▄     │
│   ██▄▄▄▄▄▄█    │
└────────────────┘"""



space = """\






      """



ascii_map = {
    "a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g,
    "h": h, "i": i, "j": j, "k": k, "l": l, "m": m, "n": n,
    "o": o, "p": p, "q": q, "r": r, "s": s, "t": t, "u": u,
    "v": v, "w": w, "x": x, "y": y, "z": z
}



ay = colorize(a, YELLOW)
by = colorize(b, YELLOW)
cy = colorize(c, YELLOW)
dy = colorize(d, YELLOW)
ey = colorize(e, YELLOW)
fy = colorize(f, YELLOW)
gy = colorize(g, YELLOW)
hy = colorize(h, YELLOW)
iy = colorize(i, YELLOW)
jy = colorize(j, YELLOW)
ky = colorize(k, YELLOW)
ly = colorize(l, YELLOW)
my = colorize(m, YELLOW)
ny = colorize(n, YELLOW)
oy = colorize(o, YELLOW)
py = colorize(p, YELLOW)
qy = colorize(q, YELLOW)
ry = colorize(r, YELLOW)
sy = colorize(s, YELLOW)
ty = colorize(t, YELLOW)
uy = colorize(u, YELLOW)
vy = colorize(v, YELLOW)
wy = colorize(w, YELLOW)
xy = colorize(x, YELLOW)
yy = colorize(y, YELLOW)
zy = colorize(z, YELLOW)

ascii_map_y = {
    "a": ay, "b": by, "c": cy, "d": dy, "e": ey, "f": fy, "g": gy,
    "h": hy, "i": iy, "j": jy, "k": ky, "l": ly, "m": my, "n": ny,
    "o": oy, "p": py, "q": qy, "r": ry, "s": sy, "t": ty, "u": uy,
    "v": vy, "w": wy, "x": xy, "y": yy, "z": zy
}

ag = colorize(a, GREEN)
bg = colorize(b, GREEN)
cg = colorize(c, GREEN)
dg = colorize(d, GREEN)
eg = colorize(e, GREEN)
fg = colorize(f, GREEN)
gg = colorize(g, GREEN)
hg = colorize(h, GREEN)
ig = colorize(i, GREEN)
jg = colorize(j, GREEN)
kg = colorize(k, GREEN)
lg = colorize(l, GREEN)
mg = colorize(m, GREEN)
ng = colorize(n, GREEN)
og = colorize(o, GREEN)
pg = colorize(p, GREEN)
qg = colorize(q, GREEN)
rg = colorize(r, GREEN)
sg = colorize(s, GREEN)
tg = colorize(t, GREEN)
ug = colorize(u, GREEN)
vg = colorize(v, GREEN)
wg = colorize(w, GREEN)
xg = colorize(x, GREEN)
yg = colorize(y, GREEN)
zg = colorize(z, GREEN)

ascii_map_g = {
    "a": ag, "b": bg, "c": cg, "d": dg, "e": eg, "f": fg, "g": gg,
    "h": hg, "i": ig, "j": jg, "k": kg, "l": lg, "m": mg, "n": ng,
    "o": og, "p": pg, "q": qg, "r": rg, "s": sg, "t": tg, "u": ug,
    "v": vg, "w": wg, "x": xg, "y": yg, "z": zg
}








