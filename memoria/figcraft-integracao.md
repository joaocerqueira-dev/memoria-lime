---
name: figcraft-integracao
description: "Como o MCP do FigCraft está ligado neste projeto (servidor figcraft-app, porta 7979) e o que fazer quando não aparece"
metadata:
  node_type: memory
  type: project
  originSessionId: f5bb0512-ea21-4f32-a677-5312e8bb34f1
  modified: 2026-10-21T14:10:39.900Z
---

O FigCraft é um app de design local (estilo Figma) em `Lime\figcraft\`. O MCP `figcraft-app` está em `Lime\.mcp.json` e roda `figcraft-cli.exe mcp --attach 7979`, conectando-se ao app aberto na porta 7979.

- Já esteve desativado por `disabledMcpjsonServers` em `.claude/settings.local.json`; agora ele usa `enabledMcpjsonServers: ["figcraft-app"]`.
- O `/mcp reconnect` não carrega servidores que estavam desativados quando a sessão começou; nesse caso é preciso reiniciar com `claude --continue`.
- O app FigCraft precisa estar aberto, senão o attach falha.
- Abra o app com a porta de controle: `figcraft\target\release\figcraft.exe --control 7979` (ou a variável `FIGCRAFT_CONTROL_PORT`). Aberto sem esse argumento, a janela aparece, mas a porta fica fechada.

**Why:** a integração demorou para funcionar por esses motivos (out/2026).
**How to apply:** se as ferramentas `mcp__figcraft-app__*` não aparecerem, verifique as configurações, a porta 7979 e se o processo `figcraft.exe` está rodando. Relacionado: [[tema-lime-conhecimento]].

Obs. (nov/2026): com `--control 7979` já aberto, `/mcp` reconecta. O MCP dá timeout "is the window visible?" se a janela estiver minimizada; e `open_file` do mesmo caminho devolve o arquivo em cache, então salve com nome novo.
