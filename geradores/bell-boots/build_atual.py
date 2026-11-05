# Gera o mock do site ATUAL da Bell Boots (tema China) para comparar com a proposta Lime.
# Uso: python build_atual.py atual.json  ->  python runcheck.py atual.json bell-boots-site-atual-v1.figcraft
import sys
sys.path.insert(0, "../lime-implementacao/gerador")
from fc import B

b = B()
FONTE = "Arial"          # o site usa Roboto, que não está instalada aqui
IMG = "img-atual/"
PRETO, TEXTO, CINZA_T, CINZA_L, CINZA_F = "#000000", "#212121", "#757575", "#E0E0E0", "#F5F5F5"
AZUL, VERDE, RODAPE, BRANCO = "#0D92CA", "#5BB85A", "#2A2A2A", "#FFFFFF"
LADO = 98            # container de 1200px em 1366 + 15px de padding


def T(parent, s, size=14, bold=False, color=TEXTO, w=None, fill=False, align=None, upper=False,
      lh=None, strike=False, under=False, x=0, y=0, name=None, ls=None):
    props = {"fontFamily": FONTE, "fontStyle": "Bold" if bold else "Regular", "fontSize": size,
             "lineHeight": lh or round(size * 1.4), "fill": color, "textCase": "upper" if upper else "original"}
    if align:
        props["textAlign"] = align
    if strike:
        props["textDecoration"] = "strikethrough"
    if under:
        props["textDecoration"] = "underline"
    if ls:
        props["letterSpacing"] = ls
    if w or fill:
        props["textAutoResize"] = "height"
    nid = b.node("text", parent, name or s[:30], x=x, y=y, w=w or (100 if fill else None), text=s, **props)
    if fill:
        b.set(nid, sizingH="fill")
    return nid


def row(parent, name="Linha", gap=0, pad=0, main=None, cross="center", sh="fill", sv="hug", fill=None, w=100, h=10, **kw):
    return b.frame(parent, name, w, h, layout="horizontal", gap=gap, pad=pad, main=main, cross=cross, sh=sh, sv=sv, fill=fill, **kw)


def col(parent, name="Coluna", gap=0, pad=0, main=None, cross=None, sh="fill", sv="hug", fill=None, w=100, h=10, **kw):
    return b.frame(parent, name, w, h, layout="vertical", gap=gap, pad=pad, main=main, cross=cross, sh=sh, sv=sv, fill=fill, **kw)


def secao(parent, name, pt=0, pb=0, gap=0, fill=None):
    return col(parent, name, gap=gap, pad=[pt, LADO, pb, LADO], fill=fill)


def pagina(nome, first=False):
    if first:
        b.c("page.rename", id=1, name=nome)
    else:
        b.new_page(nome)
    return col(None, nome, w=1366, sh="fixed", fill=BRANCO)


def icone(parent, kind, cor=TEXTO, size=24, sw=1.5):
    caminhos = {
        "busca": "M15 15 L21 21", "conta": "M4 21 C4 16 8 14 12 14 C16 14 20 16 20 21",
        "sacola": "M5 8 H19 V21 H5 Z M8.5 8 V6.5 C8.5 4.5 10 3 12 3 C14 3 15.5 4.5 15.5 6.5 V8",
        "email": "M3 5 H21 V19 H3 Z M3 5 L12 13 L21 5",
        "fone": "M6 3 H10 L11 8 L9 10 C10 13 12 15 15 16 L17 14 L21 15 V19 C21 20 20 21 19 21 C10 21 3 14 3 5 C3 4 4 3 6 3 Z",
        "caminhao": "M2 7 H14 V16 H2 Z M14 10 H19 L22 13 V16 H14 Z",
        "insta": "M7 3 H17 C19 3 21 5 21 7 V17 C21 19 19 21 17 21 H7 C5 21 3 19 3 17 V7 C3 5 5 3 7 3 Z M17 6.5 L17.5 6.5",
        "bota": "M3 2 H10 V10 L18 12 C22 13 25 15 25 18 H3 Z",
        "whats": "M12 3 C7 3 3 7 3 12 C3 14 4 16 4 17 L3 21 L7 20 C8 21 10 21 12 21 C17 21 21 17 21 12 C21 7 17 3 12 3 Z M9 8 C9 12 12 15 16 15",
        "predio": "M6 3 H18 V21 H6 Z M9 7 H11 M13 7 H15 M9 11 H11 M13 11 H15 M9 15 H11 M13 15 H15",
        "seta_b": "M5 9 L12 16 L19 9", "seta_c": "M5 15 L12 8 L19 15",
    }
    f = b.frame(parent, "Ícone " + kind, size, size, sh="fixed", sv="fixed")
    b.node("vector", f, kind, path=caminhos[kind], fills=[], stroke=cor, strokeWeight=sw)
    if kind == "busca":
        b.node("ellipse", f, "lente", x=3, y=3, w=12, h=12, fills=[], stroke=cor, strokeWeight=sw)
    if kind == "insta":
        b.node("ellipse", f, "lente", x=7, y=7, w=10, h=10, fills=[], stroke=cor, strokeWeight=sw)
    if kind == "conta":
        b.node("ellipse", f, "cabeça", x=8, y=3, w=8, h=8, fills=[], stroke=cor, strokeWeight=sw)
    return f


# ---- blocos do tema China ---------------------------------------------------
def topo(parent):
    t = row(parent, "Barra superior", main="space-between", pad=[0, LADO, 0, LADO], fill=PRETO, h=40, sv="fixed")
    T(t, "FALE CONOSCO", 13, False, BRANCO, ls="8%")
    T(t, "TELEFONES (16) 3705-3624      |      WHATSAPP (16) 99997-0470", 13, False, BRANCO, ls="8%")


def cabecalho(parent):
    h = b.frame(parent, "Cabeçalho (155px)", 1366, 156, fill=BRANCO, stroke="#333333", sh="fill", sv="fixed")
    nav = row(h, "Menu com ícones", gap=20, cross="min", sh="hug", sv="hug", x=410, y=56)
    for nm, ic in [("Adventure", 2), ("Botinas", 3), ("Casuais", 1), ("Motociclista", 4), ("Tênis", 2)]:
        it = col(nav, nm, gap=0, cross="center", sh="hug")
        b.image(it, IMG + "ic%d.png" % ic, 30, 30, name="Ícone " + nm, mode="fit")
        T(it, nm, 17, False, "#010101", upper=True, ls="6%")
    b.image(h, IMG + "logo.png", 100, 100, name="Logo Bell Boots", mode="fit")
    b.set(b.nid - 1, x=LADO - 15, y=28)
    for k, x in (("busca", 1097), ("conta", 1156), ("sacola", 1204)):
        f = icone(h, k, "#212121", 28, 1.2)
        b.set(f, x=x, y=68)
    badge = b.frame(h, "Contador", 16, 16, layout="horizontal", main="center", cross="center", fill=PRETO, cornerRadius=8, x=1233, y=60)
    T(badge, "0", 10, True, BRANCO)
    return h


def hero(parent):
    h = b.frame(parent, "Banner (carrossel)", 1366, 512, sh="fixed", sv="fixed", clip=True)
    b.image(h, IMG + "s0.jpg", 1366, 512, name="Banner 1", mode="fill")
    pts = row(h, "Paginação", gap=10, main="center", w=1366, sh="fixed", x=0, y=490)
    for i in range(5):
        b.frame(pts, "Ponto", 28 if i == 1 else 10, 10, fill=BRANCO, cornerRadius=5)
    return h


def titulo_secao(parent, txt):
    r = row(parent, "Título · " + txt, gap=14, pad=[30, 0, 12, 0])
    T(r, txt, 28, False, TEXTO)
    ln = b.rect(r, 10, 1, CINZA_L, name="Linha")
    b.set(ln, sizingH="fill")


def card(parent, nome, de, por, parc, u):
    c = col(parent, "Card " + nome[:24], gap=0, w=292, sh="fixed", cross="center")
    ext = "jpeg" if u in (0, 1, 12) else "jpg"
    b.image(c, IMG + "u%d.%s" % (u, ext), 252, 252, name="Foto", mode="fill")
    b.set(b.nid - 1, cornerRadius=0)
    b.frame(c, "espaço", 10, 12, sh="fixed", sv="fixed")
    sel = row(c, "Selo de frete", pad=[3, 8, 3, 8], fill=PRETO, sh="hug", cornerRadius=2)
    T(sel, "Frete grátis - capital", 11, False, BRANCO)
    b.frame(c, "espaço", 10, 24, sh="fixed", sv="fixed")
    nm = col(c, "Nome", pad=[0, 18, 0, 18], cross="center")
    T(nm, nome, 15, False, TEXTO, fill=True, align="center", lh=20)
    b.frame(c, "espaço", 10, 10, sh="fixed", sv="fixed")
    st = row(c, "Estrelas", gap=6, sh="hug")
    for _ in range(5):
        b.node("star", st, "estrela", w=13, h=13, fills=[AZUL])
    b.frame(c, "espaço", 10, 4, sh="fixed", sv="fixed")
    T(c, de, 12, False, CINZA_T, strike=True)
    T(c, por, 17, True, TEXTO)
    T(c, parc, 11, False, TEXTO)
    return c


def grade(parent, itens, cols=4, pitch=105, w=1170, gap=0):
    for i in range(0, len(itens), cols):
        r = row(parent, "Linha de produtos", gap=gap, cross="min", pad=[0, 0, pitch, 0])
        for it in itens[i:i + cols]:
            card(r, *it)


def rodape(parent):
    f = col(parent, "Rodapé", fill=RODAPE, gap=0)
    nl = row(f, "Newsletter", gap=14, main="center", pad=[30, LADO, 30, LADO])
    icone(nl, "email", BRANCO, 35, 1.5)
    T(nl, "RECEBA NOVIDADES", 28, True, BRANCO)
    b.frame(nl, "espaço", 8, 10, sh="fixed", sv="fixed")
    campo = row(nl, "Campo", pad=[0, 18, 0, 18], fill=BRANCO, w=392, h=42, sh="fixed", sv="fixed", cornerRadius=21)
    T(campo, "Insira seu e-mail", 13, False, "#6C757D")
    bt = row(nl, "Assinar", main="center", w=92, h=42, sv="fixed", sh="fixed", stroke=BRANCO, sw=2, cornerRadius=21)
    T(bt, "Assinar", 14, True, BRANCO)
    div = row(f, "Divisor", pad=[0, LADO, 0, LADO])
    ln = b.rect(div, 10, 1, "#FFFFFF1F", name="Linha")
    b.set(ln, sizingH="fill")
    info = row(f, "Colunas", gap=0, cross="min", pad=[34, LADO, 56, LADO])
    cols = [("Institucional", ["Política de privacidade", "Política de Privacidade e Proteção de Dados - Bell Boots",
                               "Política de Troca de Devolução", "Sobre Nós", "Mapa do Site"], 315),
            ("Minha Conta", ["Entre em Contato", "Meus Dados", "Meus Pedidos", "Rastrear Pedido"], 277)]
    for tt, ls_, wd in cols:
        c = col(info, tt, gap=4, w=wd, sh="fixed", pad=[0, 40, 0, 0])
        T(c, tt, 16, True, BRANCO)
        b.frame(c, "espaço", 10, 8, sh="fixed", sv="fixed")
        for l in ls_:
            T(c, l, 15, False, BRANCO, fill=True, lh=22)
    c = col(info, "Central de Atendimento", gap=4, w=298, sh="fixed", pad=[0, 20, 0, 0])
    T(c, "Central de Atendimento", 16, True, BRANCO)
    b.frame(c, "espaço", 10, 8, sh="fixed", sv="fixed")
    for ic, tx in [("email", "bellboots2@yahoo.com"), ("fone", "(16) 3705-3624"), ("whats", "(16) 99997-0470")]:
        r = row(c, tx, gap=8, sh="hug")
        icone(r, ic, BRANCO, 16, 1.2)
        T(r, tx, 15, False, BRANCO, lh=22)
    T(c, "Horário de Atendimento:", 15, False, BRANCO, lh=22)
    T(c, "De segunda a sexta-feira, das 8h às 18h (horário comercial).", 15, False, BRANCO, fill=True, lh=22)
    r = row(c, "Endereço", gap=8, sh="fill", cross="min")
    icone(r, "predio", BRANCO, 16, 1.2)
    T(r, "Rua Luis Alves Batista, 580 Vila Exposição - Franca - SP CEP: 14.405-424", 15, False, BRANCO, fill=True, lh=22)
    c = col(info, "Redes", gap=10, w=210, sh="fixed")
    T(c, "Siga nossas Redes", 16, True, BRANCO)
    icone(c, "insta", BRANCO, 24, 1.8)
    pg = col(f, "Formas de pagamento", gap=10, fill=BRANCO, pad=[8, LADO, 18, LADO], cross="center")
    T(pg, "Formas de Pagamento", 15, False, TEXTO, ls="6%")
    r = row(pg, "Meios", gap=14, main="center", sh="hug")
    for m, wd in [("◆ pix", 0), ("BOLETO", 0), ("VISA", 0), ("●●", 0), ("AMERICAN EXPRESS", 0), ("◍", 0), ("Hipercard", 0), ("Aura", 0)]:
        T(r, m, 13 if len(m) > 3 else 15, True, "#6B6B6B")
    dv = row(f, "Divisor claro", pad=[0, LADO, 0, LADO], fill=BRANCO)
    ln = b.rect(dv, 10, 1, CINZA_L, name="Linha")
    b.set(ln, sizingH="fill")
    lg = col(f, "Legal", gap=3, fill=BRANCO, pad=[18, LADO, 22, LADO], cross="center")
    T(lg, "BELLBOOT 2026. Todos os direitos reservados - Rua Luis Alves Batista, 580 - Vila Exposição - Franca - SP - CEP: 14.405-424",
      10, False, TEXTO, fill=True, align="center", lh=14)
    T(lg, "J. J. DUARTE DA SILVA - CNPJ: 25.108.148/0001-75 / Franca - SP.", 10, False, TEXTO, fill=True, align="center", lh=14)
    t = row(lg, "Tecnologia Irroba", gap=4, sh="hug", pad=[6, 0, 0, 0])
    T(t, "Tecnologia", 10, False, TEXTO)
    T(t, "irroba", 15, True, "#F4511E")


def breadcrumb(parent, itens):
    s = secao(parent, "Breadcrumb", pt=22, pb=10)
    r = row(s, "Trilha", gap=8, sh="hug")
    for i, it in enumerate(itens):
        T(r, it, 11, False, TEXTO)
        if i < len(itens) - 1:
            T(r, "/", 11, False, CINZA_T)


# ---- dados (lidos do site em 05/11/2026) -------------------------------------
def C(nome, de, por, parc, u):
    return (nome, "R$ " + de, "R$ " + por, parc, u)


P9, P10, P8 = "9x de R$ 22,22 sem juros", "10x de R$ 25,00 sem juros", "10x de R$ 25,99 sem juros"
LANC = [C("TENIS ADVENTURE INTRUDER 4800-COURO LEGITIMO -BRAN...", "299,99", "199,99", P9, 0),
        C("BOTA MOTOCICLISTA IRON 3000 | COURO LEGÍTIMO EMBO...", "359,90", "259,90", P8, 1),
        C("BOTA MOTOCICLISTA IRON 3100 - COURO LEGITIMO LÁTEG...", "299,99", "199,99", P9, 2),
        C("TÊNIS ADVENTURE INTRUDER 4800- COURO LEGITIMO- OLI...", "299,99", "199,99", P9, 3),
        C("TÊNIS ADVENTURE INTRUDER 4800- COURO LEGITIMO -GRA...", "299,99", "199,99", P9, 4),
        C("BOTA ADVENTURE 900 COURO LEGITIMO - OLIVA - 35", "299,99", "249,99", P10, 5),
        C("TÊNIS ADVENTURE INTRUDER 4800- COURO LEGITIMO-PRET...", "299,99", "199,99", P9, 6),
        C("TENIS ADVENTURE INTRUDER 4800 -COURO LEGITIMO-CINZ...", "299,99", "199,99", P9, 7)]
PROMO = [C("BOTA CASUAL URBAN 880 | COURO LEGÍTIMO - PRETO - 4", "299,00", "249,00", "10x de R$ 24,90 sem juros", 8),
         C("BOTA MOTOCICLISTA IRON 3000 | COURO LEGÍTIMO - PRE...", "359,90", "259,90", P8, 9),
         C("BOTA MOTOCICLISTA XTREME 2030 COURO LEGÍTIMO - CHO...", "300,00", "200,00", "10x de R$ 20,00 sem juros", 10)]
for nm, u in [("BRAN", 11), ("GRAF", 12), ("BORD", 13), ("CAFÉ", 14), ("CAMU", 15)]:
    PROMO.append(C("BOTA MOTOCICLISTA ESPID 3500 COURO LEGÍTIMO - %s..." % nm, "299,99", "199,99", P9, u))
for nm, u in [("CAFÉ - 31", 16), ("MILHO - 32", 17), ("GRAFITE - 33", 18), ("PRETO - 34", 19), ("OLIVA - 35", 5)]:
    PROMO.append(C("BOTA ADVENTURE 900 COURO LEGÍTIMO - " + nm, "299,99", "249,99", P10, u))
PROMO += [C("BOTA MOTOCICLISTA IRON 3100 - COURO LEGITIMO LÁTEG...", "299,99", "199,99", P9, 2),
          C("TÊNIS ADVENTURE INTRUDER 4800- COURO LEGITIMO -GRA...", "299,99", "199,99", P9, 4),
          C("TÊNIS ADVENTURE INTRUDER 4800- COURO LEGITIMO-PRET...", "299,99", "199,99", P9, 6),
          C("TÊNIS ADVENTURE INTRUDER 4800- COURO LEGITIMO- OLI...", "299,99", "199,99", P9, 3),
          C("TENIS ADVENTURE INTRUDER 4800-COURO LEGITIMO -BRAN...", "299,99", "199,99", P9, 0),
          C("TENIS ADVENTURE INTRUDER 4800 -COURO LEGITIMO-CINZ...", "299,99", "199,99", P9, 7),
          C("BOTA MOTOCICLISTA IRON 3000 | COURO LEGÍTIMO EMBO...", "359,90", "259,90", P8, 1)]

# =============================================================================
# 1. Home
# =============================================================================
pg = pagina("01 · Home (atual)", first=True)
topo(pg)
cabecalho(pg)
hero(pg)
s = secao(pg, "Vitrines", pb=40)
titulo_secao(s, "Lançamentos")
grade(s, LANC)
titulo_secao(s, "Promoção")
grade(s, PROMO)
rodape(pg)

# =============================================================================
# 2. Produto
# =============================================================================
pg = pagina("02 · Produto (atual)")
topo(pg)
cabecalho(pg)
breadcrumb(pg, ["BELLBOOT", "Tênis", "Tênis Adventure Intruder 4800- Couro Legitimo- Oliva"])
s = secao(pg, "Produto", pt=16, pb=0)
cols = row(s, "Foto e compra", gap=0, cross="min")
esq = col(cols, "Galeria", gap=14, w=640, sh="fixed", cross="center")
b.image(esq, "img-cliente/p4800-oliva.jpg", 571, 571, name="Foto principal", mode="fill")
th = row(esq, "Miniaturas", gap=12, sh="hug")
for fn in ["p4800-oliva-1", "p4800-oliva-2", "p4800-oliva-3", "p4800-oliva-4", "p4800-oliva-5"]:
    b.image(th, "img-cliente/" + fn + ".jpg", 70, 70, name="Miniatura", mode="fill")
dir_ = col(cols, "Compra", gap=8, pad=[0, 0, 0, 20])
T(dir_, "Tênis Adventure Intruder 4800- Couro Legitimo- Oliva", 24, False, TEXTO, fill=True, lh=28)
T(dir_, "Ref.: 33", 11, False, TEXTO)
T(dir_, "Disponibilidade: Pronta Entrega", 11, False, TEXTO)
av = row(dir_, "Avaliação", gap=6, sh="hug")
for _ in range(5):
    b.node("star", av, "estrela", w=12, h=12, fills=[], stroke="#9E9E9E", strokeWeight=1)
T(av, "Avaliar este produto", 11, False, TEXTO, under=True)
b.frame(dir_, "espaço", 10, 6, sh="fixed", sv="fixed")
T(dir_, "ESCOLHA A COR", 12, True, TEXTO)
sw = row(dir_, "Cores", gap=6, sh="hug")
for i, fn in enumerate(["p4800-cinza", "p4800-preto", "p4800-oliva", "p4800-branco", "p4800-grafite"]):
    q = b.frame(sw, "Cor " + fn, 60, 60, stroke="#333333" if i == 0 else None, sh="fixed", sv="fixed", clip=True)
    b.image(q, "img-cliente/" + fn + ".jpg", 56, 56, name="Cor", mode="fill")
    b.set(b.nid - 1, x=2, y=2)
b.frame(dir_, "espaço", 10, 6, sh="fixed", sv="fixed")
T(dir_, "Calçados Adulto", 13, True, TEXTO)
tm = row(dir_, "Tamanhos", gap=6, sh="hug")
for n in range(37, 46):
    q = b.frame(tm, "Tam " + str(n), 30, 30, layout="horizontal", main="center", cross="center", fill=CINZA_F, sh="fixed", sv="fixed")
    T(q, str(n), 12, True, TEXTO)
fr = row(dir_, "Selo", pad=[4, 8, 4, 8], fill="#9E9E9E", sh="hug")
T(fr, "FRETE GRÁTIS - capital", 13, True, BRANCO)
gm = row(dir_, "Guia de medidas", gap=6, sh="hug")
icone(gm, "caminhao", TEXTO, 14, 1)
T(gm, "Guia de Medidas", 12, False, TEXTO, under=True)
b.frame(dir_, "espaço", 10, 8, sh="fixed", sv="fixed")
T(dir_, "De R$ 299,99", 12, False, CINZA_T, strike=True)
T(dir_, "Por R$ 199,99", 24, True, TEXTO)
T(dir_, "ou R$ 179,99 à vista no boleto", 12, False, TEXTO)
b.frame(dir_, "espaço", 10, 8, sh="fixed", sv="fixed")
q = row(dir_, "Quantidade", gap=8, sh="hug")
T(q, "Quantidade:", 12, False, TEXTO)
bx = row(q, "Campo", main="center", w=56, h=40, sh="fixed", sv="fixed", stroke=CINZA_L)
T(bx, "1", 12, True, TEXTO)
bt = row(dir_, "Botão comprar", main="center", w=260, h=50, sh="fixed", sv="fixed", fill=VERDE)
T(bt, "CLIQUE PARA COMPRAR", 13, False, BRANCO)
fr = row(dir_, "Calcular frete", main="space-between", w=260, sh="fixed", cross="center")
g = row(fr, "Título", gap=6, sh="hug")
icone(g, "caminhao", "#757575", 20, 1)
T(g, "Calcular frete", 12, True, "#555555")
T(fr, "Não sei meu CEP", 10, False, AZUL)
cep = row(dir_, "CEP", gap=8, sh="hug")
cc = row(cep, "Campo", pad=[0, 10, 0, 10], w=190, h=40, sh="fixed", sv="fixed", stroke=CINZA_L)
T(cc, "Digite seu CEP", 10, False, CINZA_T)
cb = row(cep, "Calcular", main="center", w=122, h=40, sh="fixed", sv="fixed", fill="#2A2A2A")
T(cb, "Calcular", 14, False, BRANCO)

d = secao(pg, "Detalhes do produto", pt=34, pb=40, gap=14)
T(d, "DETALHES DO PRODUTO", 20, False, TEXTO)
b.image(d, "img-cliente/p4800-oliva-1.jpg", 870, 870, name="Foto da descrição", mode="fill")
b.set(b.nid - 1, x=0)
T(d, "Nosso Tênis Intruder e feito para você que gosta de se aventura {trabalhar ou passar }com muito conforto e com grande estilo.\n"
     " O Tênis 4800 e feito em couro animal legitimo de alta qualidade em acabamento nobuck ,trazendo uma ótima durabilidade para o calçado e uma ótima resistência .\n"
     " Tênis Adventure contem um solado 100% em borracha deixando o calçado muito mais resistente e muito mais confortável e com uma ótima durabilidade, não podemos deixa de falar  que o solado é ante derrapante e que contem canal de blaqueação deixado a sola com maior durabilidade e muito mais seguro.\n"
     "Nossa palmilha e feita material pu uma material de alta qualidade que traz um ótimo conforto para o calçado .",
  14, False, TEXTO, fill=True, lh=20)
b.image(d, "img-atual/tabela.png", 585, 585, name="Tabela de medidas", mode="fill")
T(d, "Discrição técnica\nCabedal em couro Legítimo\nSolado emborrachado antiderrapante.\nPalmilha anatômica com amortecimento.\nFechamento em cadarço.",
  14, False, TEXTO, fill=True, lh=20)
rodape(pg)

# =============================================================================
# 3. Categoria
# =============================================================================
pg = pagina("03 · Categoria (atual)")
topo(pg)
cabecalho(pg)
breadcrumb(pg, ["BELLBOOT", "Tênis"])
s = secao(pg, "Categoria", pt=14, pb=40)
T(s, "Tênis", 28, False, TEXTO)
b.frame(s, "espaço", 10, 52, sh="fixed", sv="fixed")
cols = row(s, "Filtros e produtos", gap=0, cross="min")
fl = col(cols, "Filtros", gap=10, w=300, sh="fixed", pad=[0, 30, 0, 0])
T(fl, "Filtros", 18, False, TEXTO)
b1 = col(fl, "Categoria", gap=10, pad=[14, 15, 18, 15], fill=CINZA_F)
T(b1, "Tênis", 13, True, TEXTO)
b.rect(b1, 150, 1, CINZA_L, name="Linha")
b.set(b.nid - 1, sizingH="fixed")
b2 = row(fl, "Faixa de Preço", main="space-between", pad=[14, 15, 14, 24], fill=CINZA_F)
T(b2, "Faixa de Preço", 13, True, "#444444")
icone(b2, "seta_b", "#BDBDBD", 16, 1)
dirc = col(cols, "Produtos", gap=0, w=880, sh="fixed")
CAT = [LANC[6], LANC[3], LANC[0], LANC[7], LANC[4]]
for i in range(0, 5, 3):
    r = row(dirc, "Linha de produtos", gap=0, cross="min", pad=[0, 0, 135, 0])
    for it in CAT[i:i + 3]:
        card(r, *it)
rodape(pg)

exec(open("mobile_atual.py",encoding="utf-8").read())
b.dump(sys.argv[1] if len(sys.argv) > 1 else "atual.json")
