---
name: figcraft-gerador-script
description: Como gerar arquivos grandes no FigCraft via `figcraft-cli run` (ids previsíveis) em vez de chamadas MCP uma a uma
metadata:
  type: reference
---

Para montar designs grandes, gere um JSON de comandos e rode `figcraft/target/release/figcraft-cli.exe run script.json --out arquivo.figcraft` (sem interface). Depois abra o resultado com `open_file`.

Regras aprendidas:
- Os ids são sequenciais e começam em 2. `page.add` e `image.place` consomem 1 id cada; `component.combineVariants` consome 1 (o set). Uma instância consome 1 + o número de descendentes do componente, em pré-ordem.
- Termine o componente antes de criar instâncias dele: adicionar filhos depois propaga cópias e consome ids.
- `style.apply` sobrescreve propriedades de texto (caixa, sublinhado). Aplique o estilo primeiro e os overrides depois.
- Não é possível mudar o tamanho de camadas dentro de instâncias. Crie uma variante própria (ex.: card mobile).
- Outros valores: `scrollPosition` aceita sticky ou fixed; `overflow` aceita horizontal; em overlays use `position` topRight ou center; o gatilho de tempo é `{type: afterDelay, ms}`.
- Se o MCP der timeout com "is the window visible?", a janela do FigCraft está minimizada: restaure-a.

Base do gerador: `geradores/figcraft/fc.py` (classe `B`) e `runcheck.py`. Ver [[figcraft-integracao]] e [[mocks-lime-aprendizados]].
