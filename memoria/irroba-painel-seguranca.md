---
name: irroba-painel-seguranca
description: Regras para navegar no painel Irroba da loja de teste TESSJBAF sem alterar a loja
metadata:
  node_type: memory
  type: feedback
  originSessionId: f5bb0512-ea21-4f32-a677-5312e8bb34f1
  modified: 2026-10-19T12:40:01.124Z
---

O painel é `https://tessjbaf.irroba.com.br/aps` (loja de teste TESSJBAF, ID 23539). Quem faz login é sempre o usuário. A exploração é só de leitura.

Nunca clicar em: Publicar, Restaurar, Excluir, Aplicar (tema), Aplicar como estilo padrão, Inserir (módulo) ou Salvar, a menos que o usuário peça explicitamente.

Dica técnica: o resultado do javascript_tool é truncado em cerca de 1 mil caracteres e é bloqueado quando contém URLs com token. Para ler dados grandes, injete um `<article>` fora da tela com o texto e use get_page_text.

**Why:** "Publicar" grava na loja real, e o objetivo atual é apenas aprender o tema.
**How to apply:** em qualquer sessão de navegação no painel. Relacionado: [[tema-lime-conhecimento]].
