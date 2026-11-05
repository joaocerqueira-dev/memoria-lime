# Bell Boots · Configurações para migrar do tema China para o Lime (sem CSS e sem JavaScript)

Referência visual: `bell-boots-lime-proposta-v2.figcraft`.
Base técnica: schema do editor do Lime levantado na loja de teste (`conhecimento/tema-lime.md`). Os nomes dos campos vêm de lá. **Confirme cada campo na loja da Bell Boots ao aplicar**, porque não mexi no painel dela.

Caminho: `Personalizar Loja > Layouts Gratuitos > Tema Lime > Editar tema`. Nada é salvo antes de **Publicar**.

---

## 0. Antes de começar (preparar o material)

| Item | O que fazer |
|---|---|
| Logo | Exportar a logo da Bell Boots em PNG com fundo transparente, versão clara (para o cabeçalho escuro). Gerar também a versão para a interação, se for usar. |
| Artes do hero | 5 artes para desktop (1366×574) e 5 para celular. Podem ser as campanhas atuais, **com o texto e o botão dentro da imagem**. |
| Artes de categoria | 5 imagens (Adventure, Botinas, Casuais, Motociclista, Tênis), com o nome da categoria na própria arte. |
| Artes dos 2 banners | "Modelo Adventure" e "Modelo Casual", desktop e celular. |
| Ícones dos benefícios | 4 imagens PNG ou SVG: frete, cartão, couro, troca. |
| Categoria "Ofertas" | Criar em Catálogo e atribuir os produtos em promoção (o menu do mock tem esse item). |
| Preços promocionais | Conferir se todos os produtos têm preço "de" e "por" cadastrados. O desconto e o preço riscado dependem disso. |

---

## 1. Aba **Configurações** (estilos globais)

| Campo | Valor |
|---|---|
| **Paleta de cores > Personalizada** | Primária: fundo `#F97316` · texto `#1C1917` |
| | Secundária: fundo `#1C1917` · texto `#FFFFFF` |
| | Neutra: fundo `#FDBA74` · texto `#1C1917` |
| | Fundo da página: `#FFFAF5` · texto `#1C1917` |
| | Conferir o selo de contraste AA nos 4 pares (todos devem ficar verdes). |
| **Tipografia > Personalizada** | Títulos: **Oswald**, caixa alta (AG), negrito, tamanho 32px, alinhamento à esquerda |
| | Textos: **Cabin**, 16px |
| **Arredondamento** | Pequeno |
| **Botões** | Botão secundário com contorno: desmarcado (sólido) |
| | Primário: fundo `#F97316`, texto `#1C1917` |
| | Secundário: fundo `#1C1917`, texto `#FFFFFF` |
| **Cabeçalho** | **Layout 2** (logo à esquerda, ícones à direita, categorias numa linha abaixo) |

> O mock usa Bahnschrift e Segoe UI só porque Oswald e Cabin não estão instaladas no FigCraft.

---

## 2. Aba **Tema > Página Inicial** (ordem dos módulos)

Use **Subir / Descer** até chegar nesta ordem:

1. Tarja informativa
2. Banner principal (Banner v2, carrossel)
3. Banner Tarja (benefícios)
4. Banner v2 em grade (categorias)
5. Lista de produtos "Mais vendidos"
6. Banner v2 em grade (2 banners)
7. Lista de produtos "Lançamentos"
8. Newsletter
9. Rodapé (informações, selos e legal)

Para módulos que ainda não estão na página, use o **"+"** e escolha na lista (Inserir). O conteúdo de cada um é cadastrado em `Personalizar Loja` (seção 5 abaixo).

### 2.1 Cabeçalho
| Campo | Valor |
|---|---|
| Posição (`header-position`) | Fixo ao rolar (sticky) |
| Ocultar ao rolar | Desmarcado |
| Expandir (`config_header_filled`) | **Ligado** (barra de ponta a ponta, sem cápsula) |
| Transição de cores (gradiente) | Desligada |
| Fundo (`headerContent-background`) | Secundária (`#1C1917`), opacidade 1 |
| Desfoque (`header-background-blur`) | 0 |
| Botões (`headerContent-btn-background`) | Branco, opacidade 0,1 · ícone (`-btn-foreground`) branco · busca (`search-foreground`) branco |
| Categorias | Texto branco, hover `#F97316`, tamanho 14, caixa alta, negrito, alinhamento ao centro |
| Subcategorias | Fundo `#1C1917`, opacidade 1, texto branco |
| Logo | Subir a logo clara nas 4 posições (Home, Home ao interagir, demais páginas, demais ao interagir). Ajustar largura e altura ao tamanho da logo (padrão 136×42) e, no celular, 90×24 |
| Filtro da logo | Nenhum |

Repita o ajuste de cores para "todas as páginas exceto a Home" (os estilos são separados).

### 2.2 Tarja informativa (`overline`)
| Campo | Valor |
|---|---|
| Fundo | Primária `#F97316`, opacidade 1 |
| Texto | `#1C1917`, 12px, caixa alta, negrito |
| Arredondamento (`overline-radius`) | 0 |

### 2.3 Banner principal (Banner v2)
| Campo | Valor |
|---|---|
| Largura (`bannerModule-width`) | 100% |
| Setas | Fundo `#1C1917` com opacidade 0,6, ícone branco |
| Paginação (`bannerModule-pagination-color`) | `#F97316` |

### 2.4 Banner Tarja (benefícios)
| Campo | Valor |
|---|---|
| Container | Fundo transparente (opacidade 0), desfoque 0 |
| Ícones | Fundo `#FDBA74`, raio 100 (círculo), tamanho 64 |
| Títulos | Texto `#1C1917`, 16px, negrito |
| Descrições | Texto `#78716C`, 14px |

### 2.5 Banners em grade (categorias e 2 banners)
Largura: **Conteúdo (1280px)**. O desenho da grade (5 colunas, 2 colunas) é definido no cadastro do banner (seção 5).

### 2.6 Listas de produtos (Mais vendidos e Lançamentos)
Configure a primeira e use **"Aplicar como estilo padrão"** para a segunda herdar.

| Campo | Valor |
|---|---|
| Largura | 1280px |
| Título | `#1C1917`, 32px, caixa alta, negrito, alinhado à esquerda |
| Link "ver todos" | `#1C1917` |
| Itens: fundo (`productGrid-background`) | `#FFFFFF`, opacidade 1 |
| Nome do produto | `#1C1917`, 16px, negrito |
| Preço | `#1C1917`, 22px, negrito |
| Preço antigo | `#78716C`, riscado |
| Botão Comprar | Fundo `#F97316`, texto `#1C1917` (herda do primário) |
| Estrelas (`rating-icon-color`) | `#F5BF2F` |
| Etiqueta de promoção (`badge-special`) | Fundo `#F97316`, texto `#1C1917`, raio 4 |
| Etiqueta de frete grátis (`shipping-label`) | Fundo `#1C1917`, texto `#FFFFFF` |
| Setas de navegação | Fundo transparente, ícone `#1C1917` |

### 2.7 Newsletter
| Campo | Valor |
|---|---|
| Largura máxima | 1280px |
| Fundo | Primária `#F97316` |
| Arredondamento | 4 |
| Título | `#1C1917`, caixa alta, negrito |
| Descrição | `#1C1917` |
| Campo | Fundo `#FFFFFF`, placeholder `#78716C` |
| Botão | Fundo `#1C1917`, texto `#FFFFFF` |

### 2.8 Rodapé
| Componente | Valor |
|---|---|
| Informações | Largura 1280px, fundo `#1C1917` (o padrão usa a primária) |
| Títulos das colunas | `#F97316`, 14px, caixa alta, negrito |
| Links | `#FFFFFF`, 14px |
| Redes sociais | Fundo do link branco com opacidade 0,05, texto branco |
| Selos | Fundo `#FFFFFF`, cor dos SVGs `#1C1917` |
| Informações legais | Fundo `#1C1917`, texto `#A8A29E`, 12px |

---

## 3. Aba **Tema > Descrição do Produto**

| Campo | Valor |
|---|---|
| Galeria (`config_carousel_orientation`) | **Vertical** (miniaturas ao lado da foto) |
| Título | `#1C1917`, 32px, caixa alta, negrito |
| Preço antigo | `#78716C`, riscado |
| Preço principal | `#1C1917`, negrito, o maior tamanho disponível |
| Desconto | `#F97316`, negrito |
| Avaliações | Estrelas `#F5BF2F` |
| Botão tabela de medidas | Fundo transparente, texto `#F97316`, borda `#F97316` |
| Botão comprar | Texto **COMPRAR**, fundo `#F97316`, texto `#1C1917`, borda `#F97316` |
| Descrição | Títulos "Descrição curta" e "DETALHES DO PRODUTO" com o texto padrão ou ajustado |

---

## 4. O que fica no **cadastro de produtos e catálogo** (sem tocar no tema)

| Item | Como |
|---|---|
| Descrição do produto | Reescrever em texto no editor de descrição (material, solado, palmilha, fechamento), em vez de só imagens grandes. Uma lista simples com marcadores já resolve a "ficha técnica". |
| Preço "de/por" | Preencher o preço promocional em todos os produtos. |
| Frete grátis | A etiqueta já aparece pela regra de frete grátis da loja. |
| Menu | Incluir a categoria **Ofertas**. |

---

## 5. Aba **Personalizar Loja** (conteúdo dos módulos)

| Módulo | Cadastro |
|---|---|
| **Tarja Informativa** | Texto: "Frete grátis para a capital · 9x sem juros · 10% off no Pix e boleto" |
| **Banners > Banner principal** | Carrossel, 5 slides, imagens de desktop e de celular separadas, link de cada um para a categoria, com setas e pontos |
| **Banners > Categorias** | Grade de 5 itens, cada um com a arte e o link da categoria |
| **Banners > Banners duplos** | Grade de 2 itens (Modelo Adventure e Modelo Casual), desktop e celular |
| **Banner Tarja** | 4 itens: ícone + título + descrição. Frete grátis / Até 10x sem juros / Couro legítimo / Troca fácil |
| **Módulos de produtos** | "Mais vendidos" (critério: mais vendidos) e "Lançamentos" (critério: mais recentes). Deixar ativos e inseri-los na página inicial |
| **Newsletter** | Título "Novidades" e texto curto |

---

## 6. O que o mock mostra, mas **não dá para fazer sem CSS/JS**

Ajuste a conversa com o cliente para não prometer o que o editor não entrega:

| No mock | Situação | Alternativa sem código |
|---|---|---|
| Hero com título e botão **editáveis** | O Banner v2 é imagem; título e botão ficam dentro da arte | Usar as artes de campanha atuais, em versões desktop e celular |
| Nome da categoria sobre a foto, nas categorias | Idem: vem da arte | Gravar o nome na imagem |
| Banners duplos com texto e botão | Idem | Idem |
| Selo "-33%" exatamente como no mock | O Lime tem a etiqueta de promoção (`badge-special`); **confirmar no painel se ela mostra o percentual** | Se não mostrar, usar a etiqueta personalizada (`custom-label`) |
| Posição das etiquetas na foto, formato do card | Definido pelo tema | Só cor, texto e raio são editáveis |
| Campo de busca largo no cabeçalho | No Layout 2, a busca é um ícone | Usar o ícone de busca |
| Caixa de benefícios com ícones na página do produto | Não existe campo para isso | Escrever os benefícios na descrição do produto |
| Abas (Descrição / Detalhes / Avaliações) e ficha em tabela | Não há campos para isso | Lista com marcadores na descrição |
| Banner da categoria e texto de SEO **no fim** da página | Não está no schema; **verificar** se o cadastro da categoria tem imagem e onde o texto é exibido | Se não houver, manter o texto no topo, mais curto |
| Filtros por cor e tamanho | Dependem do módulo de filtros e das opções cadastradas nos produtos; **verificar** | Padronizar as opções de cor e tamanho nos produtos |
| Faixas de preço do filtro (R$ 200–250 etc.) | Hoje vêm de uma lista fixa | **Verificar** se a faixa é editável no painel |
| Foto com troca no hover, zoom | Comportamento do tema | Não configurável |

---

## 7. Ordem sugerida de execução

1. Preparar o material (seção 0).
2. Cadastrar o conteúdo dos módulos (seção 5) e ajustar os produtos (seção 4).
3. Em **Configurações**: paleta, tipografia, arredondamento, botões e cabeçalho (seção 1).
4. Em **Tema > Página Inicial**: ordem e estilos (seção 2).
5. Em **Tema > Descrição do Produto** (seção 3).
6. Conferir em Desktop, Tablet e Celular no seletor de dispositivo do editor.
7. **Publicar** e revisar a loja ao vivo (home, um produto e uma categoria).
