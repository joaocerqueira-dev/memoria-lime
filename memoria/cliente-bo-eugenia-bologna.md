---
name: cliente-bo-eugenia-bologna
description: "Cliente Bô · Eugenia Bologna (kimonos, panôs, acessórios) — proposta de tema Lime só low-code no FigCraft (21/10/2026)"
metadata:
  node_type: memory
  type: project
  originSessionId: f5bb0512-ea21-4f32-a677-5312e8bb34f1
  modified: 2026-10-22T18:00:52.429Z
---

Em 21/10/2026 montei a proposta de tema Lime para a Bô (Setup 16899).
- **Briefing:** pasta do Google Drive "Setup - 16899", compartilhada pela Irroba. Tem o `Briefing Setup.docx`, fotos e o logo em PDF. O texto do briefing sai pela URL `/mobilebasic` do Docs.
- **Restrição do usuário:** sem CSS e sem JS (nada da aba Código), só configurações do tema, editor, módulos e cadastros.
- **Pedidos da cliente:**
  - Site com cara de "galeria de arte".
  - Uma única lista na Home, chamada "Em Cena".
  - Categorias: Kimonos, Panôs e Acessórios. Curto e longo são filtro, não categoria.
  - Panôs com 4 variantes de cor: Solar, Etérea, Telúrica e Magnética, com o texto "Sobre as cores".
  - Proibido falar em "coleções" por estação.
  - Cores: #026526, #E7760A, branco e preto.
  - Instagram: @boeugeniabologna.
- **Arquivos:** ficam em `conteudo-mvp/bo-eugenia-bologna/`.
  - `fotos/` e `fontes/`, com Cormorant Garamond e Jost instaladas no usuário.
  - O gerador `gerador/build_bo.py` usa `fc.py` com família por estilo e gera `Bo-Eugenia-Bologna-Tema-Lime.figcraft`.
- **Pendências de conteúdo:**
  - Fotos dos panôs e dos braceletes.
  - Fotos de produto em 3:4.
  - Preços e nomes oficiais.
  - Cor do logo: no PDF de impressão aparecem #18452B e #CA5C24, diferentes do briefing.

**Sobre a Bô (21/10):** o usuário liberou HTML com CSS inline no texto informativo, em Catálogo → Informações.
- `sobre-a-bo.html` é gerado por `gerador/sobre_html.py`: flex-wrap, clamp() e nenhum `<style>`/`<script>`.
- As imagens apontam para `URL-DA-PASTA-DE-IMAGENS/`, que precisa ser trocada depois do upload.
- `sobre-a-bo-preview.html` serve para conferir localmente.
- Os títulos acima das grades de banner viram módulo Conteúdo HTML.
- As 7 fotos de reserva agora estão na Home: banner 4, o díptico "Em movimento" e o tríptico da galeria.

**Loja atual** (boeugeniabologna.com.br, já na Irroba com o tema Lime):
- **Kimonos:** subcategorias Essenciais, Assinatura e Raros. Os modelos se chamam Yu, Yin-Yang e Yang. Os packshots são em fundo branco.
- **Panôs:** 13 produtos separados por estação (variante Verão/Primavera/Outono/Inverno). Pela subcategoria: Primavera=Solar, Verão=Etérea, Outono=Telúrica, Inverno=Magnética.
  - Estampas: Voar, Voar Linha Terracota, SunSet/MoonSet e Constelação (collab).
  - Ficha: 100% viscose, 2 m × 1,40 m.
- **Acessórios:** categoria vazia.
- **Valores:** autenticidade, criatividade e autoamor.
- **Arquivos:** imagens baixadas em `loja-atual/`.
- **Coleta:** o servidor bloqueia o Python (Cloudflare). Pelo navegador, o envio para o localhost fica preso no pedido de rede local do Chrome. Funcionou ler no navegador e baixar as fotos pelo CDN `img.irroba.com.br/fit-in/1600x1600/filters:format(jpeg):quality(88)/boeugeni/catalog/<arquivo>`.

**Aplicação na TESSJBAF (21/10/2026), por pedido do usuário. A Var foi desativada sem exclusão.**
- **Backup:** em `bo-eugenia-bologna/backup/`, com `var-*.html`, o CSS e JS da Var e `var-css-variables.json`.
- **Categorias:** Kimonos 122 (Essenciais 125, Assinatura 126, Raros 127), Panôs 123 e Acessórios 124. As demonstrativas 116 a 120 ficaram inativas.
- **Opção Cor:** id 54.
- **Produtos:** kimonos 20 a 28 e panôs 29 (Voar) e 30 (Voar Linha Terracota), estes com grade Cor e imagem por variação. Os produtos 10 a 19 da Var continuam intactos.
- **Filtro:** "Comprimento" em Filtros V2.
- **Módulos da Bô:** banners 102 a 108, lista Em Cena 109, tarja 110 e newsletter 87 renomeada.
- **Módulos da Var desativados:** 95, 96, 98, 85, 86, 97, 100 e 101.
- **Páginas:** "Sobre a Bô" (HTML inline) criada; "Nossa origem" ficou inativa.
- **Código do tema:** a aba Código está vazia.
- **Imagens:** em `catalog/bo-eugenia/`.
- **Pendências:**
  - Os títulos via `title_class` aparecem pequenos à esquerda da grade.
  - Falta o título de Em Cena.
  - O review 99 continua ativo.
  - A tipografia personalizada não carrega o Google Fonts na loja; o link continua com Montserrat e Poppins.

**22/10/2026:** o usuário pediu para trocar o banner v2 108 (chamada Sobre) por um módulo Conteúdo HTML. O arquivo é `sobre-home.html`, gerado por `gerador/sobre_home_html.py` (fundo creme #F6F3EE, foto wa35 à esquerda, título, valores e os botões "Conheça a Bô" e Instagram; prévias `sobre-home-preview*.html`). Plano: criar o módulo HTML na Home (content_top, sort 8) e desativar o 108, sem excluir. O usuário criou o módulo (htmlContent-117). O Lime coloca o Conteúdo HTML dentro de `.container` com max-width 1280px; para ocupar a largura toda, use inline no div externo `position:relative;left:50%;width:100vw;max-width:100vw;margin-left:-50vw`. O body tem overflow-x hidden, então não aparece rolagem lateral.
- **Panôs (22/10):** `panos-home.html` (gerado por `gerador/panos_home_html.py`) substitui o banner 106. As 4 atmosferas são painéis `position:sticky; top:0` que se empilham ao rolar. Eles ficam por baixo do header sticky do Lime (z-index 1000, 112px com a tarja, igual no celular), com padding-top de 112px. A imagem vem antes do texto para cada painel caber numa tela do celular. Testar no celular com um iframe de 390px da própria loja, injetando o HTML; o Chrome headless não serve para largura de celular.
- O usuário aplicou o panôs como htmlContent-118 e reordenou a Home. O banner 105 passou a usar as artes `banner-cat-{kimono,panos,acessorios}-desktop.webp` (464×825, com o nome gravado no rodapé).
- **Categorias (22/10):** `categorias-home.html` (gerado por `gerador/categorias_home_html.py`) substitui o 105. Sem `<style>`, as animações são SVG SMIL inline:
  - fusão de fotos com `<animate opacity>` e zoom lento animando o viewBox;
  - selo de texto girando em Acessórios (textPath + animateTransform rotate);
  - faixa de texto correndo, com 3 cópias de textLength 1200 e espaços ` `.
  - As artes banner-cat entram com altura de 1000 e alinhadas pelo topo (xMidYMin slice), para esconder o nome gravado.
  - No celular, o trilho vira carrossel com scroll-snap.
  - Risco: o editor do módulo pode remover `<svg>`.

**Técnicas no painel:**
- Publicar o editor: POST em `design/template/editStyles` com `css_variables` (JSON de `{name, value, context, breakpoint}`), `theme_settings`, campos diretos (`config_logo_*`), `template_id=80` e `template=_lime`.
- Configurações: POST em `design/template/settings_save`.
- Upload: só funciona feito a partir de `catalog/category`. A pasta é criada com `$.ajax` usando `{folder}` e directory `encodeURIComponent('tessjbaf/catalog/')`.
- A edição de tarja e de vídeo fica em `module/<x>/edit`.
- O atalho de status das listagens exige uma permissão que este usuário não tem.

Técnica de FigCraft aprendida: `file.open` de um arquivo já aberto não o recarrega; é preciso reabrir o app com o arquivo. para trocar a foto numa instância, use `node.set fills=[{"type":"image","image":<sha256 do arquivo>,"scale_mode":"fill"}]`. A imagem precisa já ter sido colocada no documento com `image.place`. Se a janela não responde ao controle, reabra o app com o arquivo como argumento.

**Why:** registro do trabalho para continuar a proposta e a futura implementação.
**How to apply:** antes de aplicar na Irroba, confirme no painel as opções com miniatura de imagem, o recorte do card e a posição da tarja. Ver [[tema-lime-conhecimento]] e [[figcraft-gerador-script]].
