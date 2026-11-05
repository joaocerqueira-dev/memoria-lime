import json, subprocess, sys
script = sys.argv[1]; out = sys.argv[2]
exp = dict(json.load(open(script + ".expect")))
p = subprocess.run(["C:/Users/joaoc/OneDrive/Desktop/Lime/figcraft/target/release/figcraft-cli.exe", "run", script, "--out", out],
                   capture_output=True, text=True, encoding="utf-8")
cmds = json.load(open(script, encoding="utf-8"))
bad = 0
n = 0
for line in p.stdout.splitlines():
    if not line.startswith("{"):
        print(line); continue
    r = json.loads(line)
    n += 1
    st = r["step"]
    if not r["ok"]:
        print("FALHOU passo", st, cmds[st]["command"], json.dumps(cmds[st]["params"], ensure_ascii=False)[:500])
        print("  erro:", r.get("error"))
        bad += 1
        break
    if st in exp:
        got = r["result"].get("id")
        if got != exp[st]:
            print("ID divergente no passo", st, cmds[st]["command"], "esperado", exp[st], "obtido", got,
                  json.dumps(cmds[st]["params"], ensure_ascii=False)[:300])
            bad += 1
            break
print(p.stderr[-1500:])
print("passos:", n, "ok" if not bad else "erro")
