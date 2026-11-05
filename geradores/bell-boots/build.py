# Gera a proposta Bell Boots (tema Lime) para o FigCraft via `figcraft-cli run`.
# Uso: python build.py bb.json  ->  python runcheck.py bb.json bell-boots-lime.figcraft
import sys
sys.path.insert(0, "../lime-implementacao/gerador")
from fc import B

b = B()
TITULO, CORPO = "Bahnschrift", "Segoe UI"   # substitutos de Oswald/Cabin (preset Impactante do Lime)

# Paleta: preset "Orange" do Lime ajustado à marca (laranja + carvão)
LARANJA, CARVAO, AREIA, CREME, BRANCO = "#F97316", "#1C1917", "#FDBA74", "#FFFAF5", "#FFFFFF"
CINZA, CINZA_T, CINZA_L, ESTRELA, ESCURO2 = "#E7E5E4", "#78716C", "#D6D3D1", "#F5BF2F", "#292524"
LADO = 43          # margem lateral do container de 1280px em 1366
IMG = "img-cliente/"
RAIO = 4           # arredondamento "Pequeno" do Lime


# ---- helpers ---------------------------------------------------------------
def T(parent, s, size=16, bold=False, color=CARVAO, title=False, w=None, fill=False, align=None,
      upper=False, lh=None, ls=None, name=None, strike=False, x=0, y=0):
    props = {"fontFamily": TITULO if title else CORPO, "fontStyle": "Bold" if bold else "Regular",
             "fontSize": size, "lineHeight": lh or round(size * 1.4), "fill": color,
             "textCase": "upper" if upper else "original"}
    if ls:
        props["letterSpacing"] = ls
    if align:
        props["textAlign"] = align
    if strike:
        props["textDecoration"] = "strikethrough"
    if w or fill:
        props["textAutoResize"] = "height"
    nid = b.node("text", parent, name or s[:30], x=x, y=y, w=w or (100 if fill else None), text=s, **props)
    if fill:
        b.set(nid, sizingH="fill")
    return nid


def row(parent, name="Linha", gap=0, pad=0, main=None, cross="center", sh="fill", sv="hug", fill=None, w=100, h=10, **kw):
    return b.frame(parent, name, w, h, layout="horizontal", gap=gap, pad=pad, main=main, cross=cross,
                   sh=sh, sv=sv, fill=fill, **kw)


def col(parent, name="Coluna", gap=0, pad=0, main=None, cross=None, sh="fill", sv="hug", fill=None, w=100, h=10, **kw):
    return b.frame(parent, name, w, h, layout="vertical", gap=gap, pad=pad, main=main, cross=cross,
                   sh=sh, sv=sv, fill=fill, **kw)


def secao(parent, name, pv=48, fill=None, gap=24):
    """Seção de largura total com o container de 1280px (margem lateral de 43px)."""
    return col(parent, name, gap=gap, pad=[pv, LADO, pv, LADO], fill=fill)


def botao(parent, label, kind="primario", sh="hug", w=None, h=48, size=14):
    fill = {"primario": LARANJA, "escuro": CARVAO, "claro": BRANCO}.get(kind)
    cor = BRANCO if kind == "escuro" else CARVAO
    stroke = {"contorno": CARVAO, "contorno_claro": BRANCO}.get(kind)
    if kind == "contorno_claro":
        cor = BRANCO
    f = b.frame(parent, "Botão " + label[:20], w or 160, h, layout="horizontal", main="center", cross="center",
                pad=[0, 28, 0, 28], fill=fill, stroke=stroke, sw=2, sh=sh, sv="fixed", cornerRadius=RAIO)
    T(f, label, size, True, cor, upper=True, ls="6%")
    return f


def foto(parent, w, h, label="FOTO DO PRODUTO", fill=CINZA, cor=CINZA_T, name="Foto", sh="fixed", img=None, **kw):
    f = b.frame(parent, name, w, h, fill=fill, sh=sh, sv="fixed", cornerRadius=RAIO, clip=True, **kw)
    if img:
        b.image(f, IMG + img, w, h, name="Imagem", mode="fill")
    else:
        T(f, label, 12, True, cor, w=w, align="center", ls="8%", y=h // 2 - 8)
    return f


def etiqueta(parent, txt, fill=CARVAO, cor=BRANCO, x=0, y=0, size=11):
    f = b.frame(parent, "Etiqueta " + txt[:12], 60, 20, layout="horizontal", pad=[4, 8, 4, 8], fill=fill,
                cross="center", sh="hug", sv="hug", cornerRadius=RAIO, x=x, y=y)
    T(f, txt, size, True, cor)
    return f


def icone(parent, kind, cor=CARVAO, size=24):
    """Ícones em grade 24: caminhos simples, traço de 1,5."""
    caminhos = {
        "busca": "M15 15 L21 21", "conta": "M4 21 C4 16 8 14 12 14 C16 14 20 16 20 21",
        "sacola": "M5 8 H19 V21 H5 Z M8.5 8 V6.5 C8.5 4.5 10 3 12 3 C14 3 15.5 4.5 15.5 6.5 V8",
        "frete": "M2 7 H14 V16 H2 Z M14 10 H19 L22 13 V16 H14 Z",
        "cartao": "M3 6 H21 V18 H3 Z M3 10 H21",
        "couro": "M12 3 L20 6 V12 C20 17 16 20 12 21 C8 20 4 17 4 12 V6 Z",
        "troca": "M20 12 C20 7 16 4 12 4 C9 4 7 5.5 5.5 7.5 M4 12 C4 17 8 20 12 20 C15 20 17 18.5 18.5 16.5 M4 4 V8 H8 M20 20 V16 H16",
        "seta": "M5 12 H19 M13 6 L19 12 L13 18",
        "check": "M5 12 L10 17 L19 7",
    }
    f = b.frame(parent, "Ícone " + kind, size, size, sh="fixed", sv="fixed")
    b.node("vector", f, kind, path=caminhos[kind], fills=[], stroke=cor, strokeWeight=1.5)
    if kind == "busca":
        b.node("ellipse", f, "lente", x=3, y=3, w=12, h=12, fills=[], stroke=cor, strokeWeight=1.5)
    if kind == "conta":
        b.node("ellipse", f, "cabeça", x=8, y=3, w=8, h=8, fills=[], stroke=cor, strokeWeight=1.5)
    if kind == "frete":
        b.node("ellipse", f, "roda", x=5, y=16, w=4, h=4, fills=[CARVAO if cor == CARVAO else cor])
        b.node("ellipse", f, "roda", x=16, y=16, w=4, h=4, fills=[CARVAO if cor == CARVAO else cor])
    return f


def estrelas(parent, n=5, size=14):
    r = row(parent, "Estrelas", gap=2, sh="hug")
    for _ in range(n):
        b.node("star", r, "estrela", w=size, h=size, fills=[ESTRELA])
    return r


def card(parent, w, nome, de, por, parc, badge=None, img=None, name=None):
    c = col(parent, name or "Card " + nome[:24], gap=10, w=w, sh="fixed", fill=BRANCO, pad=0)
    ph = foto(c, w, w, img=img)
    if badge:
        etiqueta(ph, badge, LARANJA, CARVAO, x=12, y=12, size=12)
    etiqueta(ph, "Frete grátis · capital", CARVAO, BRANCO, x=12, y=w - 34)
    info = col(c, "Info", gap=6, pad=[0, 4, 4, 4])
    T(info, nome, 15, True, fill=True, lh=20)
    estrelas(info)
    pr = row(info, "Preço", gap=8, sh="hug", cross="max")
    T(pr, de, 13, False, CINZA_T, strike=True)
    T(pr, por, 22, True, CARVAO, title=True)
    T(info, parc, 13, False, CINZA_T)
    botao(info, "Comprar", "primario", sh="fill", h=44, size=13)
    return c


def titulo_secao(parent, txt, link=True):
    r = row(parent, "Título da seção", main="space-between", cross="max")
    T(r, txt, 32, True, CARVAO, title=True, upper=True, ls="2%")
    if link:
        lk = row(r, "Ver todos", gap=6, sh="hug")
        T(lk, "Ver todos", 14, True, CARVAO, upper=True, ls="6%")
        icone(lk, "seta", CARVAO, 18)
    return r


def lista_produtos(parent, titulo, itens, w=302, gap=24):
    s = secao(parent, "Lista · " + titulo, pv=40, gap=24)
    titulo_secao(s, titulo)
    r = row(s, "Cards", gap=gap, main="space-between", cross="min")
    for it in itens:
        card(r, w, *it)
    return s


def tarja(parent):
    f = row(parent, "Tarja informativa", main="center", pad=[0, LADO, 0, LADO], fill=LARANJA, h=36, sv="fixed")
    T(f, "FRETE GRÁTIS PARA A CAPITAL   ·   9X SEM JUROS   ·   10% OFF NO PIX E BOLETO", 12, True, CARVAO, ls="8%")
    return f


def cabecalho(parent, sobre_hero=False):
    """Cabeçalho Lime · Layout 2: logo à esquerda, ícones à direita, categorias numa linha abaixo."""
    h = col(parent, "Cabeçalho (Layout 2)", fill=CARVAO, gap=0, pad=[0, LADO, 0, LADO])
    l1 = row(h, "Linha 1", main="space-between", pad=[12, 0, 10, 0])
    logo = row(l1, "Logo", gap=10, sh="hug")
    b.image(logo, IMG + "logo-nova-branca.png", 126, 52, name="Logo Bell Boots", mode="fit")   # versão branca, sem fundo (cabeçalho escuro)
    ic = row(l1, "Ícones", gap=12, sh="hug")
    for k in ("busca", "conta", "sacola"):
        c = b.frame(ic, "Botão " + k, 44, 44, layout="horizontal", main="center", cross="center", fill=ESCURO2, cornerRadius=RAIO)
        icone(c, k, BRANCO, 22)
    l2 = row(h, "Categorias", gap=40, main="center", pad=[0, 0, 14, 0])
    for i, nm in enumerate(["Adventure", "Botinas", "Casuais", "Motociclista", "Tênis", "Ofertas"]):
        T(l2, nm, 14, True, LARANJA if nm == "Ofertas" else BRANCO, upper=True, ls="8%")
    return h


def newsletter(parent):
    s = secao(parent, "Newsletter", pv=40)
    f = row(s, "Newsletter", main="space-between", pad=[28, 40, 28, 40], fill=LARANJA, cornerRadius=RAIO)
    t = col(f, "Texto", gap=4, sh="hug")
    T(t, "Novidades", 32, True, CARVAO, title=True, upper=True)
    T(t, "Receba lançamentos e ofertas em primeira mão.", 16, False, CARVAO)
    fm = row(f, "Formulário", gap=8, sh="hug")
    campo = row(fm, "Campo", pad=[0, 16, 0, 16], fill=BRANCO, w=360, h=48, sh="fixed", sv="fixed", cornerRadius=RAIO)
    T(campo, "Seu melhor e-mail", 14, False, CINZA_T)
    botao(fm, "Enviar", "escuro")


def rodape(parent):
    f = col(parent, "Rodapé", fill=CARVAO, gap=0)
    top = row(f, "Informações", gap=40, main="space-between", cross="min", pad=[48, LADO, 40, LADO])
    cols = [("Institucional", ["Política de privacidade", "Política de troca e devolução", "Sobre nós", "Mapa do site"]),
            ("Minha conta", ["Entrar ou cadastrar", "Meus dados", "Meus pedidos", "Rastrear pedido"]),
            ("Atendimento", ["(16) 3705-3624", "WhatsApp (16) 99997-0470", "bellboots2@yahoo.com",
                             "Seg a sex, das 8h às 18h"])]
    for tt, links in cols:
        c = col(top, tt, gap=10, w=260, sh="fixed")
        T(c, tt, 14, True, LARANJA, upper=True, ls="8%")
        for l in links:
            T(c, l, 14, False, BRANCO, fill=True)
    c = col(top, "Redes", gap=10, w=260, sh="fixed")
    T(c, "Siga nossas redes", 14, True, LARANJA, upper=True, ls="8%")
    for r in ("Instagram", "YouTube", "Facebook"):
        p = row(c, r, pad=[0, 16, 0, 16], h=40, sv="fixed", fill="#FFFFFF0D", cornerRadius=RAIO)
        T(p, r, 14, False, BRANCO)
    selos = row(f, "Selos", gap=40, main="space-between", cross="center", pad=[24, LADO, 24, LADO], fill=BRANCO)
    for tt, itens in [("Formas de pagamento", ["Pix", "Boleto", "Visa", "Master", "Amex", "Hipercard"]),
                      ("Site seguro", ["Compra protegida", "Loja verificada"])]:
        g = row(selos, tt, gap=14, sh="hug")
        T(g, tt, 13, True, CARVAO, upper=True, ls="6%")
        for i in itens:
            ch = row(g, i, pad=[0, 10, 0, 10], h=28, sv="fixed", fill=CINZA, cornerRadius=RAIO, sh="hug")
            T(ch, i, 12, True, CINZA_T)
    leg = col(f, "Legal", pad=[20, LADO, 20, LADO], gap=2, cross="center")
    T(leg, "BELLBOOT 2026. Todos os direitos reservados · Rua Luis Alves Batista, 580 · Vila Exposição · Franca - SP · CEP 14405-424",
      12, False, "#A8A29E", align="center", fill=True)
    T(leg, "J. J. Duarte da Silva · CNPJ 25.108.148/0001-75 · Tecnologia Irroba", 12, False, "#A8A29E", align="center", fill=True)
    return f


def pagina(nome, first=False):
    if first:
        b.c("page.rename", id=1, name=nome)
    else:
        b.new_page(nome)
    return col(None, nome, w=1366, sh="fixed", fill=CREME)


def breadcrumb(parent, itens):
    s = secao(parent, "Breadcrumb", pv=16)
    r = row(s, "Trilha", gap=8, sh="hug")
    for i, it in enumerate(itens):
        T(r, it, 13, i == len(itens) - 1, CARVAO if i == len(itens) - 1 else CINZA_T)
        if i < len(itens) - 1:
            T(r, "/", 13, False, CINZA_L)


P1 = ("Tênis Adventure Intruder 4800 Oliva", "R$ 299,99", "R$ 199,99", "9x de R$ 22,22 sem juros", "-33%", "p4800-oliva.jpg")
P2 = ("Bota Adventure 900 Oliva", "R$ 299,99", "R$ 249,99", "10x de R$ 25,00 sem juros", "-17%", "p900-oliva.jpg")
P3 = ("Tênis Adventure Intruder 4800 Cinza", "R$ 299,99", "R$ 199,99", "9x de R$ 22,22 sem juros", "-33%", "p4800-cinza.jpg")
P4 = ("Tênis Adventure Intruder 4800 Branco", "R$ 299,99", "R$ 199,99", "9x de R$ 22,22 sem juros", "-33%", "p4800-branco.jpg")
B1 = ("Bota Adventure 900 Café", "R$ 299,99", "R$ 249,99", "10x de R$ 25,00 sem juros", "-17%", "p900-cafe.jpg")
B2 = ("Bota Adventure 900 Milho", "R$ 299,99", "R$ 249,99", "10x de R$ 25,00 sem juros", "-17%", "p900-milho.jpg")
B3 = ("Bota Adventure 900 Grafite", "R$ 299,99", "R$ 249,99", "10x de R$ 25,00 sem juros", "-17%", "p900-grafite.jpg")
B4 = ("Bota Adventure 900 Preto", "R$ 299,99", "R$ 249,99", "10x de R$ 25,00 sem juros", "-17%", "p900-preto.jpg")
EX = ("Bota Adventure Extreme Crazy", "R$ 329,99", "R$ 279,90", "10x de R$ 27,99 sem juros", "-15%", "p900-crazy-cafe.jpg")

# =============================================================================
# 0. Proposta (resumo, tokens e comparativo)
# =============================================================================
pg = pagina("00 · Proposta", first=True)
c = col(pg, "Capa", gap=16, pad=[72, LADO, 56, LADO], fill=CARVAO)
T(c, "BELL BOOTS · MIGRAÇÃO CHINA → LIME", 13, True, LARANJA, upper=True, ls="16%")
T(c, "Uma loja que vende com a mesma força da bota.", 56, True, BRANCO, title=True, upper=True, fill=True, lh=62)
T(c, "Mesmo catálogo, mesma plataforma Irroba. Novo layout, mais claro, mais rápido de navegar e pronto para o celular.",
  18, False, "#D6D3D1", fill=True)

s = secao(pg, "Configuração Lime", pv=56, gap=28)
T(s, "O que configuramos no editor do Lime", 32, True, title=True, upper=True)
T(s, "Tudo abaixo existe no editor do tema (Configurações): nenhuma personalização exige código.", 16, False, CINZA_T, fill=True)
sw = row(s, "Paleta", gap=16, cross="min")
for nm, hx, tk, fg in [("Primária", LARANJA, "primary-background", CARVAO), ("Secundária", CARVAO, "secondary-background", BRANCO),
                       ("Neutra", AREIA, "neutral-background", CARVAO), ("Fundo da página", CREME, "body-background", CARVAO)]:
    cc = col(sw, nm, gap=8)
    r = b.frame(cc, "Amostra " + nm, 100, 96, fill=hx, stroke=CINZA_L, sh="fill", sv="fixed", cornerRadius=RAIO)
    T(cc, nm, 14, True)
    T(cc, hx + "  ·  " + tk, 12, False, CINZA_T)
cfg = row(s, "Opções", gap=16, cross="min")
for tt, tx in [("Cabeçalho", "Layout 2: logo à esquerda, ícones à direita e categorias numa linha abaixo."),
               ("Arredondamento", "Pequeno (4px): combina com o couro e o visual rústico, sem a pílula do padrão."),
               ("Botões", "Sólidos, laranja com texto carvão (contraste AA)."),
               ("Tipografia", "Preset Impactante (Oswald + Cabin): títulos condensados e em caixa alta, como nas artes de campanha. Neste mock usamos Bahnschrift e Segoe UI como substitutas.")]:
    cc = col(cfg, tt, gap=8, pad=20, fill=BRANCO, stroke=CINZA, cornerRadius=RAIO)
    T(cc, tt, 14, True, LARANJA, upper=True, ls="8%")
    T(cc, tx, 14, False, CARVAO, fill=True, lh=20)

t = secao(pg, "Antes × Depois", pv=48, gap=0, fill=BRANCO)
T(t, "Antes × depois", 32, True, title=True, upper=True)
b.set(b.rect(t, 10, 20, None, name="espaço"), sizingH="fill")
LINHAS = [("Aspecto", "Hoje (tema China)", "Proposta (tema Lime)"),
          ("Cabeçalho", "155px de altura, com ícone de bota sobre cada item do menu", "Compacto: logo e ícones na primeira linha, categorias na segunda"),
          ("Banners", "Mesma arte para todos os aparelhos, sem versão para celular", "Arte limpa por dispositivo (desktop e celular), com setas e paginação configuráveis"),
          ("Vitrines", "Dois módulos iguais, sem hierarquia", "Categorias, mais vendidos, lançamentos e banners duplos em sequência"),
          ("Card de produto", "Nome cortado, selo de frete solto, sem desconto visível", "Etiqueta de % de desconto, frete na foto e botão Comprar"),
          ("Cor da marca", "Azul do tema e botão verde sem relação com a marca", "Laranja e carvão em botões, selos e destaques"),
          ("Produto", "Botão verde, preços pequenos, frete empurrando o botão", "Preço e desconto em destaque, benefícios e compra em sequência"),
          ("Categoria", "Texto de SEO antes dos produtos e filtros de preço fora da realidade", "Filtros por cor, tamanho e preço e cards mais limpos")]
for i, (a, bb, cc) in enumerate(LINHAS):
    cab = i == 0
    r = row(t, "Linha " + a, gap=0, cross="center", pad=[14, 16, 14, 16], fill=CARVAO if cab else (CREME if i % 2 else BRANCO))
    for txt, w in [(a, 200), (bb, 520), (cc, 520)]:
        T(r, txt, 14, cab or txt == a, BRANCO if cab else CARVAO, w=w, upper=cab, ls="6%" if cab else None, lh=20)

# =============================================================================
# 1. Home
# =============================================================================
pg = pagina("01 · Home")
tarja(pg)
cabecalho(pg)
hero = b.frame(pg, "Banner principal", 1366, 512, sh="fixed", sv="fixed", clip=True)
b.image(hero, IMG + "slide-1.png", 1366, 512, name="Arte do banner", mode="fill")

ben = secao(pg, "Banner Tarja · benefícios", pv=32)
r = row(ben, "Benefícios", gap=24, main="space-between")
for ic, tt, tx_ in [("frete", "Frete grátis", "Para a capital"), ("cartao", "Até 10x sem juros", "Ou 10% off no Pix"),
                    ("couro", "Couro legítimo", "Resistência e conforto"), ("troca", "Troca fácil", "Política de devolução")]:
    it = row(r, tt, gap=14, sh="hug")
    c = b.frame(it, "Círculo", 52, 52, layout="horizontal", main="center", cross="center", fill=AREIA, cornerRadius=26)
    icone(c, ic, CARVAO, 26)
    tc = col(it, "Texto", gap=0, sh="hug")
    T(tc, tt, 16, True)
    T(tc, tx_, 13, False, CINZA_T)

cat = secao(pg, "Compre por categoria", pv=24)
titulo_secao(cat, "Compre por categoria", link=False)
r = row(cat, "Categorias", gap=20, main="space-between", cross="min")
CATIMG = {"Adventure": "p900-crazy-cafe.jpg", "Botinas": "p850-chelsea.jpg", "Casuais": "p880-preto.jpg",
          "Motociclista": "p3000-preto.jpg", "Tênis": "p4800-grafite.jpg"}
for nm in ["Adventure", "Botinas", "Casuais", "Motociclista", "Tênis"]:
    f = foto(r, 240, 300, "FOTO DA CATEGORIA", name="Categoria " + nm, img=CATIMG[nm])
    ov = row(f, "Rótulo", main="space-between", pad=[0, 16, 0, 16], h=56, sv="fixed", fill=CARVAO, w=240, sh="fixed", x=0, y=244)
    T(ov, nm, 18, True, BRANCO, title=True, upper=True, ls="6%")
    icone(ov, "seta", LARANJA, 20)

lista_produtos(pg, "Mais vendidos", [B1, B2, B3, B4])

dup = secao(pg, "Banners duplos", pv=24)
r = row(dup, "Banners", gap=24, cross="min")
for fn, nm in [("slide-2.png", "2"), ("slide-3.png", "3")]:
    b.image(r, IMG + fn, 628, 236, name="Banner " + nm, mode="fill")

lista_produtos(pg, "Lançamentos", [P1, P2, P3, P4])
newsletter(pg)
rodape(pg)

# =============================================================================
# 2. Produto
# =============================================================================
pg = pagina("02 · Produto")
tarja(pg)
cabecalho(pg)
breadcrumb(pg, ["Início", "Tênis", "Tênis Adventure Intruder 4800 Oliva"])
sec = secao(pg, "Produto", pv=8, gap=32)
dois = row(sec, "Galeria + informações", gap=48, cross="min")
gal = row(dois, "Galeria", gap=16, cross="min", w=640, sh="fixed")
th = col(gal, "Miniaturas", gap=12, sh="hug")
for i in range(5):
    foto(th, 84, 84, "", name=f"Miniatura {i + 1}", img=f"p4800-oliva-{i + 1}.jpg", stroke=LARANJA if i == 1 else None, sw=2)
foto(gal, 540, 540, "", name="Foto principal", img="p4800-oliva-2.jpg")

inf = col(dois, "Informações", gap=18)
T(inf, "Tênis Adventure Intruder 4800 · Couro legítimo · Oliva", 36, True, title=True, upper=True, fill=True, lh=40)
meta = row(inf, "Meta", gap=14, sh="hug")
estrelas(meta, 5, 16)
T(meta, "Avaliar produto", 13, False, CINZA_T)
T(meta, "·   Ref. 33   ·   Pronta entrega", 13, False, CINZA_T)
pb = col(inf, "Preço", gap=4, pad=[18, 20, 18, 20], fill=BRANCO, stroke=CINZA, cornerRadius=RAIO)
l1 = row(pb, "De", gap=10, sh="hug")
T(l1, "R$ 299,99", 16, False, CINZA_T, strike=True)
etiqueta(l1, "-33%", LARANJA, CARVAO, size=13)
T(pb, "R$ 199,99", 48, True, CARVAO, title=True)
T(pb, "ou R$ 179,99 no Pix ou boleto (10% off)", 15, True, CARVAO)
T(pb, "ou 9x de R$ 22,22 sem juros no cartão", 14, False, CINZA_T)

T(inf, "COR · OLIVA", 13, True, CARVAO, upper=True, ls="8%")
r = row(inf, "Cores", gap=10, sh="hug")
for i in range(4):
    sel = i == 1
    foto(r, 64, 64, "", name=f"Cor {i + 1}", img=["p4800-cinza.jpg", "p4800-oliva.jpg", "p4800-branco.jpg", "p4800-grafite.jpg"][i], stroke=CARVAO if sel else CINZA_L, sw=2 if sel else 1)
tr = row(inf, "Tamanho", main="space-between", cross="max")
T(tr, "TAMANHO", 13, True, CARVAO, upper=True, ls="8%")
T(tr, "Guia de medidas", 13, True, LARANJA)
r = row(inf, "Numeração", gap=8, sh="hug")
for n in range(37, 46):
    sel = n == 41
    q = b.frame(r, f"Tam {n}", 48, 44, layout="horizontal", main="center", cross="center", fill=CARVAO if sel else BRANCO,
                stroke=CARVAO if sel else CINZA_L, cornerRadius=RAIO)
    T(q, str(n), 14, True, BRANCO if sel else CARVAO)
comp = row(inf, "Comprar", gap=12, cross="center")
qt = row(comp, "Quantidade", gap=16, main="center", w=120, h=56, sh="fixed", sv="fixed", stroke=CINZA_L, fill=BRANCO, cornerRadius=RAIO)
T(qt, "−", 20, True)
T(qt, "1", 16, True)
T(qt, "+", 20, True)
botao(comp, "Comprar", "primario", sh="fill", h=56, size=16)
bn = col(inf, "Benefícios", gap=10, pad=[16, 18, 16, 18], fill=AREIA, cornerRadius=RAIO)
for ic, tx_ in [("frete", "Frete grátis para a capital"), ("couro", "100% couro legítimo"), ("troca", "Troca e devolução garantidas")]:
    rr = row(bn, tx_, gap=10, sh="hug")
    icone(rr, ic, CARVAO, 20)
    T(rr, tx_, 14, True)
cep = row(inf, "Calcular frete", gap=8, cross="center")
campo = row(cep, "CEP", pad=[0, 14, 0, 14], fill=BRANCO, stroke=CINZA_L, h=48, sv="fixed", cornerRadius=RAIO)
T(campo, "Digite seu CEP", 14, False, CINZA_T)
botao(cep, "Calcular frete", "escuro", h=48, size=13)

det = secao(pg, "Descrição", pv=32, gap=20, fill=BRANCO)
tabs = row(det, "Abas", gap=32, sh="fill")
for i, nm in enumerate(["Descrição", "Detalhes", "Avaliações"]):
    T(tabs, nm, 16, True, CARVAO if i == 0 else CINZA_T, upper=True, ls="6%")
b.set(b.rect(det, 10, 3, LARANJA, name="Aba ativa"), sizingH="fixed", width=110)
r = row(det, "Texto e ficha", gap=48, cross="min")
tx = col(r, "Texto", gap=10)
T(tx, "Descrição curta", 20, True, title=True, upper=True)
T(tx, "[Texto do produto, hoje apenas em imagens grandes, reescrito aqui para leitura rápida e melhor posicionamento no Google.]", 15, False, fill=True, lh=22)
fi = col(r, "Ficha técnica", gap=0, stroke=CINZA, cornerRadius=RAIO)
for i, (k, v) in enumerate([("Material", "Couro legítimo"), ("Solado", "[preencher]"), ("Palmilha", "[preencher]"), ("Fechamento", "[preencher]"), ("Origem", "Franca - SP")]):
    rr = row(fi, k, pad=[12, 16, 12, 16], fill=CREME if i % 2 else BRANCO, main="space-between")
    T(rr, k, 14, True)
    T(rr, v, 14, False, CINZA_T)
b.set(fi, width=420, sizingH="fixed")
lista_produtos(pg, "Você também pode gostar", [P2, P3, P4, B1])
newsletter(pg)
rodape(pg)

# =============================================================================
# 3. Categoria
# =============================================================================
pg = pagina("03 · Categoria")
tarja(pg)
cabecalho(pg)
breadcrumb(pg, ["Início", "Adventure"])
ban = secao(pg, "Banner da categoria", pv=0)
bn = row(ban, "Banner", main="space-between", pad=[0, 48, 0, 48], fill=CARVAO, h=220, sv="fixed", cornerRadius=RAIO)
t2 = col(bn, "Texto", gap=10, sh="hug")
T(t2, "Adventure", 64, True, BRANCO, title=True, upper=True)
T(t2, "Botas em couro legítimo para trilhas, aventuras e o uso diário.", 16, False, "#D6D3D1")
foto(bn, 220, 220, "", name="Foto banner", img="p900-crazy-cafe.jpg")

corpo = secao(pg, "Listagem", pv=32, gap=0)
r = row(corpo, "Filtros + produtos", gap=40, cross="min")
fl = col(r, "Filtros", gap=22, w=250, sh="fixed")
T(fl, "Filtros", 20, True, title=True, upper=True)
for tt, itens in [("Categorias", ["Adventure (24)", "Botinas", "Casuais", "Motociclista", "Tênis"]),
                  ("Faixa de preço", ["Até R$ 200", "R$ 200 a R$ 250", "R$ 250 a R$ 300", "Acima de R$ 300"])]:
    g = col(fl, tt, gap=10, pad=[0, 0, 18, 0])
    T(g, tt, 13, True, LARANJA, upper=True, ls="8%")
    for i in itens:
        rr = row(g, i, gap=10, sh="hug")
        b.frame(rr, "Caixa", 18, 18, stroke=CINZA_T, sw=1.5, cornerRadius=3, fill=BRANCO)
        T(rr, i, 14)
g = col(fl, "Cor", gap=10)
T(g, "Cor", 13, True, LARANJA, upper=True, ls="8%")
rr = row(g, "Cores", gap=8, sh="hug")
for hx in ["#4B5320", "#6B4423", "#E0A526", "#78716C", "#1C1917", "#C2A27A"]:
    b.frame(rr, "Cor", 30, 30, fill=hx, stroke=CINZA_L, cornerRadius=15)
g = col(fl, "Tamanho", gap=10)
T(g, "Tamanho", 13, True, LARANJA, upper=True, ls="8%")
rr = row(g, "Tamanhos", gap=6, wrap=True, sh="fill")
for n in range(37, 46):
    q = b.frame(rr, f"Tam {n}", 44, 36, layout="horizontal", main="center", cross="center", fill=BRANCO, stroke=CINZA_L, cornerRadius=RAIO)
    T(q, str(n), 13, True)

dir_ = col(r, "Produtos", gap=24)
bar = row(dir_, "Barra", main="space-between", pad=[0, 0, 16, 0])
T(bar, "24 produtos", 14, False, CINZA_T)
so = row(bar, "Ordenar", gap=10, sh="hug")
T(so, "Ordenar por", 13, False, CINZA_T)
sl = row(so, "Select", gap=14, pad=[0, 14, 0, 14], h=40, sv="fixed", fill=BRANCO, stroke=CINZA_L, cornerRadius=RAIO, sh="hug")
T(sl, "Mais vendidos", 14, True)
T(sl, "▾", 12, False, CINZA_T)
for linha in ([B1, B2, B3], [B4, EX, P2]):
    rr = row(dir_, "Linha de cards", gap=25, cross="min")
    for it in linha:
        card(rr, 311, *it)
pag = row(dir_, "Paginação", gap=8, main="center", pad=[12, 0, 0, 0])
for i, n in enumerate(["1", "2", "3", "→"]):
    q = b.frame(pag, "Página " + n, 44, 44, layout="horizontal", main="center", cross="center",
                fill=CARVAO if i == 0 else BRANCO, stroke=CINZA_L, cornerRadius=RAIO)
    T(q, n, 14, True, BRANCO if i == 0 else CARVAO)

seo = secao(pg, "Texto da categoria", pv=40, gap=12, fill=BRANCO)
T(seo, "Botas adventure de alta qualidade", 20, True, title=True, upper=True)
T(seo, "[Texto de SEO atual da categoria, movido para o fim da página para não empurrar os produtos para baixo.]", 15, False, CINZA_T, fill=True, lh=22)
newsletter(pg)
rodape(pg)


exec(open("mobile_lime.py",encoding="utf-8").read())

b.dump(sys.argv[1] if len(sys.argv) > 1 else "bb.json")
print("comandos:", len(b.cmds), "proximo id:", b.nid)
