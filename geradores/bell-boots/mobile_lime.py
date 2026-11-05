# Páginas mobile (390px) da proposta Lime. Executado dentro de build.py via exec.
LM = 16


def pagina_m(nome):
    b.new_page(nome)
    return col(None, nome, w=390, sh="fixed", fill=CREME)


def secao_m(parent, name, pv=28, gap=16, fill=None, pt=None, pb=None):
    return col(parent, name, gap=gap, pad=[pv if pt is None else pt, LM, pv if pb is None else pb, LM], fill=fill)


def hamburguer(parent, cor=BRANCO):
    f = b.frame(parent, "Menu", 44, 44, layout="horizontal", main="center", cross="center", fill=ESCURO2, cornerRadius=RAIO)
    g = b.frame(f, "linhas", 22, 22, sh="fixed", sv="fixed")
    b.node("vector", g, "linhas", path="M3 6 H21 M3 12 H21 M3 18 H21", fills=[], stroke=cor, strokeWeight=1.8)


def tarja_m(parent):
    f = row(parent, "Tarja informativa", main="center", pad=[0, LM, 0, LM], fill=LARANJA, h=32, sv="fixed")
    T(f, "FRETE GRÁTIS PARA A CAPITAL  ·  9X SEM JUROS", 11, True, CARVAO, ls="6%")


def cabecalho_m(parent):
    h = col(parent, "Cabeçalho mobile", fill=CARVAO, gap=0)
    l1 = row(h, "Linha 1", main="space-between", pad=[10, LM, 10, LM])
    hamburguer(l1)
    b.image(l1, IMG + "logo-nova-branca.png", 100, 44, name="Logo Bell Boots", mode="fit")
    ic = row(l1, "Ícones", gap=8, sh="hug")
    for k in ("busca", "sacola"):
        c = b.frame(ic, "Botão " + k, 44, 44, layout="horizontal", main="center", cross="center", fill=ESCURO2, cornerRadius=RAIO)
        icone(c, k, BRANCO, 22)
    return h


def card_m(parent, w, nome, de, por, parc, badge=None, img=None):
    c = col(parent, "Card " + nome[:24], gap=8, w=w, sh="fixed", fill=BRANCO)
    ph = foto(c, w, w, img=img)
    if badge:
        etiqueta(ph, badge, LARANJA, CARVAO, x=8, y=8, size=11)
    etiqueta(ph, "Frete grátis", CARVAO, BRANCO, x=8, y=w - 28, size=10)
    info = col(c, "Info", gap=5, pad=[0, 2, 2, 2])
    T(info, nome, 13, True, fill=True, lh=17)
    estrelas(info, 5, 11)
    T(info, de, 11, False, CINZA_T, strike=True)
    T(info, por, 20, True, CARVAO, title=True)
    T(info, parc, 11, False, CINZA_T, fill=True)
    botao(info, "Comprar", "primario", sh="fill", h=40, size=12)
    return c


def grade_m(parent, itens, w=171):
    for i in range(0, len(itens), 2):
        r = row(parent, "Linha de cards", gap=16, cross="min")
        for it in itens[i:i + 2]:
            card_m(r, w, *it)


def titulo_m(parent, txt, link=True):
    r = row(parent, "Título da seção", main="space-between", cross="max")
    T(r, txt, 24, True, CARVAO, title=True, upper=True, ls="2%")
    if link:
        T(r, "Ver todos", 12, True, LARANJA, upper=True, ls="6%")


def newsletter_m(parent):
    s = secao_m(parent, "Newsletter", pv=24)
    f = col(s, "Newsletter", gap=14, pad=[24, 20, 24, 20], fill=LARANJA, cornerRadius=RAIO)
    T(f, "Novidades", 28, True, CARVAO, title=True, upper=True)
    T(f, "Receba lançamentos e ofertas em primeira mão.", 14, False, CARVAO, fill=True)
    campo = row(f, "Campo", pad=[0, 16, 0, 16], fill=BRANCO, h=48, sv="fixed", cornerRadius=RAIO)
    T(campo, "Seu melhor e-mail", 14, False, CINZA_T)
    botao(f, "Enviar", "escuro", sh="fill")


def acordeao_m(parent, titulo):
    r = row(parent, titulo, main="space-between", pad=[16, LM, 16, LM])
    T(r, titulo, 13, True, LARANJA, upper=True, ls="8%")
    T(r, "+", 20, False, BRANCO)
    d = row(parent, "Divisor", pad=[0, LM, 0, LM])
    b.set(b.rect(d, 10, 1, "#FFFFFF1F", name="Linha"), sizingH="fill")


def rodape_m(parent):
    f = col(parent, "Rodapé mobile", fill=CARVAO, gap=0)
    for tt in ("Institucional", "Minha conta", "Atendimento"):
        acordeao_m(f, tt)
    at = col(f, "Contato", gap=6, pad=[16, LM, 18, LM])
    T(at, "(16) 3705-3624", 14, False, BRANCO)
    T(at, "WhatsApp (16) 99997-0470", 14, False, BRANCO)
    T(at, "Seg a sex, das 8h às 18h", 13, False, "#A8A29E")
    rd = row(f, "Redes", gap=8, pad=[0, LM, 20, LM])
    for r in ("Instagram", "YouTube", "Facebook"):
        p = row(rd, r, pad=[0, 12, 0, 12], h=36, sv="fixed", fill="#FFFFFF0D", cornerRadius=RAIO, sh="hug")
        T(p, r, 12, False, BRANCO)
    sl = col(f, "Selos", gap=8, pad=[16, LM, 16, LM], fill=BRANCO, cross="center")
    T(sl, "Formas de pagamento", 12, True, CARVAO, upper=True, ls="6%")
    g = row(sl, "Meios", gap=6, main="center", wrap=True)
    for i in ["Pix", "Boleto", "Visa", "Master", "Amex", "Hipercard"]:
        ch = row(g, i, pad=[0, 10, 0, 10], h=26, sv="fixed", fill=CINZA, cornerRadius=RAIO, sh="hug")
        T(ch, i, 11, True, CINZA_T)
    leg = col(f, "Legal", pad=[18, LM, 20, LM], gap=4, cross="center")
    T(leg, "BELLBOOT 2026. Todos os direitos reservados · Rua Luis Alves Batista, 580 · Vila Exposição · Franca - SP",
      11, False, "#A8A29E", align="center", fill=True)
    T(leg, "J. J. Duarte da Silva · CNPJ 25.108.148/0001-75 · Tecnologia Irroba", 11, False, "#A8A29E", align="center", fill=True)


def breadcrumb_m(parent, itens):
    s = secao_m(parent, "Breadcrumb", pv=12)
    r = row(s, "Trilha", gap=6, sh="fill", wrap=True)
    for i, it in enumerate(itens):
        T(r, it, 12, i == len(itens) - 1, CARVAO if i == len(itens) - 1 else CINZA_T)
        if i < len(itens) - 1:
            T(r, "/", 12, False, CINZA_L)


# ---- Home mobile ----------------------------------------------------------------
pg = pagina_m("04 · Home mobile")
tarja_m(pg)
cabecalho_m(pg)
hero = b.frame(pg, "Banner principal", 390, 146, sh="fixed", sv="fixed", clip=True)
b.image(hero, IMG + "slide-1.png", 390, 146, name="Arte do banner (usar versão mobile)", mode="fill")

ben = secao_m(pg, "Benefícios", pv=20)
for ic, tt, tx_ in [("frete", "Frete grátis", "Para a capital"), ("cartao", "Até 10x sem juros", "Ou 10% off no Pix"),
                    ("couro", "Couro legítimo", "Resistência e conforto"), ("troca", "Troca fácil", "Política de devolução")]:
    pass
gr = col(ben, "Grade de benefícios", gap=14)
itens = [("frete", "Frete grátis", "Para a capital"), ("cartao", "Até 10x sem juros", "Ou 10% off no Pix"),
         ("couro", "Couro legítimo", "Resistência e conforto"), ("troca", "Troca fácil", "Política de devolução")]
for i in range(0, 4, 2):
    r = row(gr, "Benefícios", gap=12, cross="min")
    for ic, tt, tx_ in itens[i:i + 2]:
        it = row(r, tt, gap=10, w=171, sh="fixed")
        c = b.frame(it, "Círculo", 40, 40, layout="horizontal", main="center", cross="center", fill=AREIA, cornerRadius=20)
        icone(c, ic, CARVAO, 20)
        tc = col(it, "Texto", gap=0)
        T(tc, tt, 13, True, fill=True, lh=16)
        T(tc, tx_, 11, False, CINZA_T, fill=True, lh=14)

cat = secao_m(pg, "Compre por categoria", pv=12, pt=8)
titulo_m(cat, "Compre por categoria", link=False)
vp = row(cat, "Categorias (rolagem horizontal)", gap=12, cross="min", clip=True)
CATIMG = {"Adventure": "p900-crazy-cafe.jpg", "Botinas": "p850-chelsea.jpg", "Casuais": "p880-preto.jpg",
          "Motociclista": "p3000-preto.jpg", "Tênis": "p4800-grafite.jpg"}
for nm in ["Adventure", "Botinas", "Casuais", "Motociclista", "Tênis"]:
    f = foto(vp, 150, 190, "", name="Categoria " + nm, img=CATIMG[nm])
    ov = row(f, "Rótulo", main="space-between", pad=[0, 12, 0, 12], h=44, sv="fixed", fill=CARVAO, w=150, sh="fixed", x=0, y=146)
    T(ov, nm, 14, True, BRANCO, title=True, upper=True, ls="4%")

s = secao_m(pg, "Mais vendidos", pv=28)
titulo_m(s, "Mais vendidos")
grade_m(s, [B1, B2, B3, B4])

dup = secao_m(pg, "Banners duplos", pv=8)
for fn, nm in [("slide-2.png", "2"), ("slide-3.png", "3")]:
    b.image(dup, IMG + fn, 358, 134, name="Banner " + nm, mode="fill")

s = secao_m(pg, "Lançamentos", pv=28)
titulo_m(s, "Lançamentos")
grade_m(s, [P1, P2, P3, P4])
newsletter_m(pg)
rodape_m(pg)

# ---- Produto mobile -------------------------------------------------------------
pg = pagina_m("05 · Produto mobile")
tarja_m(pg)
cabecalho_m(pg)
breadcrumb_m(pg, ["Início", "Tênis", "Intruder 4800 Oliva"])
sec = secao_m(pg, "Produto", pv=4, pb=24, gap=16)
foto(sec, 358, 358, "", name="Foto principal", img="p4800-oliva-2.jpg", sh="fill")
th = row(sec, "Miniaturas", gap=8, main="center")
for i in range(5):
    foto(th, 62, 62, "", name=f"Miniatura {i + 1}", img=f"p4800-oliva-{i + 1}.jpg", stroke=LARANJA if i == 1 else None, sw=2)
T(sec, "Tênis Adventure Intruder 4800 · Couro legítimo · Oliva", 26, True, title=True, upper=True, fill=True, lh=30)
meta = row(sec, "Meta", gap=10, sh="hug")
estrelas(meta, 5, 14)
T(meta, "Ref. 33  ·  Pronta entrega", 12, False, CINZA_T)
pb = col(sec, "Preço", gap=4, pad=[16, 16, 16, 16], fill=BRANCO, stroke=CINZA, cornerRadius=RAIO)
l1 = row(pb, "De", gap=10, sh="hug")
T(l1, "R$ 299,99", 14, False, CINZA_T, strike=True)
etiqueta(l1, "-33%", LARANJA, CARVAO, size=12)
T(pb, "R$ 199,99", 40, True, CARVAO, title=True)
T(pb, "ou R$ 179,99 no Pix ou boleto (10% off)", 14, True, CARVAO, fill=True)
T(pb, "ou 9x de R$ 22,22 sem juros no cartão", 13, False, CINZA_T, fill=True)
T(sec, "COR · OLIVA", 12, True, CARVAO, upper=True, ls="8%")
r = row(sec, "Cores", gap=8, sh="hug")
for i in range(4):
    sel = i == 1
    foto(r, 60, 60, "", name=f"Cor {i + 1}", img=["p4800-cinza.jpg", "p4800-oliva.jpg", "p4800-branco.jpg", "p4800-grafite.jpg"][i], stroke=CARVAO if sel else CINZA_L, sw=2 if sel else 1)
tr = row(sec, "Tamanho", main="space-between", cross="max")
T(tr, "TAMANHO", 12, True, CARVAO, upper=True, ls="8%")
T(tr, "Guia de medidas", 12, True, LARANJA)
r = row(sec, "Numeração", gap=8, wrap=True)
for n in range(37, 46):
    sel = n == 41
    q = b.frame(r, f"Tam {n}", 62, 44, layout="horizontal", main="center", cross="center", fill=CARVAO if sel else BRANCO,
                stroke=CARVAO if sel else CINZA_L, cornerRadius=RAIO)
    T(q, str(n), 14, True, BRANCO if sel else CARVAO)
bn = col(sec, "Benefícios", gap=8, pad=[14, 16, 14, 16], fill=AREIA, cornerRadius=RAIO)
for ic, tx_ in [("frete", "Frete grátis para a capital"), ("couro", "100% couro legítimo"), ("troca", "Troca e devolução garantidas")]:
    rr = row(bn, tx_, gap=10, sh="hug")
    icone(rr, ic, CARVAO, 18)
    T(rr, tx_, 13, True)
cep = row(sec, "Calcular frete", gap=8)
campo = row(cep, "CEP", pad=[0, 12, 0, 12], fill=BRANCO, stroke=CINZA_L, h=48, sv="fixed", cornerRadius=RAIO)
T(campo, "Digite seu CEP", 14, False, CINZA_T)
botao(cep, "Calcular", "escuro", h=48, size=12)

# barra de compra fixa (no celular fica presa ao rodapé da tela)
bar = row(pg, "Barra de compra (fixa na tela)", gap=12, pad=[10, LM, 10, LM], fill=BRANCO, stroke=CINZA)
qt = row(bar, "Quantidade", gap=12, main="center", w=104, h=52, sh="fixed", sv="fixed", stroke=CINZA_L, fill=BRANCO, cornerRadius=RAIO)
T(qt, "−", 18, True)
T(qt, "1", 15, True)
T(qt, "+", 18, True)
botao(bar, "Comprar", "primario", sh="fill", h=52, size=15)

det = secao_m(pg, "Descrição", pv=24, gap=16, fill=BRANCO)
tabs = row(det, "Abas", gap=22)
for i, nm in enumerate(["Descrição", "Detalhes", "Avaliações"]):
    T(tabs, nm, 13, True, CARVAO if i == 0 else CINZA_T, upper=True, ls="6%")
b.set(b.rect(det, 10, 3, LARANJA, name="Aba ativa"), sizingH="fixed", width=90)
T(det, "Descrição curta", 18, True, title=True, upper=True)
T(det, "[Texto do produto, hoje apenas em imagens grandes, reescrito aqui para leitura rápida e melhor posicionamento no Google.]", 14, False, fill=True, lh=21)
fi = col(det, "Ficha técnica", gap=0, stroke=CINZA, cornerRadius=RAIO)
for i, (k, v) in enumerate([("Material", "Couro legítimo"), ("Solado", "[preencher]"), ("Palmilha", "[preencher]"), ("Fechamento", "[preencher]"), ("Origem", "Franca - SP")]):
    rr = row(fi, k, pad=[12, 14, 12, 14], fill=CREME if i % 2 else BRANCO, main="space-between")
    T(rr, k, 13, True)
    T(rr, v, 13, False, CINZA_T)
s = secao_m(pg, "Você também pode gostar", pv=28)
titulo_m(s, "Você também pode gostar", link=False)
grade_m(s, [P2, P3])
newsletter_m(pg)
rodape_m(pg)

# ---- Categoria mobile -------------------------------------------------------------
pg = pagina_m("06 · Categoria mobile")
tarja_m(pg)
cabecalho_m(pg)
breadcrumb_m(pg, ["Início", "Adventure"])
ban = secao_m(pg, "Banner da categoria", pv=0, pb=8)
bn = row(ban, "Banner", main="space-between", pad=[0, 20, 0, 20], fill=CARVAO, h=120, sv="fixed", cornerRadius=RAIO)
t2 = col(bn, "Texto", gap=6, sh="fill")
T(t2, "Adventure", 36, True, BRANCO, title=True, upper=True)
T(t2, "Botas em couro legítimo para trilhas e o uso diário.", 12, False, "#D6D3D1", fill=True)
foto(bn, 90, 90, "", name="Foto banner", img="p900-crazy-cafe.jpg")

fb = secao_m(pg, "Filtrar e ordenar", pv=8, gap=8)
r = row(fb, "Barra", gap=8)
for tt in ("Filtrar", "Ordenar"):
    bt = row(r, tt, main="center", gap=8, h=44, sv="fixed", fill=BRANCO, stroke=CINZA_L, cornerRadius=RAIO)
    T(bt, tt, 13, True, upper=True, ls="6%")
    T(bt, "▾", 12, False, CINZA_T)
T(fb, "24 produtos", 13, False, CINZA_T)

corpo = secao_m(pg, "Listagem", pv=8, pb=28)
grade_m(corpo, [B1, B2, B3, B4, EX, P2])
pag = row(corpo, "Paginação", gap=8, main="center", pad=[12, 0, 0, 0])
for i, n in enumerate(["1", "2", "3", "→"]):
    q = b.frame(pag, "Página " + n, 44, 44, layout="horizontal", main="center", cross="center",
                fill=CARVAO if i == 0 else BRANCO, stroke=CINZA_L, cornerRadius=RAIO)
    T(q, n, 14, True, BRANCO if i == 0 else CARVAO)
seo = secao_m(pg, "Texto da categoria", pv=24, gap=10, fill=BRANCO)
T(seo, "Botas adventure de alta qualidade", 18, True, title=True, upper=True)
T(seo, "[Texto de SEO atual da categoria, movido para o fim da página para não empurrar os produtos para baixo.]", 14, False, CINZA_T, fill=True, lh=21)
newsletter_m(pg)
rodape_m(pg)
