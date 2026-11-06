---
name: mocks-lime-aprendizados
description: Método e lições para montar propostas Lime no FigCraft (desktop e mobile), comparar com o site atual do cliente e fechar o material de venda; genérico, sem dados de cliente
metadata:
  type: reference
---

Fluxo que funcionou para propostas de migração para o tema Lime, em mocks gerados por script ([[figcraft-gerador-script]], [[figcraft-integracao]]). Dados do tema em [[tema-lime-conhecimento]].

**Fluxo de uma proposta**
1. Auditar o site atual (tema antigo): header, vitrines, cards, produto, categoria, rodapé; medir CSS real (container, alturas, cores, fontes) pelo navegador.
2. Definir só o que o editor do Lime permite: preset de paleta ajustado à marca (primária com texto de contraste AA), preset de tipografia, arredondamento, botões, layout do cabeçalho 1/2/3. Marcar "via CSS" o que sair do schema (ou evitar, se o cliente proibir CSS/JS).
3. Gerar por script: páginas Proposta (resumo, tokens, antes×depois), Home, Produto, Categoria em desktop (1366) e mobile (390).
4. Montar também um **mock do site atual** com as mesmas dimensões, dados e fotos reais, para comparativo visual lado a lado.
5. Usar fotos e logo reais do cliente (com autorização), baixadas do CDN; remover fundo falso de logo (xadrez) com Pillow por luminância e gerar versões clara e escura.

**Lições de FigCraft**
- `open_file` guarda em cache por caminho: salve com **nome novo** a cada regeração (v1, v2...) e apague as versões antigas.
- Janela minimizada gera timeout "is the window visible?": restaurar via PowerShell (ShowWindow/SetForegroundWindow no processo figcraft).
- Fontes que não estão instaladas caem em outra: usar substitutas parecidas (ex.: Bahnschrift e Segoe UI para Oswald e Cabin; Arial para Roboto) e avisar no material.
- Auto layout: `crossAlign` min|center|max|baseline; `sizing` fill|hug|fixed; `wrap` para grades; `clip` + filhos maiores simulam rolagem horizontal; frames sem layout permitem x/y absolutos (ícones, badges, sobreposições).
- Imagens: `image.place` com mode fill (corta) ou fit; banner de arte larga fica pequeno no mobile: pedir arte mobile própria ao cliente.
- Script grande: separar em módulos e juntar por `exec(open(...).read())` antes do `b.dump` para reaproveitar helpers.

**Mobile (390px)**
- Cabeçalho Lime mobile: tarja, hambúrguer, logo, busca e sacola; categorias entram no menu.
- Padrão: 2 colunas de cards (171px com gap 16), categorias em faixa horizontal, benefícios em grade 2×2, banners duplos empilhados, rodapé em acordeão, barra de compra fixa no produto, botões Filtrar/Ordenar na categoria.
- Para medir o site atual em celular: o `resize_window` do Chrome MCP **não** muda o viewport. Truque: na própria página, trocar o body por `<iframe src="/" style="width:390px">` e medir `contentDocument` (mesma origem); navegar o iframe para produto e categoria.

**Argumentos que funcionam no antes×depois:** botão de compra com cor sem relação com a marca, header muito alto, texto de SEO antes dos produtos, filtros de preço fora da faixa real, descrição só com imagens, ausência de arte mobile, cards sem desconto visível.

**How to apply:** ao receber um novo cliente na migração para o Lime, siga o fluxo, regenere com nome de arquivo novo e deixe pendências de conteúdo (fichas técnicas, fotos, URLs) marcadas como "[preencher]".
