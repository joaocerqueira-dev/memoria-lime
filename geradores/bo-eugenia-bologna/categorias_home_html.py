# Gera a seção "Universo Bô" da Home (módulo Conteúdo HTML), no lugar do banner v2 de categorias (105).
# Sem <style> e sem <script>: as animações são SVG nativo (SMIL, <animate>), que roda só com o HTML.
#  · Kimonos e Panôs: fotos em fusão contínua + zoom lento (viewBox animado)
#  · Acessórios: foto dos braceletes com selo de texto girando no canto
#  · faixa final com os nomes das categorias correndo
# Saídas: ../categorias-home.html e ../categorias-home-preview.html.
import os

from sobre_html import SERIF, SANS, VERDE, LARANJA, PRETO, BRANCO, st, EY, P

AQUI = os.path.dirname(os.path.abspath(__file__))
CDN = "https://img.irroba.com.br/tessjbaf/catalog/bo-eugenia/"
FULL = st(position="relative", left="50%", width="100vw", max_width="100vw", margin_left="-50vw", box_sizing="border-box")
SLOT = 4.5  # segundos de cada foto na fusão


def fusao(base, fotos, atraso):
    """SVG 3:4 com as fotos empilhadas: cada uma aparece por SLOT segundos e a última volta para a primeira."""
    n = len(fotos)
    dur = SLOT * n
    s, f = 1 / n, 0.25 / n
    h = [f'<svg viewBox="0 0 600 800" preserveAspectRatio="xMidYMid slice" style="{st(position="absolute", inset="0", width="100%", height="100%", display="block")}" aria-hidden="true">'
         f'<animate attributeName="viewBox" values="0 0 600 800;30 40 540 720;0 0 600 800" dur="24s" begin="{-atraso}s" repeatCount="indefinite"/>']
    for i, foto in enumerate(fotos):
        if foto.startswith("banner-cat-"):
            # artes enviadas para o banner 105: o nome da categoria vem gravado no rodapé; a imagem fica mais alta que o quadro
            # e alinhada pelo topo, para o nome ficar de fora
            img = f'<image href="{base}{foto}-desktop.webp" x="0" y="0" width="600" height="1000" preserveAspectRatio="xMidYMin slice"'
        else:
            img = f'<image href="{base}{foto}.jpg" x="0" y="0" width="600" height="800" preserveAspectRatio="xMidYMid slice"'
        if i == 0:
            h.append(img + "/>")
            continue
        ini = i * s
        if i == n - 1:
            kt, vs = [0, ini - f, ini, 1 - f, 1], [0, 0, 1, 1, 0]
        else:
            kt, vs = [0, ini - f, ini, ini + s, ini + s + 0.001, 1], [0, 0, 1, 1, 0, 0]
        h.append(img + ' opacity="0">'
                 f'<animate attributeName="opacity" values="{";".join(map(str, vs))}" keyTimes="{";".join(f"{k:.4f}" for k in kt)}" '
                 f'dur="{dur}s" begin="{-atraso}s" repeatCount="indefinite"/></image>')
    h.append("</svg>")
    return "".join(h)


def selo(base):
    """Acessórios: foto dos braceletes com um selo de texto girando no canto superior."""
    txt = "BRACELETES · ACESSÓRIOS BÔ · "
    return (f'<svg viewBox="0 0 600 800" preserveAspectRatio="xMidYMid slice" style="{st(position="absolute", inset="0", width="100%", height="100%", display="block")}" aria-hidden="true">'
            f'<animate attributeName="viewBox" values="0 0 600 800;30 40 540 720;0 0 600 800" dur="24s" begin="-4.4s" repeatCount="indefinite"/>'
            f'<image href="{base}banner-cat-acessorios-desktop.webp" x="0" y="0" width="600" height="1000" preserveAspectRatio="xMidYMin slice"/>'
            f'<defs><path id="bo-selo" d="M430,74 a76,76 0 1,1 -0.1,0"/></defs>'
            f'<circle cx="430" cy="150" r="54" fill="none" stroke="{BRANCO}" stroke-opacity=".5"/>'
            f'<circle cx="430" cy="150" r="9" fill="{LARANJA}"><animate attributeName="r" values="7;12;7" dur="4s" repeatCount="indefinite"/></circle>'
            f'<g><animateTransform attributeName="transform" type="rotate" from="0 430 150" to="360 430 150" dur="22s" repeatCount="indefinite"/>'
            f'<text font-family="Jost, Arial, sans-serif" font-size="14" letter-spacing="3" fill="{BRANCO}">'
            f'<textPath href="#bo-selo" textLength="476" lengthAdjust="spacing">{txt}</textPath></text></g>'
            f'</svg>')


def card(i, nome, link, chamada, desenho):
    grad = "linear-gradient(to top, rgba(0,0,0,.62), rgba(0,0,0,0) 55%)"
    return (f'<a href="{link}" style="{st(flex="1 0 280px", position="relative", display="block", aspect_ratio="3/4", overflow="hidden", text_decoration="none", color=BRANCO, background=PRETO, scroll_snap_align="start")}">'
            + desenho +
            f'<span style="{st(position="absolute", inset="0", background=grad)}"></span>'
            f'<span style="{st(position="absolute", left="0", right="0", bottom="0", padding="clamp(20px,2.4vw,32px)", display="block")}">'
            f'<span style="{st(display="block", font_family=SANS, font_size="11px", letter_spacing=".24em", margin="0 0 10px", color=BRANCO)}">0{i} / 03</span>'
            f'<span style="{st(display="block", font_family=SERIF, font_weight="300", font_size="clamp(40px,3.6vw,56px)", line_height="1", margin="0 0 14px", color=BRANCO)}">{nome}</span>'
            f'<span style="{st(display="inline-block", font_family=SANS, font_size="12px", letter_spacing=".16em", text_transform="uppercase", padding_bottom="4px", border_bottom=f"1px solid {BRANCO}", color=BRANCO)}">{chamada} →</span>'
            f'</span></a>')


def faixa():
    """Nomes das categorias correndo da direita para a esquerda; 3 cópias de 1200 unidades fazem o laço sem emenda."""
    txt = "Kimonos · Panôs · Acessórios · Galeria Bô · ".replace(" ", " ")  # espaço fixo: o SVG junta espaços e a emenda das cópias some
    copias = "".join(f'<text x="{x}" y="58" font-family="Cormorant Garamond, Georgia, serif" font-style="italic" font-size="52" fill="{PRETO}" '
                     f'textLength="1200" lengthAdjust="spacingAndGlyphs">{txt}</text>' for x in (0, 1200, 2400))
    return (f'<svg viewBox="0 0 2400 80" preserveAspectRatio="xMinYMid slice" style="{st(display="block", width="100%", height="72px")}" aria-hidden="true">'
            f'<g><animateTransform attributeName="transform" type="translate" from="0 0" to="-1200 0" dur="28s" repeatCount="indefinite"/>{copias}</g></svg>')


def bloco(base):
    h = []
    a = h.append
    # o tema põe o módulo HTML dentro de .container (max-width 1280px); o bloco sai dele e ocupa a largura da janela
    a(f'<div style="{FULL};{st(background=BRANCO, color=PRETO, padding="clamp(56px,7vw,104px) 0 0")}">')
    a(f'<div style="{st(max_width="1440px", margin="0 auto", padding="0 clamp(16px,3vw,40px)", box_sizing="border-box")}">')
    a(f'<div style="{st(display="flex", flex_wrap="wrap", gap="16px 64px", align_items="flex-end", justify_content="space-between", margin="0 0 clamp(24px,3vw,40px)")}">')
    a(f'<div><p style="{EY};{st(color=VERDE)}">Universo Bô</p>'
      f'<h2 style="{st(font_family=SERIF, font_weight="300", font_size="clamp(36px,4.4vw,64px)", line_height="1.04", margin="0", color=PRETO)}">Três caminhos<br><em>para entrar na galeria.</em></h2></div>')
    a(f'<p style="{P};{st(max_width="380px", margin="0")}">Peças autorais que atravessam estações. Escolha por onde começar.</p>')
    a('</div>')
    # trilho: 3 colunas no computador; no celular vira carrossel com arraste e encaixe
    a(f'<div style="{st(display="flex", gap="8px", overflow_x="auto", scroll_snap_type="x mandatory", padding_bottom="4px", scrollbar_width="none")}">')
    a(card(1, "Kimonos", "/kimono", "Ver kimonos", fusao(base, ["banner-cat-kimono", "wa38", "ed09"], 0)))
    a(card(2, "Panôs", "/pano", "Ver panôs", fusao(base, ["banner-cat-panos", "voar-solar", "voar-telurica", "voar-magnetica"], 2.2)))
    a(card(3, "Acessórios", "/acessorios", "Conhecer", selo(base)))
    a('</div></div>')
    a(f'<div style="{st(margin_top="clamp(40px,5vw,72px)", border_top=f"1px solid {PRETO}", border_bottom=f"1px solid {PRETO}", padding="8px 0", overflow="hidden")}">{faixa()}</div>')
    a('</div>')
    return "\n".join(h)


final = bloco(CDN)
open(os.path.join(AQUI, "..", "categorias-home.html"), "w", encoding="utf-8").write(final + "\n")
prev = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Universo Bô · prévia</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@300;400&display=swap">'
        '</head><body style="margin:0;background:#fff;overflow-x:hidden"><div style="max-width:1280px;margin:0 auto">' + final + '</div></body></html>')
open(os.path.join(AQUI, "..", "categorias-home-preview.html"), "w", encoding="utf-8").write(prev)
print("ok", len(final), "caracteres")
