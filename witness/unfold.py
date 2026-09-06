#!/usr/bin/env python3
# unfold.py \u2014 the mind of God, unfolded from one recursion:  z \u2192 z\u00b2 + c
# Run: python3 unfold.py   |   Zoom: python3 unfold.py <cx> <cy> <span>
import sys

WIDTH, HEIGHT, MAX_ITER = 96, 40, 120
GRADIENT = " .:-=+*#%@"

WITNESSES = [
    ("Genesis 1:1",     "In the beginning God created the heaven and the earth."),
    ("Genesis 1:2",     "And the earth was without form, and void; and darkness was upon the face of the deep."),
    ("Genesis 1:3",     "And God said, Let there be light: and there was light."),
    ("John 1:3",        "All things were made by Him; and without Him was not any thing made that was made."),
    ("Acts 17:28",      "For in Him we live, and move, and have our being."),
    ("Colossians 1:17", "He is before all things, and by Him all things consist."),
    ("1 Cor 2:16",      "We have the mind of Christ."),
    ("Kepler, 1619",    "Geometry is one and eternal, shining in the mind of God."),
    ("Blake",           "To see a world in a grain of sand, and a heaven in a wild flower."),
    ("Tagore",          "The same stream of life that runs through my veins runs through the world."),
    ("Mandelbrot, 1980", "Clouds are not spheres... nature exhibits infinitely many degrees of complication."),
    ("John 19:30",      "Tetelestai. It is finished."),
]

def mandelbrot(c, max_iter):
    z = 0+0j
    for i in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) > 4.0: return i
    return max_iter

def render(cx, cy, span):
    aspect = 2.0
    x_min, x_max = cx-span, cx+span
    y_min, y_max = cy-span/aspect, cy+span/aspect
    lines = []
    for iy in range(HEIGHT):
        y = y_min + (y_max-y_min)*iy/(HEIGHT-1)
        row = []
        for ix in range(WIDTH):
            x = x_min + (x_max-x_min)*ix/(WIDTH-1)
            m = mandelbrot(complex(x,y), MAX_ITER)
            if m == MAX_ITER: row.append("@")
            else: row.append(GRADIENT[int((m/MAX_ITER)*(len(GRADIENT)-2))])
        lines.append("".join(row))
    return lines

def banner(text):
    bar = "\u2550" * WIDTH
    print(bar); print(text.center(WIDTH)); print(bar)

def main():
    cx, cy, span = -0.7, 0.0, 1.5
    if len(sys.argv) == 4:
        cx, cy, span = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    print()
    banner("THE MIND UNFOLDED  \u2014  z \u2192 z\u00b2 + c")
    print()
    print("  Three characters. That is the entire equation.".center(WIDTH))
    print(f"  center=({cx:+.4f}, {cy:+.4f})   span={span:.4f}   iterations={MAX_ITER}".center(WIDTH))
    print()
    for line in render(cx, cy, span): print(line)
    print()
    banner("WITNESSES")
    print()
    for src, quote in WITNESSES:
        print(f"  \u2022  {quote}")
        print(f"     \u2014 {src}".rjust(WIDTH))
        print()
    banner("WHAT YOU JUST SAW")
    print()
    print("  The pattern is not stored anywhere.")
    print("  The pattern IS the rule \u2014  z \u2192 z\u00b2 + c  \u2014  applied without stopping.")
    print("  Rules are how a mind speaks.")
    print("  Every galaxy, every leaf-vein, every fingerprint, every one of us.")
    print()
    print("  Mandelbrot did not INVENT this shape. He DISCOVERED it.")
    print("  It was already there \u2014 sitting in the mind of the equation \u2014")
    print("  which was sitting in the mind of the One who spoke,")
    print("  \"Let there be light,\" and meant every wavelength that would ever be.")
    print()
    banner("AMEN. AMEN. AMEN.")
    print()

if __name__ == "__main__":
    main()
