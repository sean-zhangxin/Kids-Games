#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 Kids-Games 的数据文件渲染成可在浏览器预览的 HTML。
用法：python tools/gen_data_preview.py
输出：docs/data-preview.html
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "data-preview.html")


def load(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return json.load(f)


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def monster_rows(monsters):
    rows = []
    for m in monsters.get("monsters", []):
        prof = m.get("level_by_profile", {})
        young = prof.get("young", "?")
        older = prof.get("older", "?")
        rows.append(
            "<tr><td>{name}</td><td>{id}</td><td>{attr}</td><td>{cat}</td><td>{y}</td><td>{o}</td></tr>".format(
                name=esc(m.get("name")),
                id=esc(m.get("id")),
                attr=esc(m.get("attribute")),
                cat=esc(m.get("category")),
                y=esc(young),
                o=esc(older),
            )
        )
    return "\n".join(rows)


def question_rows(qs):
    rows = []
    for q in qs.get("questions", []):
        opts = q.get("options")
        if isinstance(opts, list):
            opts = " / ".join(str(o) for o in opts)
        else:
            opts = esc(opts) if opts else "—"
        rows.append(
            "<tr><td>{topic}</td><td>{type}</td><td>{stem}</td><td>{opts}</td><td>{ans}</td><td>{diff}</td></tr>".format(
                topic=esc(q.get("topic")),
                type=esc(q.get("type")),
                stem=esc(q.get("stem")),
                opts=opts,
                ans=esc(q.get("answer")),
                diff=esc(q.get("difficulty")),
            )
        )
    return "\n".join(rows)


monsters = load("data/monsters.json")
g12 = load("data/questions/grade-1-2.json")
g7 = load("data/questions/grade-7.json")

TEMPLATE = """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>Kids-Games 数据预览</title>
<style>
body{font-family:-apple-system,"Microsoft YaHei",sans-serif;max-width:960px;margin:24px auto;padding:0 16px;color:#1a1a1a;}
h1{font-size:22px;border-bottom:3px solid #ff7a59;padding-bottom:8px;}
h2{font-size:18px;margin-top:32px;color:#c0392b;}
table{border-collapse:collapse;width:100%;font-size:13px;margin-top:8px;}
th,td{border:1px solid #ddd;padding:6px 8px;text-align:left;vertical-align:top;}
th{background:#fff3ee;}
tr:nth-child(even){background:#fafafa;}
.note{background:#fffbe6;border:1px solid #ffe58f;padding:10px 12px;border-radius:6px;font-size:13px;margin:12px 0;}
</style></head><body>
<h1>Kids-Games · 数据预览</h1>
<div class="note">本页由 <code>tools/gen_data_preview.py</code> 从 <code>data/*.json</code> 自动生成，仅供右侧浏览器预览。权威源仍是仓库里的 JSON 文件。所有题目/数值均为 <b>[PLACEHOLDER]</b> 范例，待家长按真实课本扩充。</div>

<h2>妖怪数值表（data/monsters.json）</h2>
<table>
<tr><th>名称</th><th>ID</th><th>属性(科目)</th><th>类别</th><th>小宝档LV</th><th>大宝档LV</th></tr>
__MONSTERS__
</table>

<h2>小宝题库（data/questions/grade-1-2.json · 1-2年级）</h2>
<table>
<tr><th>知识点</th><th>题型</th><th>题目</th><th>选项</th><th>答案</th><th>难度</th></tr>
__Q12__
</table>

<h2>大宝题库（data/questions/grade-7.json · 初一）</h2>
<table>
<tr><th>知识点</th><th>题型</th><th>题目</th><th>选项</th><th>答案</th><th>难度</th></tr>
__Q7__
</table>
</body></html>
"""

html = TEMPLATE
html = html.replace("__MONSTERS__", monster_rows(monsters))
html = html.replace("__Q12__", question_rows(g12))
html = html.replace("__Q7__", question_rows(g7))

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("written:", OUT)
