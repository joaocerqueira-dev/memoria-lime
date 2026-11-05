# Construtor de scripts para `figcraft-cli run` com previsão de ids.
import json

FONT = "Glacial Indifference"


class B:
    def __init__(self):
        self.cmds = []
        self.nid = 2            # página 1 já existe
        self.children = {1: []}
        self.names = {1: "Page 1"}
        self.page = 1
        self.var_n = 0
        self.col_n = 0
        self.style_n = 0
        self.vars = {}          # nome -> id
        self.styles = {}        # chave -> id
        self.textstyles = {}    # chave -> props

    # ---- infraestrutura ----------------------------------------------------
    def c(self, command, **params):
        self.cmds.append({"command": command, "params": params})

    def _reg(self, nid, parent, name):
        self.children.setdefault(nid, [])
        self.names[nid] = name
        p = parent if parent is not None else self.page
        self.children.setdefault(p, []).append(nid)

    def preorder(self, nid):
        out = [nid]
        for ch in self.children.get(nid, []):
            out += self.preorder(ch)
        return out

    def new_page(self, name):
        pid = self.nid
        self.nid += 1
        self.c("page.add", name=name)
        self.children[pid] = []
        self.names[pid] = name
        self.select_page(pid)
        return pid

    def select_page(self, pid):
        self.page = pid
        self.c("page.select", id=pid)

    # ---- camadas -----------------------------------------------------------
    def node(self, type, parent=None, name=None, x=0, y=0, w=None, h=None, text=None, path=None, **props):
        nid = self.nid
        self.nid += 1
        p = {"type": type, "x": x, "y": y, "select": False}
        if parent is not None:
            p["parent"] = parent
        if name:
            p["name"] = name
        if w is not None:
            p["width"] = w
        if h is not None:
            p["height"] = h
        if text is not None:
            p["text"] = text
        if path is not None:
            p["path"] = path
        if props:
            p["props"] = props
        self.cmds.append({"command": "node.create", "params": p, "expect": nid})
        self._reg(nid, parent, name or type)
        return nid

    def frame(self, parent=None, name="Frame", w=100, h=100, layout=None, gap=0, pad=0,
              fill=None, stroke=None, sw=1, sh=None, sv=None, main=None, cross=None,
              wrap=None, clip=None, x=0, y=0, comp=False, fills=None, **extra):
        props = {}
        props["fills"] = [fill] if fill else (fills or [])
        if stroke:
            props["stroke"] = stroke
            props["strokeWeight"] = sw
        if layout:
            props["layout"] = layout
            props["gap"] = gap
            props["padding"] = pad
            if main:
                props["mainAlign"] = main
            if cross:
                props["crossAlign"] = cross
            if wrap:
                props["wrap"] = True
        if clip is not None:
            props["clip"] = clip
        props.update(extra)
        nid = self.node("component" if comp else "frame", parent, name, x, y, w, h, **props)
        sz = {}
        if sh:
            sz["sizingH"] = sh
        if sv:
            sz["sizingV"] = sv
        if sz:
            self.set(nid, **sz)
        return nid

    def set(self, ids, **props):
        if not isinstance(ids, list):
            ids = [ids]
        self.c("node.set", ids=ids, **props)

    def rect(self, parent, w, h, fill=None, name="Retângulo", stroke=None, sw=1, **kw):
        props = {"fills": [fill] if fill else []}
        if stroke:
            props["stroke"] = stroke
            props["strokeWeight"] = sw
        props.update(kw)
        return self.node("rectangle", parent, name, w=w, h=h, **props)

    def text(self, parent, chars, style="corpo", color="#000000", w=None, fillw=False,
             align=None, name=None, **extra):
        st = self.textstyles[style]
        props = {"fontFamily": FONT, "fontStyle": st["fontStyle"], "fontSize": st["fontSize"],
                 "lineHeight": st["lineHeight"], "letterSpacing": st["letterSpacing"],
                 "textCase": st["textCase"], "fill": color}
        if align:
            props["textAlign"] = align
        props.update(extra)
        if w is not None or fillw:
            props["textAutoResize"] = "height"
        nid = self.node("text", parent, name or chars[:40], w=w if w else (100 if fillw else None),
                        text=chars, **props)
        if fillw:
            self.set(nid, sizingH="fill")
        if style in self.styles:
            self.c("style.apply", ids=[nid], style=self.styles[style])
            if extra:
                self.set(nid, **extra)
        return nid

    def image(self, parent, path, w, h, name="Foto", mode="fill"):
        nid = self.nid
        self.nid += 1
        p = {"path": path, "width": w, "height": h, "mode": mode}
        if parent is not None:
            p["parent"] = parent
        self.cmds.append({"command": "image.place", "params": p, "expect": nid})
        self._reg(nid, parent, name)
        self.set(nid, name=name)
        return nid

    def instance(self, comp, parent=None, x=0, y=0, name=None):
        src = self.preorder(comp)
        start = self.nid
        mapping = {}
        for k, sid in enumerate(src):
            mapping[sid] = start + k
        self.nid += len(src)
        p = {"component": comp, "x": x, "y": y}
        if parent is not None:
            p["parent"] = parent
        self.cmds.append({"command": "instance.create", "params": p, "expect": start})
        # espelha a árvore
        self._reg(start, parent, self.names[comp])
        for sid in src[1:]:
            pass
        for sid in src:
            nid = mapping[sid]
            self.names[nid] = self.names[sid]
            self.children[nid] = [mapping[ch] for ch in self.children.get(sid, [])]
        inst = Inst(start, {})
        for sid in src:
            nm = self.names[sid]
            if nm not in inst.by:
                inst.by[nm] = mapping[sid]
        inst.all = [mapping[s] for s in src]
        if name:
            self.set(start, name=name)
        return inst

    def combine(self, ids, name, x=None, y=None, cols=None, gap=24):
        sid = self.nid
        self.nid += 1
        self.cmds.append({"command": "component.combineVariants", "params": {"ids": ids}, "expect": sid})
        # reparent: tira das listas antigas
        for k, v in self.children.items():
            self.children[k] = [c for c in v if c not in ids]
        self._reg(sid, None, name)
        self.children[sid] = list(ids)
        # (o set pode estar dentro de outro pai: tratado pelo chamador com reparent)
        self.set(sid, name=name)
        return sid

    def reparent(self, ids, parent):
        if not isinstance(ids, list):
            ids = [ids]
        self.c("node.reparent", ids=ids, parent=parent)
        for k, v in self.children.items():
            self.children[k] = [c for c in v if c not in ids]
        self.children.setdefault(parent, []).extend(ids)

    def interaction(self, nid, trigger, action, transition=None, ms=None, easing=None, **kw):
        p = {"id": nid, "trigger": trigger, "action": action}
        if transition:
            p["transition"] = transition
        if ms is not None:
            p["durationMs"] = ms
        if easing:
            p["easing"] = easing
        p.update(kw)
        self.c("proto.interaction.add", **p)

    # ---- variáveis e estilos --------------------------------------------------
    def collection(self, name, modes=None):
        self.col_n += 1
        cid = f"VariableCollectionId:{self.col_n}"
        p = {"name": name}
        if modes:
            p["modes"] = modes
        self.c("variable.createCollection", **p)
        return cid

    def var(self, col, name, type, value=None, values=None, desc=None):
        self.var_n += 1
        vid = f"VariableID:{self.var_n}"
        p = {"collection": col, "name": name, "type": type}
        if values is not None:
            p["values"] = values
        else:
            p["value"] = value
        self.c("variable.create", **p)
        if desc:
            self.c("variable.update", variable=vid, description=desc)
        self.vars[name] = vid
        return vid

    def alias(self, vid, target, mode=None):
        p = {"variable": vid, "value": {"alias": target}}
        if mode:
            p["mode"] = mode
        self.c("variable.set", **p)

    def bind(self, ids, field, varname):
        if not isinstance(ids, list):
            ids = [ids]
        self.c("variable.bind", ids=ids, field=field, variable=self.vars[varname])

    def style(self, type, name, frm, key=None, desc=None):
        self.style_n += 1
        sid = f"S:{self.style_n}"
        p = {"type": type, "name": name, "from": frm}
        if desc:
            p["description"] = desc
        self.c("style.create", **p)
        if key:
            self.styles[key] = sid
        return sid

    def dump(self, path):
        clean, exp = [], []
        for k, cm in enumerate(self.cmds):
            clean.append({"command": cm["command"], "params": cm["params"]})
            if "expect" in cm:
                exp.append((k, cm["expect"]))
        with open(path, "w", encoding="utf-8") as f:
            json.dump(clean, f, ensure_ascii=False)
        with open(path + ".expect", "w", encoding="utf-8") as f:
            json.dump(exp, f)


class Inst:
    def __init__(self, id, by):
        self.id = id
        self.by = by
        self.all = []

    def __getitem__(self, k):
        return self.by[k]
