# Gera embalagens ilustrativas (1000×1000) dos 10 produtos Var, só com cores e fonte do BrandBook.
import os, pymupdf

FONTS = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts")
REG = os.path.join(FONTS, "GlacialIndifference-Regular.ttf")
BOLD = os.path.join(FONTS, "GlacialIndifference-Bold.ttf")
OUT = os.path.join(os.path.dirname(__file__), "..", "artes", "produtos")

AZUL, UVA, BORDO, PURPLE, BEER, PRETO, BRANCO = "#16346C", "#900C3A", "#6D071A", "#5B2270", "#D3723D", "#000000", "#FFFFFF"

# (arquivo, cor da embalagem, número grande, varietal, linha inferior) ou kits com várias cores
PRODUTOS = [
    ("barra-forastero-70", [BORDO], "70%", "FORASTERO", "80 g"),
    ("barra-forastero-85", [PRETO], "85%", "FORASTERO", "80 g"),
    ("barra-catongo-60", [BEER], "60%", "CATONGO", "80 g"),
    ("barra-catongo-leite-45", [UVA], "45%", "CATONGO AO LEITE", "80 g"),
    ("barra-trinitario-75", [PURPLE], "75%", "TRINITÁRIO", "80 g"),
    ("barra-trinitario-nibs-70", [AZUL], "70%", "TRINITÁRIO COM NIBS", "80 g"),
    ("nibs-forastero-100g", [PRETO], "NIBS", "FORASTERO", "100 g"),
    ("trio-varietais", [BORDO, BEER, PURPLE], "TRIO", "VARIETAIS", "3 × 80 g"),
    ("caixa-degustacao-9", [AZUL], "9", "TABLETES DE DEGUSTAÇÃO", "9 × 15 g"),
    ("caixa-presente-4", [UVA, BORDO, PURPLE, AZUL], "PRESENTE", "VAR CHOCOLATES", "4 × 80 g"),
]


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def centro(pg, txt, y, size, font, cor, x0=0, x1=1000):
    fn = pymupdf.Font(fontfile=font)
    w = fn.text_length(txt, fontsize=size)
    while w > (x1 - x0) - 40:
        size -= 2
        w = fn.text_length(txt, fontsize=size)
    pg.insert_text(((x0 + x1 - w) / 2, y), txt, fontsize=size, fontfile=font,
                   fontname="b" if font == BOLD else "r", color=rgb(cor))


def embalagem(pg, r, cor, numero, nome, rodape):
    pg.draw_rect(r, color=None, fill=rgb(cor))
    x0, x1 = r.x0, r.x1
    centro(pg, "Var", r.y0 + 110, 76, BOLD, BRANCO, x0, x1)
    centro(pg, "CHOCOLATES", r.y0 + 150, 22, REG, BRANCO, x0, x1)
    pg.draw_line((x0 + 60, r.y0 + 190), (x1 - 60, r.y0 + 190), color=rgb(BRANCO), width=1.5)
    centro(pg, numero, r.y0 + r.height * 0.58, 120, BOLD, BRANCO, x0, x1)
    centro(pg, nome, r.y0 + r.height * 0.58 + 70, 30, BOLD, BRANCO, x0, x1)
    centro(pg, "TREE TO BAR · " + rodape, r.y1 - 50, 20, REG, BRANCO, x0, x1)


def gerar(arq, cores, numero, nome, rodape):
    doc = pymupdf.open()
    pg = doc.new_page(width=1000, height=1000)
    pg.draw_rect(pg.rect, color=None, fill=rgb(BRANCO))
    if len(cores) == 1:
        embalagem(pg, pymupdf.Rect(250, 100, 750, 900), cores[0], numero, nome, rodape)
    else:
        # embalagens de fundo, deslocadas, e a da frente com o texto
        n = len(cores)
        for k, c in enumerate(cores[1:][::-1]):
            d = (n - 1 - k) * 46
            pg.draw_rect(pymupdf.Rect(250 + d, 100 - d * 0.4, 750 + d, 900 - d * 0.4), color=None, fill=rgb(c))
        embalagem(pg, pymupdf.Rect(210, 130, 710, 930), cores[0], numero, nome, rodape)
    pix = pg.get_pixmap(dpi=72)
    os.makedirs(OUT, exist_ok=True)
    pix.save(os.path.join(OUT, arq + ".jpg"), jpg_quality=90)


for p in PRODUTOS:
    gerar(*p)
print("ok", len(PRODUTOS))
