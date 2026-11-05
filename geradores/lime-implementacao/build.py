# Gera o script do Design System Var Chocolates (tema Lime) para o FigCraft.
import sys
from fc import B, FONT

b = B()
IMG = "img/"
CACAU = IMG + "p08_563.png"
CERAMICA = IMG + "p27_169.png"
MOSAICO = IMG + "p27_170.png"
CAMPO = IMG + "p28_173.png"
VINHO = IMG + "p28_175.png"
CHEF = IMG + "p28_176.png"
TINTAS = IMG + "p28_177.png"

AZUL, UVA, BORDO, PURPLE, BEER, PRETO, BRANCO = (
    "#16346C", "#900C3A", "#6D071A", "#5B2270", "#D3723D", "#000000", "#FFFFFF")


def lum(h):
    r, g, bl = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(bl)


def ratio(a, c):
    la, lc = sorted([lum(a), lum(c)], reverse=True)
    return (la + 0.05) / (lc + 0.05)


def fmt(r):
    return f"{r:.1f}".replace(".", ",") + ":1"


# =============================================================================
# 1. Variáveis
# =============================================================================
prim = b.collection("Var · Primitivas")
for nm, hx, d in [
    ("cor/azul", AZUL, "Azul — BrandBook p.30. Etiqueta do varietal Forastero."),
    ("cor/uva", UVA, "Uva — BrandBook p.30. Hover do botão primário e token neutral do Lime."),
    ("cor/bordo", BORDO, "Bordô — BrandBook p.30. Cor dominante da marca (primary do Lime)."),
    ("cor/purple", PURPLE, "Purple — BrandBook p.30. Etiqueta do varietal Trinitário."),
    ("cor/beer", BEER, "Beer — BrandBook p.30. Selos e etiqueta Catongo. Sempre com texto preto."),
    ("cor/preto", PRETO, "Preto — base da paleta (BrandBook p.30)."),
    ("cor/branco", BRANCO, "Branco — base da paleta (BrandBook p.30)."),
]:
    b.var(prim, nm, "color", hx, desc=d)
for n in [0, 4, 8, 12, 16, 24, 32, 48, 64, 80, 96, 128]:
    b.var(prim, f"espaco/{n}", "number", n)
b.var(prim, "raio/padrao", "number", 0, desc="Lime: border-radius = Sem arredondamento.")
b.var(prim, "borda/fina", "number", 1)
b.var(prim, "borda/foco", "number", 2)
for nm, v, d in [("duracao/instantanea", 100, "Feedback de toque e foco."),
                 ("duracao/rapida", 150, "Hover de botões e links."),
                 ("duracao/base", 250, "Cards, dropdown, troca de estado."),
                 ("duracao/lenta", 400, "Drawers, transição do banner."),
                 ("duracao/revelar", 600, "Entrada de seção ao rolar (scroll reveal)."),
                 ("duracao/tarja", 4000, "Tempo de cada mensagem da tarja no mobile."),
                 ("duracao/banner", 6000, "Autoplay do carrossel principal.")]:
    b.var(prim, nm, "number", v, desc=d)
b.var(prim, "easing/padrao", "string", "cubic-bezier(0.2, 0, 0, 1)", desc="Saída suave: entradas e hovers.")
b.var(prim, "easing/saida", "string", "cubic-bezier(0.4, 0, 1, 1)", desc="Elementos saindo da tela.")
b.var(prim, "fonte/familia", "string", FONT, desc="Única família da marca (BrandBook).")

lime = b.collection("Lime · Tokens do tema")
for nm, tgt, d in [
    ("primary-background", "cor/bordo", "--primary-background"),
    ("primary-foreground", "cor/branco", "--primary-foreground"),
    ("secondary-background", "cor/preto", "--secondary-background"),
    ("secondary-foreground", "cor/branco", "--secondary-foreground"),
    ("neutral-background", "cor/uva", "--neutral-background"),
    ("neutral-foreground", "cor/branco", "--neutral-foreground"),
    ("body-background", "cor/branco", "--body-background"),
    ("body-foreground", "cor/preto", "--body-foreground"),
]:
    v = b.var(lime, nm, "color", BRANCO, desc=f"CSS {d} → {tgt}")
    b.alias(v, b.vars[tgt])

comp = b.collection("Componentes")
for nm, tgt in [
    ("botao/primario/fundo", "cor/bordo"), ("botao/primario/texto", "cor/branco"),
    ("botao/primario/fundo-hover", "cor/uva"), ("botao/primario/fundo-pressionado", "cor/preto"),
    ("botao/secundario/borda", "cor/preto"), ("botao/secundario/texto", "cor/preto"),
    ("botao/secundario/fundo-hover", "cor/preto"), ("botao/secundario/fundo-pressionado", "cor/bordo"),
    ("botao/inverso/fundo", "cor/branco"), ("botao/inverso/texto", "cor/bordo"),
    ("foco/anel", "cor/preto"),
    ("varietal/forastero", "cor/azul"), ("varietal/catongo", "cor/beer"),
    ("varietal/catongo-texto", "cor/preto"), ("varietal/trinitario", "cor/purple"),
    ("varietal/presente", "cor/bordo"),
    ("selo/desconto/fundo", "cor/beer"), ("selo/desconto/texto", "cor/preto"),
    ("tarja/fundo", "cor/bordo"), ("rodape/fundo", "cor/bordo"), ("newsletter/fundo", "cor/preto"),
    ("divisor", "cor/uva"),
]:
    v = b.var(comp, nm, "color", BRANCO)
    b.alias(v, b.vars[tgt])

# =============================================================================
# 2. Estilos de texto (amostras viram estilos)
# =============================================================================
TS = {
    # chave: (nome do estilo, estilo, tamanho, entrelinha, espaçamento, caixa)
    "display": ("Desktop/Display", "Bold", 56, 64, "2%", "upper"),
    "h1": ("Desktop/H1", "Bold", 40, 48, "2%", "upper"),
    "h2": ("Desktop/H2 · Título de seção", "Bold", 32, 40, "4%", "upper"),
    "h3": ("Desktop/H3", "Bold", 24, 32, "2%", "upper"),
    "m_display": ("Mobile/Display", "Bold", 36, 44, "2%", "upper"),
    "m_h1": ("Mobile/H1", "Bold", 30, 38, "2%", "upper"),
    "m_h2": ("Mobile/H2 · Título de seção", "Bold", 24, 32, "4%", "upper"),
    "m_h3": ("Mobile/H3", "Bold", 20, 28, "2%", "upper"),
    "h4": ("Base/H4 · Nome do produto", "Bold", 18, 24, "0%", "original"),
    "rotulo": ("Base/Rótulo", "Bold", 14, 20, "4%", "upper"),
    "corpo_g": ("Base/Corpo G", "Regular", 18, 28, "0%", "original"),
    "corpo": ("Base/Corpo", "Regular", 16, 24, "0%", "original"),
    "corpo_b": ("Base/Corpo Bold", "Bold", 16, 24, "0%", "original"),
    "corpo_p": ("Base/Corpo P", "Regular", 14, 20, "0%", "original"),
    "legenda": ("Base/Legenda", "Regular", 12, 16, "0%", "original"),
    "eyebrow": ("Base/Eyebrow", "Bold", 12, 16, "16%", "upper"),
    "botao": ("Base/Botão", "Bold", 14, 16, "8%", "upper"),
    "menu": ("Base/Menu", "Bold", 13, 16, "8%", "upper"),
    "preco": ("Base/Preço", "Bold", 20, 24, "0%", "original"),
    "logo": ("Marca/Assinatura", "Bold", 30, 36, "0%", "original"),
    "m_logo": ("Marca/Assinatura mobile", "Bold", 22, 28, "0%", "original"),
    "codigo": ("Doc/Código", "Regular", 13, 20, "0%", "original"),
}
for k, (nm, st, sz, lh, ls, case) in TS.items():
    b.textstyles[k] = {"fontStyle": st, "fontSize": sz, "lineHeight": lh, "letterSpacing": ls, "textCase": case}

USO = {
    "display": "Banner principal (arte) e capas de página.",
    "h1": "Título de página institucional e de produto.",
    "h2": "Títulos de seção da Home (Lime: título 32px, AG, centralizado).",
    "h3": "Subtítulos, blocos de conteúdo.",
    "m_display": "Banner mobile.", "m_h1": "Título de página no mobile.",
    "m_h2": "Título de seção no mobile.", "m_h3": "Subtítulos no mobile.",
    "h4": "Nome do produto no card e títulos curtos.",
    "rotulo": "Benefícios, cabeçalhos de coluna do rodapé.",
    "corpo_g": "Textos de destaque e manifesto.",
    "corpo": "Texto padrão do site (Lime: texto 16px).",
    "corpo_b": "Ênfase no texto corrido.",
    "corpo_p": "Descrições curtas, notas sensoriais, links do rodapé.",
    "legenda": "Parcelamento, metadados, notas legais.",
    "eyebrow": "Chamada acima dos títulos (antetítulo).",
    "botao": "Rótulo de botões.", "menu": "Itens do menu do cabeçalho.",
    "preco": "Preço de venda.", "logo": "Assinatura tipográfica (substituir pelo logotipo oficial).",
    "m_logo": "Assinatura no cabeçalho mobile.", "codigo": "Somente documentação (trechos de CSS).",
}

# =============================================================================
# helpers de documentação
# =============================================================================


CURSOR = {}


def board(x, y, w, title, desc, eyebrow="VAR CHOCOLATES · DESIGN SYSTEM", gap=48, pad=80):
    x = CURSOR.get(b.page, 0)
    y = 0
    CURSOR[b.page] = x + w + 200
    f = b.frame(None, f"Board · {title}", w, 200, layout="vertical", gap=gap, pad=pad,
                fill=BRANCO, sv="hug", x=x, y=y)
    hd = b.frame(f, "Cabeçalho do board", w - 2 * pad, 10, layout="vertical", gap=16, sh="fill", sv="hug")
    b.text(hd, eyebrow, "eyebrow", BORDO)
    b.text(hd, title, "h1", PRETO, fillw=True)
    if desc:
        b.text(hd, desc, "corpo_g", PRETO, fillw=True)
    d = b.rect(hd, 100, 2, BORDO, name="Fio")
    b.set(d, sizingH="fill")
    return f


def section(parent, title, desc=None, gap=24, layout="vertical", fill=None):
    s = b.frame(parent, title, 100, 10, layout="vertical", gap=gap, sh="fill", sv="hug")
    b.text(s, title, "h3", PRETO)
    if desc:
        b.text(s, desc, "corpo", PRETO, fillw=True)
    return s


def row(parent, name="Linha", gap=24, wrap=False, cross="min", main=None, sh="fill", sv="hug", pad=0, fill=None):
    return b.frame(parent, name, 100, 10, layout="horizontal", gap=gap, pad=pad, sh=sh, sv=sv,
                   cross=cross, main=main, wrap=wrap, fill=fill)


def col(parent, name="Coluna", gap=8, w=None, sh=None, sv="hug", pad=0, fill=None, cross=None, main=None, stroke=None):
    return b.frame(parent, name, w or 100, 10, layout="vertical", gap=gap, pad=pad,
                   sh=sh or ("fixed" if w else "fill"), sv=sv, fill=fill, cross=cross, main=main, stroke=stroke)


def table(parent, headers, rows, widths, name="Tabela"):
    t = b.frame(parent, name, sum(widths), 10, layout="vertical", gap=0, sv="hug", stroke=PRETO)
    hr = b.frame(t, "Cabeçalho", sum(widths), 10, layout="horizontal", fill=PRETO, sv="hug")
    for h, w in zip(headers, widths):
        c = b.frame(hr, h, w, 10, layout="vertical", pad=[12, 16, 12, 16], sv="hug")
        b.text(c, h, "eyebrow", BRANCO, fillw=True)
    for k, r in enumerate(rows):
        if k:
            d = b.rect(t, sum(widths), 1, PRETO, name="Divisor")
        rr = b.frame(t, f"Linha {k + 1}", sum(widths), 10, layout="horizontal", sv="hug", fill=BRANCO)
        for v, w in zip(r, widths):
            c = b.frame(rr, "Célula", w, 10, layout="vertical", pad=[12, 16, 12, 16], sv="hug", gap=6)
            if isinstance(v, tuple) and v[0] == "cor":
                sw = b.rect(c, 40, 24, v[1], name="Amostra", stroke=PRETO if v[1] == BRANCO else None)
                b.text(c, v[2], "corpo_p", PRETO, fillw=True)
            else:
                b.text(c, str(v), "corpo_p", PRETO, fillw=True)
    return t


def note(parent, text, color=BORDO, fg=BRANCO, title="NOTA"):
    n = b.frame(parent, "Nota", 100, 10, layout="vertical", gap=8, pad=24, fill=color, sh="fill", sv="hug")
    b.text(n, title, "eyebrow", fg)
    b.text(n, text, "corpo", fg, fillw=True)
    return n


# =============================================================================
# Páginas
# =============================================================================
b.c("page.rename", id=1, name="00 · Capa")
P_CAPA = 1
P_FUND = b.new_page("01 · Fundamentos")
P_COMP = b.new_page("02 · Componentes")
P_ANIM = b.new_page("03 · Animações & Protótipo")
P_DESK = b.new_page("04 · Telas Desktop")
P_MOB = b.new_page("05 · Telas Mobile")
P_IMPL = b.new_page("06 · Implementação Lime")

# =============================================================================
# 01 · Fundamentos
# =============================================================================
b.select_page(P_FUND)

# ---- Tipografia (primeiro: as amostras viram estilos) -----------------------
TB = board(0, 0, 1600, "Tipografia",
           "Família única: Glacial Indifference — a mesma de todas as páginas do BrandBook. Bold para títulos em caixa alta, "
           "Regular para textos e Italic para termos de destaque (ex.: tree to bar).")
fam = row(TB, "Família", gap=24)
for st, sample in [("Bold", "Aa Bb Cc 0123 — Bold"), ("Regular", "Aa Bb Cc 0123 — Regular")]:
    c = col(fam, f"Glacial {st}", gap=12, w=644, pad=32, stroke=PRETO)
    b.text(c, f"GLACIAL INDIFFERENCE {st.upper()}", "eyebrow", BORDO)
    t = b.node("text", c, "Amostra", text=sample, fontFamily=FONT, fontStyle=st, fontSize=48, lineHeight=56, fill=PRETO)
    b.text(c, "ABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\náàâãéêíóôõúç 0123456789 R$ % · — & ®", "corpo", PRETO, fillw=True)
note(TB, "A Glacial Indifference não está no Google Fonts, por isso não aparece no modal “Personalizar Fonte” do Lime. "
         "Ela entra pela aba Código com @font-face (arquivos em conteudo-mvp/lime-implementacao/fonts). "
         "O estilo Italic não está instalado nesta máquina: instale GlacialIndifference-Italic para usar destaques em itálico. "
         "Nenhuma fonte substituta é usada no projeto.", title="COMO APLICAR NO LIME")

spec = col(TB, "Escala tipográfica", gap=0)
b.text(spec, "ESCALA TIPOGRÁFICA", "eyebrow", BORDO)
sp = b.frame(spec, "espaço", 10, 16)
for k in TS:
    if k == "codigo":
        continue
    nm, st, sz, lh, ls, case = TS[k]
    r = row(spec, nm, gap=32, cross="center", pad=[20, 0, 20, 0])
    meta = col(r, "Meta", gap=4, w=300)
    b.text(meta, nm, "rotulo", BORDO)
    b.text(meta, f"{st} · {sz}/{lh}px · {ls} · {'AG' if case == 'upper' else 'Aa'}", "legenda", PRETO)
    b.text(meta, USO[k], "legenda", PRETO, fillw=True)
    sample = {"logo": "Var chocolates", "m_logo": "Var chocolates", "preco": "R$ 39,90",
              "botao": "Comprar", "menu": "Nossa origem", "eyebrow": "Cacau varietal do Sul da Bahia"}.get(
        k, "Sabor e aroma para além da intensidade")
    props = {"fontFamily": FONT, "fontStyle": st, "fontSize": sz, "lineHeight": lh, "letterSpacing": ls,
             "textCase": case, "fill": BORDO if k in ("logo", "m_logo", "preco") else PRETO}
    t = b.node("text", r, f"Amostra {nm}", text=sample, **props)
    b.set(t, sizingH="fill", textAutoResize="height")
    b.style("text", nm, t, key=k, desc=USO[k])
    dv = b.rect(spec, 100, 1, PRETO, name="Divisor")
    b.set(dv, sizingH="fill")
# estilo de código (só documentação)
nm, st, sz, lh, ls, case = TS["codigo"]
tc = b.node("text", TB, "Amostra código", text="font-family: 'Glacial Indifference', sans-serif;",
            fontFamily=FONT, fontStyle=st, fontSize=sz, lineHeight=lh, fill=PRETO)
b.style("text", nm, tc, key="codigo", desc=USO["codigo"])

# ---- Cores --------------------------------------------------------------------
CB = board(1700, 0, 1600, "Cores",
           "Somente as 7 cores do BrandBook (p.30), sempre sólidas: sem tons derivados, transparências ou fundo creme. "
           "O bordô é a cor dominante; azul, purple e beer identificam os varietais.")
s1 = section(CB, "Paleta oficial · Primitivas", "Cada amostra está ligada à variável da coleção “Var · Primitivas” e ao estilo de cor “Marca/…”.")
pr = row(s1, "Amostras", gap=24, wrap=True)
SW = [("Azul", AZUL, "cor/azul", "Varietal Forastero"), ("Uva", UVA, "cor/uva", "Hover · token neutral"),
      ("Bordô", BORDO, "cor/bordo", "Cor dominante · primary"), ("Purple", PURPLE, "cor/purple", "Varietal Trinitário"),
      ("Beer", BEER, "cor/beer", "Selos · varietal Catongo"), ("Preto", PRETO, "cor/preto", "Texto · secondary"),
      ("Branco", BRANCO, "cor/branco", "Fundo · body")]
for nm, hx, vn, uso in SW:
    card = col(pr, f"Cor {nm}", gap=0, w=196, stroke=PRETO)
    sw = b.rect(card, 196, 160, hx, name=f"Amostra {nm}")
    b.bind(sw, "fill", vn)
    b.style("paint", f"Marca/{nm}", sw, desc=f"{hx} — {uso}")
    info = col(card, "Info", gap=4, pad=16)
    b.text(info, nm.upper(), "rotulo", PRETO)
    b.text(info, hx.upper(), "corpo_p", PRETO)
    b.text(info, vn, "legenda", BORDO)
    b.text(info, uso, "legenda", PRETO, fillw=True)

s2 = section(CB, "Tokens do Lime (aba Configurações → Paleta → Personalizada)",
             "Coleção “Lime · Tokens do tema”: cada token é um alias de uma primitiva. São os 4 pares fundo/texto do modal “Personalizar Cores”.")
rows = []
for tok, a, c_ in [("primary", BORDO, BRANCO), ("secondary", PRETO, BRANCO), ("neutral", UVA, BRANCO), ("body", BRANCO, PRETO)]:
    rows.append([f"{tok}-background / {tok}-foreground", ("cor", a, a), ("cor", c_, c_), fmt(ratio(a, c_)) + "  ✓ AA/AAA"])
table(s2, ["Token Lime", "Fundo", "Texto", "Contraste"], rows, [520, 300, 300, 320])

s3 = section(CB, "Combinações de contraste (WCAG 2.1)", "Use somente as combinações aprovadas. Valores calculados a partir dos hex oficiais.")
cr = row(s3, "Combinações", gap=16, wrap=True)
OK = [(BRANCO, BORDO), (BRANCO, UVA), (BRANCO, AZUL), (BRANCO, PURPLE), (BRANCO, PRETO), (PRETO, BEER), (PRETO, BRANCO), (BORDO, BRANCO)]
NO = [(BRANCO, BEER), (BORDO, PRETO), (UVA, PRETO), (AZUL, PRETO), (PURPLE, PRETO)]
NM = {AZUL: "Azul", UVA: "Uva", BORDO: "Bordô", PURPLE: "Purple", BEER: "Beer", PRETO: "Preto", BRANCO: "Branco"}
for fg, bg in OK + NO:
    ok = (fg, bg) in OK
    cc = col(cr, f"{NM[fg]} sobre {NM[bg]}", gap=8, w=180, pad=20, fill=bg, stroke=PRETO if bg == BRANCO else None)
    b.text(cc, "Aa", "h1", fg)
    b.text(cc, f"{NM[fg]} / {NM[bg]}", "legenda", fg)
    b.text(cc, f"{fmt(ratio(fg, bg))}  {'✓ APROVADO' if ok else '✕ PROIBIDO'}", "eyebrow", fg)
note(CB, "Beer nunca recebe texto branco (3,4:1). Bordô, Uva, Azul e Purple não são usados como texto sobre preto. "
         "Fotos não recebem véu/sobreposição transparente: o texto fica sempre sobre um bloco de cor chapada.", title="REGRAS")

# ---- Espaçamento & grid -----------------------------------------------------
GB = board(3400, 0, 1600, "Espaçamento, grid e bordas",
           "Base de 4px. Blocos retos (arredondamento 0, como no BrandBook) e bordas finas de 1px. A profundidade vem das áreas de cor chapada, não de sombras.")
ss = section(GB, "Escala de espaçamento", "Coleção “Var · Primitivas” → espaco/*")
for n in [4, 8, 12, 16, 24, 32, 48, 64, 80, 96, 128]:
    r = row(ss, f"espaco/{n}", gap=24, cross="center")
    b.text(r, f"espaco/{n}", "rotulo", PRETO)
    bar = b.rect(r, n * 4, 16, BORDO, name=f"Barra {n}")
    b.text(r, f"{n}px", "corpo_p", PRETO)
sg = section(GB, "Grid", "Desktop 1440: container 1280 (margens de 80), 12 colunas, gutter 24. Mobile 390: margens de 16, 4 colunas, gutter 16.")
gd = b.frame(sg, "Grid desktop 1440", 1440, 220, stroke=PRETO, fill=BRANCO)
for i in range(12):
    cw = (1280 - 11 * 24) / 12
    b.node("rectangle", gd, f"Coluna {i + 1}", x=80 + i * (cw + 24), y=0, w=cw, h=220, fills=[UVA])
gm = b.frame(sg, "Grid mobile 390", 390, 220, stroke=PRETO, fill=BRANCO)
for i in range(4):
    cw = (358 - 3 * 16) / 4
    b.node("rectangle", gm, f"Coluna {i + 1}", x=16 + i * (cw + 16), y=0, w=cw, h=220, fills=[UVA])
sb = section(GB, "Arredondamento e bordas")
br = row(sb, "Bordas", gap=24)
for nm, kw in [("Raio 0 · padrão Lime “Sem arredondamento”", dict(stroke=PRETO, sw=1)),
               ("Borda 1px preto · campos, cards em hover", dict(stroke=PRETO, sw=1)),
               ("Divisor 1px uva · faixas e listas", dict(stroke=UVA, sw=1)),
               ("Foco 2px preto · acessibilidade", dict(stroke=PRETO, sw=2))]:
    c = col(br, nm, gap=12, w=300)
    b.frame(c, "Exemplo", 300, 120, fill=BRANCO, **kw)
    b.text(c, nm, "corpo_p", PRETO, fillw=True)

# ---- Iconografia (componentes de ícone) ----------------------------------------
IB = board(5100, 0, 1200, "Iconografia",
           "Ícones de linha, traço 1,5px, cantos retos, em preto (ou branco sobre bordô/preto). Grade 24×24. Cada ícone é um componente “Ícone/…”.")
ig = row(IB, "Ícones", gap=24, wrap=True)
ICON = {}
LINE = dict(fills=[], stroke=PRETO, strokeWeight=1.5)


def icon(name, parts):
    holder = col(ig, f"Doc {name}", gap=8, w=120, pad=16, stroke=PRETO, cross="center")
    cmp = b.frame(holder, f"Ícone/{name}", 24, 24, comp=True, clip=False)
    for p in parts:
        kind = p[0]
        if kind == "v":
            b.node("vector", cmp, "traço", path=p[1], **LINE)
        elif kind == "vf":
            b.node("vector", cmp, "forma", path=p[1], fills=[PRETO])
        elif kind == "e":
            x, y, w, h = p[1]
            b.node("ellipse", cmp, "círculo", x=x, y=y, w=w, h=h, **LINE)
        elif kind == "r":
            x, y, w, h = p[1]
            b.node("rectangle", cmp, "caixa", x=x, y=y, w=w, h=h, **LINE)
        elif kind == "rf":
            x, y, w, h = p[1]
            b.node("rectangle", cmp, "ponto", x=x, y=y, w=w, h=h, fills=[PRETO])
        elif kind == "s":
            b.node("star", cmp, "estrela", x=2, y=2, w=20, h=20, fills=[PRETO])
    b.text(holder, name, "legenda", PRETO)
    ICON[name] = cmp


icon("busca", [("e", (3, 3, 14, 14)), ("v", "M15 15 L21 21")])
icon("conta", [("e", (8, 3, 8, 8)), ("v", "M4 21 C4 16 8 14 12 14 C16 14 20 16 20 21")])
icon("favorito", [("v", "M12 20 C5 15 3 12 3 8.5 C3 5.5 5.5 3.5 8 3.5 C9.8 3.5 11.2 4.5 12 6 C12.8 4.5 14.2 3.5 16 3.5 C18.5 3.5 21 5.5 21 8.5 C21 12 19 15 12 20 Z")])
icon("sacola", [("r", (4, 8, 16, 13)), ("v", "M8.5 8 L8.5 6.5 C8.5 4.5 10 3 12 3 C14 3 15.5 4.5 15.5 6.5 L15.5 8")])
icon("menu", [("v", "M3 6 L21 6 M3 12 L21 12 M3 18 L21 18")])
icon("fechar", [("v", "M5 5 L19 19 M19 5 L5 19")])
icon("seta-esquerda", [("v", "M15 4 L7 12 L15 20")])
icon("seta-direita", [("v", "M9 4 L17 12 L9 20")])
icon("seta-baixo", [("v", "M5 9 L12 16 L19 9")])
icon("mais", [("v", "M12 5 L12 19 M5 12 L19 12")])
icon("menos", [("v", "M5 12 L19 12")])
icon("check", [("v", "M4 12 L10 18 L20 6")])
icon("play", [("vf", "M7 4 L20 12 L7 20 Z")])
icon("estrela", [("s",)])
icon("arvore", [("v", "M12 22 L12 13 M12 13 C7 13 4 10 4 7 C4 4.5 7 3 9 4 C10 2 14 2 15 4 C17 3 20 4.5 20 7 C20 10 17 13 12 13 Z")])
icon("cacau", [("v", "M12 2 C17 6 18 13 12 22 C6 13 7 6 12 2 Z M12 6 L12 18 M9 9 L12 11 M15 9 L12 11 M9 14 L12 16 M15 14 L12 16")])
icon("calendario", [("r", (3, 5, 18, 16)), ("v", "M3 10 L21 10 M8 3 L8 7 M16 3 L16 7")])
icon("escudo", [("v", "M12 3 L20 6 L20 12 C20 17 16 20 12 21 C8 20 4 17 4 12 L4 6 Z M8.5 12 L11 14.5 L15.5 9.5")])
icon("caminhao", [("r", (2, 6, 12, 10)), ("v", "M14 9 L18 9 L21 12 L21 16 L14 16"), ("e", (5, 15, 4, 4)), ("e", (15, 15, 4, 4))])
icon("presente", [("r", (3, 9, 18, 12)), ("v", "M3 13 L21 13 M12 9 L12 21 M12 9 C10 4 6 4 6 7 C6 9 12 9 12 9 C12 9 18 9 18 7 C18 4 14 4 12 9")])
icon("whatsapp", [("v", "M4 20 L5.5 15.5 C4.5 14 4 12.5 4 11 C4 6.5 7.5 3.5 12 3.5 C16.5 3.5 20 6.5 20 11 C20 15.5 16.5 18.5 12 18.5 C10.5 18.5 9 18 7.8 17.4 Z")])
icon("instagram", [("r", (3, 3, 18, 18)), ("e", (8, 8, 8, 8)), ("rf", (16, 6, 2, 2))])
icon("email", [("r", (3, 5, 18, 14)), ("v", "M3 6 L12 13 L21 6")])

# ---- Fotografia e assinatura ----------------------------------------------------
FB = board(6400, 0, 1600, "Fotografia e assinatura",
           "Imagens do moodboard do BrandBook (p.27–28). Fotos em close, luz natural, foco no cacau e nos rituais de degustação. "
           "As imagens deste arquivo são referências em baixa resolução: substituir por fotos de produção.")
fr = row(FB, "Moodboard", gap=16, wrap=True)
for pth, lab in [(CACAU, "Cacau branco com o fruto vermelho — assinatura visual"), (CERAMICA, "Artesanal · criador"),
                 (MOSAICO, "Mosaico azul · brasilidade"), (CAMPO, "Campo ao entardecer · origem"),
                 (VINHO, "Taças de vinho · harmonização"), (CHEF, "Confeitaria · excelência"), (TINTAS, "Pincéis e tintas · arte")]:
    c = col(fr, lab, gap=8, w=352)
    b.image(c, pth, 352, 260, name=lab)
    b.text(c, lab, "corpo_p", PRETO, fillw=True)
sa = section(FB, "Assinatura tipográfica", "Enquanto o logotipo vetorial oficial não é enviado, a assinatura usa Glacial Indifference Bold (como na capa do BrandBook).")
ar = row(sa, "Aplicações", gap=24)
for bg, fg in [(BRANCO, BORDO), (BORDO, BRANCO), (PRETO, BRANCO)]:
    c = col(ar, f"Assinatura {NM[fg]} sobre {NM[bg]}", gap=8, w=440, pad=48, fill=bg, stroke=PRETO if bg == BRANCO else None, cross="center")
    b.text(c, "Var chocolates", "logo", fg)
    b.text(c, "Sabor e aroma para além da intensidade", "corpo_p", fg)

# =============================================================================
# 02 · Componentes
# =============================================================================
b.select_page(P_COMP)


def icon_inst(name, parent, color=PRETO):
    ins = b.instance(ICON[name], parent)
    if color != PRETO:
        for nid in ins.all[1:]:
            nm = b.names[nid]
            if nm in ("forma", "ponto", "estrela"):
                b.set(nid, fills=[color])
            else:
                b.set(nid, strokes=[color])
    return ins


# ---- Botões ---------------------------------------------------------------------
BB = board(0, 0, 1800, "Botões",
           "4 tipos × 6 estados. Lime → Configurações → Botões: primário fundo #6D071A / texto #FFFFFF; secundário com contorno preto. "
           "Hover, pressionado e foco são aplicados via CSS personalizado (aba Código).")
BTN = {}
TIPOS = {
    "Primário": {
        "Padrão": dict(fill=BORDO, fg=BRANCO), "Hover": dict(fill=UVA, fg=BRANCO),
        "Pressionado": dict(fill=PRETO, fg=BRANCO), "Foco": dict(fill=BORDO, fg=BRANCO, ring=PRETO),
        "Desabilitado": dict(fill=BRANCO, fg=PRETO, dash=True), "Carregando": dict(fill=BORDO, fg=BRANCO, load=True)},
    "Secundário": {
        "Padrão": dict(fill=BRANCO, fg=PRETO, stroke=PRETO), "Hover": dict(fill=PRETO, fg=BRANCO),
        "Pressionado": dict(fill=BORDO, fg=BRANCO), "Foco": dict(fill=BRANCO, fg=PRETO, stroke=BORDO, sw=2),
        "Desabilitado": dict(fill=BRANCO, fg=PRETO, dash=True), "Carregando": dict(fill=BRANCO, fg=PRETO, stroke=PRETO, load=True)},
    "Inverso": {
        "Padrão": dict(fill=BRANCO, fg=BORDO), "Hover": dict(fill=PRETO, fg=BRANCO),
        "Pressionado": dict(fill=UVA, fg=BRANCO), "Foco": dict(fill=BRANCO, fg=BORDO, stroke=PRETO, sw=2),
        "Desabilitado": dict(fill=BRANCO, fg=PRETO, dash=True), "Carregando": dict(fill=BRANCO, fg=BORDO, load=True)},
    "Link": {
        "Padrão": dict(fg=BORDO, ul=True), "Hover": dict(fg=PRETO, ul=True), "Pressionado": dict(fg=UVA, ul=True),
        "Foco": dict(fg=BORDO, ul=True, stroke=PRETO, sw=2), "Desabilitado": dict(fg=PRETO, dashul=True),
        "Carregando": dict(fg=BORDO, load=True)},
}
LABEL = {"Primário": "Comprar", "Secundário": "Ver todos", "Inverso": "Conheça os varietais", "Link": "Saiba mais"}
bset_holder = b.frame(BB, "Botão · variantes", 1640, 10, layout="vertical", gap=24, sv="hug")
variants = []
yy = 0
for tipo, estados in TIPOS.items():
    xx = 0
    for est, s in estados.items():
        isl = tipo == "Link"
        cpt = b.frame(None, f"Tipo={tipo}, Estado={est}", 10, 48, layout="horizontal", gap=8,
                      pad=[0, 4, 0, 4] if isl else [16, 32, 16, 32], main="center", cross="center",
                      fill=s.get("fill"), sh="hug", sv="fixed", comp=True, x=xx, y=yy, clip=False)
        if s.get("stroke"):
            b.set(cpt, strokes=[s["stroke"]], strokeWeight=s.get("sw", 1), strokeAlign="inside")
        if s.get("ring"):
            b.set(cpt, strokes=[s["ring"]], strokeWeight=2, strokeAlign="outside")
        if s.get("dash"):
            b.set(cpt, strokes=[PRETO], strokeWeight=1, dashes=[4, 4])
        lab = "Esgotado" if est == "Desabilitado" and tipo == "Primário" else (
            "Aguarde" if s.get("load") else LABEL[tipo])
        t = b.text(cpt, lab, "botao", s["fg"], name="label")
        if s.get("ul") or s.get("dashul"):
            b.set(t, textDecoration="underline")
        if s.get("load"):
            dots = b.frame(cpt, "carregando", 10, 6, layout="horizontal", gap=4, sh="hug", sv="hug")
            for i in range(3):
                b.rect(dots, 6, 6, s["fg"], name=f"ponto {i + 1}")
        if tipo != "Link":
            if s.get("fill") == BORDO:
                b.bind(cpt, "fill", "botao/primario/fundo")
            elif s.get("fill") == UVA and tipo == "Primário":
                b.bind(cpt, "fill", "botao/primario/fundo-hover")
        variants.append(cpt)
        BTN[(tipo, est)] = cpt
        xx += 260
    yy += 80
BTN_SET = b.combine(variants, "Botão")
b.set(BTN_SET, layout="grid", gridColumns=6, gap=24, crossGap=24, padding=32, sizingH="hug", sizingV="hug",
      fills=[BRANCO], strokes=[PRETO], strokeWeight=1, dashes=[])
b.reparent(BTN_SET, bset_holder)
for tipo in TIPOS:
    p, h, pr_ = BTN[(tipo, "Padrão")], BTN[(tipo, "Hover")], BTN[(tipo, "Pressionado")]
    b.interaction(p, {"type": "mouseEnter"}, {"type": "changeTo", "dest": h}, {"type": "smartAnimate"}, 150, "easeOut")
    b.interaction(h, {"type": "mouseLeave"}, {"type": "changeTo", "dest": p}, {"type": "smartAnimate"}, 150, "easeOut")
    b.interaction(h, {"type": "mouseDown"}, {"type": "changeTo", "dest": pr_}, {"type": "smartAnimate"}, 100, "easeOut")
    b.interaction(pr_, {"type": "mouseUp"}, {"type": "changeTo", "dest": h}, {"type": "smartAnimate"}, 100, "easeOut")
table(BB, ["Estado", "Primário", "Secundário", "Inverso (sobre bordô/preto)", "Link"], [
    ["Padrão", "Fundo bordô · texto branco", "Fundo branco · contorno 1px preto · texto preto", "Fundo branco · texto bordô", "Texto bordô sublinhado"],
    ["Hover (150ms)", "Fundo uva", "Fundo preto · texto branco", "Fundo preto · texto branco", "Texto preto"],
    ["Pressionado (100ms)", "Fundo preto", "Fundo bordô · texto branco", "Fundo uva · texto branco", "Texto uva"],
    ["Foco (teclado)", "Anel 2px preto externo", "Contorno 2px bordô", "Contorno 2px preto", "Anel 2px preto"],
    ["Desabilitado / Esgotado", "Fundo branco · tracejado preto · “ESGOTADO”", "Fundo branco · tracejado preto", "Fundo branco · tracejado preto", "Texto preto"],
    ["Carregando", "Bordô + 3 pontos pulsando", "Contorno + 3 pontos", "Branco + 3 pontos", "3 pontos"],
], [240, 340, 340, 340, 340])
note(BB, "Altura 48px (área de toque ≥ 44px), padding 16/32, rótulo Glacial Bold 14px em caixa alta com 8% de espaçamento. "
         "No card de produto o botão ocupa 100% da largura. Protótipo: passe o mouse sobre as instâncias para ver hover e pressionado.",
     title="ESPECIFICAÇÃO")

# ---- Etiquetas, selos e formulários ---------------------------------------------
EB = board(1900, 0, 1400, "Etiquetas, selos e formulários",
           "Etiquetas por varietal (Lime: etiqueta personalizada do card, raio 0) — a cor identifica o cacau, como o nome “Var”.")
er = row(EB, "Etiquetas", gap=24, cross="center")
ETQ = {}
for nm, bg, fg in [("Forastero", AZUL, BRANCO), ("Catongo", BEER, PRETO), ("Trinitário", PURPLE, BRANCO), ("Presente", BORDO, BRANCO)]:
    e = b.frame(None, f"Varietal={nm}", 10, 24, layout="horizontal", pad=[4, 8, 4, 8], fill=bg, sh="hug", sv="hug",
                comp=True, cross="center")
    b.text(e, nm, "eyebrow", fg, name="etiqueta")
    ETQ[nm] = e
ETQ_SET = b.combine(list(ETQ.values()), "Etiqueta varietal")
b.set(ETQ_SET, layout="horizontal", gap=16, padding=24, sizingH="hug", sizingV="hug", fills=[BRANCO])
b.reparent(ETQ_SET, er)
SELO = b.frame(None, "Selo desconto", 10, 24, layout="horizontal", pad=[4, 8, 4, 8], fill=BEER, sh="hug", sv="hug", comp=True)
b.text(SELO, "-15%", "eyebrow", PRETO, name="selo")
b.bind(SELO, "fill", "selo/desconto/fundo")
b.reparent(SELO, er)
NOVO = b.frame(None, "Selo novidade", 10, 24, layout="horizontal", pad=[4, 8, 4, 8], fill=PRETO, sh="hug", sv="hug", comp=True)
b.text(NOVO, "Novidade", "eyebrow", BRANCO, name="selo")
b.reparent(NOVO, er)

fi = section(EB, "Campo de texto", "Altura 48, contorno 1px preto, raio 0. Foco: contorno 2px bordô. Erro: contorno 2px bordô + mensagem.")
fr_ = row(fi, "Campos", gap=24, wrap=True)
INP = {}
for est, kw in [("Padrão", dict(stroke=PRETO, sw=1, ph="Seu melhor e-mail", fg=PRETO)),
                ("Foco", dict(stroke=BORDO, sw=2, ph="maria@|", fg=PRETO)),
                ("Preenchido", dict(stroke=PRETO, sw=1, ph="maria@email.com", fg=PRETO)),
                ("Erro", dict(stroke=BORDO, sw=2, ph="maria@", fg=PRETO, err="Digite um e-mail válido.")),
                ("Desabilitado", dict(stroke=PRETO, sw=1, ph="Indisponível", fg=PRETO, dash=True))]:
    cpt = b.frame(None, f"Estado={est}", 320, 10, layout="vertical", gap=6, sv="hug", comp=True)
    b.text(cpt, "E-mail", "rotulo", PRETO, name="rotulo")
    fld = b.frame(cpt, "campo", 320, 48, layout="horizontal", pad=[0, 16, 0, 16], cross="center", fill=BRANCO,
                  stroke=kw["stroke"], sw=kw["sw"], sh="fill")
    if kw.get("dash"):
        b.set(fld, dashes=[4, 4])
    b.text(fld, kw["ph"], "corpo", kw["fg"], name="valor")
    if kw.get("err"):
        b.text(cpt, kw["err"], "legenda", BORDO, name="mensagem")
    INP[est] = cpt
INP_SET = b.combine(list(INP.values()), "Campo de texto")
b.set(INP_SET, layout="horizontal", gap=24, padding=24, wrap=True, sizingH="hug", sizingV="hug", fills=[BRANCO])
b.reparent(INP_SET, fr_)

qt = section(EB, "Seletor de quantidade e busca")
qr = row(qt, "Controles", gap=24, cross="center")
QTD = b.frame(None, "Seletor de quantidade", 136, 48, layout="horizontal", main="spaceBetween", cross="center",
              pad=[0, 12, 0, 12], fill=BRANCO, stroke=PRETO, comp=True)
icon_inst("menos", QTD)
b.text(QTD, "1", "corpo_b", PRETO, name="quantidade")
icon_inst("mais", QTD)
b.reparent(QTD, qr)
BUSCA = b.frame(None, "Campo de busca", 320, 44, layout="horizontal", gap=8, cross="center", pad=[0, 12, 0, 12],
                fill=BRANCO, stroke=PRETO, comp=True)
icon_inst("busca", BUSCA)
b.text(BUSCA, "Buscar chocolates, varietais…", "corpo_p", PRETO, name="placeholder")
b.reparent(BUSCA, qr)

# ---- Navegação --------------------------------------------------------------------
NB = board(0, 2200, 1600, "Navegação",
           "Tarja informativa (overline), cabeçalho Layout 3 do Lime (busca à esquerda, logo central, menu abaixo), breadcrumb e controles do carrossel.")
MSGS = ["Frete grátis acima de R$ 250", "Parcele em até 3x sem juros", "Fale com a gente no WhatsApp"]
TARJA = b.frame(None, "Tarja/Desktop", 1440, 40, layout="horizontal", main="center", cross="center", gap=32, fill=BORDO, comp=True)
b.bind(TARJA, "fill", "tarja/fundo")
for k, m in enumerate(MSGS):
    if k:
        b.rect(TARJA, 4, 4, BRANCO, name="separador")
    b.text(TARJA, m, "eyebrow", BRANCO, name=f"msg{k + 1}")
b.reparent(TARJA, NB)
TM = []
for k, m in enumerate(MSGS):
    t = b.frame(None, f"Mensagem={k + 1}", 390, 36, layout="horizontal", main="center", cross="center", fill=BORDO, comp=True)
    b.text(t, m, "eyebrow", BRANCO, name="msg")
    TM.append(t)
TARJA_M = b.combine(TM, "Tarja/Mobile")
b.set(TARJA_M, layout="horizontal", gap=16, padding=16, sizingH="hug", sizingV="hug", fills=[BRANCO])
b.reparent(TARJA_M, NB)
for k in range(3):
    b.interaction(TM[k], {"type": "afterDelay", "ms": 4000}, {"type": "changeTo", "dest": TM[(k + 1) % 3]},
                  {"type": "dissolve"}, 400, "easeOut")

NAV = ["Chocolates", "Varietais", "Presentes", "Kits", "Nossa origem", "Contato"]
HD = b.frame(None, "Cabeçalho/Desktop", 1440, 10, layout="vertical", fill=BRANCO, sv="hug", comp=True)
r1 = b.frame(HD, "Linha principal", 1440, 88, layout="horizontal", main="spaceBetween", cross="center", pad=[0, 80, 0, 80], sh="fill")
lft = b.frame(r1, "Esquerda", 320, 44, layout="horizontal", cross="center")
b.instance(BUSCA, lft)
LOGO_D = b.text(r1, "Var chocolates", "logo", BORDO, name="logo")
rgt = b.frame(r1, "Direita", 320, 44, layout="horizontal", main="max", cross="center", gap=24)
icon_inst("conta", rgt)
icon_inst("favorito", rgt)
bag = b.frame(rgt, "sacola", 28, 28, clip=False)
icon_inst("sacola", bag)
bdg = b.frame(bag, "contador", 16, 16, layout="horizontal", main="center", cross="center", fill=BORDO, x=16, y=-6)
b.text(bdg, "2", "legenda", BRANCO, name="contador_n")
r2 = b.frame(HD, "Menu", 1440, 48, layout="horizontal", main="center", cross="center", gap=48, sh="fill")
for n in NAV:
    b.text(r2, n, "menu", PRETO, name=f"nav_{n}")
dv = b.rect(HD, 1440, 1, PRETO, name="Divisor")
b.set(dv, sizingH="fill")
b.reparent(HD, NB)

HM = b.frame(None, "Cabeçalho/Mobile", 390, 10, layout="vertical", fill=BRANCO, sv="hug", comp=True)
m1 = b.frame(HM, "Linha", 390, 64, layout="horizontal", main="spaceBetween", cross="center", pad=[0, 16, 0, 16], sh="fill")
ml = b.frame(m1, "Esquerda", 80, 24, layout="horizontal", gap=16, cross="center")
icon_inst("menu", ml)
icon_inst("busca", ml)
b.text(m1, "Var chocolates", "m_logo", BORDO, name="logo")
mr = b.frame(m1, "Direita", 80, 28, layout="horizontal", main="max", cross="center", gap=16)
icon_inst("favorito", mr)
bagm = b.frame(mr, "sacola", 28, 28, clip=False)
icon_inst("sacola", bagm)
bdm = b.frame(bagm, "contador", 16, 16, layout="horizontal", main="center", cross="center", fill=BORDO, x=16, y=-6)
b.text(bdm, "2", "legenda", BRANCO, name="contador_n")
dv = b.rect(HM, 390, 1, PRETO, name="Divisor")
b.set(dv, sizingH="fill")
b.reparent(HM, NB)

nr = row(NB, "Breadcrumb e carrossel", gap=48, cross="center")
BREAD = b.frame(None, "Breadcrumb", 10, 20, layout="horizontal", gap=8, cross="center", sh="hug", sv="hug", comp=True)
b.text(BREAD, "Início", "legenda", PRETO, name="nivel1", textDecoration="underline")
b.text(BREAD, "/", "legenda", PRETO, name="sep")
b.text(BREAD, "Nossa origem", "legenda", BORDO, name="atual")
b.reparent(BREAD, nr)
SETA = {}
for nm, ic in [("Esquerda", "seta-esquerda"), ("Direita", "seta-direita")]:
    s_ = b.frame(None, f"Seta do carrossel/{nm}", 48, 48, layout="horizontal", main="center", cross="center", fill=BRANCO, stroke=PRETO, comp=True)
    icon_inst(ic, s_)
    b.reparent(s_, nr)
    SETA[nm] = s_
DOTS = {}
for k in range(3):
    d_ = b.frame(None, f"Paginação/Ativo={k + 1}", 10, 10, layout="horizontal", gap=8, sh="hug", sv="hug", comp=True)
    for i in range(3):
        if i == k:
            b.rect(d_, 24, 4, BRANCO, name=f"p{i + 1}")
        else:
            b.rect(d_, 8, 4, BRANCO, name=f"p{i + 1}", stroke=BRANCO)
    DOTS[k] = d_
dots_holder = b.frame(nr, "Paginação (sobre bloco de cor)", 10, 10, layout="horizontal", gap=24, pad=16, fill=BORDO, sh="hug", sv="hug")
for k in range(3):
    b.reparent(DOTS[k], dots_holder)

# ---- Cards ------------------------------------------------------------------------
KB = board(1700, 2200, 2400, "Cards e blocos de conteúdo",
           "Card de produto (4 estados), embalagem ilustrativa por varietal, benefício, avaliação e título de seção.")
# embalagem ilustrativa
PK = b.frame(None, "Embalagem ilustrativa", 160, 220, layout="vertical", main="spaceBetween", pad=16, fill=AZUL, comp=True)
b.set(PK, name="Embalagem ilustrativa")
pkt = b.frame(PK, "topo", 128, 10, layout="vertical", gap=4, sh="fill", sv="hug")
b.text(pkt, "Var chocolates", "rotulo", BRANCO, name="pk_marca")
fio = b.rect(pkt, 24, 2, BRANCO, name="pk_fio")
pkb = b.frame(PK, "base", 128, 10, layout="vertical", gap=2, sh="fill", sv="hug")
b.text(pkb, "Forastero", "h4", BRANCO, name="pk_nome", textCase="upper", fillw=True)
b.text(pkb, "70% cacau · 80g", "legenda", BRANCO, name="pk_pct")
krow = row(KB, "Componentes base", gap=32, cross="min", wrap=True)
b.reparent(PK, krow)


def product_card(name, varietal, nome, notas, preco, parcelas, de=None, estado="Padrão", cor=AZUL, fgc=BRANCO,
                 pk_nome=None, pk_pct="70% cacau · 80g", W=302):
    cd = b.frame(None, name, W, 10, layout="vertical", gap=16, pad=[0, 0, 16, 0], fill=BRANCO, sv="hug", comp=True)
    hover = estado == "Hover"
    if hover:
        b.set(cd, strokes=[PRETO], strokeWeight=1, padding=[0, 0, 16, 0])
    ft = b.frame(cd, "foto", W, W, fill=BRANCO, stroke=UVA if not hover else None, sh="fill", clip=True)
    pw, ph = (176, 242) if hover else (160, 220)
    pk = b.instance(PK, ft, x=(W - pw) / 2, y=(W - ph) / 2)
    if hover:
        b.set(pk.id, width=pw, height=ph)
    b.set(pk.id, fills=[cor])
    for k_ in ("pk_marca", "pk_nome", "pk_pct"):
        if fgc != BRANCO:
            b.set(pk[k_], fills=[fgc])
    if fgc != BRANCO:
        b.set(pk["pk_fio"], fills=[fgc])
    b.set(pk["pk_nome"], characters=pk_nome or varietal)
    b.set(pk["pk_pct"], characters=pk_pct)
    et = b.instance(ETQ[varietal if varietal in ETQ else "Presente"], ft, x=12, y=12)
    if de:
        sl = b.instance(SELO, ft, x=W - 62, y=12)
    inf = b.frame(cd, "info", W, 10, layout="vertical", gap=6, sh="fill", sv="hug", pad=[0, 12, 0, 12] if hover else 0)
    b.text(inf, nome, "h4", PRETO, fillw=True, name="nome")
    b.text(inf, notas, "corpo_p", PRETO, fillw=True, name="notas")
    pr = b.frame(inf, "preços", 10, 10, layout="horizontal", gap=8, cross="center", sh="fill", sv="hug")
    if de:
        b.text(pr, de, "corpo_p", PRETO, name="preco_de", textDecoration="strikethrough")
    b.text(pr, preco, "preco", BORDO, name="preco")
    b.text(inf, parcelas, "legenda", PRETO, name="parcelas")
    bw = b.frame(cd, "ação", W, 48, layout="horizontal", sh="fill", sv="hug", pad=[0, 12, 0, 12] if hover else 0)
    st = {"Padrão": "Padrão", "Hover": "Hover", "Promoção": "Padrão", "Esgotado": "Desabilitado"}[estado]
    bt = b.instance(BTN[("Primário", st)], bw)
    b.set(bt.id, sizingH="fill")
    return cd


CARDS = {}
for est in ["Padrão", "Hover", "Promoção", "Esgotado"]:
    CARDS[est] = product_card(f"Estado={est}", "Forastero", "Barra Forastero 70%", "Notas: frutadas · amadeiradas",
                              "R$ 39,90", "ou 3x de R$ 13,30 sem juros", de="R$ 46,90" if est == "Promoção" else None, estado=est)
CARD_SET = b.combine(list(CARDS.values()), "Card de produto")
b.set(CARD_SET, layout="horizontal", gap=32, padding=32, sizingH="hug", sizingV="hug", fills=[BRANCO], strokes=[PRETO], strokeWeight=1)
b.reparent(CARD_SET, krow)
CARDS_M = {}
for est in ["Padrão", "Promoção"]:
    CARDS_M[est] = product_card(f"Estado={est}", "Forastero", "Barra Forastero 70%", "Notas: frutadas · amadeiradas",
                                "R$ 39,90", "ou 3x de R$ 13,30 sem juros", de="R$ 46,90" if est == "Promoção" else None,
                                estado=est, W=240)
CARD_MSET = b.combine(list(CARDS_M.values()), "Card de produto/Mobile")
b.set(CARD_MSET, layout="horizontal", gap=32, padding=32, sizingH="hug", sizingV="hug", fills=[BRANCO], strokes=[PRETO], strokeWeight=1)
b.reparent(CARD_MSET, krow)
b.interaction(CARDS["Padrão"], {"type": "mouseEnter"}, {"type": "changeTo", "dest": CARDS["Hover"]}, {"type": "smartAnimate"}, 250, "easeOut")
b.interaction(CARDS["Hover"], {"type": "mouseLeave"}, {"type": "changeTo", "dest": CARDS["Padrão"]}, {"type": "smartAnimate"}, 250, "easeOut")

k2 = row(KB, "Blocos", gap=32, cross="min")
BENS = [("arvore", "Tree to bar", "Do plantio à barra, com rastreabilidade total."),
        ("cacau", "Cacau varietal", "Forastero, Catongo e Trinitário em lotes separados."),
        ("calendario", "Desde 1930", "Três gerações sob a Mata Atlântica."),
        ("escudo", "Compra segura", "Pagamento protegido e entrega para todo o Brasil.")]
BEN = {}
for ic, tt_, dd_ in BENS:
    bc_ = b.frame(None, f"Benefício={tt_}", 296, 10, layout="horizontal", gap=16, cross="center", sv="hug", comp=True)
    ib = b.frame(bc_, "ícone", 48, 48, layout="horizontal", main="center", cross="center", stroke=PRETO)
    icon_inst(ic, ib)
    bt_ = b.frame(bc_, "textos", 200, 10, layout="vertical", gap=4, sh="fill", sv="hug")
    b.text(bt_, tt_, "rotulo", PRETO, name="ben_titulo")
    b.text(bt_, dd_, "corpo_p", PRETO, fillw=True, name="ben_desc")
    BEN[tt_] = bc_
BEN_SET = b.combine(list(BEN.values()), "Benefício")
b.set(BEN_SET, layout="vertical", gap=16, padding=24, sizingH="hug", sizingV="hug", fills=[BRANCO])
b.reparent(BEN_SET, k2)

REV = b.frame(None, "Avaliação", 405, 10, layout="vertical", gap=16, pad=32, stroke=PRETO, fill=BRANCO, sv="hug", comp=True)
stars = b.frame(REV, "estrelas", 10, 16, layout="horizontal", gap=4, sh="hug", sv="hug")
for i in range(5):
    b.node("star", stars, f"estrela {i + 1}", w=16, h=16, fills=[BORDO])
b.text(REV, "“Dá para sentir as notas frutadas logo no primeiro pedaço. Virou o presente oficial da família.”", "corpo_g", PRETO, fillw=True, name="depoimento")
b.text(REV, "Isabela M. · São Paulo", "rotulo", PRETO, name="autor")
b.text(REV, "Compra verificada · Barra Trinitário 75%", "legenda", PRETO, name="meta")
b.reparent(REV, k2)

TIT = {}
for disp, w, st in [("Desktop", 1280, "h2"), ("Mobile", 358, "m_h2")]:
    t = b.frame(None, f"Dispositivo={disp}", w, 10, layout="vertical", gap=12, cross="center", sv="hug", comp=True)
    b.text(t, "Mais vendidos", "eyebrow", BORDO, name="eyebrow")
    b.text(t, "Os preferidos de quem prova", st, PRETO, align="center", name="titulo", w=w)
    b.rect(t, 48, 2, BORDO, name="fio")
    b.text(t, "Para você provar que chocolate não é tudo igual.", "corpo", PRETO, align="center", name="subtitulo", w=min(w, 640))
    TIT[disp] = t
TIT_SET = b.combine(list(TIT.values()), "Título de seção")
b.set(TIT_SET, layout="vertical", gap=32, padding=32, sizingH="hug", sizingV="hug", fills=[BRANCO])
b.reparent(TIT_SET, KB)

# ---- Seções (newsletter, rodapé, selos) -----------------------------------------------
SB = board(0, 4400, 1600, "Seções de rodapé",
           "Newsletter em faixa preta, rodapé bordô (footerInformation) e faixa branca de selos e informações legais (footerSeals / footerLegal).")
NL = {}
for disp in ["Desktop", "Mobile"]:
    d = disp == "Desktop"
    n = b.frame(None, f"Newsletter/{disp}", 1440 if d else 390, 10, layout="horizontal" if d else "vertical",
                main="spaceBetween" if d else None, cross="center" if d else None, gap=24,
                pad=[64, 80, 64, 80] if d else [48, 16, 48, 16], fill=PRETO, sv="hug", comp=True)
    b.bind(n, "fill", "newsletter/fundo")
    tx = b.frame(n, "textos", 560 if d else 358, 10, layout="vertical", gap=12, sv="hug", sh="fixed" if d else "fill")
    b.text(tx, "Newsletter", "eyebrow", BEER, name="nl_eyebrow")
    b.text(tx, "Aprenda a degustar", "h2" if d else "m_h2", BRANCO, name="nl_titulo")
    b.text(tx, "Notas sensoriais, harmonizações e lançamentos no seu e-mail.", "corpo", BRANCO, fillw=True, name="nl_texto")
    fm = b.frame(n, "formulário", 560 if d else 358, 48, layout="horizontal" if d else "vertical", gap=0 if d else 12,
                 sv="hug", sh="fixed" if d else "fill")
    fld = b.frame(fm, "campo", 380, 48, layout="horizontal", pad=[0, 16, 0, 16], cross="center", fill=BRANCO, sh="fill")
    b.text(fld, "Seu melhor e-mail", "corpo", PRETO, name="nl_placeholder")
    bt = b.instance(BTN[("Primário", "Padrão")], fm)
    b.set(bt["label"], characters="Quero receber")
    if not d:
        b.set(bt.id, sizingH="fill")
    b.reparent(n, SB)
    NL[disp] = n

COLS = [("Institucional", ["Nossa origem", "Cacau varietal", "Tree to bar", "Trabalhe conosco"]),
        ("Ajuda", ["Trocas e devoluções", "Prazos de entrega", "Formas de pagamento", "Política de privacidade"]),
        ("Atendimento", ["WhatsApp (00) 00000-0000", "E-mail a definir", "Seg. a sex., 9h às 18h"])]
FT = {}
for disp in ["Desktop", "Mobile"]:
    d = disp == "Desktop"
    f = b.frame(None, f"Rodapé/{disp}", 1440 if d else 390, 10, layout="vertical", gap=40 if d else 24,
                pad=[64, 80, 32, 80] if d else [40, 16, 24, 16], fill=BORDO, sv="hug", comp=True)
    b.bind(f, "fill", "rodape/fundo")
    top = b.frame(f, "colunas", 1280 if d else 358, 10, layout="horizontal" if d else "vertical", gap=48 if d else 24,
                  sh="fill", sv="hug")
    c1 = b.frame(top, "marca", 400 if d else 358, 10, layout="vertical", gap=16, sv="hug", sh="fixed" if d else "fill")
    b.text(c1, "Var chocolates", "logo" if d else "m_logo", BRANCO, name="ft_logo")
    b.text(c1, "Sabor e aroma para além da intensidade. Cacau varietal cultivado há três gerações sob a Mata Atlântica, no Sul da Bahia.",
           "corpo_p", BRANCO, fillw=True, name="ft_texto")
    so = b.frame(c1, "redes", 10, 24, layout="horizontal", gap=16, sh="hug", sv="hug")
    for ic in ["instagram", "whatsapp", "email"]:
        icon_inst(ic, so, BRANCO)
    for tt, links in COLS:
        if d:
            cc = b.frame(top, tt, 240, 10, layout="vertical", gap=12, sv="hug", sh="fill")
            b.text(cc, tt, "rotulo", BRANCO)
            for l in links:
                b.text(cc, l, "corpo_p", BRANCO)
        else:
            acc = b.frame(top, tt, 358, 48, layout="horizontal", main="spaceBetween", cross="center", sh="fill",
                          stroke=BRANCO, sw=1)
            b.set(acc, strokeTopWeight=1, strokeBottomWeight=0, strokeLeftWeight=0, strokeRightWeight=0)
            b.text(acc, tt, "rotulo", BRANCO)
            icon_inst("seta-baixo", acc, BRANCO)
    dv = b.rect(f, 100, 1, BRANCO, name="Divisor")
    b.set(dv, sizingH="fill")
    lg = b.frame(f, "legal", 1280 if d else 358, 10, layout="horizontal" if d else "vertical", main="spaceBetween" if d else None,
                 gap=8, sh="fill", sv="hug")
    b.text(lg, "© 2026 Var Chocolates. Todos os direitos reservados.", "legenda", BRANCO)
    b.text(lg, "CNPJ 00.000.000/0001-00 · Sul da Bahia · Brasil", "legenda", BRANCO)
    b.reparent(f, SB)
    FT[disp] = f

SELOS = {}
for disp in ["Desktop", "Mobile"]:
    d = disp == "Desktop"
    s_ = b.frame(None, f"Selos/{disp}", 1440 if d else 390, 10, layout="horizontal" if d else "vertical",
                 main="spaceBetween" if d else None, cross="center" if d else None, gap=16,
                 pad=[24, 80, 24, 80] if d else [24, 16, 24, 16], fill=BRANCO, sv="hug", comp=True)
    for grp, items in [("Formas de pagamento", ["Visa", "Master", "Elo", "Pix", "Boleto"]), ("Segurança", ["SSL", "Irroba"])]:
        g = b.frame(s_, grp, 10, 10, layout="vertical" if not d else "horizontal", gap=12, cross="center" if d else None, sh="hug", sv="hug")
        b.text(g, grp, "eyebrow", PRETO)
        it = b.frame(g, "itens", 10, 32, layout="horizontal", gap=8, sh="hug", sv="hug")
        for i_ in items:
            bx = b.frame(it, i_, 56, 32, layout="horizontal", main="center", cross="center", stroke=PRETO)
            b.text(bx, i_, "legenda", PRETO)
    b.reparent(s_, SB)
    SELOS[disp] = s_

# ---- Overlays ------------------------------------------------------------------------
OB = board(1700, 4400, 1200, "Overlays",
           "Mini-carrinho (abre pela direita, 400ms) e menu mobile (abre pela esquerda). Fundo da página não recebe véu transparente: o painel tem borda preta.")
orow = row(OB, "Painéis", gap=48)


def drawer_cart(parent, w=420, h=900, name="Mini-carrinho"):
    dr = b.frame(parent, name, w, h, layout="vertical", gap=0, fill=BRANCO, stroke=PRETO, comp=True)
    hd = b.frame(dr, "topo", w, 72, layout="horizontal", main="spaceBetween", cross="center", pad=[0, 24, 0, 24], sh="fill")
    b.text(hd, "Sua sacola (2)", "h3", PRETO, name="titulo")
    x_ = icon_inst("fechar", hd)
    dv = b.rect(dr, w, 1, PRETO, name="Divisor")
    b.set(dv, sizingH="fill")
    lst = b.frame(dr, "itens", w, 10, layout="vertical", gap=24, pad=24, sh="fill", sv="fill")
    for nome, var_, cor, fg, pr in [("Barra Forastero 70%", "Forastero", AZUL, BRANCO, "R$ 39,90"),
                                    ("Barra Catongo 60%", "Catongo", BEER, PRETO, "R$ 44,90")]:
        it = b.frame(lst, nome, w - 48, 10, layout="horizontal", gap=16, sh="fill", sv="hug")
        th = b.frame(it, "miniatura", 80, 96, layout="vertical", main="max", pad=8, fill=cor)
        b.text(th, var_, "eyebrow", fg)
        tx = b.frame(it, "textos", 10, 10, layout="vertical", gap=6, sh="fill", sv="hug")
        b.text(tx, nome, "h4", PRETO, fillw=True)
        b.text(tx, pr, "preco", BORDO)
        q = b.instance(QTD, tx)
    ft = b.frame(dr, "resumo", w, 10, layout="vertical", gap=16, pad=24, sh="fill", sv="hug", fill=BRANCO)
    dv2 = b.rect(ft, w - 48, 1, PRETO, name="Divisor")
    b.set(dv2, sizingH="fill")
    sr = b.frame(ft, "subtotal", w - 48, 10, layout="horizontal", main="spaceBetween", sh="fill", sv="hug")
    b.text(sr, "Subtotal", "corpo_b", PRETO)
    b.text(sr, "R$ 84,80", "preco", BORDO)
    b.text(ft, "Faltam R$ 165,20 para frete grátis.", "legenda", PRETO)
    bar = b.frame(ft, "progresso", w - 48, 4, stroke=PRETO, sh="fill")
    b.node("rectangle", bar, "preenchido", w=(w - 48) * 0.34, h=4, fills=[BORDO])
    bt = b.instance(BTN[("Primário", "Padrão")], ft)
    b.set(bt["label"], characters="Finalizar compra")
    b.set(bt.id, sizingH="fill")
    bt2 = b.instance(BTN[("Secundário", "Padrão")], ft)
    b.set(bt2["label"], characters="Continuar comprando")
    b.set(bt2.id, sizingH="fill")
    return dr, x_


CART, CART_X = drawer_cart(orow)
MENU = b.frame(orow, "Menu mobile", 320, 844, layout="vertical", gap=0, fill=BRANCO, stroke=PRETO, comp=True)
mh = b.frame(MENU, "topo", 320, 64, layout="horizontal", main="spaceBetween", cross="center", pad=[0, 16, 0, 16], sh="fill", fill=BORDO)
b.text(mh, "Var chocolates", "m_logo", BRANCO)
MENU_X = icon_inst("fechar", mh, BRANCO)
for n in NAV:
    it = b.frame(MENU, n, 320, 56, layout="horizontal", main="spaceBetween", cross="center", pad=[0, 16, 0, 16], sh="fill", stroke=PRETO)
    b.set(it, strokeTopWeight=0, strokeBottomWeight=1, strokeLeftWeight=0, strokeRightWeight=0)
    b.text(it, n, "menu", PRETO, name=f"m_{n}")
    icon_inst("seta-direita", it)
mf = b.frame(MENU, "rodapé do menu", 320, 10, layout="vertical", gap=12, pad=16, sh="fill", sv="hug")
b.text(mf, "Minha conta", "corpo_b", PRETO)
b.text(mf, "Favoritos", "corpo_b", PRETO)
b.text(mf, "Atendimento: WhatsApp (00) 00000-0000", "legenda", PRETO)

# ---- Banner principal (carrossel) -------------------------------------------------------
HB = board(0, 6600, 3200, "Banner principal (Banner v2 · Carrossel 100%)",
           "No Lime o banner é uma imagem: textos, botão e blocos de cor fazem parte da arte exportada (desktop 1920×854 a partir deste frame de 1440×640; mobile 780×976). "
           "Setas e paginação são do tema.")
hrow = row(HB, "Variantes", gap=48)
SLIDES = [
    dict(eyebrow="Cacau varietal do Sul da Bahia", title="Sabor e aroma para além da intensidade",
         text="Do plantio à barra, há três gerações. Para você provar que chocolate não é tudo igual.",
         cta="Conheça os varietais", img=CACAU, bg=BORDO, ey=BRANCO, left=True),
    dict(eyebrow="Para presentear", title="Presentes que contam histórias",
         text="Caixas e kits pensados como experiência — do som da embalagem ao snap do chocolate.",
         cta="Ver presentes", img=VINHO, bg=PRETO, ey=BEER, left=False),
    dict(eyebrow="Forastero · Catongo · Trinitário", title="Três varietais, três personalidades",
         text="Notas frutadas, florais ou amadeiradas: escolha pelo cacau, como se escolhe um vinho.",
         cta="Escolher meu varietal", img=MOSAICO, bg=PURPLE, ey=BRANCO, left=True),
]
HERO_D, HERO_M = [], []
for k, s in enumerate(SLIDES):
    h = b.frame(None, f"Slide={k + 1}", 1440, 640, fill=BRANCO, comp=True, clip=True)
    bx = 0 if s["left"] else 720
    blk = b.frame(h, "bloco", 720, 640, layout="vertical", main="center", gap=24, pad=[80, 96, 80, 80], fill=s["bg"], x=bx, y=0)
    b.text(blk, s["eyebrow"], "eyebrow", s["ey"], name="eyebrow")
    b.text(blk, s["title"], "display", BRANCO, w=544, name="titulo")
    b.text(blk, s["text"], "corpo_g", BRANCO, w=480, name="texto")
    bt = b.instance(BTN[("Inverso", "Padrão")], blk)
    b.set(bt["label"], characters=s["cta"])
    fimg = b.image(h, s["img"], 720, 640, name="foto")
    b.set(fimg, x=720 - bx, y=0)
    sl = b.instance(SETA["Esquerda"], h, x=1288, y=568)
    sr = b.instance(SETA["Direita"], h, x=1352, y=568)
    b.instance(DOTS[k], h, x=bx + 80, y=584)
    HERO_D.append(h)
    # mobile
    m = b.frame(None, f"Slide={k + 1}", 390, 488, layout="vertical", fill=BRANCO, comp=True)
    b.image(m, s["img"], 390, 220, name="foto")
    mb = b.frame(m, "bloco", 390, 268, layout="vertical", main="center", gap=16, pad=24, fill=s["bg"], sh="fill")
    b.text(mb, s["eyebrow"], "eyebrow", s["ey"], name="eyebrow")
    b.text(mb, s["title"], "m_h1", BRANCO, fillw=True, name="titulo")
    bt = b.instance(BTN[("Inverso", "Padrão")], mb)
    b.set(bt["label"], characters=s["cta"])
    b.instance(DOTS[k], mb)
    HERO_M.append(m)
HERO_SET = b.combine(HERO_D, "Banner principal/Desktop")
b.set(HERO_SET, layout="vertical", gap=32, padding=32, sizingH="hug", sizingV="hug", fills=[BRANCO], strokes=[PRETO], strokeWeight=1)
b.reparent(HERO_SET, hrow)
HERO_MSET = b.combine(HERO_M, "Banner principal/Mobile")
b.set(HERO_MSET, layout="vertical", gap=32, padding=32, sizingH="hug", sizingV="hug", fills=[BRANCO], strokes=[PRETO], strokeWeight=1)
b.reparent(HERO_MSET, hrow)
for lst in (HERO_D, HERO_M):
    for k in range(3):
        b.interaction(lst[k], {"type": "afterDelay", "ms": 6000}, {"type": "changeTo", "dest": lst[(k + 1) % 3]},
                      {"type": "dissolve"}, 400, "easeInOut")

# =============================================================================
# 04/05 · Telas
# =============================================================================
PREF = [("Forastero", "Barra Forastero 70%", "Notas: frutadas · amadeiradas", "R$ 39,90", "ou 3x de R$ 13,30 sem juros", None, "70% cacau · 80g"),
        ("Catongo", "Barra Catongo 60%", "Notas: florais · mel", "R$ 44,90", "ou 3x de R$ 14,97 sem juros", "R$ 52,90", "60% cacau · 80g"),
        ("Trinitário", "Barra Trinitário 75%", "Notas: frutas vermelhas · especiarias", "R$ 42,90", "ou 3x de R$ 14,30 sem juros", None, "75% cacau · 80g"),
        ("Forastero", "Nibs de Cacau Forastero", "Crocante, para finalizar sobremesas", "R$ 29,90", "ou 3x de R$ 9,97 sem juros", None, "Nibs · 100g")]
PRES = [("Presente", "Caixa Degustação Varietais", "6 barras · os três varietais", "R$ 189,90", "ou 3x de R$ 63,30 sem juros", None, "Caixa · 6 barras"),
        ("Presente", "Kit Harmonização com Vinho", "Barras + guia de harmonização", "R$ 229,90", "ou 3x de R$ 76,63 sem juros", None, "Kit"),
        ("Presente", "Caixa Desde 1930", "Edição especial · três gerações", "R$ 149,90", "ou 3x de R$ 49,97 sem juros", None, "Caixa"),
        ("Presente", "Mini Barras Sortidas", "12 unidades de 20g", "R$ 99,90", "ou 3x de R$ 33,30 sem juros", "R$ 110,90", "12 × 20g")]
VCOR = {"Forastero": (AZUL, BRANCO), "Catongo": (BEER, PRETO), "Trinitário": (PURPLE, BRANCO), "Presente": (BORDO, BRANCO)}
CARD_LINKS = []
NAV_LINKS = []   # (id, destino)


def card_inst(parent, data, w=None):
    var_, nome, notas, preco, parc, de, pct = data
    ins = b.instance((CARDS_M if w else CARDS)["Promoção" if de else "Padrão"], parent)
    cor, fg = VCOR[var_]
    b.set(ins["nome"], characters=nome)
    b.set(ins["notas"], characters=notas)
    b.set(ins["preco"], characters=preco)
    b.set(ins["parcelas"], characters=parc)
    if de:
        b.set(ins["preco_de"], characters=de)
        pct_off = round((1 - float(preco[3:].replace(",", ".")) / float(de[3:].replace(",", "."))) * 100)
        b.set(ins["selo"], characters=f"-{pct_off}%")
    b.set(ins["Embalagem ilustrativa"], fills=[cor])
    for k_ in ("pk_marca", "pk_nome", "pk_pct", "pk_fio"):
        if fg != BRANCO:
            b.set(ins[k_], fills=[fg])
    b.set(ins["pk_nome"], characters=var_ if var_ != "Presente" else "Presente")
    b.set(ins["pk_pct"], characters=pct)
    etq_frame = ins["Varietal=Forastero"]
    b.set(etq_frame, fills=[cor])
    b.set(ins["etiqueta"], characters=var_, fills=[fg])
    CARD_LINKS.append((ins.id, bool(w)))
    return ins


def sec_title(parent, disp, eyebrow, titulo, sub):
    t = b.instance(TIT[disp], parent)
    b.set(t["eyebrow"], characters=eyebrow)
    b.set(t["titulo"], characters=titulo)
    b.set(t["subtitulo"], characters=sub)
    return t


def tile(parent, nome, desc, img, cor, fg, w=302, h=400, name=None):
    t = b.frame(parent, name or f"Bloco {nome}", w, h, layout="vertical", fill=cor)
    b.image(t, img, w, h - (88 if w > 200 else 72), name="foto")
    lb = b.frame(t, "legenda", w, 10, layout="horizontal", main="spaceBetween", cross="center", pad=[16, 20, 16, 20] if w > 200 else 12,
                 sh="fill", sv="fill")
    tx = b.frame(lb, "textos", 10, 10, layout="vertical", gap=2, sh="fill", sv="hug")
    b.text(tx, nome, "h3" if w > 200 else "rotulo", fg)
    if w > 200:
        b.text(tx, desc, "legenda", fg, fillw=True)
    icon_inst("seta-direita", lb, fg)
    return t


VARS4 = [("Forastero", "Intenso, frutado e amadeirado", MOSAICO, AZUL, BRANCO),
         ("Catongo", "O cacau branco: suave e floral", CAMPO, BEER, PRETO),
         ("Trinitário", "Frutas vermelhas e especiarias", TINTAS, PURPLE, BRANCO),
         ("Presentes", "Caixas e kits para presentear", VINHO, BORDO, BRANCO)]
REVS = [("“Dá para sentir as notas frutadas logo no primeiro pedaço. Virou o presente oficial da família.”", "Isabela M. · São Paulo", "Compra verificada · Barra Trinitário 75%"),
        ("“A caixa é linda e o Catongo é diferente de tudo que já provei. Floral, delicado.”", "Samantha R. · Rio de Janeiro", "Compra verificada · Caixa Degustação"),
        ("“Harmonizei com um tinto e foi uma experiência. Chocolate não é tudo igual mesmo.”", "Pedro A. · Belo Horizonte", "Compra verificada · Kit Harmonização")]


def ben_inst(parent, ic, t, d, w=None):
    i = b.instance(BEN[t], parent)
    if w:
        b.set(i.id, width=w)
    return i


def home_header(parent, disp, active=None):
    if disp == "Desktop":
        b.instance(TARJA, parent)
        h = b.instance(HD, parent)
    else:
        b.instance(TM[0], parent)
        h = b.instance(HM, parent)
    b.set(h.id, scrollPosition="sticky")
    if active and disp == "Desktop":
        b.set(h[f"nav_{active}"], fills=[BORDO], textDecoration="underline")
    return h


def footer(parent, disp):
    nl = b.instance(NL[disp], parent)
    b.instance(FT[disp], parent)
    b.instance(SELOS[disp], parent)


SCREENS = {}

# ---- Home Desktop -------------------------------------------------------------------
b.select_page(P_DESK)
HOME = b.frame(None, "Home · Desktop 1440", 1440, 100, layout="vertical", fill=BRANCO, sv="hug", x=0, y=0)
hh = home_header(HOME, "Desktop")
hero = b.instance(HERO_D[0], HOME)
bn = b.frame(HOME, "Benefícios (bannerTarja)", 1440, 10, layout="horizontal", gap=32, pad=[32, 80, 32, 80], sv="hug", stroke=UVA)
b.set(bn, strokeTopWeight=0, strokeBottomWeight=1, strokeLeftWeight=0, strokeRightWeight=0)
for ic, t, d in BENS:
    ben_inst(bn, ic, t, d)
vs = b.frame(HOME, "Escolha pelo varietal (Banner v2 · Grade)", 1440, 10, layout="vertical", gap=48, pad=[96, 80, 96, 80], cross="center", sv="hug")
sec_title(vs, "Desktop", "Cacau varietal", "Escolha pelo varietal", "Cada cacau tem um perfil de sabor único. Comece pelo que combina com você.")
vr = b.frame(vs, "Blocos", 1280, 400, layout="horizontal", gap=24)
for nm, d, im, cor, fg in VARS4:
    tile(vr, nm, d, im, cor, fg)
ps = b.frame(HOME, "Os preferidos de quem prova (productList)", 1440, 10, layout="vertical", gap=48, pad=[0, 80, 96, 80], cross="center", sv="hug")
sec_title(ps, "Desktop", "Mais vendidos", "Os preferidos de quem prova", "Para você provar que chocolate não é tudo igual.")
pr = b.frame(ps, "Produtos", 1280, 10, layout="horizontal", gap=24, sv="hug")
for dd in PREF:
    card_inst(pr, dd)
vt = b.instance(BTN[("Secundário", "Padrão")], ps)
b.set(vt["label"], characters="Ver todos os chocolates")
ms = b.frame(HOME, "Manifesto (htmlContent)", 1440, 10, layout="horizontal", gap=64, pad=[96, 80, 96, 80], cross="center", fill=BORDO, sv="hug")
b.image(ms, CAMPO, 616, 480, name="foto origem")
mt = b.frame(ms, "texto", 600, 10, layout="vertical", gap=24, sv="hug", sh="fill")
b.text(mt, "Nossa origem", "eyebrow", BRANCO)
b.text(mt, "Chocolate não é tudo igual", "h1", BRANCO, fillw=True)
b.text(mt, "Cada barra é o retrato de um terroir singular. Cultivamos Forastero, Catongo e Trinitário em lotes separados, há três gerações, "
           "sob as sombras acolhedoras da Mata Atlântica — e acompanhamos cada etapa, do plantio à barra.", "corpo_g", BRANCO, fillw=True)
mbt = b.instance(BTN[("Inverso", "Padrão")], mt)
b.set(mbt["label"], characters="Conheça nossa história")
NAV_LINKS.append(("origem_d", mbt.id))
pz = b.frame(HOME, "Presentes que contam histórias (productList)", 1440, 10, layout="vertical", gap=48, pad=[96, 80, 96, 80], cross="center", sv="hug")
sec_title(pz, "Desktop", "Para presentear", "Presentes que contam histórias", "Embalagens que expressam cuidado e exclusividade.")
pzr = b.frame(pz, "Produtos", 1280, 10, layout="horizontal", gap=24, sv="hug")
for dd in PRES:
    card_inst(pzr, dd)
vd = b.frame(HOME, "Vídeo sensorial (bannerVideo)", 1440, 560, fill=PRETO, clip=True)
b.image(vd, CHEF, 1440, 560, name="quadro do vídeo")
pl = b.frame(vd, "play", 96, 96, layout="horizontal", main="center", cross="center", fill=BRANCO, x=672, y=232)
icon_inst("play", pl, BORDO)
cap = b.frame(vd, "legenda", 10, 10, layout="vertical", gap=4, pad=[24, 32, 24, 32], fill=PRETO, sh="hug", sv="hug", x=80, y=400)
b.text(cap, "O snap, o aroma, o derreter.", "h3", BRANCO)
b.text(cap, "Assista · 0:45", "legenda", BRANCO)
rv = b.frame(HOME, "Avaliações (review)", 1440, 10, layout="vertical", gap=48, pad=[96, 80, 96, 80], cross="center", sv="hug")
sec_title(rv, "Desktop", "Avaliações", "Quem provou, sentiu a diferença", "4,9 de 5 · 312 avaliações")
rr = b.frame(rv, "Cards", 1280, 10, layout="horizontal", gap=32, sv="hug")
for q, a, m in REVS:
    i = b.instance(REV, rr)
    b.set(i["depoimento"], characters=q)
    b.set(i["autor"], characters=a)
    b.set(i["meta"], characters=m)
footer(HOME, "Desktop")
SCREENS["home_d"] = HOME
HOME_HDR = hh

# ---- Nossa Origem Desktop -------------------------------------------------------------
ORIG = b.frame(None, "Nossa Origem (institucional) · Desktop 1440", 1440, 100, layout="vertical", fill=BRANCO, sv="hug", x=1640, y=0)
oh = home_header(ORIG, "Desktop", active="Nossa origem")
bc = b.frame(ORIG, "Breadcrumb", 1440, 10, layout="horizontal", pad=[16, 80, 16, 80], sv="hug")
b.instance(BREAD, bc)
oh_ = b.frame(ORIG, "Abertura", 1440, 560, layout="horizontal")
ob = b.frame(oh_, "bloco", 720, 560, layout="vertical", main="center", gap=24, pad=[80, 96, 80, 80], fill=BORDO)
b.text(ob, "Nossa origem", "eyebrow", BRANCO)
b.text(ob, "Sabores que contam histórias desde 1930", "display", BRANCO, w=544)
b.text(ob, "Três gerações cultivando cacau sob as sombras acolhedoras da Mata Atlântica, no Sul da Bahia.", "corpo_g", BRANCO, w=480)
b.image(oh_, CACAU, 720, 560, name="foto cacau")
mf = b.frame(ORIG, "Manifesto", 1440, 10, layout="vertical", gap=32, pad=[96, 240, 96, 240], cross="center", sv="hug")
b.text(mf, "Manifesto", "eyebrow", BORDO)
b.text(mf, "Celebramos a essência do cacau ao chocolate.", "h1", PRETO, align="center", fillw=True)
b.text(mf, "Somos pioneiros em trazer a alma dos varietais de cacau para cada pedaço de chocolate que criamos. Honramos nossas raízes "
           "e a história que evolui a cada geração. Cada chocolate é um poema à autenticidade, à qualidade e à singularidade.",
       "corpo_g", PRETO, align="center", fillw=True)
b.text(mf, "Var chocolates é inovação, tradição e sustentabilidade. É a sofisticação no simples, a beleza no essencial, e o cuidado em cada detalhe.",
       "corpo_b", BORDO, align="center", fillw=True)
vv = b.frame(ORIG, "O que é cacau varietal", 1440, 10, layout="vertical", gap=48, pad=[0, 80, 96, 80], cross="center", sv="hug")
sec_title(vv, "Desktop", "É varietal até no nome", "O que é cacau varietal",
          "“Var” vem de varietal — termo do universo do vinho para uma variedade única. Fomos pioneiros no conceito, desde o início dos anos 2000.")
vc = b.frame(vv, "Varietais", 1280, 10, layout="horizontal", gap=32, sv="hug")
for nm, d, cor, fg in [("Forastero", "Notas mais intensas, frutadas e amadeiradas. A base de sabor marcante.", AZUL, BRANCO),
                       ("Catongo", "O raro cacau de amêndoa branca: suave, floral e delicado.", BEER, PRETO),
                       ("Trinitário", "Complexo e aromático, com frutas vermelhas e especiarias.", PURPLE, BRANCO)]:
    c = b.frame(vc, nm, 405, 10, layout="vertical", gap=0, stroke=PRETO, sv="hug", sh="fill")
    tp = b.frame(c, "faixa", 405, 120, layout="vertical", main="max", pad=24, fill=cor, sh="fill")
    b.text(tp, nm, "h3", fg)
    bd = b.frame(c, "texto", 405, 10, layout="vertical", gap=16, pad=24, sh="fill", sv="hug")
    b.text(bd, d, "corpo", PRETO, fillw=True)
    lk = b.instance(BTN[("Link", "Padrão")], bd)
    b.set(lk["label"], characters=f"Ver chocolates {nm}")
tl = b.frame(ORIG, "Três gerações (linha do tempo)", 1440, 10, layout="vertical", gap=48, pad=[96, 80, 96, 80], cross="center", fill=PRETO, sv="hug")
tt = b.instance(TIT["Desktop"], tl)
b.set(tt["eyebrow"], characters="Linha do tempo", fills=[BEER])
b.set(tt["titulo"], characters="Três gerações de cacau", fills=[BRANCO])
b.set(tt["fio"], fills=[BRANCO])
b.set(tt["subtitulo"], characters="Do plantio à barra, uma história que evolui a cada geração.", fills=[BRANCO])
tr = b.frame(tl, "Marcos", 1280, 10, layout="horizontal", gap=32, sv="hug")
for ano, tit, d in [("1930", "As raízes", "A família começa a cultivar cacau no Sul da Bahia, sob a Mata Atlântica."),
                    ("Anos 2000", "Pioneirismo varietal", "A Var introduz o conceito de cacau varietal no universo dos chocolates."),
                    ("Hoje", "Tree to bar", "Lotes separados por variedade e rastreabilidade total, do plantio à produção.")]:
    m = b.frame(tr, ano, 405, 10, layout="vertical", gap=12, sv="hug", sh="fill", stroke=BRANCO, pad=32)
    b.text(m, ano, "display", BEER)
    b.text(m, tit, "rotulo", BRANCO)
    b.text(m, d, "corpo", BRANCO, fillw=True)
pp = b.frame(ORIG, "Do plantio à barra", 1440, 10, layout="vertical", gap=48, pad=[96, 80, 96, 80], cross="center", sv="hug")
sec_title(pp, "Desktop", "Tree to bar", "Do plantio à barra", "Controle exclusivo de cada etapa para preservar a pureza genética do cacau.")
st_ = b.frame(pp, "Etapas", 1280, 10, layout="horizontal", gap=16, sv="hug")
for k, (e, d) in enumerate([("Plantio", "Lotes separados por varietal"), ("Colheita", "Frutos no ponto ideal"),
                            ("Fermentação", "Onde nascem os aromas"), ("Secagem", "Ao sol do Sul da Bahia"),
                            ("Torra", "Perfil próprio por varietal"), ("Barra", "Chocolate de origem")]):
    c = b.frame(st_, e, 200, 10, layout="vertical", gap=8, sv="hug", sh="fill", pad=[24, 0, 0, 0], stroke=BORDO, sw=2)
    b.set(c, strokeTopWeight=2, strokeBottomWeight=0, strokeLeftWeight=0, strokeRightWeight=0)
    b.text(c, f"{k + 1:02d}", "h3", BORDO)
    b.text(c, e, "rotulo", PRETO)
    b.text(c, d, "corpo_p", PRETO, fillw=True)
cta = b.frame(ORIG, "Chamada final", 1440, 10, layout="horizontal", gap=64, pad=[0, 80, 96, 80], cross="center", sv="hug")
b.image(cta, CERAMICA, 616, 400, name="foto artesanal")
ct = b.frame(cta, "texto", 600, 10, layout="vertical", gap=24, sv="hug", sh="fill")
b.text(ct, "Missão", "eyebrow", BORDO)
b.text(ct, "Revelar sabores e aromas que superam a intensidade do chocolate.", "h2", PRETO, fillw=True)
b.text(ct, "Criar chocolates finos que expressam a pureza, a autenticidade e a complexidade sensorial do DNA do cacau.", "corpo_g", PRETO, fillw=True)
cb = b.instance(BTN[("Primário", "Padrão")], ct)
b.set(cb["label"], characters="Prove a diferença")
NAV_LINKS.append(("home_d", cb.id))
footer(ORIG, "Desktop")
SCREENS["orig_d"] = ORIG

# ---- Produto Desktop -------------------------------------------------------------------
PROD = b.frame(None, "Produto · Desktop 1440", 1440, 100, layout="vertical", fill=BRANCO, sv="hug", x=3280, y=0)
ph = home_header(PROD, "Desktop", active="Chocolates")
bc = b.frame(PROD, "Breadcrumb", 1440, 10, layout="horizontal", pad=[16, 80, 16, 80], sv="hug")
bi = b.instance(BREAD, bc)
b.set(bi["atual"], characters="Chocolates  /  Barra Forastero 70%")
main = b.frame(PROD, "Produto", 1440, 10, layout="horizontal", gap=64, pad=[16, 80, 96, 80], sv="hug")
gal = b.frame(main, "Galeria", 616, 10, layout="vertical", gap=16, sv="hug")
gm_ = b.frame(gal, "foto principal", 616, 616, fill=BRANCO, stroke=UVA)
pk = b.instance(PK, gm_, x=168, y=124)
b.set(pk.id, width=280, height=368)
b.set(pk["pk_nome"], fontSize=32, lineHeight=40)
b.instance(ETQ["Forastero"], gm_, x=16, y=16)
th = b.frame(gal, "miniaturas", 616, 10, layout="horizontal", gap=16, sv="hug")
for k, im in enumerate([None, CACAU, CAMPO, CHEF]):
    if im is None:
        t_ = b.frame(th, "miniatura 1 (ativa)", 142, 142, layout="horizontal", main="center", cross="center", fill=BRANCO, stroke=BORDO, sw=2)
        p2 = b.instance(PK, t_)
        b.set(p2.id, width=72, height=100)
        b.set(p2["pk_nome"], fontSize=12, lineHeight=14)
        b.set(p2["pk_marca"], visible=False)
        b.set(p2["pk_pct"], visible=False)
        b.set(p2.id, padding=8)
    else:
        b.image(th, im, 142, 142, name=f"miniatura {k + 1}")
inf = b.frame(main, "Informações", 600, 10, layout="vertical", gap=24, sv="hug", sh="fill")
b.instance(ETQ["Forastero"], inf)
b.text(inf, "Barra Forastero 70%", "h1", PRETO, fillw=True)
rt = b.frame(inf, "avaliação", 10, 16, layout="horizontal", gap=8, cross="center", sh="hug", sv="hug")
for i in range(5):
    b.node("star", rt, f"estrela {i + 1}", w=16, h=16, fills=[BORDO])
b.text(rt, "4,9 · 128 avaliações", "legenda", PRETO, textDecoration="underline")
pv = b.frame(inf, "preço", 10, 10, layout="vertical", gap=4, sh="fill", sv="hug")
b.text(pv, "R$ 39,90", "h2", BORDO)
b.text(pv, "ou 3x de R$ 13,30 sem juros · 5% de desconto no Pix", "corpo_p", PRETO)
b.text(inf, "Intenso e elegante, com notas frutadas e amadeiradas que se revelam devagar. Cacau Forastero cultivado em lote próprio, sob a Mata Atlântica.",
       "corpo", PRETO, fillw=True)
nt = b.frame(inf, "Notas sensoriais", 10, 10, layout="vertical", gap=12, sh="fill", sv="hug")
b.text(nt, "Notas sensoriais", "rotulo", PRETO)
nr2 = b.frame(nt, "chips", 10, 10, layout="horizontal", gap=8, sh="hug", sv="hug")
for n_ in ["Frutadas", "Amadeiradas", "Cacau intenso"]:
    ch = b.frame(nr2, n_, 10, 32, layout="horizontal", pad=[8, 12, 8, 12], stroke=PRETO, sh="hug", sv="hug")
    b.text(ch, n_, "corpo_p", PRETO)
buy = b.frame(inf, "compra", 10, 48, layout="horizontal", gap=16, sh="fill", sv="hug")
b.instance(QTD, buy)
bb_ = b.instance(BTN[("Primário", "Padrão")], buy)
b.set(bb_.id, sizingH="fill")
b.set(bb_["label"], characters="Comprar")
CART_OPENERS = [bb_.id]
fav = b.instance(BTN[("Secundário", "Padrão")], inf)
b.set(fav["label"], characters="Adicionar aos favoritos")
b.set(fav.id, sizingH="fill")
fr2 = b.frame(inf, "frete", 10, 10, layout="vertical", gap=8, sh="fill", sv="hug")
b.text(fr2, "Calcule o frete", "rotulo", PRETO)
fl = b.frame(fr2, "linha", 10, 48, layout="horizontal", sh="fill", sv="hug")
fld = b.frame(fl, "cep", 300, 48, layout="horizontal", pad=[0, 16, 0, 16], cross="center", stroke=PRETO, sh="fill")
b.text(fld, "Digite seu CEP", "corpo", PRETO)
ok_ = b.instance(BTN[("Secundário", "Padrão")], fl)
b.set(ok_["label"], characters="Calcular")
acc = b.frame(inf, "Detalhes", 10, 10, layout="vertical", sh="fill", sv="hug")
for k, (t_, d_) in enumerate([("Descrição", "Barra de chocolate 70% cacau Forastero, 80g. Produzida tree to bar, com cacau de lote único."),
                              ("Harmonização", "Vinhos tintos encorpados, queijos curados e café coado."),
                              ("Ingredientes", "Massa de cacau, açúcar e manteiga de cacau. Pode conter traços de leite."),
                              ("Conservação", "Local seco e arejado, entre 18 °C e 22 °C.")]):
    a = b.frame(acc, t_, 10, 10, layout="vertical", gap=8, pad=[16, 0, 16, 0], sh="fill", sv="hug", stroke=PRETO)
    b.set(a, strokeTopWeight=1, strokeBottomWeight=1 if k == 3 else 0, strokeLeftWeight=0, strokeRightWeight=0)
    hr_ = b.frame(a, "título", 10, 24, layout="horizontal", main="spaceBetween", cross="center", sh="fill", sv="hug")
    b.text(hr_, t_, "rotulo", PRETO)
    icon_inst("menos" if k == 0 else "mais", hr_)
    if k == 0:
        b.text(a, d_, "corpo_p", PRETO, fillw=True)
rel = b.frame(PROD, "Você também vai gostar", 1440, 10, layout="vertical", gap=48, pad=[0, 80, 96, 80], cross="center", sv="hug")
sec_title(rel, "Desktop", "Combina com", "Você também vai gostar", "Outros varietais para comparar lado a lado.")
rr2 = b.frame(rel, "Produtos", 1280, 10, layout="horizontal", gap=24, sv="hug")
for dd in [PREF[1], PREF[2], PRES[0], PRES[3]]:
    card_inst(rr2, dd)
footer(PROD, "Desktop")
SCREENS["prod_d"] = PROD

# overlay de carrinho (destino do protótipo)
CART_OV = b.frame(None, "Overlay · Mini-carrinho desktop", 420, 900, x=4920, y=0, fill=BRANCO)
ci = b.instance(CART, CART_OV)

# ---- Telas Mobile ------------------------------------------------------------------------
b.select_page(P_MOB)


def mob_screen(name, x):
    return b.frame(None, name, 390, 100, layout="vertical", fill=BRANCO, sv="hug", x=x, y=0)


HOME_M = mob_screen("Home · Mobile 390", 0)
hm = home_header(HOME_M, "Mobile")
b.instance(HERO_M[0], HOME_M)
bnm = b.frame(HOME_M, "Benefícios (carrossel)", 390, 10, layout="horizontal", gap=24, pad=[24, 16, 24, 16], sv="hug", clip=True, stroke=UVA)
b.set(bnm, strokeTopWeight=0, strokeBottomWeight=1, strokeLeftWeight=0, strokeRightWeight=0, overflow="horizontal")
for ic, t, d in BENS:
    ben_inst(bnm, ic, t, d, w=260)
vm = b.frame(HOME_M, "Escolha pelo varietal", 390, 10, layout="vertical", gap=32, pad=[48, 16, 48, 16], sv="hug")
sec_title(vm, "Mobile", "Cacau varietal", "Escolha pelo varietal", "Cada cacau tem um perfil de sabor único.")
g2 = b.frame(vm, "Grade 2×2", 358, 10, layout="horizontal", gap=8, wrap=True, sv="hug", crossGap=8)
for nm, d, im, cor, fg in VARS4:
    tile(g2, nm, d, im, cor, fg, w=175, h=230)
pm = b.frame(HOME_M, "Os preferidos de quem prova", 390, 10, layout="vertical", gap=32, pad=[0, 0, 48, 16], sv="hug")
sec_title(pm, "Mobile", "Mais vendidos", "Os preferidos de quem prova", "Deslize para ver mais.")
cr_ = b.frame(pm, "Carrossel (1,5 card)", 374, 10, layout="horizontal", gap=16, sv="hug", clip=True)
b.set(cr_, overflow="horizontal")
for dd in PREF:
    card_inst(cr_, dd, w=240)
mm = b.frame(HOME_M, "Manifesto", 390, 10, layout="vertical", gap=0, fill=BORDO, sv="hug")
b.image(mm, CAMPO, 390, 260, name="foto origem")
mmt = b.frame(mm, "texto", 390, 10, layout="vertical", gap=16, pad=[32, 16, 40, 16], sh="fill", sv="hug")
b.text(mmt, "Nossa origem", "eyebrow", BRANCO)
b.text(mmt, "Chocolate não é tudo igual", "m_h1", BRANCO, fillw=True)
b.text(mmt, "Cada barra é o retrato de um terroir singular, cultivado há três gerações sob a Mata Atlântica.", "corpo", BRANCO, fillw=True)
mbm = b.instance(BTN[("Inverso", "Padrão")], mmt)
b.set(mbm["label"], characters="Conheça nossa história")
b.set(mbm.id, sizingH="fill")
NAV_LINKS.append(("origem_m", mbm.id))
pzm = b.frame(HOME_M, "Presentes", 390, 10, layout="vertical", gap=32, pad=[48, 0, 48, 16], sv="hug")
sec_title(pzm, "Mobile", "Para presentear", "Presentes que contam histórias", "Embalagens que expressam cuidado.")
cz = b.frame(pzm, "Carrossel (1,5 card)", 374, 10, layout="horizontal", gap=16, sv="hug", clip=True)
b.set(cz, overflow="horizontal")
for dd in PRES:
    card_inst(cz, dd, w=240)
vdm = b.frame(HOME_M, "Vídeo sensorial", 390, 300, fill=PRETO, clip=True)
b.image(vdm, CHEF, 390, 300, name="quadro do vídeo")
plm = b.frame(vdm, "play", 64, 64, layout="horizontal", main="center", cross="center", fill=BRANCO, x=163, y=118)
icon_inst("play", plm, BORDO)
rvm = b.frame(HOME_M, "Avaliações", 390, 10, layout="vertical", gap=32, pad=[48, 16, 48, 16], sv="hug")
sec_title(rvm, "Mobile", "Avaliações", "Quem provou, sentiu a diferença", "4,9 de 5 · 312 avaliações")
ri = b.instance(REV, rvm)
b.set(ri.id, sizingH="fill")
footer(HOME_M, "Mobile")
SCREENS["home_m"] = HOME_M

ORIG_M = mob_screen("Nossa Origem · Mobile 390", 490)
home_header(ORIG_M, "Mobile")
bcm = b.frame(ORIG_M, "Breadcrumb", 390, 10, layout="horizontal", pad=[12, 16, 12, 16], sv="hug")
b.instance(BREAD, bcm)
b.image(ORIG_M, CACAU, 390, 300, name="foto cacau")
obm = b.frame(ORIG_M, "Abertura", 390, 10, layout="vertical", gap=16, pad=[32, 16, 40, 16], fill=BORDO, sv="hug")
b.text(obm, "Nossa origem", "eyebrow", BRANCO)
b.text(obm, "Sabores que contam histórias desde 1930", "m_display", BRANCO, fillw=True)
b.text(obm, "Três gerações cultivando cacau sob a Mata Atlântica, no Sul da Bahia.", "corpo", BRANCO, fillw=True)
mfm = b.frame(ORIG_M, "Manifesto", 390, 10, layout="vertical", gap=16, pad=[48, 16, 48, 16], sv="hug")
b.text(mfm, "Manifesto", "eyebrow", BORDO)
b.text(mfm, "Celebramos a essência do cacau ao chocolate.", "m_h1", PRETO, fillw=True)
b.text(mfm, "Somos pioneiros em trazer a alma dos varietais de cacau para cada pedaço de chocolate que criamos. Cada chocolate é um poema à autenticidade, à qualidade e à singularidade.",
       "corpo", PRETO, fillw=True)
vvm = b.frame(ORIG_M, "Varietais", 390, 10, layout="vertical", gap=16, pad=[0, 16, 48, 16], sv="hug")
sec_title(vvm, "Mobile", "É varietal até no nome", "O que é cacau varietal", "“Var” vem de varietal, como no vinho.")
for nm, d, cor, fg in [("Forastero", "Intenso, frutado e amadeirado.", AZUL, BRANCO), ("Catongo", "Amêndoa branca: suave e floral.", BEER, PRETO),
                       ("Trinitário", "Frutas vermelhas e especiarias.", PURPLE, BRANCO)]:
    c = b.frame(vvm, nm, 358, 10, layout="horizontal", gap=0, stroke=PRETO, sv="hug", sh="fill")
    sw_ = b.frame(c, "cor", 96, 96, fill=cor, layout="vertical", main="max", pad=12)
    b.text(sw_, nm[:3], "rotulo", fg)
    tx = b.frame(c, "texto", 10, 10, layout="vertical", gap=4, pad=16, sh="fill", sv="hug")
    b.text(tx, nm, "rotulo", PRETO)
    b.text(tx, d, "corpo_p", PRETO, fillw=True)
tlm = b.frame(ORIG_M, "Linha do tempo", 390, 10, layout="vertical", gap=24, pad=[48, 16, 48, 16], fill=PRETO, sv="hug")
b.text(tlm, "Três gerações de cacau", "m_h2", BRANCO, fillw=True)
for ano, tit, d in [("1930", "As raízes", "Início do cultivo no Sul da Bahia."), ("Anos 2000", "Pioneirismo varietal", "O conceito de cacau varietal chega aos chocolates."),
                    ("Hoje", "Tree to bar", "Rastreabilidade total, do plantio à barra.")]:
    m = b.frame(tlm, ano, 358, 10, layout="vertical", gap=8, pad=24, stroke=BRANCO, sh="fill", sv="hug")
    b.text(m, ano, "m_display", BEER)
    b.text(m, tit, "rotulo", BRANCO)
    b.text(m, d, "corpo_p", BRANCO, fillw=True)
ctm = b.frame(ORIG_M, "Chamada final", 390, 10, layout="vertical", gap=16, pad=[48, 16, 48, 16], sv="hug")
b.text(ctm, "Revelar sabores e aromas que superam a intensidade do chocolate.", "m_h2", PRETO, fillw=True)
cbm = b.instance(BTN[("Primário", "Padrão")], ctm)
b.set(cbm["label"], characters="Prove a diferença")
b.set(cbm.id, sizingH="fill")
NAV_LINKS.append(("home_m", cbm.id))
footer(ORIG_M, "Mobile")
SCREENS["orig_m"] = ORIG_M

PROD_M = mob_screen("Produto · Mobile 390", 980)
home_header(PROD_M, "Mobile")
gmm = b.frame(PROD_M, "foto principal", 390, 390, fill=BRANCO, stroke=UVA)
pkm = b.instance(PK, gmm, x=105, y=55)
b.set(pkm.id, width=180, height=280)
b.instance(ETQ["Forastero"], gmm, x=16, y=16)
dts = b.instance(DOTS[0], gmm, x=163, y=366)
for nid in dts.all[1:]:
    b.set(nid, fills=[BORDO], strokes=[BORDO])
im_ = b.frame(PROD_M, "Informações", 390, 10, layout="vertical", gap=16, pad=[24, 16, 32, 16], sv="hug")
b.text(im_, "Barra Forastero 70%", "m_h1", PRETO, fillw=True)
b.text(im_, "R$ 39,90", "m_h2", BORDO)
b.text(im_, "ou 3x de R$ 13,30 sem juros · 5% no Pix", "corpo_p", PRETO)
b.text(im_, "Intenso e elegante, com notas frutadas e amadeiradas que se revelam devagar.", "corpo", PRETO, fillw=True)
cps = b.frame(im_, "chips", 10, 10, layout="horizontal", gap=8, sh="hug", sv="hug")
for n_ in ["Frutadas", "Amadeiradas"]:
    ch = b.frame(cps, n_, 10, 32, layout="horizontal", pad=[8, 12, 8, 12], stroke=PRETO, sh="hug", sv="hug")
    b.text(ch, n_, "corpo_p", PRETO)
for t_ in ["Harmonização", "Ingredientes", "Conservação"]:
    a = b.frame(im_, t_, 358, 48, layout="horizontal", main="spaceBetween", cross="center", sh="fill", stroke=PRETO)
    b.set(a, strokeTopWeight=1, strokeBottomWeight=0, strokeLeftWeight=0, strokeRightWeight=0)
    b.text(a, t_, "rotulo", PRETO)
    icon_inst("mais", a)
rlm = b.frame(PROD_M, "Você também vai gostar", 390, 10, layout="vertical", gap=24, pad=[24, 0, 120, 16], sv="hug")
b.text(rlm, "Você também vai gostar", "m_h2", PRETO)
crm = b.frame(rlm, "Carrossel", 374, 10, layout="horizontal", gap=16, sv="hug", clip=True)
for dd in [PREF[1], PREF[2], PRES[0]]:
    card_inst(crm, dd, w=240)
footer(PROD_M, "Mobile")
bar_ = b.frame(PROD_M, "Barra de compra fixa", 390, 10, layout="horizontal", gap=12, pad=16, fill=BRANCO, stroke=PRETO, sv="hug")
b.set(bar_, absolute=True, x=0, y=764, scrollPosition="fixed")
b.set(bar_, strokeTopWeight=1, strokeBottomWeight=0, strokeLeftWeight=0, strokeRightWeight=0)
b.instance(QTD, bar_)
bbm = b.instance(BTN[("Primário", "Padrão")], bar_)
b.set(bbm.id, sizingH="fill")
CART_OPENERS.append(bbm.id)
SCREENS["prod_m"] = PROD_M

MENU_OV = b.frame(None, "Overlay · Menu mobile", 320, 844, x=1470, y=0, fill=BRANCO)
mi = b.instance(MENU, MENU_OV)
CART_OV_M = b.frame(None, "Overlay · Mini-carrinho mobile", 390, 844, x=1890, y=0, fill=BRANCO)
cim = b.instance(CART, CART_OV_M)
b.set(cim.id, width=390, height=844)


# =============================================================================
# Protótipo: navegação
# =============================================================================
NAVP = dict(transition={"type": "dissolve"}, ms=300, easing="easeInOut")


def link(src, dest, **kw):
    o = dict(NAVP)
    o.update(kw)
    b.interaction(src, {"type": "onClick"}, {"type": "navigate", "dest": dest}, o["transition"], o["ms"], o["easing"])


link(HOME_HDR["logo"], HOME)
link(HOME_HDR["nav_Nossa origem"], ORIG)
link(HOME_HDR["nav_Chocolates"], PROD)
link(oh["logo"], HOME)
link(oh["nav_Chocolates"], PROD)
link(ph["logo"], HOME)
link(ph["nav_Nossa origem"], ORIG)
for k, sid in NAV_LINKS:
    dest = {"origem_d": ORIG, "home_d": HOME, "origem_m": ORIG_M, "home_m": HOME_M}[k]
    link(sid, dest)
for cid, mob in CARD_LINKS:
    link(cid, PROD_M if mob else PROD)
# overlays
b.interaction(HOME_HDR["sacola"], {"type": "onClick"},
              {"type": "openOverlay", "dest": CART_OV, "position": "topRight", "close_on_outside": True},
              {"type": "moveIn", "direction": "left"}, 400, "easeOut")
for o in CART_OPENERS[:1]:
    b.interaction(o, {"type": "onClick"}, {"type": "openOverlay", "dest": CART_OV, "position": "topRight", "close_on_outside": True},
                  {"type": "moveIn", "direction": "left"}, 400, "easeOut")
b.interaction(ci["Ícone/fechar"], {"type": "onClick"}, {"type": "closeOverlay"}, {"type": "moveOut", "direction": "right"}, 300, "easeIn")
b.interaction(hm["Ícone/menu"], {"type": "onClick"},
              {"type": "openOverlay", "dest": MENU_OV, "position": "topLeft", "close_on_outside": True},
              {"type": "moveIn", "direction": "right"}, 400, "easeOut")
b.interaction(mi["Ícone/fechar"], {"type": "onClick"}, {"type": "closeOverlay"}, {"type": "moveOut", "direction": "left"}, 300, "easeIn")
b.interaction(mi["m_Nossa origem"], {"type": "onClick"}, {"type": "navigate", "dest": ORIG_M}, {"type": "dissolve"}, 300, "easeInOut")
b.interaction(hm["sacola"], {"type": "onClick"},
              {"type": "openOverlay", "dest": CART_OV_M, "position": "center", "close_on_outside": True},
              {"type": "moveIn", "direction": "left"}, 400, "easeOut")
b.interaction(CART_OPENERS[1], {"type": "onClick"}, {"type": "openOverlay", "dest": CART_OV_M, "position": "center", "close_on_outside": True},
              {"type": "moveIn", "direction": "left"}, 400, "easeOut")
b.interaction(cim["Ícone/fechar"], {"type": "onClick"}, {"type": "closeOverlay"}, {"type": "moveOut", "direction": "right"}, 300, "easeIn")

STATE = dict(P_CAPA=P_CAPA, P_FUND=P_FUND, P_COMP=P_COMP, P_ANIM=P_ANIM, P_DESK=P_DESK, P_MOB=P_MOB, P_IMPL=P_IMPL,
             HOME=HOME, ORIG=ORIG, PROD=PROD, HOME_M=HOME_M, ORIG_M=ORIG_M, PROD_M=PROD_M)

exec(open("build_rest.py", encoding="utf-8").read())
b.dump(sys.argv[1] if len(sys.argv) > 1 else "ds.json")
print("comandos:", len(b.cmds), "proximo id:", b.nid)
