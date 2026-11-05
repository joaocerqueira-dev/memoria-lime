# Gera a seção de panôs da Home (módulo Conteúdo HTML), no lugar do banner v2 "Panôs" (106).
# Só CSS inline. Efeito: as quatro atmosferas são painéis sticky que se empilham ao rolar a página.
# Saídas: ../panos-home.html e ../panos-home-preview.html.
import os

from sobre_html import SERIF, SANS, VERDE, PRETO, BRANCO, st, EY, P

AQUI = os.path.dirname(os.path.abspath(__file__))
CDN = "https://img.irroba.com.br/tessjbaf/catalog/bo-eugenia/"
TOPO = "112px"  # cabeçalho sticky do Lime (z-index 1000) + tarja; os painéis colam no topo, por baixo dele, e reservam essa faixa
ATM = [
    ("Solar", "solar", "Quente · clara · intensa", "Luz de meio-dia: amarelos e laranjas que aquecem e acendem o rosto.", "#F2B33D", PRETO),
    ("Etérea", "eterea", "Fria · clara · suave", "Azuis enevoados e cinzas leves, como o céu antes da chuva.", "#C9D8DE", PRETO),
    ("Telúrica", "telurica", "Quente · profunda · densa", "Terra, ferrugem e cobre: a estampa com o peso do chão.", "#7B3A1D", BRANCO),
    ("Magnética", "magnetica", "Fria · profunda · intensa", "Azul-noite e contrastes firmes, para quem gosta de presença.", "#1E2D5E", BRANCO),
]
FULL = st(position="relative", left="50%", width="100vw", max_width="100vw", margin_left="-50vw", box_sizing="border-box")


def bloco(base):
    h = []
    a = h.append
    # o tema põe o módulo HTML dentro de .container (max-width 1280px); o bloco sai dele e ocupa a largura da janela
    a(f'<div style="{FULL};{st(background=BRANCO, color=PRETO)}">')
    # abertura
    a(f'<div style="{st(max_width="1280px", margin="0 auto", padding="clamp(64px,8vw,120px) 16px clamp(40px,5vw,64px)", box_sizing="border-box", display="flex", flex_wrap="wrap", gap="24px 64px", align_items="flex-end")}">')
    a(f'<div style="{st(flex="1 1 320px")}"><p style="{EY};{st(color=VERDE)}">Panôs · Estampa Voar</p>'
      f'<h2 style="{st(font_family=SERIF, font_weight="300", font_size="clamp(38px,5vw,72px)", line_height="1.02", margin="0", color=PRETO)}">'
      f'Uma estampa,<br><em style="{st(font_style="italic")}">quatro atmosferas.</em></h2></div>')
    a(f'<div style="{st(flex="1 1 320px")}"><p style="{P};{st(margin="0 0 12px")}">Temperatura, luz, profundidade e intensidade mudam a mesma estampa. '
      f'Role a página e veja cada atmosfera chegar sobre a anterior.</p>'
      f'<p style="{st(font_family=SANS, font_size="12px", letter_spacing=".2em", text_transform="uppercase", margin="0", color=PRETO)}">100% viscose · 2 m × 1,40 m</p></div>')
    a('</div>')
    # painéis empilháveis
    a('<div>')
    for i, (nome, slug, sub, frase, cor, fg) in enumerate(ATM, 1):
        linha = "rgba(255,255,255,.45)" if fg == BRANCO else "rgba(0,0,0,.35)"
        a(f'<div style="{st(position="sticky", top="0", z_index=str(i), background=cor, color=fg, min_height="100vh", padding_top=TOPO, display="flex", align_items="center", box_shadow="0 -24px 48px rgba(0,0,0,.18)", box_sizing="border-box", overflow="hidden")}">')
        a(f'<div style="{st(width="100%", max_width="1440px", margin="0 auto", padding="clamp(20px,4vw,72px) clamp(16px,4vw,64px)", box_sizing="border-box", display="flex", flex_wrap="wrap", gap="20px clamp(32px,5vw,80px)", align_items="center")}">')
        # imagem primeiro: no celular ela fica no alto e o painel inteiro cabe numa tela antes do próximo cobrir
        a(f'<div style="{st(flex="1.4 1 340px", min_width="0", position="relative")}">')
        a(f'<a href="/pano-estampa-voar" style="{st(display="block")}"><img src="{base}voar-{slug}.jpg" alt="Panô estampa Voar na atmosfera {nome}" '
          f'style="{st(display="block", width="100%", height="auto", max_height="64vh", aspect_ratio="10/7", object_fit="cover", margin="0")}"></a>')
        a(f'<a href="/pano-estampa-voar-linha-terracota" style="{st(position="absolute", right="12px", bottom="12px", width="clamp(84px,20%,180px)", display="block", text_decoration="none", background=cor, padding="6px", box_sizing="border-box")}">'
          f'<img src="{base}terracota-{slug}.jpg" alt="Panô Voar Linha Terracota na atmosfera {nome}" style="{st(display="block", width="100%", aspect_ratio="1/1", object_fit="cover", margin="0")}">'
          f'<span style="{st(display="block", font_family=SANS, font_size="9px", letter_spacing=".16em", text_transform="uppercase", margin="6px 0 0", color=fg)}">Linha Terracota</span></a>')
        a('</div>')
        # texto
        a(f'<div style="{st(flex="1 1 300px", min_width="0")}">')
        a(f'<p style="{st(font_family=SANS, font_size="12px", letter_spacing=".24em", margin="0 0 clamp(12px,2vw,20px)", color=fg, border_bottom=f"1px solid {linha}", padding_bottom="12px")}">0{i} / 04 · ATMOSFERA</p>')
        a(f'<p style="{st(font_family=SERIF, font_style="italic", font_weight="300", font_size="clamp(52px,10vw,152px)", line_height=".9", margin="0 0 clamp(10px,1.6vw,20px)", color=fg, letter_spacing="-.01em")}">{nome}</p>')
        a(f'<p style="{st(font_family=SANS, font_size="12px", letter_spacing=".2em", text_transform="uppercase", margin="0 0 12px", color=fg)}">{sub}</p>')
        a(f'<p style="{st(font_family=SANS, font_weight="300", font_size="16px", line_height="1.6", margin="0 0 clamp(20px,2.4vw,32px)", max_width="420px", color=fg)}">{frase}</p>')
        a(f'<a href="/pano-estampa-voar" style="{st(display="inline-block", font_family=SANS, font_size="13px", letter_spacing=".12em", text_transform="uppercase", text_decoration="none", padding="14px 28px", border=f"1px solid {fg}", color=fg)}">Ver panô Voar · {nome}</a>')
        a('</div>')
        a('</div></div>')
    a('</div>')
    # fechamento
    a(f'<div style="{st(position="relative", z_index="5", background=PRETO, color=BRANCO, padding="clamp(48px,6vw,88px) 16px", text_align="center")}">')
    a(f'<p style="{st(font_family=SERIF, font_style="italic", font_weight="300", font_size="clamp(26px,3vw,40px)", line_height="1.25", margin="0 auto 32px", max_width="760px", color=BRANCO)}">'
      f'São caminhos de harmonização, nunca regras: a escolha é sua.</p>')
    btn = st(display="inline-block", font_family=SANS, font_size="13px", letter_spacing=".12em", text_transform="uppercase", text_decoration="none", padding="16px 36px", margin="6px")
    a(f'<a href="/pano" style="{btn};{st(background=BRANCO, color=PRETO, border=f"1px solid {BRANCO}")}">Ver todos os panôs</a>'
      f'<a href="/pano-estampa-voar-linha-terracota" style="{btn};{st(color=BRANCO, border=f"1px solid {BRANCO}")}">Linha Terracota</a>')
    a('</div>')
    a('</div>')
    return "\n".join(h)


final = bloco(CDN)
open(os.path.join(AQUI, "..", "panos-home.html"), "w", encoding="utf-8").write(final + "\n")
prev = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Panôs · prévia</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@300;400&display=swap">'
        '</head><body style="margin:0;background:#fff;overflow-x:hidden">'
        f'<div style="position:sticky;top:0;z-index:50;height:{TOPO};background:#fff;border-bottom:1px solid #000;display:flex;align-items:center;justify-content:center;font-family:Jost,sans-serif;font-size:13px;letter-spacing:.1em">CABEÇALHO DO TEMA</div>'
        '<div style="max-width:1280px;margin:0 auto">' + bloco("gerador/img/") + '</div><div style="height:60vh"></div></body></html>')
open(os.path.join(AQUI, "..", "panos-home-preview.html"), "w", encoding="utf-8").write(prev)
print("ok", len(final), "caracteres")
