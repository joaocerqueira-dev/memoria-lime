# Gera a página "Sobre a Bô" para Catálogo → Informações: HTML com CSS apenas inline (sem <style> e sem <script>).
# Saídas: ../sobre-a-bo.html (colar no modo código do editor) e ../sobre-a-bo-preview.html (prévia local com as fotos).
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
SERIF = "'Cormorant Garamond', Georgia, serif"
SANS = "'Jost', Arial, sans-serif"
VERDE, LARANJA, PRETO, BRANCO = "#026526", "#E7760A", "#000000", "#FFFFFF"
ATM = [("Solar", "quente · clara · intensa", "#F2B33D", PRETO), ("Etérea", "fria · clara · suave", "#C9D8DE", PRETO),
       ("Telúrica", "quente · profunda · densa", "#7B3A1D", BRANCO), ("Magnética", "fria · profunda · intensa", "#1E2D5E", BRANCO)]
FOTOS = {"abertura": "ia03", "par1": "wa35", "par2": "wa38", "atelie": "ed09",
         "Solar": "voar-solar", "Etérea": "voar-eterea", "Telúrica": "voar-telurica", "Magnética": "voar-magnetica"}


def st(**kw):
    return ";".join(f"{k.replace('_', '-')}:{v}" for k, v in kw.items())


EY = st(font_family=SANS, font_size="12px", letter_spacing=".2em", text_transform="uppercase", margin="0 0 16px", color=PRETO)
P = st(font_family=SANS, font_size="17px", line_height="1.75", font_weight="300", margin="0 0 20px", color=PRETO)
H2 = st(font_family=SERIF, font_weight="300", font_size="clamp(34px,4.6vw,60px)", line_height="1.08", margin="0 0 28px", color=PRETO)
H3 = st(font_family=SERIF, font_weight="400", font_size="28px", line_height="1.2", margin="0 0 12px", color=PRETO)
FIO = st(border="0", border_top=f"1px solid {PRETO}", margin="0", width="100%")
BLOCO = st(margin="0 auto 96px", max_width="1120px", padding="0 16px", box_sizing="border-box")


def img(key, base, alt, ratio=None):
    s = st(display="block", width="100%", height="auto", margin="0")
    if ratio:
        s += ";" + st(aspect_ratio=ratio, object_fit="cover")
    return f'<img src="{base}{FOTOS[key]}.jpg" alt="{alt}" style="{s}">'


def pagina(base):
    h = []
    a = h.append
    a(f'<div style="{st(width="100%", background=BRANCO, color=PRETO)}">')
    # 1 · abertura
    a(f'<div style="{BLOCO};{st(text_align="center", padding_top="24px")}">')
    a(f'<p style="{EY};{st(color=VERDE)}">Bô · Eugenia Bologna</p>')
    a(f'<h2 style="{H2};{st(max_width="860px", margin_left="auto", margin_right="auto")}">Uma galeria de kimonos que não pertencem a nenhuma estação.</h2>')
    a(f'<p style="{P};{st(max_width="640px", margin_left="auto", margin_right="auto")}">Kimonos, panôs e acessórios pensados como peças autorais: '
      f'feitos para durar, para atravessar gerações e para serem escolhidos pelo que dizem, não pelo calendário.</p>')
    a('</div>')
    a(f'<div style="{st(margin="0 auto 24px", max_width="1440px")}">{img("abertura", base, "Kimono branco bordado com dragão em meio à névoa", "16/7")}</div>')
    a(f'<p style="{st(font_family=SANS, font_size="12px", letter_spacing=".2em", text_transform="uppercase", text_align="center", margin="0 0 96px")}">Kimono longo · Névoa</p>')
    # 2 · a marca (duas colunas)
    a(f'<div style="{BLOCO}"><hr style="{FIO}">')
    a(f'<div style="{st(display="flex", flex_wrap="wrap", gap="32px 64px", padding_top="32px")}">')
    a(f'<div style="{st(flex="1 1 240px")}"><p style="{EY}">01 · A marca</p></div>')
    a(f'<div style="{st(flex="2 1 420px")}">')
    a(f'<p style="{P}">A Bô nasce do desejo de Eugenia Bologna de unir o trabalho como estilista ao serviço como consultora de imagem, '
      f'trazendo cor e sentimentos positivos à vida.</p>')
    a(f'<p style="{P}">O kimono é o centro de tudo: peças curtas e longas, bordadas e estampadas, que vestem mulheres de 13 a 98 anos.</p>')
    a(f'<p style="{P}">Não trabalhamos com coleções de primavera, verão, outono ou inverno. Enquanto um tecido ou uma matéria-prima '
      f'existir, o mesmo kimono pode continuar sendo produzido por anos, sob demanda ou em pouquíssimas unidades.</p>')
    a('</div></div></div>')
    # 3 · citação
    a(f'<div style="{BLOCO};{st(text_align="center")}">')
    a(f'<p style="{st(font_family=SERIF, font_style="italic", font_weight="300", font_size="clamp(28px,3.4vw,44px)", line_height="1.25", margin="0 auto", max_width="900px")}">'
      f'“Uma peça pode estar Em Cena pela sua força autoral, estética ou narrativa, mesmo que tenha sido criada há anos.”</p>')
    a(f'<p style="{EY};{st(margin_top="24px")}">Eugenia Bologna</p>')
    a('</div>')
    # 4 · valores da marca (página Nossos Valores da loja atual)
    a(f'<div style="{BLOCO}">')
    a(f'<div style="{st(display="flex", flex_wrap="wrap", gap="40px")}">')
    for n, t, d in [("I", "Autenticidade", "Moda como forma de expressão, assim como a fala e a escrita: uma extensão da personalidade de cada pessoa."),
                    ("II", "Criatividade", "Estampas e bordados autorais, que nascem de uma narrativa e não de uma tendência."),
                    ("III", "Autoamor", "Nossa missão é contribuir para a autoconfiança, com peças que dialogam com a identidade de cada cliente.")]:
        a(f'<div style="{st(flex="1 1 260px", border_top=f"1px solid {PRETO}", padding_top="24px")}">')
        a(f'<p style="{EY};{st(color=VERDE)}">{n}</p><h3 style="{H3}">{t}</h3><p style="{P};{st(margin="0")}">{d}</p></div>')
    a('</div></div>')
    # 5 · par de imagens
    a(f'<div style="{BLOCO}"><div style="{st(display="flex", flex_wrap="wrap", gap="16px")}">')
    for k, alt in [("par1", "Kimono azul com dragão bordado nas costas"), ("par2", "Kimono preto com bordado prateado, em preto e branco")]:
        a(f'<div style="{st(flex="1 1 300px")}">{img(k, base, alt, "3/4")}</div>')
    a('</div></div>')
    # 6 · atmosferas
    a(f'<div style="{BLOCO}"><hr style="{FIO}">')
    a(f'<div style="{st(display="flex", flex_wrap="wrap", gap="32px 64px", padding_top="32px", margin_bottom="40px")}">')
    a(f'<div style="{st(flex="1 1 240px")}"><p style="{EY}">02 · As atmosferas</p></div>')
    a(f'<div style="{st(flex="2 1 420px")}"><p style="{P}">Cada estampa Bô nasce em quatro atmosferas cromáticas: Solar, Etérea, Telúrica e Magnética. '
      f'Elas exploram diferentes relações entre temperatura, luminosidade, profundidade e intensidade e podem dialogar de maneiras distintas '
      f'com cada beleza. São caminhos de harmonização, nunca regras: a escolha é sua.</p></div></div>')
    a(f'<div style="{st(display="flex", flex_wrap="wrap", gap="8px")}">')
    for nm, d, hx, fg in ATM:
        a(f'<div style="{st(flex="1 1 160px")}">{img(nm, base, f"Panô estampa Voar na atmosfera {nm}", "1/1")}'
          f'<p style="{st(font_family=SERIF, font_style="italic", font_size="26px", margin="12px 0 0", color=PRETO)}">{nm}</p>'
          f'<p style="{st(font_family=SANS, font_size="11px", letter_spacing=".2em", text_transform="uppercase", margin="4px 0 0", color=PRETO)}">{d}</p></div>')
    a('</div></div>')
    # 7 · ateliê: imagem + texto
    a(f'<div style="{BLOCO}"><div style="{st(display="flex", flex_wrap="wrap", gap="48px", align_items="center")}">')
    a(f'<div style="{st(flex="1 1 360px")}">{img("atelie", base, "Kimono branco texturizado entre galhos secos", "1/1")}</div>')
    a(f'<div style="{st(flex="1 1 360px")}"><p style="{EY}">03 · Para quem</p>')
    a(f'<p style="{st(font_family=SERIF, font_weight="300", font_size="clamp(56px,7vw,96px)", line_height="1", margin="0 0 16px")}">13 a 98</p>')
    a(f'<p style="{P}">É a faixa de idade de quem veste Bô. O kimono não tem idade, tamanho de tendência nem prazo de validade: '
      f'ele se adapta a quem o escolhe.</p></div>')
    a('</div></div>')
    # 8 · chamada final
    a(f'<div style="{st(background=VERDE, color=BRANCO, padding="80px 16px", text_align="center", margin="0")}">')
    a(f'<p style="{EY};{st(color=BRANCO)}">Em cena agora</p>')
    a(f'<p style="{st(font_family=SERIF, font_weight="300", font_size="clamp(30px,3.6vw,48px)", line_height="1.15", margin="0 auto 32px", max_width="720px", color=BRANCO)}">'
      f'Conheça as peças que escolhemos para este momento.</p>')
    btn = st(display="inline-block", font_family=SANS, font_size="13px", letter_spacing=".12em", text_transform="uppercase",
             text_decoration="none", padding="16px 40px", margin="8px")
    a(f'<a href="/kimonos" style="{btn};{st(background=BRANCO, color=PRETO)}">Ver kimonos</a>')
    a(f'<a href="https://www.instagram.com/boeugeniabologna/" style="{btn};{st(border=f"1px solid {BRANCO}", color=BRANCO)}">@boeugeniabologna</a>')
    a('</div>')
    a('</div>')
    return "\n".join(h)


final = pagina("URL-DA-PASTA-DE-IMAGENS/")
open(os.path.join(AQUI, "..", "sobre-a-bo.html"), "w", encoding="utf-8").write(final + "\n")
prev = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Sobre a Bô · prévia</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@300;400&display=swap">'
        '</head><body style="margin:0;background:#fff">'
        '<div style="font-family:Jost,sans-serif;text-align:center;padding:24px;border-bottom:1px solid #000;font-size:13px;letter-spacing:.1em">CABEÇALHO DO TEMA · KIMONOS · PANÔS · ACESSÓRIOS</div>'
        '<h1 style="font-family:\'Cormorant Garamond\',serif;font-weight:400;font-size:32px;text-transform:uppercase;text-align:center;margin:48px 0">Sobre a Bô</h1>'
        + pagina("gerador/img/") + '</body></html>')
open(os.path.join(AQUI, "..", "sobre-a-bo-preview.html"), "w", encoding="utf-8").write(prev)
print("ok", len(final), "caracteres")
