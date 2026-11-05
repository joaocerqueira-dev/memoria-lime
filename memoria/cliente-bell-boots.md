---
name: cliente-bell-boots
description: "Bell Boots (bellboots.com.br, tema China → Lime): auditoria do site atual e mock no FigCraft gerado por script; pendências (fotos reais, logo)"
metadata:
  node_type: memory
  type: project
  originSessionId: ef163070-5617-4869-a740-93eaa819d764
  modified: 2026-11-05T14:43:31.394Z
---

Loja de calçados em couro (Franca-SP) na Irroba, hoje no tema antigo **China**. Proposta de migração para o **Lime** montada em 05/11/2026.

- Arquivo: `conteudo-mvp\bell-boots\bell-boots-lime-proposta-v10.figcraft (a versão muda a cada regeração, por causa do cache)` (7 páginas: 00 Proposta, 01-03 desktop 1366, 04-06 mobile 390: Home, Produto, Categoria; mobile vem de mobile_lime.py, executado por build.py). Gerador: `conteudo-mvp\bell-boots\build.py` (usa `fc.py` do gerador do Var) + `runcheck.py`.
- Decisões: preset Orange ajustado (primária #F97316 com texto #1C1917, secundária #1C1917, neutra #FDBA74, fundo #FFFAF5), cabeçalho Layout 2, arredondamento Pequeno (4px), tipografia Impactante. No mock as fontes são Bahnschrift (títulos) e Segoe UI (texto), porque Oswald/Cabin não estão instaladas.
- Problemas do site atual usados no argumento: botão de compra verde #5BB85A, azul #0D92CA do tema sem relação com a marca, header de 155px com ícones de bota, SEO antes dos produtos, filtros de preço fora da faixa real (R$ 199–330), descrição só com imagens.
- Fotos reais do cliente (autorizadas pelo usuário em 05/11/2026) baixadas do CDN img.irroba.com.br para `conteudo-mvp/bell-boots/img-cliente/` (produtos 1200px, 4 banners, logo): o mock usa as imagens do hero, banners duplos, cards, categorias, galeria e logo. Logo nova enviada pelo usuário (`conteudo-mvp/bell-boots/logo-nova.png`, preta com xadrez falso de fundo): fundo removido com Pillow (alfa por luminância) e salva em `img-cliente/logo-nova-preta.png` e `logo-nova-branca.png` (a branca vai no cabeçalho escuro; para o Lime, subir a versão certa em cada posição da logo). O arquivo v10 é o atual. Banners novos do usuário (banner-1.png, banner-2.png, banne-3.png [sic], 2048×768) copiados para img-cliente/slide-1..3.png: slide 1 é o hero da Home (sem carrossel); slides 2 e 3 substituem os banners duplos da Home. Os banners 2 e 3 têm barras pretas em cima e embaixo na própria arte.
- Pendências: ficha técnica com "[preencher]", comparativo em artifact.

- Mock do site ATUAL (tema China) para comparar: `conteudo-mvpell-bootsell-boots-site-atual-v3.figcraft` (6 páginas: Home, Produto 4800 Oliva, Categoria Tênis em desktop + as 3 em mobile 390 via mobile_atual.py, medido no site real com iframe de 390px; truque: o resize_window do Chrome MCP não muda o viewport); gerado por `build_atual.py`, imagens em `img-atual/`, fonte Arial no lugar de Roboto). Dados lidos do site em 05/11/2026 (28 cards na Home: Lançamentos 8 + Promoção 20).

**Why:** material de venda para convencer o lojista a migrar.
**How to apply:** ao retomar, regenere com `python build.py bb.json && python runcheck.py bb.json <novo-nome>.figcraft` e abra com `open_file`. O app guarda em cache o arquivo de mesmo caminho, então use um nome novo a cada regeração. Se o MCP der timeout, restaure a janela do FigCraft. Ver [[figcraft-gerador-script]], [[figcraft-integracao]] e [[tema-lime-conhecimento]].
