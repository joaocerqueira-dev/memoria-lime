---
name: irroba-painel-mecanica
description: Como o painel Irroba aceita alterações por script (POST, upload, editor, módulos, catálogo, informações) e as armadilhas conhecidas; genérico, sem dados de cliente
metadata:
  type: reference
---

Aprendizados práticos sobre o painel Irroba (`https://<loja>.irroba.com.br/aps`) e o tema Lime, obtidos aplicando propostas em loja de teste. Antes de qualquer escrita, ler [[irroba-painel-seguranca]]; o mapa das telas está em `conhecimento/personalizar-loja.txt` e o schema do tema em `conhecimento/tema-lime.md` ([[tema-lime-conhecimento]]).

**Como o painel aceita alterações**
- Formulários de módulo aceitam POST com o FormData do próprio form (`form[id^=form]`), usando a mesma `action`.
- Upload de imagens: `common/filemanager/upload&directory=<loja>/catalog/<pasta>/`. As imagens ficam no CDN `img.irroba.com.br/<loja>/catalog/...`; a URL `fit-in/1600x1600/filters:format(jpeg):quality(88)/` devolve versões redimensionadas, e sem filtros vem o original.
- O editor visual (aba Tema) só grava ao **Publicar**. Campos ocultos de imagem só valem se escolhidos pelo modal do gerenciador de arquivos (não por valor digitado).
- O classificador do Claude Code pode pedir confirmação explícita antes de Publicar ou de gravar na loja.
- Para ler dados grandes pelo navegador, o resultado do `javascript_tool` é truncado (~1 mil caracteres) e bloqueia URLs com token/cookie: imprimir só nomes ou últimos segmentos, ou injetar um `<article>` fora da tela e usar `get_page_text`.
- Sites hospedados na Irroba podem estar atrás do Cloudflare: o Python (requests) é bloqueado; ler pelo navegador e baixar as imagens direto pelo CDN.

**Módulos (Personalizar Loja)**
- Tipos usados: Banner v2 (grade ou carrossel, desktop e mobile separados), Banner Tarja (benefícios e "Tarja Informativa"), Conteúdo HTML, Lista de produtos, Newsletter, Banner de Vídeo, Depoimentos.
- Tarja de mensagens = módulo `banner_tarja`; o JS do tema a move para antes do `body > header` e ela aparece em vários layouts.
- Banner de Vídeo vem com um iframe `about:blank`; sem URL não mostra nada. Dá para montar capa e legenda por JS.
- Módulos de demonstração da loja de teste devem ser **desativados**, não excluídos.
- Títulos de seção via `title_class` podem sair pequenos e à esquerda da grade; títulos acima de grades de banner funcionam melhor como módulo Conteúdo HTML.

**Aba Código (CSS/JS)**
- O JS é salvo numa linha só: usar apenas comentários `/* */`, nunca `//`.
- Fontes personalizadas podem ir embutidas em base64 no CSS (subset Latin) quando não estão no Google Fonts.
- Quando o cliente proíbe CSS/JS, trabalhar só com Configurações, editor, módulos e cadastros.

**Catálogo e conteúdo**
- Páginas de "Informações" (Catálogo → Informações) aceitam HTML com CSS inline quando liberado: usar flex-wrap e `clamp()`, sem `<style>` nem `<script>`; imagens com URL absoluta do CDN depois do upload.
- Produtos podem ser criados como cópias; variações de cor usam uma opção do tipo Cor com grade e imagem por variação.
- Filtros V2 permitem filtros por atributo (ex.: comprimento) sem mudar a categoria; usar filtro em vez de categoria para atributos como curto/longo.
- Comentários/avaliações: moderação, estrelas nos cards e carrossel 3/2/1 são configuráveis. **Bug conhecido:** o botão de salvar do módulo de depoimentos parece estar dentro do form de exclusão (`setting/review/delete`); uma avaliação de teste sumiu após salvar.
- Categorias novas entram por Catálogo → Categorias; categorias demonstrativas devem ficar inativas, não excluídas.

**How to apply:** use esta lista para planejar uma aplicação na loja de teste, revisar ou desfazer o que foi alterado e para evitar as armadilhas acima.
