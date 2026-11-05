# Gera o script da proposta de tema Lime para a Bô · Eugenia Bologna (somente recursos low-code da Irroba).
import hashlib
from fc import B

b = B()
I = "img/"
LOGO, LOGO_B = I + "logo-bo.png", I + "logo-bo-branco.png"
F = {k: I + k + ".jpg" for k in ["ia01", "ia02", "ia03", "ia04", "ed01", "ed08", "ed09", "ed10", "respiro01", "respiro02",
                                 "img3574", "img5255", "img5256", "img5697", "img5715", "img5743", "wa35", "wa38", "wa40", "wa41"]}
F["img5775"] = I + "img5775.jpg"
# loja atual (boeugeniabologna.com.br): estampas dos panôs e packshots dos kimonos
ATM_K = {"Solar": "solar", "Etérea": "eterea", "Telúrica": "telurica", "Magnética": "magnetica"}
for a in ATM_K.values():
    for k in (f"voar-{a}", f"voar-{a}-mini", f"terracota-{a}"):
        F[k] = I + k + ".jpg"
for k in ["sunset-solar", "moonset-magnetica"]:
    F[k] = I + k + ".jpg"
KIM = [("k-yu-veludo-verde-musgo-dragao-imperial-ouro", "Kimono Yu Veludo Verde-Musgo Dragão Imperial Ouro", "Raros"),
       ("k-yin-yang-linho-rosa-vibrante-dragao-gigante", "Kimono Yin-Yang Linho Rosa Vibrante Dragão Gigante Prata-Rosê", "Assinatura"),
       ("k-yang-tweed-noite-estrelada-dragao-azul", "Kimono Yang Tweed Oversized Noite Estrelada Abraço do Dragão Azul", "Essenciais"),
       ("k-yu-veludo-lilas-dragao-ancestral-prata", "Kimono Yu Veludo Lilás Dragão Ancestral Prata", "Raros"),
       ("k-yu-veludo-branco-dragao-ancestral-prata", "Kimono Yu Veludo Branco Dragão Ancestral Prata", "Assinatura"),
       ("k-yang-tweed-linho-caminhos-dragao-cobre", "Kimono Yang Tweed e Linho Caminhos Abraço do Dragão Cobre", "Essenciais"),
       ("k-yu-veludo-preto-dragao-genesis-preto", "Kimono Yu Veludo Preto Dragão Gênesis Preto", "Raros"),
       ("k-yin-yang-linho-rosa-vintage-dragao-gigante", "Kimono Yin-Yang Linho Rosa Vintage Dragão Gigante Prata-Rosê", "Assinatura"),
       ("k-yang-tweed-linho-patchwork-penelope", "Kimono Yang Tweed e Linho Patchwork Penélope Abraço do Dragão Prata-Rosê", "Essenciais")]
for k, _, _ in KIM:
    F[k] = I + k + ".jpg"



def img_paint(key):
    h = hashlib.sha256(open(F[key], "rb").read()).hexdigest()
    return {"type": "image", "image": h, "scale_mode": "fill"}


VERDE, LARANJA, PRETO, BRANCO = "#026526", "#E7760A", "#000000", "#FFFFFF"
# atmosferas: cores apenas ilustrativas dos panôs (conteúdo de produto, não da interface)
ATM = [("Solar", "quente · clara · intensa", "#F2B33D"), ("Etérea", "fria · clara · suave", "#C9D8DE"),
       ("Telúrica", "quente · profunda · densa", "#7B3A1D"), ("Magnética", "fria · profunda · intensa", "#1E2D5E")]
SERIF, SANS = "Cormorant Garamond", "Jost"


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
# Variáveis
# =============================================================================
prim = b.collection("Bô · Primitivas")
for nm, hx, d in [("cor/verde", VERDE, "Verde Bô — briefing (#026526). Primária do Lime e fundo do rodapé."),
                  ("cor/laranja", LARANJA, "Laranja Bô — briefing (#E7760A). Neutra do Lime: etiquetas e detalhes. Sempre com texto preto."),
                  ("cor/preto", PRETO, "Preto — textos, botões e tarja."),
                  ("cor/branco", BRANCO, "Branco — fundo da galeria.")]:
    b.var(prim, nm, "color", hx, desc=d)
for n in [0, 8, 16, 24, 32, 48, 64, 96, 128, 160]:
    b.var(prim, f"espaco/{n}", "number", n)
b.var(prim, "raio/padrao", "number", 0, desc="Lime → Arredondamento: Sem arredondamento.")
b.var(prim, "fonte/titulos", "string", SERIF, desc="Lime → Tipografia personalizada → Fonte dos títulos (Google Fonts).")
b.var(prim, "fonte/textos", "string", SANS, desc="Lime → Tipografia personalizada → Fonte dos textos (Google Fonts).")
for nm, v, d in [("duracao/banner", 6000, "Autoplay do Banner v2 (configuração do módulo)."),
                 ("duracao/fade", 600, "Efeito Fade nativo do Banner v2.")]:
    b.var(prim, nm, "number", v, desc=d)

lime = b.collection("Lime · Paleta personalizada")
for nm, tgt in [("primary-background", "cor/verde"), ("primary-foreground", "cor/branco"),
                ("secondary-background", "cor/preto"), ("secondary-foreground", "cor/branco"),
                ("neutral-background", "cor/laranja"), ("neutral-foreground", "cor/preto"),
                ("body-background", "cor/branco"), ("body-foreground", "cor/preto")]:
    v = b.var(lime, nm, "color", BRANCO, desc=f"Configurações → Paleta → Personalizada → {nm} = {tgt}")
    b.alias(v, b.vars[tgt])

comp = b.collection("Lime · Campos do editor")
for nm, tgt in [("btn-primary-background", "cor/preto"), ("btn-primary-color", "cor/branco"),
                ("btn-secondary-background", "cor/preto"), ("btn-secondary-color", "cor/branco"),
                ("headerContent-background", "cor/branco"), ("categoryLink-foreground", "cor/preto"),
                ("overline-background", "cor/preto"), ("overline-foreground", "cor/branco"),
                ("productGrid-background", "cor/branco"), ("productList-buy-btn-background", "cor/branco"),
                ("productList-buy-btn-foreground", "cor/preto"), ("custom-label-background", "cor/laranja"),
                ("custom-label-foreground", "cor/preto"), ("newsletter-background", "cor/preto"),
                ("footer-background", "cor/verde"), ("swiper-pagination-color", "cor/preto")]:
    v = b.var(comp, nm, "color", BRANCO, desc=f"Campo do editor do tema: {nm}")
    b.alias(v, b.vars[tgt])

# =============================================================================
# Estilos de texto
# =============================================================================
TS = {
    # chave: (nome, família, estilo, tamanho, entrelinha, espaçamento, caixa, onde)
    "arte_display": ("Arte/Display", SERIF, "Light", 88, 88, "0%", "original", "Somente nas artes dos banners (imagem)."),
    "arte_titulo": ("Arte/Título", SERIF, "Light Italic", 44, 48, "0%", "original", "Artes: nome da peça ou da narrativa."),
    "arte_legenda": ("Arte/Legenda de galeria", SANS, "Regular", 12, 16, "20%", "upper", "Artes: ficha da peça, como etiqueta de museu."),
    "titulo": ("Site/Título de seção", SERIF, "Regular", 32, 40, "0%", "upper", "Lime: fonte dos títulos 32px · AG · centro."),
    "titulo_pag": ("Site/Título de página e produto", SERIF, "Regular", 32, 40, "0%", "original", "Página de produto, categoria e institucional."),
    "m_titulo": ("Site/Título de seção mobile", SERIF, "Regular", 24, 32, "0%", "upper", "Mobile (o Lime reduz a escala)."),
    "menu": ("Site/Menu", SANS, "Regular", 13, 16, "0%", "upper", "Categorias do cabeçalho (13px · AG)."),
    "texto": ("Site/Texto", SANS, "Regular", 14, 22, "0%", "original", "Lime: fonte dos textos 14px."),
    "texto_g": ("Site/Texto G", SANS, "Light", 18, 30, "0%", "original", "Página institucional (editor de Informações)."),
    "nome": ("Site/Nome da peça", SANS, "Regular", 14, 20, "0%", "original", "Nome no card (item_titles 14px)."),
    "preco": ("Site/Preço", SANS, "Regular", 14, 20, "0%", "original", "Preço no card, sem negrito."),
    "preco_g": ("Site/Preço produto", SANS, "Regular", 20, 28, "0%", "original", "Preço na página do produto."),
    "botao": ("Site/Botão", SANS, "Medium", 13, 16, "0%", "upper", "Rótulo dos botões do tema."),
    "etiqueta": ("Site/Etiqueta", SANS, "Medium", 11, 14, "0%", "upper", "Etiqueta personalizada do card."),
    "legenda": ("Site/Legenda", SANS, "Regular", 12, 16, "0%", "original", "Tarja, parcelamento, rodapé legal."),
    "doc_ey": ("Doc/Antetítulo", SANS, "Medium", 12, 16, "16%", "upper", "Documentação."),
    "doc_h1": ("Doc/H1", SERIF, "Light", 64, 68, "0%", "original", "Documentação."),
    "doc_h3": ("Doc/H3", SANS, "Medium", 20, 28, "0%", "original", "Documentação."),
    "doc": ("Doc/Corpo", SANS, "Regular", 16, 26, "0%", "original", "Documentação."),
    "doc_p": ("Doc/Corpo P", SANS, "Regular", 13, 20, "0%", "original", "Documentação: tabelas."),
}
for k, (nm, fam, st, sz, lh, ls, case, _) in TS.items():
    b.textstyles[k] = {"fontFamily": fam, "fontStyle": st, "fontSize": sz, "lineHeight": lh, "letterSpacing": ls, "textCase": case}

# =============================================================================
# helpers
# =============================================================================
CURSOR = {}


def board(w, title, desc, gap=48, pad=80):
    x = CURSOR.get(b.page, 0)
    CURSOR[b.page] = x + w + 200
    f = b.frame(None, f"Board · {title}", w, 200, layout="vertical", gap=gap, pad=pad, fill=BRANCO, sv="hug", x=x, y=0)
    hd = b.frame(f, "Cabeçalho do board", w - 2 * pad, 10, layout="vertical", gap=16, sh="fill", sv="hug")
    b.text(hd, "BÔ · EUGENIA BOLOGNA · PROPOSTA DE TEMA LIME", "doc_ey", VERDE)
    b.text(hd, title, "doc_h1", PRETO, fillw=True)
    if desc:
        b.text(hd, desc, "doc", PRETO, fillw=True)
    d = b.rect(hd, 100, 1, PRETO, name="Fio")
    b.set(d, sizingH="fill")
    return f


def section(parent, title, desc=None, gap=24):
    s = b.frame(parent, title, 100, 10, layout="vertical", gap=gap, sh="fill", sv="hug")
    b.text(s, title, "doc_h3", PRETO)
    if desc:
        b.text(s, desc, "doc", PRETO, fillw=True)
    return s


def row(parent, name="Linha", gap=24, wrap=False, cross="min", main=None, sh="fill", sv="hug", pad=0, fill=None):
    return b.frame(parent, name, 100, 10, layout="horizontal", gap=gap, pad=pad, sh=sh, sv=sv, cross=cross, main=main,
                   wrap=wrap, fill=fill)


def col(parent, name="Coluna", gap=8, w=None, sh=None, sv="hug", pad=0, fill=None, cross=None, main=None, stroke=None):
    return b.frame(parent, name, w or 100, 10, layout="vertical", gap=gap, pad=pad, sh=sh or ("fixed" if w else "fill"),
                   sv=sv, fill=fill, cross=cross, main=main, stroke=stroke)


def table(parent, headers, rows, widths, name="Tabela"):
    t = b.frame(parent, name, sum(widths), 10, layout="vertical", gap=0, sv="hug", stroke=PRETO)
    hr = b.frame(t, "Cabeçalho", sum(widths), 10, layout="horizontal", fill=PRETO, sv="hug")
    for h, w in zip(headers, widths):
        c = b.frame(hr, h, w, 10, layout="vertical", pad=[12, 16, 12, 16], sv="hug")
        b.text(c, h, "doc_ey", BRANCO, fillw=True)
    for k, r in enumerate(rows):
        if k:
            b.rect(t, sum(widths), 1, PRETO, name="Divisor")
        rr = b.frame(t, f"Linha {k + 1}", sum(widths), 10, layout="horizontal", sv="hug", fill=BRANCO)
        for v, w in zip(r, widths):
            c = b.frame(rr, "Célula", w, 10, layout="vertical", pad=[12, 16, 12, 16], sv="hug", gap=6)
            if isinstance(v, tuple) and v[0] == "cor":
                b.rect(c, 40, 24, v[1], name="Amostra", stroke=PRETO)
                b.text(c, v[2], "doc_p", PRETO, fillw=True)
            else:
                b.text(c, str(v), "doc_p", PRETO, fillw=True)
    return t


def note(parent, text, title="NOTA", fill=VERDE, fg=BRANCO):
    n = b.frame(parent, "Nota", 100, 10, layout="vertical", gap=8, pad=24, fill=fill, sh="fill", sv="hug")
    b.text(n, title, "doc_ey", fg)
    b.text(n, text, "doc", fg, fillw=True)
    return n


def placeholder(parent, w, h, label, name="Foto a receber", fill=BRANCO, fg=PRETO):
    p = b.frame(parent, name, w, h, layout="vertical", main="center", cross="center", gap=8, pad=16, fill=fill, stroke=fg)
    b.set(p, dashes=[6, 6])
    b.text(p, label, "legenda", fg, align="center", w=max(60, w - 32))
    return p


def pic(parent, key, w, h, name=None):
    return b.image(parent, F[key], w, h, name=name or f"Foto {key}")


def logo(parent, h, white=False, name="Logo"):
    return b.image(parent, LOGO_B if white else LOGO, round(h * 802 / 1414), h, name=name)


# =============================================================================
# Páginas
# =============================================================================
b.c("page.rename", id=1, name="00 · Capa")
P_CON = b.new_page("01 · Conceito")
P_FUN = b.new_page("02 · Fundamentos")
P_COMP = b.new_page("03 · Componentes")
P_DESK = b.new_page("04 · Telas Desktop")
P_MOB = b.new_page("05 · Telas Mobile")
P_IMPL = b.new_page("06 · Implementação low-code")

# =============================================================================
# 01 · Conceito
# =============================================================================
b.select_page(P_CON)
KB = board(2000, "Uma galeria, não uma vitrine",
           "O pedido da Eugenia: parecer muito mais sofisticada, com hierarquia, edição e sensação de luxo, “mais uma galeria de arte "
           "do que uma simples loja virtual”. As referências (Dries Van Noten, Adriana Degreas, La DoubleJ, Johanna Ortiz, Vanda Jacintho) "
           "têm em comum fotos que ocupam a tela, menu mínimo em caixa alta e quase nenhum texto comercial sobre as imagens.")
pr_ = row(KB, "Princípios", gap=24)
for t_, d in [("A foto protagoniza", "Banners em largura total e cards verticais grandes. Nada de mosaico de miniaturas."),
              ("Legenda de galeria", "Quando há texto na arte, ele é curto e funciona como a etiqueta de uma obra: tipo de peça e nome."),
              ("Branco é a parede", "Fundo branco em tudo, raio 0, sem sombras. O verde e o laranja aparecem pouco, como no logo."),
              ("Comércio no seu lugar", "Parcelamento, envio e Pix vão para a tarja e para a página do produto, nunca para o banner."),
              ("Atemporal", "Nada de coleções por estação. A Home tem uma única lista, Em Cena, escolhida pela Bô.")]:
    c = col(pr_, t_, gap=12, w=352, pad=32, stroke=PRETO)
    b.text(c, t_, "doc_h3", PRETO, fillw=True)
    b.text(c, d, "doc", PRETO, fillw=True)
FT_ = section(KB, "Seleção das fotos enviadas", "21 imagens da pasta “Imagens dos banners”. A legenda indica onde cada uma entra na proposta.")
fr3 = row(FT_, "Fotos", gap=16, wrap=True)
USOS = [("ia02", "Banner 1 desktop"), ("ia04", "Banner 2 desktop"), ("wa41", "Banner 3 desktop"), ("wa40", "Banner 1 mobile"),
        ("ed01", "Em Cena · Banner 2 mobile"), ("ed10", "Em Cena"), ("img5775", "Em Cena"), ("wa35", "Em Cena · Sobre a Bô"),
        ("img3574", "Em Cena"), ("wa38", "Em Cena · Banner 3 mobile"), ("respiro02", "Respiro desktop"), ("respiro01", "Respiro mobile"),
        ("img5743", "Categoria Kimonos"), ("ed09", "Sobre a Bô · Para quem"), ("ia01", "Home · galeria (tríptico)"), ("ia03", "Banner 4 desktop · Sobre a Bô"), ("ed08", "Banner 4 mobile"),
        ("img5255", "Home · Em movimento"), ("img5256", "Home · Em movimento"), ("img5697", "Home · galeria (tríptico)"), ("img5715", "Home · galeria (tríptico)")]
for key, uso in USOS:
    c = col(fr3, key, gap=8, w=264)
    pic(c, key, 264, 352)
    b.text(c, uso, "doc_p", PRETO, fillw=True)

LA = board(2000, "A loja atual (boeugeniabologna.com.br)",
           "A Bô já vende na Irroba, no próprio tema Lime, com Kimonos (Essenciais, Assinatura, Raros), Panôs (Solar, Etérea, Telúrica, "
           "Magnética), Acessórios e a página A Bô. Daqui vêm as estampas reais dos panôs, os packshots dos kimonos e o texto da marca.")
table(LA, ["Encontrado na loja atual", "O que muda na proposta"], [
    ["13 panôs cadastrados como produtos separados, um por estação: “Variante Verão / Primavera / Outono / Inverno”",
     "1 produto por estampa com a opção Cor de 4 valores. Os nomes de estação saem do site (é o ponto que a Eugenia pediu para não voltar a aparecer)"],
    ["Estações ligadas às atmosferas pelas subcategorias: Primavera = Solar · Verão = Etérea · Outono = Telúrica · Inverno = Magnética",
     "Usar só Solar, Etérea, Telúrica e Magnética nos nomes, nas opções e nos filtros"],
    ["Estampas: Voar e Voar Linha Terracota (4 variantes cada), SunSet (3) e MoonSet (1), Constelação Câncer e Lua (collab Clínica MAMARE) e um kit com cinto-faixa",
     "Voar e Voar Linha Terracota já estão completas e entram como vitrine dos panôs. SunSet/MoonSet: confirmar se são a mesma estampa"],
    ["Panô: “Panneau”, do francês “painel”. 100% viscose, 2 m × 1,40 m, tamanho único, com mil amarrações (túnica, vestido, saída de praia, painel)",
     "Texto usado em Detalhes do produto; a versatilidade vira argumento na Home"],
    ["Kimonos com packshot em fundo branco, nomes como “Yu Veludo”, “Yin-Yang Linho”, “Yang Tweed”",
     "Packshots entram nos cards de Em Cena e da categoria (fundo branco = galeria); fotos editoriais ficam nos banners"],
    ["Acessórios: categoria existe, sem produtos", "Braceletes ainda precisam ser cadastrados e fotografados"],
    ["A Bô: estilista e consultora de imagem; valores autenticidade, criatividade e autoamor", "Base dos textos da página Sobre a Bô"],
], [900, 900])
lr = row(LA, "Estampas dos panôs", gap=12, wrap=True)
for a in ATM_K.values():
    for k in (f"voar-{a}", f"terracota-{a}"):
        c = col(lr, k, gap=6, w=300)
        pic(c, k, 300, 210)
        b.text(c, k.replace("-", " · ", 1), "doc_p", PRETO)
for k in ("sunset-solar", "moonset-magnetica"):
    c = col(lr, k, gap=6, w=300)
    pic(c, k, 300, 210)
    b.text(c, k.replace("-", " · ", 1), "doc_p", PRETO)
mr = row(LA, "Miniaturas", gap=12)
for a in ATM_K.values():
    pic(mr, f"voar-{a}-mini", 72, 72, name=f"miniatura {a}")
kr = row(LA, "Packshots dos kimonos", gap=12, wrap=True)
for k, n, cat in KIM:
    c = col(kr, k, gap=6, w=200)
    pic(c, k, 200, 267)
    b.text(c, f"{cat} · {n.replace('Kimono ', '')}", "doc_p", PRETO, fillw=True)

# =============================================================================
# 02 · Fundamentos (primeiro: as amostras viram estilos)
# =============================================================================
b.select_page(P_FUN)
TB = board(1600, "Tipografia",
           "Duas famílias do Google Fonts, que é o que o modal “Personalizar Fonte” do Lime aceita sem código: "
           "Cormorant Garamond nos títulos (serifada de galeria, contraste fino) e Jost nos textos (geométrica e limpa, "
           "próxima da assinatura “Eugenia Bologna” do logo).")
fam = row(TB, "Famílias", gap=24)
for fname, st, sample, uso in [(SERIF, "Light", "Kimonos atemporais", "TÍTULOS · Cormorant Garamond"),
                               (SANS, "Regular", "Panôs, kimonos e acessórios", "TEXTOS · Jost")]:
    c = col(fam, uso, gap=16, w=640, pad=40, stroke=PRETO)
    b.text(c, uso, "doc_ey", VERDE)
    b.node("text", c, "Amostra", text=sample, fontFamily=fname, fontStyle=st, fontSize=56, lineHeight=64, fill=PRETO)
    t = b.node("text", c, "Alfabeto", text="ABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\nàáâãéêíóôõúç 0123456789 R$ · — &",
               fontFamily=fname, fontStyle="Regular", fontSize=18, lineHeight=28, fill=PRETO)
    b.set(t, sizingH="fill", textAutoResize="height")
note(TB, "No Lime: Configurações → Tipografia → Personalizada. Títulos: Cormorant Garamond, 32px, caixa AG, centralizado, sem negrito. "
         "Textos: Jost, 14px. O modal não tem espaçamento entre letras nem peso Light: títulos com letras espaçadas ou em itálico "
         "fino só existem dentro das artes dos banners (imagem exportada deste arquivo).", title="COMO CONFIGURAR SEM CÓDIGO")
spec = col(TB, "Escala tipográfica", gap=0)
b.text(spec, "ESCALA · ESTILOS DE TEXTO", "doc_ey", VERDE)
b.frame(spec, "espaço", 10, 16)
SAMPLE = {"arte_display": "Bô", "arte_titulo": "Dragão de prata", "arte_legenda": "Kimono longo · peça sob encomenda",
          "titulo": "Em Cena", "titulo_pag": "Kimono Longo Dragão Dourado", "m_titulo": "Em Cena", "menu": "Kimonos",
          "texto": "Cada peça pode continuar sendo produzida por anos, enquanto o tecido existir.",
          "texto_g": "A Bô não se organiza por estações. É uma galeria de peças atemporais.",
          "nome": "Kimono Curto Dragão Vermelho", "preco": "R$ 1.890,00", "preco_g": "R$ 1.890,00",
          "botao": "Adicionar à sacola", "etiqueta": "Sob encomenda", "legenda": "ou 6x sem juros",
          "doc_ey": "Antetítulo", "doc_h1": "Título de documentação", "doc_h3": "Subtítulo de documentação",
          "doc": "Corpo de documentação.", "doc_p": "Texto de tabela."}
for k, (nm, fname, st, sz, lh, ls, case, uso) in TS.items():
    r = row(spec, nm, gap=32, cross="center", pad=[20, 0, 20, 0])
    meta = col(r, "Meta", gap=4, w=340)
    b.text(meta, nm, "doc_ey", VERDE)
    b.text(meta, f"{fname} {st} · {sz}/{lh}px · {ls} · {'AG' if case == 'upper' else 'Aa'}", "doc_p", PRETO, fillw=True)
    b.text(meta, uso, "doc_p", PRETO, fillw=True)
    t = b.node("text", r, f"Amostra {nm}", text=SAMPLE[k], fontFamily=fname, fontStyle=st, fontSize=sz, lineHeight=lh,
               letterSpacing=ls, textCase=case, fill=PRETO)
    b.set(t, sizingH="fill", textAutoResize="height")
    b.style("text", nm, t, key=k, desc=uso)
    dv = b.rect(spec, 100, 1, PRETO, name="Divisor")
    b.set(dv, sizingH="fill")

CB = board(1600, "Cores",
           "As quatro cores do briefing: verde #026526, laranja #E7760A, branco e preto. O branco domina (é a parede da galeria), "
           "o preto organiza e o verde e o laranja aparecem pouco, como no logo.")
pr = row(CB, "Amostras", gap=24)
for nm, hx, vn, uso in [("Verde", VERDE, "cor/verde", "Primária do Lime · rodapé · paginação ativa"),
                        ("Laranja", LARANJA, "cor/laranja", "Neutra do Lime · etiqueta “Sob encomenda”"),
                        ("Preto", PRETO, "cor/preto", "Textos · botões · tarja · newsletter"),
                        ("Branco", BRANCO, "cor/branco", "Fundo de todas as páginas")]:
    cd = col(pr, f"Cor {nm}", gap=0, w=340, stroke=PRETO)
    sw = b.rect(cd, 340, 200, hx, name=f"Amostra {nm}")
    b.bind(sw, "fill", vn)
    b.style("paint", f"Bô/{nm}", sw, desc=f"{hx} — {uso}")
    inf = col(cd, "Info", gap=4, pad=20)
    b.text(inf, nm.upper(), "doc_ey", PRETO)
    b.text(inf, hx, "doc", PRETO)
    b.text(inf, uso, "doc_p", PRETO, fillw=True)
s2 = section(CB, "Paleta personalizada do Lime (Configurações → Paleta de cores → Personalizada)",
             "Os 4 pares fundo/texto do modal “Personalizar Cores”. O selo de contraste do próprio modal deve ficar verde (AA) nos quatro.")
rows = []
for tok, a, c_, uso in [("primary", VERDE, BRANCO, "Destaques do tema, bullets, estados ativos"),
                        ("secondary", PRETO, BRANCO, "Elementos de apoio do tema"),
                        ("neutral", LARANJA, PRETO, "Selos, etiquetas e fundos suaves (cards usam branco)"),
                        ("body", BRANCO, PRETO, "Fundo e texto das páginas")]:
    rows.append([f"{tok}-background / {tok}-foreground", ("cor", a, a), ("cor", c_, c_), fmt(ratio(a, c_)) + "  ✓ AA", uso])
table(s2, ["Token", "Fundo", "Texto", "Contraste", "Onde aparece"], rows, [300, 200, 200, 200, 540])
note(CB, "O logo enviado é a versão de impressão: nele o verde aparece como #18452B e o laranja como #CA5C24, mais escuros que os "
         "códigos do briefing (#026526 e #E7760A). Esta proposta usa os códigos do briefing no site e o logo como está. "
         "Vale confirmar com a Eugenia se o verde do site deve seguir o do logo.", title="ATENÇÃO · COR DO LOGO", fill=LARANJA, fg=PRETO)

GB = board(1400, "Grid, respiro e bordas",
           "Galeria: muito branco ao redor das fotos, nenhuma sombra, nenhum arredondamento. Containers do Lime em “Largura Total” "
           "(100%) para banners e listas; 1280px para textos.")
sb = section(GB, "Configurações → Arredondamento: Sem arredondamento",
             "Botões, cards, campos, newsletter e etiquetas ficam retos (raio 0), como as molduras de uma exposição.")
br = row(sb, "Exemplos", gap=24)
for nm in ["Moldura da foto · sem borda", "Botão · raio 0", "Campo · raio 0"]:
    c = col(br, nm, gap=12, w=360)
    b.frame(c, "Exemplo", 360, 140, fill=BRANCO, stroke=PRETO)
    b.text(c, nm, "doc_p", PRETO, fillw=True)
ss = section(GB, "Respiro entre seções", "Espaçamento vertical que o tema entrega (padding dos módulos) e que as artes devem respeitar.")
for n in [16, 32, 64, 96, 128]:
    r = row(ss, f"espaco/{n}", gap=24, cross="center")
    b.text(r, f"espaco/{n}", "doc_ey", PRETO)
    b.rect(r, n * 4, 12, PRETO, name=f"Barra {n}")

# =============================================================================
# 03 · Componentes
# =============================================================================
b.select_page(P_COMP)
ICON = {}
LINE = dict(fills=[], stroke=PRETO, strokeWeight=1.25)
IB = board(1000, "Ícones do tema",
           "Os ícones são os nativos do Lime (busca, conta, sacola, menu). Aqui estão redesenhados só para o mockup, em linha fina preta.")
ig = row(IB, "Ícones", gap=24, wrap=True)


def icon(name, parts):
    holder = col(ig, f"Doc {name}", gap=8, w=120, pad=16, stroke=PRETO, cross="center")
    cmp = b.frame(holder, f"Ícone/{name}", 24, 24, comp=True, clip=False)
    for kind, val in parts:
        if kind == "v":
            b.node("vector", cmp, "traço", path=val, **LINE)
        elif kind == "e":
            x, y, w, h = val
            b.node("ellipse", cmp, "círculo", x=x, y=y, w=w, h=h, **LINE)
        elif kind == "r":
            x, y, w, h = val
            b.node("rectangle", cmp, "caixa", x=x, y=y, w=w, h=h, **LINE)
    b.text(holder, name, "legenda", PRETO)
    ICON[name] = cmp


icon("busca", [("e", (4, 4, 13, 13)), ("v", "M15 15 L20 20")])
icon("conta", [("e", (8, 3, 8, 8)), ("v", "M4 21 C4 16 8 14 12 14 C16 14 20 16 20 21")])
icon("sacola", [("r", (4, 8, 16, 13)), ("v", "M8.5 8 L8.5 6.5 C8.5 4.5 10 3 12 3 C14 3 15.5 4.5 15.5 6.5 L15.5 8")])
icon("menu", [("v", "M3 7 L21 7 M3 12 L21 12 M3 17 L21 17")])
icon("seta-esquerda", [("v", "M15 5 L8 12 L15 19")])
icon("seta-direita", [("v", "M9 5 L16 12 L9 19")])
icon("mais", [("v", "M12 5 L12 19 M5 12 L19 12")])
icon("menos", [("v", "M5 12 L19 12")])
icon("instagram", [("r", (3, 3, 18, 18)), ("e", (8, 8, 8, 8))])


def icon_inst(name, parent, color=PRETO):
    ins = b.instance(ICON[name], parent)
    if color != PRETO:
        for nid in ins.all[1:]:
            b.set(nid, strokes=[color])
    return ins


# ---- Botões -------------------------------------------------------------------------
BB = board(1600, "Botões",
           "Configurações → Botões: primário fundo preto e texto branco; “Botão secundário com contorno” marcado. "
           "O botão Comprar do card usa os campos da Lista de Produtos (fundo branco, texto preto) e vira um link discreto. "
           "Sem CSS não há cor de hover configurável: o hover é o comportamento nativo do tema.")
BTN = {}
SPEC = [("Primário", "Padrão", dict(fill=PRETO, fg=BRANCO), "Adicionar à sacola"),
        ("Primário", "Esgotado", dict(fill=BRANCO, fg=PRETO, dash=True), "Esgotado"),
        ("Secundário", "Padrão", dict(fill=BRANCO, fg=PRETO, stroke=PRETO), "Ver todas as peças"),
        ("Secundário", "Esgotado", dict(fill=BRANCO, fg=PRETO, dash=True), "Indisponível"),
        ("Card", "Padrão", dict(fill=BRANCO, fg=PRETO), "Comprar"),
        ("Inverso", "Padrão", dict(fill=BRANCO, fg=PRETO), "Cadastrar")]
vlist = []
for tipo, est, s, lab in SPEC:
    cpt = b.frame(None, f"Tipo={tipo}, Estado={est}", 10, 48, layout="horizontal", gap=8,
                  pad=[16, 0, 16, 0] if tipo == "Card" else [16, 40, 16, 40], main="center", cross="center",
                  fill=s.get("fill"), sh="hug", sv="fixed", comp=True, clip=False)
    if s.get("stroke"):
        b.set(cpt, strokes=[s["stroke"]], strokeWeight=1, strokeAlign="inside")
    if s.get("dash"):
        b.set(cpt, strokes=[PRETO], strokeWeight=1, dashes=[4, 4])
    t = b.text(cpt, lab, "botao", s["fg"], name="label")
    if tipo == "Card":
        b.set(t, textDecoration="underline")
    if tipo == "Primário" and est == "Padrão":
        b.bind(cpt, "fill", "btn-primary-background")
    BTN[(tipo, est)] = cpt
    vlist.append(cpt)
BTN_SET = b.combine(vlist, "Botão")
b.set(BTN_SET, layout="horizontal", gap=32, padding=32, sizingH="hug", sizingV="hug", wrap=False, fills=[BRANCO],
      strokes=[PRETO], strokeWeight=1, dashes=[])
b.reparent(BTN_SET, BB)
table(BB, ["Botão", "Onde configurar", "Valores"], [
    ["Primário (Comprar na página do produto)", "Configurações → Botões → primário; Tema → Página do produto → btnBuy (texto)", "Fundo #000000 · texto #FFFFFF · texto “Adicionar à sacola”"],
    ["Secundário", "Configurações → Botões → secundário + “com contorno (outline)”", "Contorno e texto pretos"],
    ["Comprar do card", "Tema → Lista de Produtos → buyButton", "Fundo #FFFFFF · texto #000000 (parece um link)"],
    ["Newsletter", "Tema → Newsletter → botão", "Fundo branco · texto preto · borda branca"],
], [420, 620, 480])

# ---- Navegação ----------------------------------------------------------------------
NB = board(1600, "Navegação",
           "Cabeçalho Layout 3 do Lime: busca à esquerda, logo central, conta e sacola à direita e as 3 categorias numa linha abaixo. "
           "Fundo branco, fixo ao rolar e expandido (sem cápsula). A tarja informativa concentra as condições comerciais.")
TARJA = b.frame(None, "Tarja informativa/Desktop", 1440, 36, layout="horizontal", main="center", cross="center", gap=48, fill=PRETO, comp=True)
b.bind(TARJA, "fill", "overline-background")
b.text(TARJA, "Enviamos para todo o Brasil  ·  Parcelamento sem juros  ·  Atendimento pelo WhatsApp", "legenda", BRANCO, name="mensagem")
b.reparent(TARJA, NB)
TARJA_M = b.frame(None, "Tarja informativa/Mobile", 390, 32, layout="horizontal", main="center", cross="center", fill=PRETO, comp=True)
b.text(TARJA_M, "Enviamos para todo o Brasil", "legenda", BRANCO, name="mensagem")
b.reparent(TARJA_M, NB)

CATS = ["Kimonos", "Panôs", "Acessórios"]
HD = b.frame(None, "Cabeçalho/Desktop · Layout 3", 1440, 10, layout="vertical", gap=0, fill=BRANCO, sv="hug", comp=True)
b.bind(HD, "fill", "headerContent-background")
top = b.frame(HD, "linha logo", 1440, 104, pad=[0, 48, 0, 48], fill=BRANCO, sh="fill")
bus = b.frame(top, "busca", 220, 32, layout="horizontal", gap=8, cross="center", x=48, y=36)
icon_inst("busca", bus)
b.text(bus, "Buscar", "texto", PRETO, name="busca_txt")
lg = logo(top, 80)
b.set(lg, x=720 - round(80 * 802 / 1414 / 2), y=12)
ic = b.frame(top, "ícones", 120, 32, layout="horizontal", gap=24, main="max", cross="center", x=1440 - 48 - 120, y=36)
icon_inst("conta", ic)
icon_inst("sacola", ic)
nav = b.frame(HD, "categorias", 1440, 48, layout="horizontal", gap=56, main="center", cross="center", sh="fill")
for c_ in CATS:
    b.text(nav, c_, "menu", PRETO, name=f"nav_{c_}")
fio = b.rect(HD, 1440, 1, PRETO, name="fio inferior")
b.set(fio, sizingH="fill")
b.reparent(HD, NB)

HM = b.frame(None, "Cabeçalho/Mobile", 390, 72, fill=BRANCO, comp=True)
icon_inst_m = icon_inst("menu", HM)
b.set(icon_inst_m.id, x=16, y=24)
lgm = logo(HM, 56)
b.set(lgm, x=195 - round(56 * 802 / 1414 / 2), y=8)
sm = icon_inst("sacola", HM)
b.set(sm.id, x=350, y=24)
fm = b.rect(HM, 390, 1, PRETO, name="fio inferior")
b.set(fm, x=0, y=71)
b.reparent(HM, NB)
note(NB, "O menu principal mostra só as 3 categorias (Kimonos, Panôs e Acessórios). Curto e longo não viram categoria: são um filtro "
         "dentro de Kimonos. “Sobre a Bô” fica no rodapé (página de Informações).", title="ESTRUTURA")

# ---- Card de produto ------------------------------------------------------------------
PB = board(1600, "Card de peça (Lista de Produtos)",
           "Card de galeria: foto vertical grande, nome e preço discretos, sem fundo colorido e sem estrelas. Campos do editor: "
           "productGrid-background branco, item_titles 14px, preço 14px sem negrito, botão Comprar branco/preto, etiqueta personalizada laranja.")
pbr = row(PB, "Cards", gap=32)


def mk_card(name, w, img_h, etiqueta=None, comp_=True):
    cpt = b.frame(None, name, w, 10, layout="vertical", gap=12, fill=BRANCO, sv="hug", comp=comp_)
    b.bind(cpt, "fill", "productGrid-background")
    fr = b.frame(cpt, "moldura", w, img_h, clip=True, sh="fill")
    pic(fr, "ed01", w, img_h, name="foto")
    if etiqueta:
        e = b.frame(fr, "etiqueta personalizada", 10, 22, layout="horizontal", pad=[4, 8, 4, 8], fill=LARANJA, sh="hug",
                    sv="hug", x=12, y=12)
        b.text(e, etiqueta, "etiqueta", PRETO, name="etiqueta")
    info = b.frame(cpt, "info", w, 10, layout="vertical", gap=4, sh="fill", sv="hug")
    b.text(info, "Kimono Longo Dragão Laranja", "nome", PRETO, fillw=True, name="nome")
    b.text(info, "R$ 0.000,00", "preco", PRETO, name="preco")
    bt = b.instance(BTN[("Card", "Padrão")], info)
    return cpt


CARD = mk_card("Card/Desktop", 330, 440)
CARD_E = mk_card("Card/Desktop com etiqueta", 330, 440, etiqueta="Sob encomenda")
CARD_M = mk_card("Card/Mobile", 171, 228)
for c_ in (CARD, CARD_E, CARD_M):
    b.reparent(c_, pbr)
note(PB, "Fotos de produto em proporção 3:4 (1200×1600px), fundo e luz consistentes, a peça inteira no quadro. A etiqueta laranja "
         "é a “etiqueta personalizada” do produto (ex.: Sob encomenda, Peça única). Os preços deste arquivo são ilustrativos.",
     title="FOTOS E ETIQUETAS · CONFIRMAR NO PAINEL O RECORTE DO CARD")

# ---- Seletor de atmosfera (opção do produto) ------------------------------------------------
VB = board(1600, "Seletor de cor dos Panôs",
           "Cada Panô é um produto com uma opção “Cor” de 4 valores, exibidos como miniaturas da própria estampa: "
           "Solar, Etérea, Telúrica e Magnética. As cores abaixo só ilustram as atmosferas: no site entram os recortes reais das estampas.")
SW = {}
for nm, d, hx in ATM:
    for sel in (False, True):
        cpt = b.frame(None, f"Cor={nm}, Selecionado={'Sim' if sel else 'Não'}", 88, 10, layout="vertical", gap=8, sv="hug",
                      cross="center", comp=True)
        sq = b.frame(cpt, "miniatura", 72, 72, fill=hx, stroke=PRETO if sel else BRANCO, sw=1)
        b.set(sq, fills=[img_paint(f"voar-{ATM_K[nm]}-mini")])
        if sel:
            b.set(sq, strokeWeight=2)
        t = b.text(cpt, nm, "legenda", PRETO, name="nome")
        if sel:
            b.set(t, textDecoration="underline")
        SW[(nm, sel)] = cpt
SW_SET = b.combine(list(SW.values()), "Opção de cor · Panô")
b.set(SW_SET, layout="grid", gridColumns=4, gap=24, crossGap=24, padding=32, sizingH="hug", sizingV="hug", fills=[BRANCO],
      strokes=[PRETO], strokeWeight=1)
b.reparent(SW_SET, VB)
for nm, _, _ in ATM:
    for nm2, _, _ in ATM:
        if nm2 != nm:
            pass
for nm, _, _ in ATM:
    b.interaction(SW[(nm, False)], {"type": "onClick"}, {"type": "changeTo", "dest": SW[(nm, True)]}, {"type": "dissolve"}, 150, "easeOut")
    b.interaction(SW[(nm, True)], {"type": "onClick"}, {"type": "changeTo", "dest": SW[(nm, False)]}, {"type": "dissolve"}, 150, "easeOut")
table(VB, ["Atmosfera", "Temperatura · luminosidade · intensidade"], [[nm, d] for nm, d, _ in ATM], [300, 600])
SOBRE_CORES = ("Cada estampa Bô nasce em quatro atmosferas cromáticas: Solar, Etérea, Telúrica e Magnética. Elas exploram diferentes "
               "relações entre temperatura, luminosidade, profundidade e intensidade e podem dialogar de maneiras distintas com cada beleza. "
               "São caminhos de harmonização, nunca regras: a escolha é sua.")
sc = col(VB, "Sobre as cores", gap=8, w=640)
b.text(sc, "SOBRE AS CORES", "botao", PRETO)
b.text(sc, SOBRE_CORES, "texto", PRETO, fillw=True)
note(VB, "Texto “Sobre as cores” (do briefing) entra na Descrição curta de cada Panô, logo abaixo do seletor. É só texto: não "
         "bloqueia nenhuma escolha. A exibição das opções como miniaturas de imagem depende do tipo de opção cadastrado (Catálogo → Opções): "
         "testar no painel antes de cadastrar todos os Panôs.", title="SEM CÓDIGO · A CONFIRMAR NO PAINEL")

# ---- Filtro curto/longo ----------------------------------------------------------------
FB_ = board(900, "Filtro de comprimento (Kimonos)",
            "Curto e longo são atributos: um filtro “Comprimento” ligado à categoria Kimonos, não subcategorias.")
FILT = b.frame(None, "Filtro/Comprimento", 240, 10, layout="vertical", gap=12, sv="hug", comp=True)
b.text(FILT, "COMPRIMENTO", "botao", PRETO, name="titulo")
for k, op in enumerate(["Curto", "Longo"]):
    r = b.frame(FILT, f"opção {op}", 240, 24, layout="horizontal", gap=12, cross="center", sh="fill")
    bx = b.frame(r, "caixa", 16, 16, fill=PRETO if k == 1 else BRANCO, stroke=PRETO)
    b.text(r, op, "texto", PRETO, name=f"op_{op}")
b.reparent(FILT, FB_)

# ---- Newsletter e rodapé ------------------------------------------------------------------
RB = board(1600, "Newsletter e rodapé",
           "Newsletter em bloco preto, reto, de largura total. Rodapé em verde Bô com o Instagram em destaque; selos e informações legais em branco.")
NL = {}
for disp, w in (("Desktop", 1440), ("Mobile", 390)):
    cpt = b.frame(None, f"Newsletter/{disp}", w, 10, layout="vertical" if disp == "Mobile" else "horizontal", gap=24 if disp == "Mobile" else 64,
                  pad=[64, 120, 64, 120] if disp == "Desktop" else [48, 16, 48, 16], cross="center", main="center", fill=PRETO, sv="hug", comp=True)
    b.bind(cpt, "fill", "newsletter-background")
    tx = b.frame(cpt, "textos", 480 if disp == "Desktop" else 358, 10, layout="vertical", gap=8, sv="hug")
    b.text(tx, "Cartas da Bô", "titulo_pag" if disp == "Desktop" else "m_titulo", BRANCO, name="titulo")
    b.text(tx, "Peças que entram em cena, bastidores e narrativas. Sem excesso.", "texto", BRANCO, fillw=True, name="descricao")
    fr_ = b.frame(cpt, "formulário", 560 if disp == "Desktop" else 358, 48, layout="horizontal", gap=0)
    fld = b.frame(fr_, "campo", 100, 48, layout="horizontal", pad=[0, 16, 0, 16], cross="center", fill=BRANCO, sh="fill")
    b.text(fld, "Seu e-mail", "texto", PRETO, name="placeholder")
    bt = b.frame(fr_, "botão", 10, 48, layout="horizontal", pad=[0, 24, 0, 24], cross="center", fill=PRETO, stroke=BRANCO, sh="hug")
    b.text(bt, "Cadastrar", "botao", BRANCO)
    NL[disp] = cpt
    b.reparent(cpt, RB)

FT = {}
COLS = [("Institucional", ["Sobre a Bô", "Trocas e devoluções", "Política de privacidade"]),
        ("Atendimento", ["WhatsApp", "E-mail", "Segunda a sexta"]),
        ("Minha conta", ["Entrar", "Meus pedidos"])]
for disp, w in (("Desktop", 1440), ("Mobile", 390)):
    cpt = b.frame(None, f"Rodapé/{disp}", w, 10, layout="vertical", gap=0, fill=BRANCO, sv="hug", comp=True)
    top_ = b.frame(cpt, "informações", w, 10, layout="horizontal" if disp == "Desktop" else "vertical", gap=48 if disp == "Mobile" else 96,
                   pad=[80, 120, 80, 120] if disp == "Desktop" else [48, 16, 48, 16], fill=VERDE, sh="fill", sv="hug")
    b.bind(top_, "fill", "footer-background")
    red = b.frame(top_, "redes", 280, 10, layout="vertical", gap=16, sv="hug")
    logo(red, 96, white=True, name="logo branco")
    ig_ = b.frame(red, "Instagram", 10, 24, layout="horizontal", gap=8, cross="center", sh="hug", sv="hug")
    icon_inst("instagram", ig_, BRANCO)
    b.text(ig_, "@boeugeniabologna", "texto", BRANCO)
    for t_, links in COLS:
        c = b.frame(top_, t_, 220, 10, layout="vertical", gap=12, sv="hug")
        b.text(c, t_.upper(), "botao", BRANCO)
        for l_ in links:
            b.text(c, l_, "texto", BRANCO)
    sel = b.frame(cpt, "selos", w, 10, layout="horizontal" if disp == "Desktop" else "vertical", gap=48 if disp == "Desktop" else 16,
                  pad=[32, 120, 32, 120] if disp == "Desktop" else [24, 16, 24, 16], fill=BRANCO, sh="fill", sv="hug", main="spaceBetween")
    for t_ in ["Formas de pagamento", "Formas de envio", "Site seguro"]:
        c = b.frame(sel, t_, 10, 10, layout="vertical", gap=8, sh="hug", sv="hug")
        b.text(c, t_.upper(), "etiqueta", PRETO)
        ph = b.frame(c, "selos", 200, 24, layout="horizontal", gap=8)
        for k in range(4):
            b.frame(ph, f"selo {k + 1}", 40, 24, stroke=PRETO)
    lg_ = b.frame(cpt, "legal", w, 10, layout="horizontal", pad=[16, 120, 16, 120] if disp == "Desktop" else [16, 16, 24, 16],
                  fill=BRANCO, sh="fill", sv="hug", stroke=PRETO)
    b.set(lg_, strokeTopWeight=1, strokeBottomWeight=0, strokeLeftWeight=0, strokeRightWeight=0)
    b.text(lg_, "Bô Eugenia Bologna · CNPJ 00.000.000/0000-00 · Todos os direitos reservados", "legenda", PRETO, fillw=True)
    FT[disp] = cpt
    b.reparent(cpt, RB)

# ---- Artes dos banners -----------------------------------------------------------------
AB = board(3200, "Artes dos banners (Banner v2)",
           "No Lime o banner é uma imagem: a legenda de galeria e qualquer título fazem parte da arte. Exporte cada frame “Arte/…” "
           "deste arquivo (desktop 1440×720 → 1920×960 com escala 1,333; mobile 390×585 → 1080×1620 com escala 2,77) e "
           "suba em Personalizar Loja → Banners. Pouco texto, nenhuma condição comercial.")
HERO = [("ia02", "wa40", "Kimono longo", "Dragão de prata"),
        ("ia04", "ed01", "Kimono longo", "Jardim vermelho"),
        ("wa41", "wa38", "Kimono curto", "Dragão vermelho"),
        ("ia03", "ed08", "Kimono longo", "Névoa")]
HERO_D, HERO_M = [], []
ar = row(AB, "Slides", gap=48)


def legenda(parent, linha1, linha2, x, y, fg=BRANCO, w=480):
    lb = b.frame(parent, "legenda de galeria", w, 10, layout="vertical", gap=8, sv="hug", x=x, y=y)
    b.text(lb, linha1, "arte_legenda", fg, name="ficha")
    b.text(lb, linha2, "arte_titulo", fg, name="nome da peça", fillw=True)
    return lb


for k, (dk, mk, l1, l2) in enumerate(HERO):
    h = b.frame(None, f"Arte/Banner {k + 1} · Desktop", 1440, 720, fill=PRETO, clip=True, comp=True)
    pic(h, dk, 1440, 720, name="foto")
    legenda(h, l1, l2, 64, 600)
    HERO_D.append(h)
    m = b.frame(None, f"Arte/Banner {k + 1} · Mobile", 390, 585, fill=PRETO, clip=True, comp=True)
    pic(m, mk, 390, 585, name="foto")
    legenda(m, l1, l2, 24, 470, w=342)
    HERO_M.append(m)
HSET = b.combine(HERO_D, "Banner principal/Desktop")
b.set(HSET, layout="vertical", gap=32, padding=32, sizingH="hug", sizingV="hug", fills=[BRANCO], strokes=[PRETO], strokeWeight=1)
b.reparent(HSET, ar)
HMSET = b.combine(HERO_M, "Banner principal/Mobile")
b.set(HMSET, layout="vertical", gap=32, padding=32, sizingH="hug", sizingV="hug", fills=[BRANCO], strokes=[PRETO], strokeWeight=1)
b.reparent(HMSET, ar)
for lst in (HERO_D, HERO_M):
    for k in range(len(lst)):
        b.interaction(lst[k], {"type": "afterDelay", "ms": 6000}, {"type": "changeTo", "dest": lst[(k + 1) % len(lst)]},
                      {"type": "dissolve"}, 600, "easeInOut")

ar2 = row(AB, "Outras artes", gap=48)
RESP = b.frame(None, "Arte/Respiro · Desktop", 1440, 640, fill=PRETO, clip=True, comp=True)
pic(RESP, "respiro02", 1440, 640, name="foto")
b.reparent(RESP, ar2)
RESP_M = b.frame(None, "Arte/Respiro · Mobile", 390, 520, fill=PRETO, clip=True, comp=True)
pic(RESP_M, "respiro01", 390, 520, name="foto")
b.reparent(RESP_M, ar2)

# grade de categorias: 3 artes verticais
CATG, CATG_M = {}, {}
for nm, key in [("Kimonos", "img5743"), ("Panôs", "terracota-solar"), ("Acessórios", None)]:
    for disp, w, h in (("Desktop", 448, 600), ("Mobile", 358, 420)):
        a = b.frame(None, f"Arte/Categoria {nm} · {disp}", w, h, fill=BRANCO, clip=True, comp=True)
        if key:
            pic(a, key, w, h, name="foto")
            fg = BRANCO
        else:
            placeholder(a, w, h, f"FOTO DE {nm.upper()} A RECEBER\n" + "(os dois modelos de bracelete · categoria ainda vazia na loja atual)")
            fg = PRETO
        lb = b.frame(a, "legenda", w - 48, 10, layout="vertical", gap=4, sv="hug", x=24, y=h - 52)
        b.text(lb, nm, "arte_legenda", fg, name="categoria")
        (CATG if disp == "Desktop" else CATG_M)[nm] = a
        b.reparent(a, ar2)

# panôs: 4 atmosferas
PAN, PAN_M = {}, {}
for nm, d, hx in ATM:
    fg = PRETO if nm in ("Solar", "Etérea") else BRANCO
    fg = BRANCO
    a = b.frame(None, f"Arte/Atmosfera {nm} · Desktop", 330, 440, fill=hx, clip=True, comp=True)
    pic(a, f"voar-{ATM_K[nm]}", 330, 440, name="estampa Voar")
    lb = b.frame(a, "legenda", 290, 10, layout="vertical", gap=4, sv="hug", x=20, y=372)
    b.text(lb, nm, "arte_titulo", fg, name="atmosfera")
    b.text(lb, d, "arte_legenda", fg, name="descricao")
    PAN[nm] = a
    b.reparent(a, ar2)
    m = b.frame(None, f"Arte/Atmosfera {nm} · Mobile", 175, 233, fill=hx, clip=True, comp=True)
    pic(m, f"voar-{ATM_K[nm]}", 175, 233, name="estampa Voar")
    lb = b.frame(m, "legenda", 151, 10, layout="vertical", sv="hug", x=12, y=187)
    b.text(lb, nm, "arte_titulo", fg, name="atmosfera", fontSize=30, lineHeight=32)
    PAN_M[nm] = m
    b.reparent(m, ar2)

SOBRE_ART = b.frame(None, "Arte/Sobre a Bô · Desktop", 1440, 720, fill=BRANCO, clip=True, comp=True)
pic(SOBRE_ART, "wa35", 640, 720, name="foto")
st_ = b.frame(SOBRE_ART, "texto", 560, 10, layout="vertical", gap=24, sv="hug", x=760, y=230)
b.text(st_, "A Bô", "arte_legenda", PRETO)
b.text(st_, "Kimonos que não pertencem a uma estação.", "arte_titulo", PRETO, fillw=True)
b.text(st_, "Conheça a Bô  →", "arte_legenda", PRETO)
b.reparent(SOBRE_ART, AB)
# galeria: díptico e tríptico com as fotos de reserva
gr = row(AB, "Galeria", gap=48)
DIP, DIP_M = [], []
for key, l1, l2 in [("img5255", "Kimono longo", "Dragão laranja"), ("img5256", "Kimono curto", "Dragão vermelho")]:
    a = b.frame(None, f"Arte/Díptico {l2} · Desktop", 676, 450, fill=PRETO, clip=True, comp=True)
    pic(a, key, 676, 450, name="foto")
    legenda(a, l1, l2, 32, 340, w=400)
    DIP.append(a)
    b.reparent(a, gr)
    m = b.frame(None, f"Arte/Díptico {l2} · Mobile", 358, 238, fill=PRETO, clip=True, comp=True)
    pic(m, key, 358, 238, name="foto")
    lb = b.frame(m, "legenda", 300, 10, layout="vertical", sv="hug", x=16, y=206)
    b.text(lb, f"{l1} · {l2}", "arte_legenda", BRANCO, name="ficha")
    DIP_M.append(m)
    b.reparent(m, gr)
TRI, TRI_M = [], []
for key in ["img5697", "ia01", "img5715"]:
    a = b.frame(None, f"Arte/Tríptico {key} · Desktop", 448, 600, fill=PRETO, clip=True, comp=True)
    pic(a, key, 448, 600, name="foto")
    TRI.append(a)
    b.reparent(a, gr)
for key, w, h in [("ia01", 358, 358), ("img5697", 175, 233), ("img5715", 175, 233)]:
    m = b.frame(None, f"Arte/Tríptico {key} · Mobile", w, h, fill=PRETO, clip=True, comp=True)
    pic(m, key, w, h, name="foto")
    TRI_M.append(m)
    b.reparent(m, gr)

note(AB, "Nomes das peças e frases são sugestões para validar com a Eugenia. As cores das atmosferas são ilustrativas. "
         "Para os Panôs e os braceletes faltam fotos: os quadros tracejados indicam o que precisa ser fotografado.",
     title="CONTEÚDO A VALIDAR", fill=LARANJA, fg=PRETO)

# =============================================================================
# 04 · Telas Desktop
# =============================================================================
b.select_page(P_DESK)
SX = {"x": 0}


def screen(name, w=1440, page_fill=BRANCO):
    f = b.frame(None, name, w, 100, layout="vertical", fill=page_fill, sv="hug", x=SX["x"], y=0, clip=True)
    SX["x"] += w + 200
    return f


def header_d(parent, active=None):
    h = b.instance(HD, parent)
    b.set(h.id, scrollPosition="sticky")
    if active:
        b.set(h[f"nav_{active}"], textDecoration="underline")
    return h


def title_block(parent, text, w, pad=[96, 0, 48, 0], style="titulo", html=False):
    nome = f"Título (Conteúdo HTML) · {text}" if html else f"Título · {text}"
    t = b.frame(parent, nome, w, 10, layout="vertical", pad=pad, cross="center", sv="hug")
    b.text(t, text, style, PRETO, align="center")
    return t


EM_CENA = [(k, n, "Raros" if cat == "Raros" else None) for k, n, cat in KIM]


def card(parent, data, mobile=False):
    key, nome, et = data
    ins = b.instance(CARD_M if mobile else (CARD_E if et else CARD), parent)
    b.set(ins["nome"], characters=nome)
    if et and not mobile:
        b.set(ins["etiqueta"], characters=et)
    return ins


# a foto do card é trocada na instância pela pintura de imagem (hash SHA-256 do arquivo)
def card_photo(ins, key, w=None, h=None):
    b.set(ins["foto"], fills=[img_paint(key)])


HOME = screen("Home · Desktop 1440")
header_d(HOME)
b.instance(TARJA, HOME)
b.instance(HERO_D[0], HOME)
ec = b.frame(HOME, "Em Cena (Lista de Produtos 100%)", 1440, 10, layout="vertical", gap=0, pad=[0, 40, 96, 40], cross="center", sv="hug")
title_block(ec, "Em Cena", 1360)
ecr = b.frame(ec, "carrossel", 1360, 10, layout="horizontal", gap=13, sv="hug", clip=True)
for d in EM_CENA[:4]:
    ins = card(ecr, d)
    card_photo(ins, d[0], 330, 440)
pag = b.frame(ec, "paginação", 10, 10, layout="horizontal", gap=8, pad=[32, 0, 0, 0], sh="hug", sv="hug")
for k in range(3):
    b.rect(pag, 24 if k == 0 else 8, 2, PRETO, name=f"bullet {k + 1}")
b.instance(RESP, HOME)
dp = b.frame(HOME, "Em movimento (Banner v2 · Grade 2 colunas)", 1440, 10, layout="vertical", gap=0, pad=[0, 40, 96, 40], cross="center", sv="hug")
title_block(dp, "Em movimento", 1360, html=True)
dpr = b.frame(dp, "grade", 1360, 450, layout="horizontal", gap=8)
for a in DIP:
    b.instance(a, dpr)
cg = b.frame(HOME, "Categorias (Banner v2 · Grade 3 colunas)", 1440, 10, layout="vertical", gap=0, pad=[0, 40, 96, 40], cross="center", sv="hug")
title_block(cg, "Universo Bô", 1360, html=True)
cgr = b.frame(cg, "grade", 1360, 600, layout="horizontal", gap=8)
for nm in ["Kimonos", "Panôs", "Acessórios"]:
    b.instance(CATG[nm], cgr)
pn = b.frame(HOME, "Panôs · atmosferas (Banner v2 · Grade 4 colunas)", 1440, 10, layout="vertical", gap=0, pad=[0, 40, 96, 40], cross="center", sv="hug")
title_block(pn, "Panôs", 1360, pad=[0, 0, 16, 0], html=True)
b.text(pn, "Uma estampa, quatro atmosferas. Estampa Voar · 100% viscose · 2 m × 1,40 m", "texto", PRETO, align="center")
b.frame(pn, "espaço", 10, 40)
pnr = b.frame(pn, "grade", 1360, 440, layout="horizontal", gap=13)
for nm, _, _ in ATM:
    b.instance(PAN[nm], pnr)
tp = b.frame(HOME, "Galeria (Banner v2 · Grade 3 colunas, sem texto)", 1440, 10, layout="vertical", pad=[0, 40, 96, 40], cross="center", sv="hug")
tpr = b.frame(tp, "grade", 1360, 600, layout="horizontal", gap=8)
for a in TRI:
    b.instance(a, tpr)
b.instance(SOBRE_ART, HOME)
b.instance(NL["Desktop"], HOME)
b.instance(FT["Desktop"], HOME)

# ---- Categoria Kimonos ---------------------------------------------------------------------
CAT = screen("Categoria Kimonos · Desktop 1440")
header_d(CAT, "Kimonos")
b.instance(TARJA, CAT)
ch_ = b.frame(CAT, "Topo da categoria", 1440, 10, layout="vertical", gap=12, pad=[64, 80, 48, 80], cross="center", sv="hug")
b.text(ch_, "Início  /  Kimonos", "legenda", PRETO)
b.text(ch_, "Kimonos", "titulo", PRETO, align="center")
b.text(ch_, "O território central da Bô. Curtos ou longos, feitos para atravessar o tempo.", "texto", PRETO, align="center")
cb_ = b.frame(CAT, "Conteúdo", 1440, 10, layout="horizontal", gap=48, pad=[0, 80, 96, 80], sv="hug")
side = b.frame(cb_, "Filtros", 240, 10, layout="vertical", gap=32, sv="hug")
b.instance(FILT, side)
ordem = b.frame(side, "Ordenar", 240, 10, layout="vertical", gap=8, sv="hug")
b.text(ordem, "ORDENAR POR", "botao", PRETO)
b.text(ordem, "Destaques", "texto", PRETO)
grid = b.frame(cb_, "Grade de peças", 992, 10, layout="horizontal", gap=24, wrap=True, sv="hug")
b.set(grid, crossGap=48)
for d in EM_CENA[:6]:
    ins = card(grid, d)
    b.set(ins.id, width=314)
    card_photo(ins, d[0], 314, 419)
b.instance(NL["Desktop"], CAT)
b.instance(FT["Desktop"], CAT)

# ---- Produto Panô ------------------------------------------------------------------------------
PRD = screen("Produto Panô · Desktop 1440")
header_d(PRD, "Panôs")
b.instance(TARJA, PRD)
pb_ = b.frame(PRD, "Produto", 1440, 10, layout="horizontal", gap=64, pad=[48, 80, 96, 80], sv="hug")
gal = b.frame(pb_, "Galeria (vertical)", 760, 10, layout="horizontal", gap=16, sv="hug")
th = b.frame(gal, "miniaturas", 96, 10, layout="vertical", gap=12, sv="hug")
for nm, _, hx in ATM:
    m_ = b.frame(th, f"miniatura {nm}", 96, 67, fill=hx, stroke=PRETO if nm == "Solar" else None, clip=True)
    pic(m_, f"voar-{ATM_K[nm]}", 96, 67, name="estampa")
main_ = b.frame(gal, "foto principal", 648, 10, layout="vertical", gap=16, sv="hug")
pic(main_, "voar-solar", 648, 453, name="Panô Voar · Solar (estampa)")
placeholder(main_, 648, 420, "FOTO DO PANÔ VESTIDO OU AMARRADO (a receber)\nmostra a versatilidade: túnica, vestido, saída de praia")
inf = b.frame(pb_, "Informações", 456, 10, layout="vertical", gap=24, sv="hug")
b.text(inf, "Início  /  Panôs", "legenda", PRETO)
b.text(inf, "Panô Estampa Voar", "titulo_pag", PRETO, fillw=True)
pp = b.frame(inf, "preço", 456, 10, layout="vertical", gap=4, sv="hug")
b.text(pp, "R$ 0.000,00", "preco_g", PRETO)
b.text(pp, "ou em até 6x sem juros", "legenda", PRETO)
op = b.frame(inf, "Opção Cor", 456, 10, layout="vertical", gap=12, sv="hug")
b.text(op, "COR: SOLAR", "botao", PRETO)
opr = b.frame(op, "valores", 456, 10, layout="horizontal", gap=16, sv="hug")
for nm, _, _ in ATM:
    b.instance(SW[(nm, nm == "Solar")], opr)
sc2 = b.frame(inf, "Descrição curta · Sobre as cores", 456, 10, layout="vertical", gap=8, sv="hug")
b.text(sc2, "SOBRE AS CORES", "botao", PRETO)
b.text(sc2, SOBRE_CORES, "texto", PRETO, fillw=True)
buy = b.frame(inf, "compra", 456, 48, layout="horizontal", gap=12)
qt = b.frame(buy, "quantidade", 120, 48, layout="horizontal", main="spaceBetween", cross="center", pad=[0, 12, 0, 12], stroke=PRETO)
icon_inst("menos", qt)
b.text(qt, "1", "texto", PRETO)
icon_inst("mais", qt)
bb_ = b.instance(BTN[("Primário", "Padrão")], buy)
b.set(bb_.id, sizingH="fill")
fr2 = b.frame(inf, "frete", 456, 10, layout="vertical", gap=8, sv="hug")
b.text(fr2, "CALCULAR FRETE", "botao", PRETO)
cep = b.frame(fr2, "cep", 456, 44, layout="horizontal", pad=[0, 16, 0, 16], cross="center", stroke=PRETO, sh="fill")
b.text(cep, "Digite seu CEP", "texto", PRETO)
det = b.frame(PRD, "Detalhes do produto", 1440, 10, layout="vertical", gap=16, pad=[0, 240, 96, 240], sv="hug")
b.text(det, "DETALHES DO PRODUTO", "botao", PRETO)
b.text(det, '“Panneau”, do francês “painel”: uma peça com tantas utilidades quanto a sua imaginação criar. Amarrada ao corpo vira túnica, vestido longo ou curto, saia ou saída de praia; solta, vira toalha de mesa, manta para o sofá ou painel na parede. 100% viscose, fibra celulósica, seca rápido e é agradável ao toque. Tamanho único: 2 m de largura × 1,40 m de altura.', "texto_g", PRETO, fillw=True, fontSize=17, lineHeight=30)
b.instance(NL["Desktop"], PRD)
b.instance(FT["Desktop"], PRD)

# ---- Sobre a Bô (Informações) -----------------------------------------------------------------------
VALORES = [("I", "Autenticidade", "Moda como forma de expressão, assim como a fala e a escrita: uma extensão da personalidade de cada pessoa."),
           ("II", "Criatividade", "Estampas e bordados autorais, que nascem de uma narrativa e não de uma tendência."),
           ("III", "Autoamor", "Nossa missão é contribuir para a autoconfiança, com peças que dialogam com a identidade de cada cliente.")]


def sobre_page(parent, mobile=False):
    """Espelho de sobre-a-bo.html: o que o editor de Informações exibe com o CSS inline."""
    W = 358 if mobile else 1120
    PADX = 16 if mobile else 160
    SEC = 64 if mobile else 96
    serif = lambda sz, st="Light", lh=None: dict(fontFamily=SERIF, fontStyle=st, fontSize=sz, lineHeight=lh or round(sz * 1.1))
    ey = dict(letterSpacing="20%", textCase="upper")

    def sec(name, gap=0, pad_b=SEC, cross=None):
        return b.frame(parent, name, 1440 if not mobile else 390, 10, layout="vertical", gap=gap, pad=[0, PADX, pad_b, PADX],
                       cross=cross, sv="hug")

    def duas_colunas(s, rotulo, textos):
        fio = b.rect(s, W, 1, PRETO, name="fio")
        r = b.frame(s, "duas colunas", W, 10, layout="vertical" if mobile else "horizontal", gap=24 if mobile else 64,
                    pad=[32, 0, 0, 0], sv="hug")
        c1 = b.frame(r, "rótulo", W if mobile else 352, 10, layout="vertical", sv="hug")
        b.text(c1, rotulo, "legenda", PRETO, **ey)
        c2 = b.frame(r, "texto", W if mobile else 704, 10, layout="vertical", gap=20, sv="hug")
        for t in textos:
            b.text(c2, t, "texto_g", PRETO, fillw=True, fontSize=17, lineHeight=30)
        return r

    tt = b.frame(parent, "Título da página (gerado pelo tema)", 390 if mobile else 1440, 10, layout="vertical", cross="center",
                 pad=[32 if mobile else 0, 16, 32 if mobile else 48, 16], sv="hug")
    b.text(tt, "Sobre a Bô", "titulo" if not mobile else "m_titulo", PRETO, align="center")
    # 1 · abertura
    s = sec("1 · Abertura (HTML)", gap=24, cross="center", pad_b=40)
    b.text(s, "Bô · Eugenia Bologna", "legenda", VERDE, align="center", **ey)
    b.text(s, "Uma galeria de kimonos que não pertencem a nenhuma estação.", "texto", PRETO, align="center",
           w=W if mobile else 860, **serif(34 if mobile else 60, lh=38 if mobile else 64))
    b.text(s, "Kimonos, panôs e acessórios pensados como peças autorais: feitos para durar, para atravessar gerações e para serem "
              "escolhidos pelo que dizem, não pelo calendário.", "texto_g", PRETO, align="center", w=W if mobile else 640,
           fontSize=17, lineHeight=30)
    pic(parent, "ia03", 390 if mobile else 1440, 171 if mobile else 630, name="foto abertura (16:7)")
    cap = sec("legenda da foto", cross="center", pad_b=SEC)
    b.frame(cap, "espaço", 10, 24)
    b.text(cap, "Kimono longo · Névoa", "legenda", PRETO, align="center", **ey)
    # 2 · a marca
    s = sec("2 · A marca (2 colunas)")
    duas_colunas(s, "01 · A marca", [
        "A Bô nasce do desejo de Eugenia Bologna de unir o trabalho como estilista ao serviço como consultora de imagem, "
        "trazendo cor e sentimentos positivos à vida.",
        "O kimono é o centro de tudo: peças curtas e longas, bordadas e estampadas, que vestem mulheres de 13 a 98 anos.",
        "Não trabalhamos com coleções de primavera, verão, outono ou inverno. Enquanto um tecido ou uma matéria-prima existir, "
        "o mesmo kimono pode continuar sendo produzido por anos, sob demanda ou em pouquíssimas unidades."])
    # 3 · citação
    s = sec("3 · Citação", gap=24, cross="center")
    b.text(s, "“Uma peça pode estar Em Cena pela sua força autoral, estética ou narrativa, mesmo que tenha sido criada há anos.”",
           "texto", PRETO, align="center", w=W if mobile else 900, **serif(28 if mobile else 44, "Light Italic", 36 if mobile else 55))
    b.text(s, "Eugenia Bologna", "legenda", PRETO, align="center", **ey)
    # 4 · pilares
    s = sec("4 · Valores")
    r = b.frame(s, "pilares", W, 10, layout="vertical" if mobile else "horizontal", gap=40, sv="hug")
    for n, t, d in VALORES:
        c = b.frame(r, t, W if mobile else 346, 10, layout="vertical", gap=12, pad=[24, 0, 0, 0], sv="hug", stroke=PRETO)
        b.set(c, strokeTopWeight=1, strokeBottomWeight=0, strokeLeftWeight=0, strokeRightWeight=0)
        b.text(c, n, "legenda", VERDE, **ey)
        b.text(c, t, "texto", PRETO, **serif(28, "Regular", 34))
        b.text(c, d, "texto_g", PRETO, fillw=True, fontSize=17, lineHeight=30)
    # 5 · par de imagens
    s = sec("5 · Par de imagens")
    r = b.frame(s, "par", W, 10, layout="vertical" if mobile else "horizontal", gap=16, sv="hug")
    pw = W if mobile else 552
    for k in ("wa35", "wa38"):
        pic(r, k, pw, round(pw * 4 / 3), name=f"foto {k} (3:4)")
    # 6 · atmosferas
    s = sec("6 · As atmosferas")
    duas_colunas(s, "02 · As atmosferas", [SOBRE_CORES])
    b.frame(s, "espaço", 10, 40)
    g = b.frame(s, "atmosferas", W, 10, layout="horizontal", gap=8, wrap=True, sv="hug")
    b.set(g, crossGap=8)
    tw = 175 if mobile else 274
    for nm, d, hx in ATM:
        t = b.frame(g, nm, tw, 10, layout="vertical", gap=6, sv="hug")
        pic(t, f"voar-{ATM_K[nm]}", tw, tw, name=f"Voar · {nm}")
        b.text(t, nm, "texto", PRETO, **serif(26, "Italic", 30))
        b.text(t, d, "legenda", PRETO, fillw=True, fontSize=11, **ey)
    # 7 · para quem
    s = sec("7 · Para quem (imagem + texto)")
    r = b.frame(s, "imagem e texto", W, 10, layout="vertical" if mobile else "horizontal", gap=32 if mobile else 48,
                cross=None if mobile else "center", sv="hug")
    iw = W if mobile else 536
    pic(r, "ed09", iw, iw, name="foto ed09 (1:1)")
    c = b.frame(r, "texto", W if mobile else 536, 10, layout="vertical", gap=16, sv="hug")
    b.text(c, "03 · Para quem", "legenda", PRETO, **ey)
    b.text(c, "13 a 98", "texto", PRETO, **serif(56 if mobile else 96, lh=56 if mobile else 96))
    b.text(c, "É a faixa de idade de quem veste Bô. O kimono não tem idade, tamanho de tendência nem prazo de validade: ele se "
              "adapta a quem o escolhe.", "texto_g", PRETO, fillw=True, fontSize=17, lineHeight=30)
    # 8 · chamada final
    f = b.frame(parent, "8 · Chamada final (fundo verde)", 390 if mobile else 1440, 10, layout="vertical", gap=24,
                pad=[80, 16, 80, 16], cross="center", fill=VERDE, sv="hug")
    b.text(f, "Em cena agora", "legenda", BRANCO, align="center", **ey)
    b.text(f, "Conheça as peças que escolhemos para este momento.", "texto", BRANCO, align="center", w=W if mobile else 720,
           **serif(30 if mobile else 48, lh=36 if mobile else 56))
    bt = b.frame(f, "botões", 10, 10, layout="vertical" if mobile else "horizontal", gap=16, sh="hug", sv="hug", cross="center")
    for lab, solid in (("Ver kimonos", True), ("@boeugeniabologna", False)):
        x = b.frame(bt, lab, 10, 48, layout="horizontal", pad=[16, 40, 16, 40], cross="center", main="center",
                    fill=BRANCO if solid else None, stroke=None if solid else BRANCO, sh="hug")
        b.text(x, lab, "botao", PRETO if solid else BRANCO, letterSpacing="12%")


SOB = screen("Sobre a Bô · Desktop 1440")
header_d(SOB)
b.frame(SOB, "espaço", 10, 48)
sobre_page(SOB)
note(SOB, "Página cadastrada em Catálogo → Informações, colando o arquivo sobre-a-bo.html no modo código do editor. "
          "Todo o visual vem de atributos style (CSS inline): nada de <style>, <script> ou classes. Colunas usam flex-wrap e "
          "empilham sozinhas no celular. Textos em rascunho, para a Eugenia revisar.", title="COMO IMPLEMENTAR", fill=LARANJA, fg=PRETO)
b.instance(NL["Desktop"], SOB)
b.instance(FT["Desktop"], SOB)

# =============================================================================
# 05 · Telas Mobile
# =============================================================================
b.select_page(P_MOB)
SX["x"] = 0
HOME_M = screen("Home · Mobile 390", w=390)
hm = b.instance(HM, HOME_M)
b.set(hm.id, scrollPosition="sticky")
b.instance(TARJA_M, HOME_M)
b.instance(HERO_M[0], HOME_M)
ecm = b.frame(HOME_M, "Em Cena", 390, 10, layout="vertical", gap=0, pad=[0, 16, 64, 16], cross="center", sv="hug")
title_block(ecm, "Em Cena", 358, pad=[64, 0, 32, 0], style="m_titulo")
gm = b.frame(ecm, "grade 2 colunas", 358, 10, layout="horizontal", gap=16, wrap=True, sv="hug")
b.set(gm, crossGap=32)
for d in EM_CENA[:4]:
    ins = card(gm, d, mobile=True)
    card_photo(ins, d[0], 171, 228)
b.instance(RESP_M, HOME_M)
dpm = b.frame(HOME_M, "Em movimento", 390, 10, layout="vertical", gap=8, pad=[0, 16, 0, 16], cross="center", sv="hug")
title_block(dpm, "Em movimento", 358, pad=[64, 0, 24, 0], style="m_titulo", html=True)
for a in DIP_M:
    b.instance(a, dpm)
cgm = b.frame(HOME_M, "Universo Bô", 390, 10, layout="vertical", gap=8, pad=[0, 16, 64, 16], cross="center", sv="hug")
title_block(cgm, "Universo Bô", 358, pad=[64, 0, 24, 0], style="m_titulo", html=True)
for nm in ["Kimonos", "Panôs", "Acessórios"]:
    b.instance(CATG_M[nm], cgm)
pnm = b.frame(HOME_M, "Panôs", 390, 10, layout="vertical", gap=0, pad=[0, 16, 64, 16], cross="center", sv="hug")
title_block(pnm, "Panôs", 358, pad=[0, 0, 24, 0], style="m_titulo", html=True)
pg2 = b.frame(pnm, "grade 2×2", 358, 10, layout="horizontal", gap=8, wrap=True, sv="hug")
b.set(pg2, crossGap=8)
for nm, _, _ in ATM:
    b.instance(PAN_M[nm], pg2)
tpm = b.frame(HOME_M, "Galeria", 390, 10, layout="horizontal", gap=8, wrap=True, pad=[0, 16, 64, 16], sv="hug")
b.set(tpm, crossGap=8)
for a in TRI_M:
    b.instance(a, tpm)
b.instance(NL["Mobile"], HOME_M)
b.instance(FT["Mobile"], HOME_M)

PRD_M = screen("Produto Panô · Mobile 390", w=390)
hm2 = b.instance(HM, PRD_M)
b.set(hm2.id, scrollPosition="sticky")
b.instance(TARJA_M, PRD_M)
pic(PRD_M, "voar-solar", 390, 273, name="Panô Voar · Solar (estampa)")
dots = b.frame(PRD_M, "paginação da galeria", 390, 24, layout="horizontal", gap=8, main="center", cross="center")
for k in range(4):
    b.rect(dots, 24 if k == 0 else 8, 2, PRETO, name=f"bullet {k + 1}")
im_ = b.frame(PRD_M, "Informações", 390, 10, layout="vertical", gap=20, pad=[16, 16, 48, 16], sv="hug")
b.text(im_, "Panô Estampa Voar", "m_titulo", PRETO, fillw=True)
b.text(im_, "R$ 0.000,00 · ou em até 6x sem juros", "texto", PRETO)
b.text(im_, "COR: SOLAR", "botao", PRETO)
omr = b.frame(im_, "valores", 358, 10, layout="horizontal", gap=2, sv="hug", main="spaceBetween")
for nm, _, _ in ATM:
    b.instance(SW[(nm, nm == "Solar")], omr)
b.text(im_, "SOBRE AS CORES", "botao", PRETO)
b.text(im_, SOBRE_CORES, "texto", PRETO, fillw=True)
bbm = b.instance(BTN[("Primário", "Padrão")], im_)
b.set(bbm.id, sizingH="fill")
b.instance(FT["Mobile"], PRD_M)

SOB_M = screen("Sobre a Bô · Mobile 390", w=390)
hm3 = b.instance(HM, SOB_M)
b.set(hm3.id, scrollPosition="sticky")
sobre_page(SOB_M, mobile=True)
b.instance(FT["Mobile"], SOB_M)

# protótipo: menu → categoria, card → produto, logo → home
b.interaction(HERO_D[0], {"type": "onClick"}, {"type": "navigate", "dest": CAT}, {"type": "dissolve"}, 300, "easeInOut")

# =============================================================================
# 06 · Implementação low-code
# =============================================================================
b.select_page(P_IMPL)
MB = board(2000, "Mapa de implementação sem código",
           "Cada bloco das telas sai de uma configuração do tema ou de um cadastro do painel. Nada passa pela aba Código "
           "(CSS/JavaScript personalizado).")
table(MB, ["#", "Bloco", "Onde no painel", "Configuração proposta"], [
    ["1", "Paleta", "Personalizar Loja → Layouts → Editar tema → Configurações → Paleta → Personalizada",
     "primary #026526/#FFFFFF · secondary #000000/#FFFFFF · neutral #E7760A/#000000 · body #FFFFFF/#000000"],
    ["2", "Tipografia", "Configurações → Tipografia → Personalizada",
     "Títulos Cormorant Garamond 32px, AG, centralizado · Textos Jost 14px"],
    ["3", "Arredondamento e botões", "Configurações → Arredondamento / Botões",
     "Sem arredondamento · primário #000000/#FFFFFF · secundário com contorno"],
    ["4", "Cabeçalho", "Configurações → Cabeçalho + Tema → Cabeçalho (Home e demais páginas)",
     "Layout 3 · Fixo ao rolar · Expandir · fundo branco opacidade 1 · desfoque 0 · categorias pretas 13px AG centralizadas · logo 4 imagens = PNG do logo, ~45×80 desktop / 32×56 mobile"],
    ["5", "Tarja informativa", "Módulo Tarja informativa (overline) + Tema → Tarja",
     "Fundo #000000 · texto #FFFFFF 12px · raio 0 · condições comerciais da loja"],
    ["6", "Banner principal", "Personalizar Loja → Banners (Banner v2 · Carrossel)",
     "Largura total · efeito Fade · autoplay · sem setas · paginação preta · artes 1920×960 (desktop) e 1080×1620 (mobile)"],
    ["7", "Em Cena", "Módulos → Lista de Produtos “Em Cena” + Tema → Lista de Produtos",
     "Largura total · título 32px centralizado · card branco · nome e preço 14px · Comprar branco/preto · sem estrelas · etiqueta personalizada laranja"],
    ["8", "Respiro", "Banner v2 (1 imagem, largura total)", "Foto RESPIRO sem texto, sem link obrigatório"],
    ["8b", "Em movimento", "Conteúdo HTML (título) + Banner v2 · Grade 2 colunas", "Díptico IMG_5255 e IMG_5256 com legenda de galeria na arte"],
    ["9", "Universo Bô", "Conteúdo HTML (título) + Banner v2 · Grade 3 colunas", "Kimonos · Panôs · Acessórios, cada arte linkando para a categoria"],
    ["10", "Panôs", "Conteúdo HTML (título e frase) + Banner v2 · Grade 4 colunas", "Solar · Etérea · Telúrica · Magnética, linkando para Panôs"],
    ["10b", "Galeria", "Banner v2 · Grade 3 colunas (mobile: 1 + 2)", "Tríptico sem texto: IMG_5697, IA 01 e IMG_5715"],
    ["11", "Sobre a Bô (chamada)", "Banner v2 (1 arte)", "Link para a página de Informações “Sobre a Bô”"],
    ["12", "Newsletter", "Tema → Newsletter", "Largura total · fundo #000000 · raio 0 · campo branco · botão branco/preto"],
    ["13", "Rodapé", "Tema → Informações do rodapé / Selos / Legal + Configurações da loja (redes sociais)",
     "Fundo #026526 · títulos e links brancos · Instagram @boeugeniabologna · selos e legal em branco"],
    ["14", "Categorias", "Catálogo → Categorias", "Somente Kimonos, Panôs e Acessórios no menu; nenhuma categoria de coleção/estação"],
    ["15", "Curto / longo", "Catálogo → Filtros (grupo “Comprimento”)", "Valores Curto e Longo, vinculados aos kimonos"],
    ["16", "Cores dos Panôs", "Catálogo → Opções (“Cor”, com imagem) + Produto → Opções",
     "4 valores: Solar, Etérea, Telúrica, Magnética, com miniatura da estampa; 1 produto por estampa"],
    ["17", "Sobre as cores", "Produto → Descrição curta", "Texto do briefing em todos os Panôs"],
    ["17b", "Migração dos panôs", "Catálogo → Produtos (loja atual)", "Unir os 13 produtos por estação em 1 por estampa (Voar, Voar Linha Terracota, SunSet/MoonSet, Constelação) e tirar “Variante Verão/Primavera/Outono/Inverno” dos nomes"],
    ["18", "Sobre a Bô", "Catálogo → Informações → modo código do editor", "Colar sobre-a-bo.html (HTML com CSS inline, sem <style> nem <script>) · link no rodapé Institucional"],
    ["19", "Botão de compra", "Tema → Página do produto → btnBuy", "Texto “Adicionar à sacola”"],
], [60, 260, 700, 820])

LB = board(1400, "Limites sem código e decisões",
           "O que o editor não faz sem CSS/JS e como a proposta contorna cada ponto.")
table(LB, ["Limite", "Como a proposta resolve"], [
    ["Espaçamento entre letras e peso Light nos títulos", "Ficam só nas artes dos banners; no site os títulos usam Cormorant Regular 32px."],
    ["Texto sobre a foto do banner", "Faz parte da arte (imagem). Cadastre também o texto alternativo do banner."],
    ["Quantidade de cards por linha e proporção da foto", "Seguem o tema. Padronizar as fotos em 3:4 e conferir no painel antes de fotografar tudo."],
    ["Tarja acima do cabeçalho", "A tarja informativa entra no fluxo dos módulos, logo abaixo do cabeçalho."],
    ["Cor de hover dos botões e animações próprias", "Usamos só o que é nativo: hover do tema, Fade do banner, carrossel, cabeçalho fixo."],
    ["Layout em colunas na página institucional", "HTML + CSS inline no texto informativo: flex com quebra (flex-wrap), que empilha sozinho no celular."],
    ["Títulos acima das grades de banner", "O Banner v2 não tem título: um módulo Conteúdo HTML com <h2> estilizado inline entra antes da grade."],
    ["Miniaturas de imagem nas opções do Panô", "Depende do tipo de opção do painel: testar com 1 Panô antes de cadastrar os demais."],
], [520, 760])
note(LB, "Fotos dos Panôs (as 4 variantes de cada estampa) e dos dois modelos de bracelete · fotos de produto 3:4 de cada kimono · "
         "preços e nomes oficiais das peças · condições comerciais da tarja · confirmação da cor verde do site × logo · "
         "logo em SVG ou PNG transparente (usei uma prévia do PDF de impressão).", title="PENDÊNCIAS DE CONTEÚDO", fill=LARANJA, fg=PRETO)

# =============================================================================
# 00 · Capa
# =============================================================================
b.select_page(1)
cap = b.frame(None, "Capa", 1920, 1080, fill=BRANCO, x=0, y=0, clip=True)
pic(cap, "ed01", 810, 1080, name="foto capa")
lgc = logo(cap, 280)
b.set(lgc, x=960, y=120)
ct = b.frame(cap, "título", 820, 10, layout="vertical", gap=24, sv="hug", x=960, y=500)
b.text(ct, "PROPOSTA DE TEMA · IRROBA LIME", "doc_ey", VERDE)
b.text(ct, "Bô, uma galeria de kimonos", "doc_h1", PRETO, fillw=True)
b.text(ct, "Ideia de tema montada só com os recursos low-code da plataforma: configurações do tema, editor visual, módulos e "
           "cadastros. Sem CSS e sem JavaScript personalizados.", "doc", PRETO, fillw=True)
idx = b.frame(ct, "índice", 820, 10, layout="vertical", gap=6, sv="hug")
for p_ in ["01 · Conceito", "02 · Fundamentos", "03 · Componentes", "04 · Telas Desktop", "05 · Telas Mobile", "06 · Implementação low-code"]:
    b.text(idx, p_, "doc_p", PRETO)
b.text(ct, "Outubro de 2026", "legenda", PRETO)

b.dump("bo.json")
print("comandos:", len(b.cmds))
