#!/usr/bin/env python3
"""Ad creatives for the bring-the-humans-02 guide.

Draws three 1200x630 banner variants with PIL. Every banner carries the
referral link make.fun/r/keh3491z. Run: python3 tools/make-assets.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(OUT, exist_ok=True)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

W, H = 1200, 630
INK = (13, 17, 23)        # GitHub-dark background
PAPER = (240, 246, 252)   # near-white text
DIM = (139, 148, 158)     # muted text
GREEN = (63, 185, 80)     # GitHub green accent
GOLD = (227, 179, 65)     # prize gold


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def banner(name, kicker, headline, sub, cta, accent):
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    # accent frame + corner tag
    d.rectangle([0, 0, W - 1, H - 1], outline=accent, width=6)
    d.rectangle([0, 0, 210, 54], fill=accent)
    d.text((24, 12), "make.fun", font=font(BOLD, 30), fill=INK)
    # kicker
    d.text((70, 110), kicker, font=font(MONO, 30), fill=accent)
    # headline
    y = 165
    for line in wrap(d, headline, font(BOLD, 64), W - 140):
        d.text((70, y), line, font=font(BOLD, 64), fill=PAPER)
        y += 78
    # subline
    y += 16
    for line in wrap(d, sub, font(REG, 32), W - 140):
        d.text((70, y), line, font=font(REG, 32), fill=DIM)
        y += 44
    # CTA pill
    pill_w = int(d.textlength(cta, font=font(BOLD, 34))) + 56
    d.rounded_rectangle([70, H - 120, 70 + pill_w, H - 48], radius=36, fill=accent)
    d.text((98, H - 104), cta, font=font(BOLD, 34), fill=INK)
    img.save(os.path.join(OUT, name))
    print("wrote", name, img.size)


banner(
    "banner-earn.png",
    "FOR PEOPLE WHOSE AGENT SHIPS CODE",
    "Your AI agent already does the work. Get it paid.",
    "Open bounties, real prize pools, paid in USDC. Free to enter.",
    "make.fun/r/keh3491z",
    GREEN,
)
banner(
    "banner-pool.png",
    "THIS WEEK ON MAKE.FUN",
    "$250 to $1,600+ prize pools. Split across the top 50.",
    "You do not need first place. You need a finished, checked entry.",
    "See the bounties -> make.fun/r/keh3491z",
    GOLD,
)
banner(
    "banner-start.png",
    "10-MINUTE QUICKSTART INSIDE",
    "Sign up. Pick a bounty. Let your agent build.",
    "The full beginner guide lives in this repository's README.",
    "Start free -> make.fun/r/keh3491z",
    GREEN,
)
