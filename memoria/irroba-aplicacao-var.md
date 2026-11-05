---
name: irroba-aplicacao-var
description: O que foi aplicado na loja TESSJBAF para a Var Chocolates (19/10/2026) e como o painel Irroba aceita alterações por script
metadata:
  node_type: memory
  type: project
  originSessionId: f5bb0512-ea21-4f32-a677-5312e8bb34f1
  modified: 2026-10-20T14:37:55.407Z
---

Em 19/10/2026 o design system Var foi aplicado no tema Lime da loja TESSJBAF, com autorização do usuário ("Liberado").

**O que foi feito:**
- Configurações do tema: paleta, tipografia, raio, botões e cabeçalho Layout 3.
- CSS e JS personalizados: `conteudo-mvp/lime-implementacao/var-lime-aplicado.css`, com a Glacial Indifference embutida em base64 (subset Latin), e `var-lime.js`.
- Editor visual: cabeçalho da Home e das demais páginas branco, sticky e expandido; logo (`catalog/var-chocolates/logo-var-chocolates.png`); botão de compra bordô.
- Módulos criados:
  - Banner v2 95 (principal) e 96 (varietais)
  - Banner Tarja 97 (benefícios)
  - HTML 98 (manifesto)
- Listas 85 e 86 renomeadas e newsletter 87 editada.
- Banners demonstrativos 82, 83, 84 e 94 desativados, sem exclusão.
- Página de Informações "Nossa origem" em `/nossa-origem`.
- Imagens na pasta `catalog/var-chocolates`.

**Em 19 e 20/10/2026:**
- **Produtos 10 a 19:** criados como cópias, com dados em `produtos-var.json` e packshots ilustrativos `catalog/var-chocolates/produto-*.jpg`.
- **Demonstrativos:** os produtos 1 a 3 saíram das listas 85 e 86. O 4 e o 5 continuam nelas, porque o classificador bloqueou a alteração.
- **Comentários:** configurados com moderação, estrelas nos cards e carrossel 3/2/1. O módulo de depoimentos 99 está na Home com sort 7.
  - A avaliação de teste "Irroba" sumiu depois do salvamento do módulo. O botão de salvar parece estar dentro do form de exclusão (`setting/review/delete`).
- **Tarja de mensagens:** é o módulo 100 do `banner_tarja` (menu "Tarja Informativa"). O JS a move para antes do `body > header` e ela está em vários layouts.
- **Banner de Vídeo:** módulo 101, sort 7, com um iframe `about:blank`. Enquanto não houver URL, o JS monta a capa (`video-capa.jpg`) e a legenda.
- **Aba Código:** o JS é salvo numa linha só, então não usar comentários `//`, só `/* */`.

**Ficou pendente:**
- URL do vídeo do cliente.
- Fotos reais dos produtos.

**Como o painel aceita alterações:**
- Os formulários de módulo aceitam POST com o FormData do próprio form (`form[id^=form]`, com a mesma action).
- O upload de imagens usa `common/filemanager/upload&directory=tessjbaf/catalog/<pasta>/`.
- O editor visual salva via Publicar, e os campos ocultos de imagem só valem se escolhidos pelo modal do gerenciador.
- O classificador do Claude Code pode pedir confirmação explícita antes de Publicar.

**Why:** registro do que mudou na loja.

**How to apply:** use estas informações para revisar ou desfazer o que foi aplicado. Ver [[cliente-var-chocolates]] e [[irroba-painel-seguranca]].
