---
name: tema-lime-conhecimento
description: "Base de conhecimento do tema LIME da Irroba (editor, paletas, tipografia, schema de componentes, anatomia da Home) — ler antes de criar personalizações"
metadata:
  node_type: memory
  type: project
  originSessionId: f5bb0512-ea21-4f32-a677-5312e8bb34f1
  modified: 2026-10-19T12:39:52.002Z
---

O conhecimento completo do tema LIME (Irroba, código 940001, template_id 80, `_lime`) está em
`conhecimento/tema-lime.md` neste repositório (levantado em 19/10/2026). Mapa das telas de "Personalizar Loja" em `conhecimento/personalizar-loja.txt`.

Resumo essencial:
- Editor = 3 abas: Tema (editor visual com painéis por componente), Código (CSS/JS), Configurações (paleta, fontes, arredondamento, botões, layout do cabeçalho 1/2/3).
- 8 tokens de cor semânticos (primary/secondary/neutral/body × background/foreground) + 6 presets de paleta (Padrão, Orange, Indigo, Emerald, Terracotta, Sand) + personalizada.
- 6 presets de tipografia (Padrão, Moderno, Clássico, Minimalista, Impactante, Amigável) + personalizada (Google Fonts).
- O schema oficial dos campos fica no JSON `script#template-editor-bootstrap` da página do editor; dá para reextraí-lo com JS caso o tema mude.
- O conteúdo (imagens/textos) vem dos módulos em Personalizar Loja; o editor só cuida de estilo, ordem e visibilidade.

**Why:** o objetivo é criar no FigCraft um MVP de personalizações do Lime para apresentar a clientes, e ele deve respeitar apenas o que o editor realmente permite.
**How to apply:** antes de propor ou desenhar uma personalização, consulte o arquivo; use os tokens e os nomes de campo dele; marque como "via CSS personalizado" o que estiver fora do schema. Ver [[figcraft-integracao]] e [[irroba-painel-seguranca]].
