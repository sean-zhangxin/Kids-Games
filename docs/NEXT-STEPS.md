# Kids-Games · 下一步 / 会话交接（2026-08-09）

> 这份文件给"接手的新会话"看。当前会话因被钉在 C 盘工作区、E 盘 md/json 预览报"文件不存在"而结束；新会话工作区在 **E 盘**，该问题自动消失。

## 项目是什么
亲子妖怪 RPG（学习型）。核心循环：**收服野生妖怪 → 用课程挑战当"招式"打怪（答对=命中、答错=己方挨打）→ 攒经验升级 → 达到门槛进化**。学习即战力。
两孩玩同一套机制、同一主题世界，但**题目按登录身份分流**：小宝(7岁)答 1–2 年级题，大宝(12岁)答初一题。
目标设备：华为手机/平板（Android 系），离线优先；交付用 **Godot 引擎 HTML5 导出**（APK 可额外出）。
仓库：`sean-zhangxin/Kids-Games`（私有）。工作区：`E:\WorkBuddy\Kids-Games`。

## 已拍板设计基线（勿擅自推翻，除非用户明确同意）
1. 战斗属性 = 语/数/英 三系 RPS：**语文 > 英语 > 数学 > 语文**。
2. 等级(LV) 只涨 HP/ATK 基线（`ATK=10+2×LV`，`HP=40+8×LV`）。**克制倍率恒为 ×1.5(克制)/×0.67(被克)/×1.0(同级)，绝不随 LV 变化**——红线，防年长练级碾压年幼。
3. 身份路由：登录身份 → 年级 → 题库。小宝走 `data/questions/grade-1-2.json`，大宝走 `grade-7.json`。
4. 进化双门槛：等级达标(LV≥T_LV `[PLACEHOLDER]`) **AND** 通过"本妖怪属性科目综合考试"（N题@本身份年级，正确率≥X% `[PLACEHOLDER]`）。
5. 题型→限制映射：选择题统一 10s 倒计时、填空限 3 次、连线无时限、跟读限 2 次；超时/超限 = miss = 己方挨打（复用软惩罚）。
6. 软惩罚：妖怪 HP 归零 = 昏厥 → 撤退回基地，收藏不丢（Pokémon 式）。
7. 建造/家园元层已砍，当前聚焦妖怪 RPG 主线。
8. 所有数值仍标 `[PLACEHOLDER]`，真机 playtest 校准前不得拍死。

## 已完成产物（均在 E:\WorkBuddy\Kids-Games，已 push origin/main）
- `README.md`：项目说明，妖怪 RPG 定位 + 数据驱动原则 + Godot 路线。
- `docs/paper-prototype-02-battle-loop.md`(+`.html`)：v0.3 战斗+收服+进化循环设计，含身份路由 / 双门槛 / 题型限制 / 系统交互矩阵 / playtest 信号 A~F。
- `docs/tuning-01.md`(+`.csv`+`.html`)：数值调校表。ANCHOR（锁死：克制倍率、命中系数、时限、题型限制、双门槛逻辑）与 `[PLACEHOLDER]`（ATK/HP 曲线、EXP、T_LV、考试题数/限时/正确率、收服阈值）分离列出。
- `data/monsters.json`：妖怪数值表（starters 3 / wild 6 / trainer 1），每只带 `attribute`(chinese/math/english) + `level_by_profile`{grade-1-2, grade-7}（实现难度按年龄调）+ `move_types`。
- `data/question-schema.json`：题目 JSON Schema（topic 轴供综合考覆盖 ≥3 知识点）。
- `data/questions/grade-1-2.json` / `grade-7.json`：双年级样例题库，每科 3 题（`[PLACEHOLDER]` 范例，待家长按真实课本扩充）。
- `docs/data-index.md`：给家长 / 12 岁加题加妖怪的指引。
- `tools/gen_data_preview.py` + `docs/data-preview.html`：JSON→HTML 预览生成器（数据更新后跑一次重新生成预览）。

## ⚠️ 已知坑
- **md/json 预览（仅限旧 C 盘会话）**：本会话工作空间被钉在 C 盘，md/json 预览器按会话工作区为根找文件，E 盘跨盘绝对路径不可达 → 报"文件不存在"。**新会话在 E 盘工作区，此问题消失**。看文档最稳方式：HTML 预览版（data-preview.html 等）或直接去 GitHub 仓库看。
- **GitHub MCP 连接器令牌受限**：建库(`create_repository` 403)/枚举(422)/读私有库(404)均失败。同步**一律走 git over SSH**（已验证 `ssh -T git@github.com` 通）。不要在 MCP 工具里建库 / 推送。

## ▶ 下一步待办（用户将重开会话继续）
1. **进 Godot 搭 P1 MVP**：单 Godot 工程，1 妖怪 + 战斗 + 收服 + 进化双门槛，语文起手；实现双孩身份路由 + 题型限制；读 `data/` 跑起来。
2. 进 MVP 前建议补充：让家长按真实课本把每科题库扩到 ≥10 题、topic ≥4（当前每科仅 3 题范例）；题库 topic 轴已就绪供综合考。
3. （可选）把剩余 md 设计文档补 HTML 预览版——但新会话在 E 盘已能直接预览 md，此条可省。

## 文件速查
- 设计基线：`docs/paper-prototype-02-battle-loop.md`
- 数值：`docs/tuning-01.md`
- 数据：`data/*.json`（怪物 / 双年级题库 / schema）
- 预览：`docs/data-preview.html`（跑 `tools/gen_data_preview.py` 重新生成）
- 远程：`git@github.com:sean-zhangxin/Kids-Games.git`（SSH，main 分支）
