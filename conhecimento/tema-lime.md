# Tema LIME (Irroba) — Base de conhecimento

Levantado em 19/10/2026 na loja de teste **TESSJBAF** (ID 23539), painel `https://tessjbaf.irroba.com.br/aps`.
Fonte: navegação no editor + JSON `#template-editor-bootstrap` embutido na página do editor (schema oficial dos campos).
Complementa `mapeamento/personalizar-loja.txt` (mapa das 6 telas de "Personalizar Loja").

---

## 1. Identidade do tema

| Item | Valor |
|---|---|
| Nome / código comercial | LIME — 940001 (tema mais novo; TERRACOTA 940002 é o irmão da mesma geração) |
| `template_id` / código interno | 80 / `_lime` |
| Classe no `<body>` | `theme-_lime` + `radius-<none\|small\|medium\|large>` + `buttons-solid` (ou outline) |
| Estrutura | "Nova estrutura de template": módulos da Home ficam no mesmo nível, posição fixa "Topo do Conteúdo", só a ordem muda |
| Módulos exclusivos do Lime | Tarja Informativa (Banner Tarja), Banner de Vídeo, Filtro de Gênero |
| Container padrão | 1280px centralizado (margem lateral ~27–43px em 1366px); opção "Largura Total" = 100% |

## 2. Caminho no painel

`Personalizar Loja > Layouts Gratuitos` (rota `design/template`) → bloco **Tema atual** → **Editar tema**.
O editor tem 3 áreas (barra superior, ícones da esquerda):

| Ícone | Nome | Rota | Função |
|---|---|---|---|
| `palette` | **Tema** | `design/template/editor&template_id=80` | Editor visual (pré-visualização + painéis por componente) |
| `code` | **Código** | `design/template/advanced` | CSS Personalizado + JavaScript Personalizado (dois editores lado a lado, aviso "Personalize com cuidado") |
| `tune` | **Configurações** | `design/template/settings` | Estilos globais: paleta, fontes, arredondamento, botões, layout do cabeçalho |
| `reset_wrench` | Restaurar | — | Restaura o tema (destrutivo) |
| botão "LIME" | — | — | Tooltip "Última edição: data por usuário" |

Restante da barra: seletor de página (**Página Inicial** / **Descrição do Produto**), escopo de dispositivo (**Todos** / Desktop / Tablet / Celular), Ajuda (tour "Conheça o editor"), Ver loja, **Publicar** (salva tudo — nada é salvo antes disso).

> ⚠️ Em explorações nunca clicar em **Publicar**, **Restaurar**, **Excluir**, **Aplicar como estilo padrão** nem **Inserir** — alteram a loja.

### Escopo por dispositivo
- **Todos**: estilos gerais; personalizações por dispositivo são mantidas.
- Desktop / Tablet / Celular: alteração só naquele dispositivo. Campos mostram "Usar padrão geral" para voltar ao valor geral.

## 3. Como o editor visual funciona

1. Escolhe a página → clica num componente na pré-visualização (iframe `#storePreview`, que carrega a loja real).
2. Abre um **painel flutuante arrastável** (canto superior esquerdo, ~360px) com título do componente e seções acordeão.
3. Cada componente tem **sub-elementos** clicáveis (título, botões, preços…) com painel próprio.
4. Ao selecionar um **módulo** aparece a barra inferior: **Excluir · Subir · Descer · Ocultar · Editar** (Editar abre a página do módulo no painel).
5. Um botão **"+"** azul no topo do módulo selecionado abre o modal **Adicionar Módulo**, que lista os módulos cadastrados agrupados por tipo (Banner Versão 2, Instagram, Lançamentos, Listas de Produtos, Lembrete Carrinho…) com status Ativo/Inativo e ações Inserir/Inserido/Editar.
6. Rodapé do painel: **"Aplicar como estilo padrão"** — replica o estilo do componente para todos do mesmo tipo.
7. Todas as mudanças são CSS variables (`--nome-do-campo`) aplicadas ao vivo no iframe; campos com `storage: setting` gravam configuração da loja (logos, textos, toggles).

Elementos editáveis no DOM da loja: `[data-component]`, `[data-editable-type]`, `[data-editable-sub-element]`, `[data-selector]`, módulos com `data-module-id` / `data-layout-module-id`.

## 4. Configurações globais (aba Configurações)

### 4.1 Paleta de cores (`color_palette`)
8 tokens semânticos. Ordem dos swatches: primária, texto s/ primária, secundária, texto s/ secundária, neutra, texto s/ neutra, fundo da página, texto da página.

| Preset (`value`) | primary-bg | primary-fg | secondary-bg | secondary-fg | neutral-bg | neutral-fg | body-bg | body-fg |
|---|---|---|---|---|---|---|---|---|
| Padrão (`default`) | #E7D158 | #171716 | #171716 | #FFFFFF | #968D58 | #171716 | #FFFFFF | #171716 |
| Orange (`orange`) | #F97316 | #FFFFFF | #1C1917 | #FFFFFF | #FDBA74 | #1C1917 | #FFFAF5 | #1C1917 |
| Indigo (`indigo`) | #4F46E5 | #FFFFFF | #1E1B4B | #FFFFFF | #A5B4FC | #1E1B4B | #F6F6F6 | #1E1B4B |
| Emerald (`emerald`) ✓ atual | #10B981 | #113137 | #113137 | #FFFFFF | #A7F3D0 | #113137 | #FFFFFF | #113137 |
| Terracotta (`terracotta`) | #C47A5A | #2F1F1A | #2F1F1A | #FFFFFF | #EAD2C7 | #2F1F1A | #FFFFFF | #2F1F1A |
| Sand (`sand`) | #C9A27E | #2B211A | #2B211A | #FFFFFF | #EADCCF | #2B211A | #FFFFFF | #2B211A |
| Personalizada (`custom`) | modal "Personalizar Cores" com os 4 pares fundo/texto e selo de contraste AA (verde ok / vermelho ajustar) |

Tokens CSS: `--primary-background`, `--primary-foreground`, `--secondary-*`, `--neutral-*`, `--body-*`.
Nos campos do schema, `default` costuma referenciar esses tokens (ex.: `default=body-background`).

### 4.2 Tipografia (`typography`)
| Preset | Título (fonte / tam / peso / entrelinha / espaçamento / caixa) | Texto |
|---|---|---|
| Padrão `default` | Poppins 24px 400 normal 0 none | Poppins 14px 400 normal |
| Moderno `modern` | Montserrat 24px 700 1.3 -0.5px | Poppins 16px 400 1.6 |
| Clássico `classic` | Playfair Display 24px 600 1.4 0.5px UPPER | Lora 16px 400 1.8 |
| Minimalista `clean` | Lato 22px 300 1.2 2px UPPER | Roboto 14px 400 1.7 0.2px |
| Impactante `strong` | Oswald 32px 700 1.1 -1px UPPER | Cabin 18px 400 1.5 0.5px |
| Amigável `friendly` | Quicksand 24px 700 1.4 | Fira Sans 16px 400 1.6 |
| Personalizada `custom` ✓ atual | modal "Personalizar Fonte": fonte de títulos e de textos (1.960 Google Fonts), tamanho, caixa (none/AG/ag/Ag), alinhamento (esq/centro/dir), negrito, itálico, sublinhado | |

Atual: títulos **Montserrat 24px**, textos **Poppins 16px**. Tokens: `--title-font-family`, `--title-font-size`, `--title-transform`, `--title-align`, `--text-*`.
Escalas: `font_sizes_title` = 14/16/18/20/22/24/32px; `font_sizes_text` = 12/14/16/18px.

### 4.3 Arredondamento (`theme_fields[border-radius]`)
`none` (Sem arredondamento) · `small` (Pequeno ~4px) · `medium` (Médio ~8px) · `large` (Grande — pílula; atual). Vira classe `radius-*` no body. No `large`, botões/header/newsletter usam 9999px/80px e cards 24px.

### 4.4 Botões
- Checkbox **Botão secundário com contorno (outline)** (`btn-secondary-outline`).
- `btn-primary-background` (#E7D158 atual), `btn-primary-color` (#171716), `btn-secondary-background` (#171716), `btn-secondary-color` (#FFFFFF).
  Obs.: os botões têm cores próprias, independentes da paleta.

### 4.5 Cabeçalho (`theme_fields[header-layout]`)
- **Layout 1** ✓ — logotipo à esquerda e categorias ao centro (ícones à direita).
- **Layout 2** — logotipo à esquerda, ícones à direita, categorias numa linha abaixo.
- **Layout 3** — busca à esquerda, logotipo centralizado, conta/carrinho à direita, categorias abaixo.
  Dica do painel: com muitas categorias, use o menu abaixo do logotipo.

## 5. Anatomia da Página Inicial (estado atual, desktop 1366px)

Ordem dos componentes (y = topo):
1. **header** (0, h88, fixo e sobreposto ao banner) — cápsula `.headerContent` 1280×72, raio 80px, fundo secundária a 60% + `backdrop-filter: blur`, padding 16/24, grid logo | categorias (944px, centralizadas) | 3 botões redondos 40px (busca, conta, carrinho).
2. **banner_v2** (0, 1366×598) — carrossel largura total, imagem 1366×574; paginação em pílula (fundo secundária 30% + blur 32px), bullets 30×8 na cor primária.
3. **productList** "Mais vendidos" (y598, h336, padding 32) — título 24px Montserrat à esquerda + setas de navegação (botões com raio 24, borda neutra 25%, blur) à direita; carrossel de 4 cards de 300px.
   - **Card**: imagem quadrada (wrapper raio 24px, borda neutra 25%), botão compartilhar 32px branco circular no canto superior esquerdo; fundo do card = neutra a 8%; título 14px; preço 18px bold; botão COMPRAR 212×40 pílula (btn-primary).
4. **banner_v2** (desktop / mobile separados: `.hidden-xs` / `.hidden-sm`).
5. **productList** "Lançamentos".
6. **newsletter** (h88) — cápsula 1280px raio 80px fundo primária; título "Novidades" 24px, descrição, campo e botão "Enviar" (secundária, pílula) em linha.
7. **footerInformation** (h240, fundo secundária, padding 40/16) — coluna de redes sociais (pílulas 200×40, branco 5%) + colunas Institucional / Minha Conta / Atendimento (títulos na cor primária, links brancos 16px).
8. **footerSeals** (h156, fundo branco) — Formas de pagamento | Formas de envio | Site Seguro (SVGs na cor do texto).
9. **footerLegal** (h106, 14px, borda superior neutra 25%) — razão social / créditos.

Página **Descrição do Produto**: galeria (orientação do carrossel), título, preço antigo/novo/desconto, economia, avaliações, botão tabela de medidas, botão comprar (texto editável), títulos das descrições.

## 6. Schema dos componentes (campos editáveis)

Notação: `campo [tipo] padrão faixa`. **TXT(prefixo)** = pacote tipográfico padrão:
`-foreground [color]`, `-font-size [select]`, `-text-decoration [none|underline]`, `-text-transform [none|uppercase|lowercase|capitalize]`, `-font-weight [bold]`, `-font-style [italic]` (às vezes `-text-align`).
Flags: **M** movível · **D** excluível · **R** replicável (vários na página).

### header — Cabeçalho (`header`)
- Layout: `header-position` relative(Padrão)/sticky(Fixo ao rolar)/**fixed**(Fixo na tela, sobrepõe); `header-hide-on-scroll` 0/1; `config_header_filled` (Expandir: tira margem e raio, compartilhado Home/demais); `config_header_gradient_enabled` (transição de cores, vale p/ toda a loja).
- Aparência: `headerContent-background` (secundária) e `-before-background` OU gradiente `-gradient-start` (neutra) → `-gradient-end` (primária); `headerContent-background-opacity` 0–1 (0.7); `header-background-blur` 0–100px (10).
- Interação (hover/rolagem): `headerContent-background-hover` + opacidade (0.6).
- **buttons**: `headerContent-btn-background` (body, 0.1), `-btn-foreground` (primária), `search-foreground`; versões `-hover`.
- **mobileIcons** (só mobile): fundo/ícone e versões ao tocar (#FDF7EF).
- **categories**: `categoryLink-foreground`, `-foreground-hover`, `-background`, `-font-size`, decoração, caixa, `categoryLink-align` (flex-start/center/flex-end).
- **subcategories**: fundo + opacidade, `subcategory-background-blur`, TXT, alinhamento.
- **logo**: `logo-filter` (none / alto contraste `grayscale(100%) invert(1)` na interação); 4 imagens: logo Home, logo Home ao interagir, logo demais páginas, logo demais ao interagir; largura/altura desktop (atual 136×42; máx 400×100) e mobile (90×24).
- Estilos de cabeçalho são separados: "somente na Home" × "todas as páginas exceto a Home".

### banner_v2 — Banner (`.bannerModule`) M D R
`bannerModule-width` 1280px | 100%. Sub: setas (`-nav-background` c/ opacidade, `-nav-foreground`, `-nav-border`), paginação (`bannerModule-pagination-color`).

### productList — Lista de Produtos (`.productList`) M D R
- `productList-width` 1280px|100%, `productList-background` (+opac).
- title: TXT(`productList-title`) + `-text-align`, padrão 20px.
- link "ver todos": `productList-link-foreground`.
- navigation: `nav-background`, `nav-foreground`, `nav-border`.
- items: `productGrid-background` (neutra, opac 0.08), `-foreground`, `-base-font-size`, `-rating-icon-color` (#f5bf2f).
- item_titles: cor + tamanho. prices: preço (cor, tamanho, bold/itálico) + preço antigo (cor, tamanho, decoração line-through).
- buyButton: `productList-buy-btn-background` / `-foreground` (herdam btn-primary).
- pagination: `swiper-pagination-color`. review: cor + `productGrid-review-icon-size` 12–32px.
- badge-special (Promoção): fundo (+opac), texto, borda, tamanho, `-radius` 0–80 (8).
- custom-label (etiqueta personalizada, grava na etiqueta): texto, cor de fundo, cor do texto, fonte 10–20px, raio 0–50px.
- shipping-label (frete grátis): fundo, texto, borda.

### overline — Tarja informativa (`.overlineModule > .container`) M D (única)
`overline-background` (primária, opac 1), `overline-foreground`, `overline-radius` 0–80 (80); TXT(`overline`) 14px.

### bannerTarja — Banner Tarja (`.bannerTarjaModule`) M D R
- Container: `bannerTarjaModule-background` (+opac), `-background-blur` 0–100 (20); `bannerTarja-width`.
- items (M D): fundo (+opac), `-item-radius` 0–100 (8), `-item-size` 100–500px.
- icons: fundo, raio 0–100, tamanho 64–180px.
- titles: TXT; descriptions: TXT + alinhamento left/center/right/justify.

### bannerVideo — Banner de Vídeo (`.bannerVideoModule`) M D R
`bannerVideo-width` 1280px(Conteúdo) | **100%**.

### htmlContent — Conteúdo HTML (`.htmlContent`) M D R
`htmlContent-max-width` 1280px | 100%.

### review — Avaliações (`.reviewModule`) M D
Largura; setas; paginação.

### newsletter — Newsletter (`.newsletterModule`) M D (única)
`newsletter-max-width`, `newsletter-background` (+opac), `newsletter-radius` 0–80 (24). Sub: título TXT, descrição TXT, campos (fundo, texto, placeholder), botão (fundo, texto, borda).

### filter_gender — Filtro de Gênero (`.filterGender`) M D R
Largura, fundo (+opac), raio 0–80; título TXT. Cada gênero (`filter_gender_male` `.gender--male`, `_female`, `_boy`, `_girl`) tem: fundo + raio, título TXT + alinhamento, legenda TXT + alinhamento, botões de numeração (fundo, texto, borda, raio).

### footerInformation — Informações do rodapé (`.footerContent--top`)
`footerInformation-width`, `footer-background` (primária, opac 1); exibir contatos / telefone / WhatsApp / e-mail. Sub: títulos TXT (primária, 16px), links TXT (secundária-fg, 14px), redes sociais (cor do ícone, fundo do link, texto TXT).

### footerSeals — Selos do rodapé (`.footerContent--bottom`)
Largura, fundo; títulos dos selos TXT; `footerSeals-seals-foreground` (cor dos SVGs).

### footerLegal — Informações legais (`.footer-legal-info`)
Fundo, texto, tamanho (12px).

### pageProduct — Página do produto (`.product-content`, não editável no todo)
- gallery: `config_carousel_orientation` (vertical 1 / horizontal 0).
- title: TXT(`pageProduct-title`). priceOld / priceMain / priceDiscount / product_spare: TXT.
- productDescription: textos "Descrição curta" e "DETALHES DO PRODUTO".
- review: cor. btnSizeGuide: fundo, texto, borda.
- btnBuy: texto (padrão "COMPRAR") + fundo, texto, borda.

## 7. Módulos (conteúdo) × editor (estilo)
O **conteúdo** (imagens, textos, itens, vídeo) é cadastrado em `Personalizar Loja > Banners / Tarja Informativa / Banner de Vídeo / Módulos`; o editor do tema só ajusta **estilo, ordem, visibilidade e inclusão** na página. Cada painel tem atalho "Editar" que leva ao cadastro do módulo.
- Banner v2: Grade (grid desenhado) ou Carrossel (Desktop e Mobile separados, setas, dots, efeito Fade, itens por tela).
- Tarja: largura/altura das imagens, layout Horizontal/Vertical/Apenas imagem, itens visíveis por dispositivo, autoplay, loop, setas, pontos; itens = título + descrição + link + imagem.
- Banner de Vídeo: URL (YouTube/Vimeo) ou iframe, separado Desktop/Mobile, link de redirecionamento.

## 8. Tradução para o FigCraft (MVP de personalizações)

Estratégia para montar mockups apresentáveis aos clientes:
1. **Variáveis** no FigCraft = os 8 tokens de paleta (uma *mode* por preset: Padrão, Orange, Indigo, Emerald, Terracotta, Sand) + tokens de botão + raio (none 0 / small 4 / medium 8 / large 9999).
2. **Estilos de texto** = presets de tipografia (Título/Texto × 6 presets).
3. **Componentes** espelhando o schema, com variantes:
   - Header (Layout 1/2/3 × sólido/gradiente × expandido/cápsula).
   - Banner v2 (largura total/1280), Tarja informativa, Banner Tarja (itens), Banner de vídeo.
   - Card de produto (com/sem promoção, etiqueta, frete grátis) + Lista de produtos (carrossel 4 colunas).
   - Newsletter, Rodapé (informações, selos, legal), Filtro de gênero.
4. **Frames de página**: Home Desktop 1366 (ou 1440) e Mobile 390, montados com auto layout na ordem real da seção 5.
5. Cada personalização proposta ao cliente deve usar **somente opções que o editor oferece** (seções 4 e 6) — ou marcar como "via CSS personalizado" (aba Código) quando extrapolar.
