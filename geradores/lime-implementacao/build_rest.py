# Continuação do build.py (executado com exec no mesmo escopo).

# =============================================================================
# 03 · Animações & Protótipo
# =============================================================================
b.select_page(P_ANIM)
AB = board(0, 0, 1800, "Tokens de movimento",
           "Movimento discreto e elegante: cor e opacidade mudam rápido; painéis deslizam devagar. Nada pisca, quica ou gira. "
           "Valores na coleção “Var · Primitivas” → duracao/* e easing/*.")
tl_ = section(AB, "Durações")
for nm, v, d in [("duracao/instantanea", 100, "Pressionado, foco"), ("duracao/rapida", 150, "Hover de botões e links"),
                 ("duracao/base", 250, "Card de produto, acordeão, dropdown"), ("duracao/lenta", 400, "Mini-carrinho, menu mobile, troca do banner"),
                 ("duracao/revelar", 600, "Seções entrando na tela")]:
    r = row(tl_, nm, gap=24, cross="center")
    m = col(r, "meta", gap=2, w=320)
    b.text(m, nm, "rotulo", BORDO)
    b.text(m, d, "legenda", PRETO)
    b.rect(r, v * 1.6, 24, BORDO, name=f"{v}ms")
    b.text(r, f"{v}ms", "corpo_b", PRETO)
table(AB, ["Token", "Valor", "Uso", "CSS"], [
    ["easing/padrao", "cubic-bezier(0.2, 0, 0, 1)", "Entradas, hovers e trocas de estado", "var(--var-easing)"],
    ["easing/saida", "cubic-bezier(0.4, 0, 1, 1)", "Painéis e elementos saindo da tela", "—"],
    ["duracao/tarja", "4000ms", "Rotação das mensagens da tarja no mobile", "tema"],
    ["duracao/banner", "6000ms", "Autoplay do Banner v2", "configuração do módulo"],
], [320, 360, 520, 440])
note(AB, "Com “reduzir movimento” ativo no sistema (prefers-reduced-motion), o autoplay, os deslocamentos e as revelações são desligados; ficam apenas as trocas de cor.",
     title="ACESSIBILIDADE")

CAT = board(1900, 0, 1900, "Catálogo de animações",
            "Cada animação usada no site, com gatilho, propriedades, tempo e onde ela é aplicada no tema Lime.")
table(CAT, ["Animação", "Gatilho", "O que muda", "Tempo · easing", "Onde aplicar"], [
    ["Hover do botão", "Mouse sobre", "Fundo bordô → uva (primário); branco → preto (secundário)", "150ms · padrão", "CSS .btn-primary:hover"],
    ["Pressionado", "Clique/toque", "Fundo preto (primário) · bordô (secundário)", "100ms · padrão", "CSS :active"],
    ["Foco de teclado", "Tab", "Anel 2px preto a 2px de distância", "instantâneo", "CSS :focus-visible"],
    ["Card de produto", "Mouse sobre", "Borda 1px preto; foto/embalagem amplia 4%; botão vira uva", "250ms · padrão", "CSS .productList .product:hover"],
    ["Banner principal", "Automático (6s) e setas", "Troca de slide com dissolver", "400ms · ease-in-out", "Banner v2 (tema)"],
    ["Tarja mobile", "Automático (4s)", "Uma mensagem por vez, dissolver", "400ms · padrão", "Tarja informativa (tema)"],
    ["Cabeçalho fixo", "Rolagem", "Cabeçalho permanece no topo (sticky), fundo branco opaco", "—", "Lime: header-position sticky"],
    ["Mini-carrinho", "Clique na sacola / Comprar", "Painel entra pela direita; sai pela direita", "400ms entrada · 300ms saída", "Tema (carrinho lateral)"],
    ["Menu mobile", "Clique no ícone de menu", "Painel entra pela esquerda", "400ms · padrão", "Tema (menu mobile)"],
    ["Adicionar à sacola", "Clique em Comprar", "Botão: Comprar → Aguarde (3 pontos) → Adicionado ✓ → Comprar; contador pulsa", "800ms + 1200ms", "Tema + CSS"],
    ["Revelar seção", "Seção entra na tela", "Opacidade 0 → 1 e desloca 16px para cima", "600ms · padrão", "CSS .var-reveal + JS (aba Código)"],
    ["Acordeão do produto", "Clique", "Abre o conteúdo; ícone + vira −", "250ms · padrão", "Tema (descrição do produto)"],
    ["Link sublinhado", "Mouse sobre", "Bordô → preto", "150ms · padrão", "CSS a:hover"],
], [300, 280, 520, 300, 340])

DEMO = board(0, 1400, 2400, "Demonstrações interativas (protótipo)",
             "Abra o modo Apresentar a partir do fluxo “Demonstrações de animação”. Passe o mouse nos botões e no card; o banner e a tarja trocam sozinhos.")
d1 = section(DEMO, "Botões (hover e pressionado)")
dr_ = row(d1, "Botões", gap=24, cross="center")
for tipo in ["Primário", "Secundário", "Link"]:
    b.instance(BTN[(tipo, "Padrão")], dr_)
inv_bg = b.frame(dr_, "fundo bordô", 10, 10, layout="horizontal", pad=16, fill=BORDO, sh="hug", sv="hug")
b.instance(BTN[("Inverso", "Padrão")], inv_bg)
d2 = section(DEMO, "Card de produto (hover), “Adicionar à sacola” e revelar seção")
dr2 = row(d2, "Cards", gap=48, cross="min", wrap=True)
b.instance(CARDS["Padrão"], dr2)
FB_ = {}
for est, lab in [("Padrão", "Comprar"), ("Carregando", "Aguarde"), ("Adicionado", "Adicionado ✓")]:
    cp = b.frame(None, f"Estado={est}", 302, 48, layout="horizontal", gap=8, main="center", cross="center",
                 fill=PRETO if est == "Adicionado" else BORDO, comp=True)
    b.text(cp, lab, "botao", BRANCO, name="label")
    if est == "Carregando":
        dts_ = b.frame(cp, "carregando", 10, 6, layout="horizontal", gap=4, sh="hug", sv="hug")
        for i in range(3):
            b.rect(dts_, 6, 6, BRANCO, name=f"ponto {i + 1}")
    FB_[est] = cp
FB_SET = b.combine(list(FB_.values()), "Feedback · Adicionar à sacola")
b.set(FB_SET, layout="vertical", gap=16, padding=24, sizingH="hug", sizingV="hug", fills=[BRANCO], strokes=[PRETO], strokeWeight=1)
b.reparent(FB_SET, dr2)
b.interaction(FB_["Padrão"], {"type": "onClick"}, {"type": "changeTo", "dest": FB_["Carregando"]}, {"type": "smartAnimate"}, 150, "easeOut")
b.interaction(FB_["Carregando"], {"type": "afterDelay", "ms": 800}, {"type": "changeTo", "dest": FB_["Adicionado"]}, {"type": "smartAnimate"}, 250, "easeOut")
b.interaction(FB_["Adicionado"], {"type": "afterDelay", "ms": 1200}, {"type": "changeTo", "dest": FB_["Padrão"]}, {"type": "smartAnimate"}, 250, "easeOut")
fbx = col(dr2, "Demo feedback", gap=12, w=302)
b.text(fbx, "Clique para testar", "eyebrow", BORDO)
b.instance(FB_["Padrão"], fbx)
RV_ = {}
for est, op, dy in [("Oculto", 0, 16), ("Visível", 1, 0)]:
    cp = b.frame(None, f"Estado={est}", 400, 220, comp=True, fill=BRANCO, stroke=PRETO)
    inner = b.frame(cp, "conteúdo", 352, 172, layout="vertical", gap=12, pad=24, fill=BORDO, x=24, y=24 + dy, opacity=op)
    b.text(inner, "Revelar seção", "eyebrow", BRANCO)
    b.text(inner, "Chocolate não é tudo igual", "h3", BRANCO, fillw=True)
    b.text(inner, "opacidade 0 → 1 · desloca 16px · 600ms", "legenda", BRANCO)
    RV_[est] = cp
RV_SET = b.combine(list(RV_.values()), "Revelar seção")
b.set(RV_SET, layout="horizontal", gap=24, padding=24, sizingH="hug", sizingV="hug", fills=[BRANCO])
b.reparent(RV_SET, dr2)
b.interaction(RV_["Oculto"], {"type": "afterDelay", "ms": 800}, {"type": "changeTo", "dest": RV_["Visível"]}, {"type": "smartAnimate"}, 600, "easeOut")
b.interaction(RV_["Visível"], {"type": "afterDelay", "ms": 2400}, {"type": "changeTo", "dest": RV_["Oculto"]}, {"type": "instant"})
rvx = col(dr2, "Demo revelar", gap=12, w=400)
b.text(rvx, "Repete sozinho", "eyebrow", BORDO)
b.instance(RV_["Oculto"], rvx)
d3 = section(DEMO, "Banner principal (autoplay 6s) e tarja mobile (4s)")
b.instance(HERO_D[0], d3)
b.instance(TM[0], d3)

# =============================================================================
# 00 · Capa
# =============================================================================
b.select_page(P_CAPA)
CAPA = b.frame(None, "Capa", 1440, 810, layout="horizontal", fill=BRANCO, x=0, y=0)
cb_ = b.frame(CAPA, "bloco", 840, 810, layout="vertical", main="center", gap=24, pad=[96, 96, 96, 96], fill=BORDO)
b.text(cb_, "Design system · Tema Lime (Irroba)", "eyebrow", BRANCO)
b.text(cb_, "Var chocolates", "display", BRANCO, textCase="original", fontSize=88, lineHeight=96)
b.text(cb_, "Sabor e aroma para além da intensidade", "h3", BRANCO, fillw=True)
b.rect(cb_, 48, 2, BRANCO, name="fio")
b.text(cb_, "Versão 1.0 · 19/10/2026\nBase: BrandBook Var Chocolates (MMORÁVEL Consultoria) · Referências: Luzz Cacau e Dengo",
       "corpo", BRANCO, fillw=True)
b.image(CAPA, CACAU, 600, 810, name="cacau")
CURSOR[P_CAPA] = 1640

SUM = board(1540, 0, 1440, "Sumário", "Como este arquivo está organizado.")
table(SUM, ["Página", "Conteúdo"], [
    ["00 · Capa", "Capa, sumário, essência da marca e guia de uso do arquivo."],
    ["01 · Fundamentos", "Tipografia (estilos de texto), cores (variáveis, estilos e contraste), espaçamento, grid, bordas, ícones, fotografia e assinatura."],
    ["02 · Componentes", "Botões (4 tipos × 6 estados), etiquetas, selos, campos, navegação, cabeçalhos, cards, título de seção, newsletter, rodapé, overlays e banner."],
    ["03 · Animações & Protótipo", "Tokens de movimento, catálogo de animações e demonstrações interativas."],
    ["04 · Telas Desktop", "Home, Nossa Origem (institucional), Produto e overlay do mini-carrinho — 1440px."],
    ["05 · Telas Mobile", "Home, Nossa Origem, Produto, menu e mini-carrinho — 390px."],
    ["06 · Implementação Lime", "Configurações do tema, ordem dos módulos, CSS/JS personalizados e checklist de publicação."],
], [360, 920])

ESS = board(3080, 0, 1600, "Essência da marca", "Resumo do BrandBook que orienta cada decisão de interface.")
er_ = row(ESS, "Missão e promessa", gap=32)
for t_, d_ in [("Missão", "Criar chocolates finos que expressam a pureza, autenticidade e complexidade sensorial do DNA do cacau."),
               ("Promessa", "Revelar sabores e aromas que superam a intensidade do chocolate, explorando suas nuances mais profundas e sofisticadas."),
               ("Arquétipo", "Criador: inovação, autenticidade e excelência criativa. “Elegantemente simples, sem ser simplório.”")]:
    c = col(er_, t_, gap=12, pad=32, fill=BORDO)
    b.text(c, t_, "eyebrow", BRANCO)
    b.text(c, d_, "corpo_g", BRANCO, fillw=True)
tv = section(ESS, "Tom de voz", "Elegante, acolhedor, com bom humor e didático. Poético e sensorial, mas objetivo.")
table(tv, ["Faça", "Evite"], [
    ["“Para você provar que chocolate não é tudo igual.”", "Ser genérico: “O melhor chocolate do Brasil!”"],
    ["“Notas: frutadas · florais · amadeiradas.”", "Excesso de tecnicismo sem explicar o termo."],
    ["“Sabores que contam histórias desde 1930.”", "Negligenciar a história e a origem."],
    ["“Escolha pelo cacau, como se escolhe um vinho.”", "Ser simplório ou infantil."],
], [720, 720])
pe = section(ESS, "Personas")
pr2 = row(pe, "Personas", gap=32)
for t_, d_ in [("Isabela · 40 · São Paulo", "Empresária, ama gastronomia e origem. Harmoniza com vinhos e queijos. A Home e o produto mostram notas sensoriais e harmonização."),
               ("Sam · 35", "Curadora de lifestyle: presentear é uma experiência e a embalagem deve expressar cuidado. Por isso os presentes ganham seção própria e destaque no banner.")]:
    c = col(pr2, t_, gap=12, pad=32, stroke=PRETO)
    b.text(c, t_, "rotulo", BORDO)
    b.text(c, d_, "corpo", PRETO, fillw=True)

USE = board(4780, 0, 1440, "Como usar este arquivo", "Convenções para quem vai desenhar ou implementar.")
table(USE, ["Recurso", "Onde encontrar", "Regra"], [
    ["Variáveis", "Var · Primitivas · Lime · Tokens do tema · Componentes", "Primitivas guardam os hex; tokens e componentes são aliases."],
    ["Estilos de cor", "Marca/Azul … Marca/Branco", "Ligados às primitivas — nunca digitar hex soltos."],
    ["Estilos de texto", "Desktop/*, Mobile/*, Base/*, Marca/*", "Somente Glacial Indifference (Bold e Regular)."],
    ["Componentes", "02 · Componentes", "Variantes nomeadas Propriedade=Valor (ex.: Tipo=Primário, Estado=Hover)."],
    ["Protótipo", "Fluxos “Home desktop”, “Home mobile”, “Demonstrações de animação”", "Hover, autoplay, overlays e navegação entre telas."],
    ["Conteúdo", "Telas", "Nomes, notas e preços são ilustrativos. Fotos do moodboard em baixa resolução: substituir."],
], [260, 560, 520])

# =============================================================================
# 06 · Implementação Lime
# =============================================================================
b.select_page(P_IMPL)
IM = board(0, 0, 1600, "Configurações do tema (aba Configurações)",
           "Tudo o que o editor do Lime permite configurar sem código.")
table(IM, ["Configuração", "Valor", "Observação"], [
    ["Paleta", "Personalizada: primary #6D071A/#FFFFFF · secondary #000000/#FFFFFF · neutral #900C3A/#FFFFFF · body #FFFFFF/#000000", "Todos os pares passam no selo AA do modal."],
    ["Tipografia", "Personalizada · títulos 32px, AG, centralizado · texto 16px", "A família é aplicada pelo CSS (Glacial não está no Google Fonts)."],
    ["Arredondamento", "Sem arredondamento", "Blocos retos do BrandBook."],
    ["Botões", "Primário: fundo #6D071A, texto #FFFFFF · Secundário: fundo #FFFFFF, texto #000000", "Contorno e estados via CSS."],
    ["Cabeçalho", "Layout 3 · fixo ao rolar (sticky) · fundo branco, opacidade 1 · expandido", "Busca à esquerda, logo central, categorias abaixo."],
    ["Banner v2", "Carrossel 100% · setas e paginação ligadas · desktop 1920×854 · mobile 780×976", "Texto e botão fazem parte da arte."],
    ["Etiquetas personalizadas", "Forastero #16346C · Trinitário #5B2270 · Catongo #D3723D (texto preto) · Presente #6D071A", "Fonte 12px, raio 0."],
], [300, 780, 360])
MO = board(1700, 0, 1600, "Ordem dos módulos da Home", "Personalizar Loja → módulos, nesta ordem.")
table(MO, ["#", "Módulo Lime", "Conteúdo", "Componente no FigCraft"], [
    ["1", "overline (Tarja)", "3 mensagens: frete, parcelamento, WhatsApp", "Tarja/Desktop · Tarja/Mobile"],
    ["2", "header Layout 3", "Busca · logo · conta, favoritos, sacola · menu", "Cabeçalho/Desktop · Cabeçalho/Mobile"],
    ["3", "banner_v2 Carrossel 100%", "3 slides: tagline, presentes, varietais", "Banner principal/Desktop · /Mobile"],
    ["4", "bannerTarja (4 itens)", "Tree to bar · Cacau varietal · Desde 1930 · Compra segura", "Benefício"],
    ["5", "banner_v2 Grade (4 blocos)", "Escolha pelo varietal", "Bloco de varietal (tela)"],
    ["6", "productList", "Os preferidos de quem prova", "Card de produto"],
    ["7", "htmlContent", "Manifesto “Chocolate não é tudo igual”", "Manifesto (tela)"],
    ["8", "productList", "Presentes que contam histórias", "Card de produto"],
    ["9", "bannerVideo 100%", "O snap, o aroma, o derreter", "Vídeo sensorial (tela)"],
    ["10", "review", "Quem provou, sentiu a diferença", "Avaliação"],
    ["11", "newsletter", "Aprenda a degustar", "Newsletter/Desktop · /Mobile"],
    ["12", "footerInformation", "Marca, institucional, ajuda, atendimento", "Rodapé/Desktop · /Mobile"],
    ["13", "footerSeals · footerLegal", "Pagamentos, segurança, CNPJ", "Selos/Desktop · /Mobile"],
], [60, 340, 560, 480])
CSSB = board(0, 1700, 1600, "CSS e JS personalizados (aba Código)",
             "Arquivos completos em conteudo-mvp/lime-implementacao (var-lime.css e var-lime.js). Trecho principal:")
code = open("lime.css", encoding="utf-8").read().split("/* 4.")[0]
cbx = b.frame(CSSB, "Código", 1440, 10, layout="vertical", pad=32, fill=PRETO, sv="hug", sh="fill")
b.text(cbx, code, "codigo", BRANCO, fillw=True)
CK = board(1700, 1700, 1600, "Checklist de publicação", "Antes de clicar em Publicar no editor do tema.")
table(CK, ["✓", "Item"], [
    ["☐", "Logotipo vetorial oficial recebido e aplicado (substitui a assinatura tipográfica)."],
    ["☐", "Arquivos .woff2 da Glacial Indifference (Regular, Bold, Italic) enviados e URLs trocadas no CSS."],
    ["☐", "Fotos de produção em alta resolução (produtos em fundo branco, cacau, fazenda)."],
    ["☐", "Artes do banner exportadas: 1920×854 (desktop) e 780×976 (mobile)."],
    ["☐", "Etiquetas personalizadas criadas por varietal."],
    ["☐", "Textos revisados com o tom de voz e aprovados pelos guardiões da marca."],
    ["☐", "Contrastes conferidos no modal Personalizar Cores (todos AA)."],
    ["☐", "Teste no mobile: tarja, menu, carrossel de produtos, mini-carrinho."],
], [80, 1360])

# =============================================================================
# Fluxos do protótipo
# =============================================================================
b.select_page(P_DESK)
b.c("proto.flow.add", start=HOME, name="Home desktop")
b.select_page(P_MOB)
b.c("proto.flow.add", start=HOME_M, name="Home mobile")
b.select_page(P_ANIM)
b.c("proto.flow.add", start=DEMO, name="Demonstrações de animação")
b.select_page(P_CAPA)
