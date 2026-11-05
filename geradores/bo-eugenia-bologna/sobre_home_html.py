# Gera a chamada institucional da Home (módulo Conteúdo HTML), no lugar do banner v2 "Sobre a Bô (chamada)".
# CSS apenas inline, sem <style> e sem <script>. Saídas: ../sobre-home.html e ../sobre-home-preview.html.
import os

from sobre_html import SERIF, SANS, VERDE, PRETO, BRANCO, st, EY, P

AQUI = os.path.dirname(os.path.abspath(__file__))
CDN = "https://img.irroba.com.br/tessjbaf/catalog/bo-eugenia/"
CREME = "#F6F3EE"
VALORES = [("I", "Autenticidade"), ("II", "Criatividade"), ("III", "Autoamor")]


def bloco(base):
    h = []
    a = h.append
    # o tema põe o módulo HTML dentro de .container (max-width 1280px); o bloco sai dele e ocupa a largura da janela
    a(f'<div style="{st(position="relative", left="50%", width="100vw", max_width="100vw", margin="0 0 0 -50vw", background=CREME, color=PRETO, box_sizing="border-box")}">')
    a(f'<div style="{st(display="flex", flex_wrap="wrap", align_items="stretch", width="100%")}">')
    # imagem
    a(f'<div style="{st(flex="1 1 300px", min_width="0")}">'
      f'<a href="/sobre-a-bo" style="{st(display="block")}">'
      f'<img src="{base}wa35.jpg" alt="Mulher de costas vestindo kimono azul com dragão bordado" '
      f'style="{st(display="block", width="100%", height="100%", max_height="880px", aspect_ratio="4/5", object_fit="cover", margin="0")}"></a></div>')
    # texto
    a(f'<div style="{st(flex="1 1 300px", min_width="0", display="flex", flex_direction="column", justify_content="center", padding="clamp(48px,7vw,112px) clamp(16px,6vw,96px)", box_sizing="border-box")}">')
    a(f'<p style="{EY};{st(color=VERDE)}">A Bô · Eugenia Bologna</p>')
    a(f'<h2 style="{st(font_family=SERIF, font_weight="300", font_size="clamp(34px,4vw,56px)", line_height="1.08", margin="0 0 24px", color=PRETO)}">'
      f'Kimonos que não pertencem a nenhuma estação.</h2>')
    a(f'<p style="{P};{st(max_width="520px")}">Peças autorais, bordadas e estampadas, feitas para durar e atravessar gerações. '
      f'Escolhidas pelo que dizem, não pelo calendário.</p>')
    # valores
    a(f'<div style="{st(display="flex", flex_wrap="wrap", gap="0", margin="16px 0 40px", border_top=f"1px solid {PRETO}", max_width="520px")}">')
    for n, t in VALORES:
        a(f'<div style="{st(flex="1 1 96px", padding="16px 12px 0 0", box_sizing="border-box")}">'
          f'<p style="{st(font_family=SANS, font_size="11px", letter_spacing=".2em", margin="0 0 6px", color=VERDE)}">{n}</p>'
          f'<p style="{st(font_family=SERIF, font_style="italic", font_size="clamp(19px,1.8vw,24px)", line_height="1.2", margin="0", color=PRETO)}">{t}</p></div>')
    a('</div>')
    btn = st(display="inline-block", font_family=SANS, font_size="13px", letter_spacing=".12em", text_transform="uppercase",
             text_decoration="none", padding="16px 36px", margin="0 12px 12px 0", box_sizing="border-box")
    a(f'<div><a href="/sobre-a-bo" style="{btn};{st(background=PRETO, color=BRANCO, border=f"1px solid {PRETO}")}">Conheça a Bô</a>'
      f'<a href="https://www.instagram.com/boeugeniabologna/" target="_blank" rel="noopener" '
      f'style="{btn};{st(background="transparent", color=PRETO, border=f"1px solid {PRETO}")}">@boeugeniabologna</a></div>')
    a('</div></div></div>')
    return "\n".join(h)


final = bloco(CDN)
open(os.path.join(AQUI, "..", "sobre-home.html"), "w", encoding="utf-8").write(final + "\n")
prev = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Chamada Sobre · prévia</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@300;400&display=swap">'
        '</head><body style="margin:0;background:#fff">' + bloco("img/") + '</body></html>')
open(os.path.join(AQUI, "..", "sobre-home-preview.html"), "w", encoding="utf-8").write(prev.replace('src="img/', 'src="gerador/img/'))
open(os.path.join(AQUI, "..", "sobre-home-preview-390.html"), "w", encoding="utf-8").write(
    prev.replace('src="img/', 'src="gerador/img/').replace('<body style="margin:0;background:#fff">', '<body style="margin:0;background:#ccc"><div style="width:390px;background:#fff">').replace('</body>', '</div></body>'))
print("ok", len(final), "caracteres")
