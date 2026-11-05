---
name: cliente-var-chocolates
description: "Primeiro cliente do MVP — Var Chocolates (chocolate varietal, bordô #6D071A); proposta de layout Lime em conteudo-mvp"
metadata:
  node_type: memory
  type: project
  originSessionId: f5bb0512-ea21-4f32-a677-5312e8bb34f1
  modified: 2026-10-19T15:14:54.767Z
---

Cliente do MVP: **Var Chocolates**, com BrandBook em `Lime\conteudo-mvp\BRAND BOOk Var (1).pdf`. Referências escolhidas pelo cliente: luzzcacau.com.br e dengo.com.br.
A proposta de layout no Lime está em `Lime\conteudo-mvp\proposta-var-chocolates-lime.md` (19/10/2026). Aprovada e montada em 19/10/2026: design system completo em `conteudo-mvp\Var-Chocolates-Design-System.figcraft` (7 páginas: capa, fundamentos, componentes, animações, telas desktop/mobile, implementação Lime). CSS/JS/fontes woff2 em `conteudo-mvp\lime-implementacao`; o gerador Python fica em `lime-implementacao\gerador` (rode `python build.py ds.json` e depois `python runcheck.py ds.json saida.figcraft` dentro da pasta).

Decisões da proposta:
- Paleta personalizada: primária bordô #6D071A, secundária preto, neutra Uva #900C3A, fundo branco.
- Raio 0, cabeçalho Layout 3, botões bordô e outline preto.
- Fonte única: Glacial Indifference (Bold nos títulos em caixa alta, Regular nos textos, Italic nos destaques), carregada via @font-face na aba Código, porque não está no Google Fonts.

O PDF é renderizado com PyMuPDF (`pip install pymupdf`), já que o poppler não está instalado.

**Why:** o MVP de personalizações começa por este cliente.
**Regra do usuário (19/10/2026):** cores e fonte devem seguir estritamente o BrandBook. Usar só os 7 hex sólidos (Azul #16346C, Uva #900C3A, Bordô #6D071A, Purple #5B2270, Beer #D3723D, preto, branco), sem tons, transparências, creme ou fontes substitutas.

**How to apply:** ao montar no FigCraft, siga a proposta e o [[tema-lime-conhecimento]]. O BrandBook exige aval dos guardiões (Carolina ou Pedro Magalhães) para qualquer desvio.
