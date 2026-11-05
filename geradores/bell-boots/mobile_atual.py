# =============================================================================
# MOBILE (390px): medido no site real em largura de celular
# (trecho executado dentro de build_atual.py via exec)
# =============================================================================
LM = 15


def pagina_m(nome):
    b.new_page(nome)
    return col(None, nome, w=390, sh="fixed", fill=BRANCO)


def secao_m(parent, name, pt=0, pb=0, gap=0, fill=None):
    return col(parent, name, gap=gap, pad=[pt, LM, pb, LM], fill=fill)


def hamburguer(parent, cor="#000000"):
    f = b.frame(parent, "Menu hambúrguer", 24, 24, sh="fixed", sv="fixed")
    b.node("vector", f, "linhas", path="M2 5 H22 M2 12 H22 M2 19 H22", fills=[], stroke=cor, strokeWeight=2.2)
    return f


def cabecalho_m(parent):
    h = col(parent, "Cabeçalho mobile", fill=BRANCO, gap=0)
    l1 = b.frame(h, "Linha 1", 390, 56, fill=BRANCO, sh="fill", sv="fixed")
    hb = hamburguer(l1)
    b.set(hb, x=LM, y=16)
    b.image(l1, IMG + "logo.png", 90, 40, name="Logo Bell Boots", mode="fit")
    b.set(b.nid - 1, x=150, y=8)
    sc = icone(l1, "sacola", "#212121", 26, 1.2)
    b.set(sc, x=390 - LM - 26, y=15)
    l2 = row(h, "Busca", pad=[0, LM, 12, LM])
    cp = row(l2, "Campo de busca", pad=[0, 10, 0, 10], h=36, sv="fixed", stroke=CINZA_L, main="space-between")
    T(cp, "O que você procura hoje?", 12, False, "#9E9E9E")
    icone(cp, "busca", "#000000", 18, 1.8)
    return h


def hero_m(parent):
    h = b.frame(parent, "Banner (carrossel)", 390, 146, sh="fixed", sv="fixed", clip=True)
    b.image(h, IMG + "s0.jpg", 390, 146, name="Banner 1", mode="fill")
    pts = row(h, "Paginação", gap=6, main="center", w=390, sh="fixed", x=0, y=118)
    for i in range(5):
        b.frame(pts, "Ponto", 16 if i == 1 else 7, 7, fill=BRANCO, cornerRadius=4)
    return h


def titulo_m(parent, txt):
    r = row(parent, "Título · " + txt, gap=10, pad=[28, 0, 14, 0])
    T(r, txt, 24, False, TEXTO)
    ln = b.rect(r, 10, 1, CINZA_L, name="Linha")
    b.set(ln, sizingH="fill")


def card_m(parent, nome, de, por, parc, u):
    c = col(parent, "Card " + nome[:24], gap=0, w=180, sh="fixed", cross="center", pad=[0, 0, 40, 0])
    ext = "jpeg" if u in (0, 1, 12) else "jpg"
    b.image(c, IMG + "u%d.%s" % (u, ext), 150, 150, name="Foto", mode="fill")
    b.frame(c, "espaço", 10, 8, sh="fixed", sv="fixed")
    sel = row(c, "Selo de frete", pad=[2, 6, 2, 6], fill=PRETO, sh="hug", cornerRadius=2)
    T(sel, "Frete grátis - capital", 10, False, BRANCO)
    b.frame(c, "espaço", 10, 14, sh="fixed", sv="fixed")
    nm = col(c, "Nome", pad=[0, 8, 0, 8], cross="center")
    T(nm, nome, 13, False, TEXTO, fill=True, align="center", lh=17)
    b.frame(c, "espaço", 10, 8, sh="fixed", sv="fixed")
    st = row(c, "Estrelas", gap=4, sh="hug")
    for _ in range(5):
        b.node("star", st, "estrela", w=12, h=12, fills=[AZUL])
    b.frame(c, "espaço", 10, 3, sh="fixed", sv="fixed")
    T(c, de, 11, False, CINZA_T, strike=True)
    T(c, por, 15, True, TEXTO)
    T(c, parc.replace(" sem juros", ""), 10, False, TEXTO)
    T(c, "sem juros", 10, False, TEXTO)
    b.frame(c, "espaço", 10, 8, sh="fixed", sv="fixed")
    bt = row(c, "Comprar", main="center", w=136, h=34, sh="fixed", sv="fixed", fill=CINZA_L)
    T(bt, "COMPRAR", 12, False, TEXTO)
    return c


def grade_m(parent, itens):
    for i in range(0, len(itens), 2):
        r = row(parent, "Linha de produtos", gap=0, cross="min", main="space-between")
        for it in itens[i:i + 2]:
            card_m(r, *it)


def acordeao(parent, titulo):
    c = col(parent, "Grupo " + titulo, gap=0)
    r = row(c, titulo, main="space-between", pad=[14, LM, 14, LM])
    T(r, titulo, 15, True, BRANCO)
    icone(r, "seta_b", BRANCO, 18, 1.5)
    d = row(c, "Divisor", pad=[0, LM, 0, LM])
    b.set(b.rect(d, 10, 1, "#FFFFFF1F", name="Linha"), sizingH="fill")


def rodape_m(parent):
    f = col(parent, "Rodapé mobile", fill=RODAPE, gap=0)
    nl = col(f, "Newsletter", gap=12, pad=[26, LM, 26, LM], cross="center")
    icone(nl, "email", BRANCO, 32, 1.5)
    T(nl, "RECEBA NOVIDADES", 22, True, BRANCO)
    campo = row(nl, "Campo", pad=[0, 16, 0, 16], fill=BRANCO, h=42, sv="fixed", cornerRadius=21)
    T(campo, "Insira seu e-mail", 13, False, "#6C757D")
    bt = row(nl, "Assinar", main="center", w=110, h=38, sv="fixed", sh="fixed", stroke=BRANCO, sw=2, cornerRadius=19)
    T(bt, "Assinar", 14, True, BRANCO)
    d = row(f, "Divisor", pad=[0, LM, 0, LM])
    b.set(b.rect(d, 10, 1, "#FFFFFF1F", name="Linha"), sizingH="fill")
    acordeao(f, "Institucional")
    acordeao(f, "Minha Conta")
    acordeao(f, "Central de Atendimento")
    redes = row(f, "Redes", gap=10, pad=[16, LM, 22, LM])
    T(redes, "Siga nossas Redes", 15, True, BRANCO)
    icone(redes, "insta", BRANCO, 22, 1.8)
    pg_ = col(f, "Formas de pagamento", gap=8, fill=BRANCO, pad=[10, LM, 14, LM], cross="center")
    T(pg_, "Formas de Pagamento", 13, False, TEXTO, ls="6%")
    r = row(pg_, "Meios", gap=10, main="center", sh="hug")
    for m in ["◆ pix", "BOLETO", "VISA", "●●", "AMEX", "Hipercard"]:
        T(r, m, 12, True, "#6B6B6B")
    lg = col(f, "Legal", gap=3, fill=BRANCO, pad=[12, LM, 18, LM], cross="center")
    T(lg, "BELLBOOT 2026. Todos os direitos reservados - Rua Luis Alves Batista, 580 - Vila Exposição - Franca - SP - CEP: 14.405-424",
      10, False, TEXTO, fill=True, align="center", lh=14)
    T(lg, "J. J. DUARTE DA SILVA - CNPJ: 25.108.148/0001-75 / Franca - SP.", 10, False, TEXTO, fill=True, align="center", lh=14)
    t = row(lg, "Tecnologia Irroba", gap=4, sh="hug", pad=[6, 0, 0, 0])
    T(t, "Tecnologia", 10, False, TEXTO)
    T(t, "irroba", 15, True, "#F4511E")


def breadcrumb_m(parent, itens):
    s = secao_m(parent, "Breadcrumb", pt=10, pb=8)
    r = row(s, "Trilha", gap=6, sh="fill", wrap=True)
    for i, it in enumerate(itens):
        T(r, it, 11, False, TEXTO)
        if i < len(itens) - 1:
            T(r, "/", 11, False, CINZA_T)


# ---- Home mobile ---------------------------------------------------------------
pg = pagina_m("04 · Home mobile (atual)")
cabecalho_m(pg)
hero_m(pg)
s = secao_m(pg, "Vitrines", pb=30)
titulo_m(s, "Lançamentos")
grade_m(s, LANC)
titulo_m(s, "Promoção")
grade_m(s, PROMO[:8])
rodape_m(pg)

# ---- Produto mobile ------------------------------------------------------------
pg = pagina_m("05 · Produto mobile (atual)")
cabecalho_m(pg)
breadcrumb_m(pg, ["BELLBOOT", "Tênis", "Tênis Adventure Intruder 4800- Couro Legitimo- Oliva"])
s = secao_m(pg, "Produto", pt=6, gap=12)
b.image(s, "img-cliente/p4800-oliva.jpg", 360, 360, name="Foto principal", mode="fill")
th = row(s, "Miniaturas", gap=8, main="center")
for fn in ["p4800-oliva-1", "p4800-oliva-2", "p4800-oliva-3", "p4800-oliva-4", "p4800-oliva-5"]:
    b.image(th, "img-cliente/" + fn + ".jpg", 62, 62, name="Miniatura", mode="fill")
T(s, "Tênis Adventure Intruder 4800- Couro Legitimo- Oliva", 22, False, TEXTO, fill=True, lh=26)
T(s, "Ref.: 33", 11, False, TEXTO)
T(s, "Disponibilidade: Pronta Entrega", 11, False, TEXTO)
av = row(s, "Avaliação", gap=5, sh="hug")
for _ in range(5):
    b.node("star", av, "estrela", w=12, h=12, fills=[], stroke="#9E9E9E", strokeWeight=1)
T(av, "Avaliar este produto", 11, False, TEXTO, under=True)
T(s, "ESCOLHA A COR", 12, True, TEXTO)
sw = row(s, "Cores", gap=6, sh="fill", wrap=True)
for i, fn in enumerate(["p4800-cinza", "p4800-preto", "p4800-oliva", "p4800-branco", "p4800-grafite"]):
    q = b.frame(sw, "Cor " + fn, 66, 66, stroke="#333333" if i == 0 else None, sh="fixed", sv="fixed", clip=True)
    b.image(q, "img-cliente/" + fn + ".jpg", 62, 62, name="Cor", mode="fill")
    b.set(b.nid - 1, x=2, y=2)
T(s, "Calçados Adulto", 13, True, TEXTO)
tm = row(s, "Tamanhos", gap=6, sh="fill", wrap=True)
for n in range(37, 46):
    q = b.frame(tm, "Tam " + str(n), 36, 36, layout="horizontal", main="center", cross="center", fill=CINZA_F, sh="fixed", sv="fixed")
    T(q, str(n), 13, True, TEXTO)
fr = row(s, "Selo", pad=[4, 8, 4, 8], fill="#9E9E9E", sh="hug")
T(fr, "FRETE GRÁTIS - capital", 12, True, BRANCO)
gm = row(s, "Guia de medidas", gap=6, sh="hug")
icone(gm, "caminhao", TEXTO, 14, 1)
T(gm, "Guia de Medidas", 12, False, TEXTO, under=True)
T(s, "De R$ 299,99", 12, False, CINZA_T, strike=True)
T(s, "Por R$ 199,99", 26, True, TEXTO)
T(s, "ou R$ 179,99 à vista no boleto", 12, False, TEXTO)
qb = row(s, "Quantidade e comprar", gap=12, cross="center")
q = col(qb, "Quantidade", gap=2, sh="hug")
T(q, "Quantidade:", 11, False, TEXTO)
bx = row(q, "Campo", main="center", w=60, h=40, sh="fixed", sv="fixed", stroke=CINZA_L)
T(bx, "1", 13, True, TEXTO)
bt = row(qb, "Botão comprar", main="center", h=55, sv="fixed", fill=VERDE)
T(bt, "CLIQUE PARA COMPRAR", 13, False, BRANCO)
g = row(s, "Calcular frete", gap=6, sh="hug")
icone(g, "caminhao", "#757575", 20, 1)
T(g, "Calcular frete", 12, True, "#555555")
cep = row(s, "CEP", gap=8)
cc = row(cep, "Campo", pad=[0, 10, 0, 10], h=40, sv="fixed", stroke=CINZA_L)
T(cc, "Digite seu CEP", 11, False, CINZA_T)
cb = row(cep, "Calcular", main="center", w=110, h=40, sh="fixed", sv="fixed", fill="#2A2A2A")
T(cb, "Calcular", 14, False, BRANCO)
d = secao_m(pg, "Detalhes do produto", pt=26, pb=34, gap=12)
T(d, "DETALHES DO PRODUTO", 18, False, TEXTO)
b.image(d, "img-cliente/p4800-oliva-1.jpg", 360, 360, name="Foto da descrição", mode="fill")
T(d, "Nosso Tênis Intruder e feito para você que gosta de se aventura {trabalhar ou passar }com muito conforto e com grande estilo.\n"
     " O Tênis 4800 e feito em couro animal legitimo de alta qualidade em acabamento nobuck ,trazendo uma ótima durabilidade para o calçado e uma ótima resistência .\n"
     " Tênis Adventure contem um solado 100% em borracha deixando o calçado muito mais resistente e muito mais confortável e com uma ótima durabilidade.",
  13, False, TEXTO, fill=True, lh=19)
b.image(d, "img-atual/tabela.png", 360, 360, name="Tabela de medidas", mode="fill")
rodape_m(pg)

# ---- Categoria mobile ----------------------------------------------------------
pg = pagina_m("06 · Categoria mobile (atual)")
cabecalho_m(pg)
breadcrumb_m(pg, ["BELLBOOT", "Tênis"])
s = secao_m(pg, "Categoria", pt=6, pb=30, gap=14)
T(s, "Tênis", 26, False, TEXTO)
fb = row(s, "Filtros", main="space-between", pad=[0, 14, 0, 14], h=42, sv="fixed", fill=CINZA_F)
T(fb, "Filtros", 14, True, "#444444")
icone(fb, "seta_b", "#9E9E9E", 18, 1.2)
grade_m(s, CAT)
rodape_m(pg)
