# 数据目录说明（Data Index）

给家长与 12 岁孩子：如何不碰代码、只改 JSON 就增删妖怪和题目。
这是「数据驱动 / 孩子可改」原则（见 README）的落地指引。

## 文件地图

| 文件 | 作用 |
|---|---|
| `data/monsters.json` | 妖怪数值：玩家初始妖怪（starters）、野怪（wild）、训练师（trainers） |
| `data/question-schema.json` | 题目的结构定义（JSON Schema），加题时对照，确保字段齐全 |
| `data/questions/grade-1-2.json` | 小宝（7岁，1–2年级）题库 |
| `data/questions/grade-7.json` | 大宝（12岁，初一）题库 |

> ⚠️ 题目按**登录身份**路由：小宝的文件里 `grade` 必须写 `grade-1-2`，大宝的文件写 `grade-7`，不要写反。

## 加一道题（改对应的 grade 文件）

在 `questions` 数组里复制一条已有对象，改这些字段：

- `id`：唯一，建议 `科目-年级-序号`，如 `ma-g12-04`
- `subject`：`chinese` / `math` / `english`（= 战斗属性，决定这道题属于哪系妖怪）
- `topic`：知识点轴（如 拼音 / 识字 / 分数 / 方程）。**综合考靠 `topic` 保证覆盖 ≥3 个不同知识点**，所以别把所有题都填同一个 topic
- `difficulty`：1–5，越高掉越多知识结晶
- `type`：
  - `choice` 选择题 → **必须带 `options` 数组**，选择题统一 10s 倒计时
  - `fill` 填空题 → 无时限，限 3 次尝试
  - `match` 连线 → 无时限
  - `speak` 跟读 → 限 2 次录制
- `stem` 题干、`answer` 标准答案、`rationale` 答错时的软提示

## 加一只妖怪（改 `monsters.json`）

在 `wild` 数组加一项：

- `id` 唯一、`name` 显示名
- `attribute`：`chinese` / `math` / `english`（战斗属性，决定克制关系）
- `biome` 出没区域（meadow / water / forest…）
- `level_by_profile`：**给两个档**——`grade-1-2` 是小宝世界的等级、`grade-7` 是大宝世界的等级。这就是「难度按年龄调」的实现
- `move_types`：该怪出招会抽的题型（从对应 grade 题库抽题）

## 校验

1. **JSON 必须合法**：用任意在线 JSON 校验器贴进去检查（逗号、引号、括号别漏）。
2. 题目可用 `question-schema.json` 校验结构（进阶，家长可用支持 JSON Schema 的工具）。

## 数值纪律（别在这里改）

- 怪物 HP / ATK **不要直接写死**，由公式派生（见 `tuning-01` §1，当前初值 `ATK=10+2×LV`、`HP=40+8×LV`）；改 `level_by_profile` 即可调强弱。
- 克制倍率、题型时限等**锁死值**在 `tuning-01`，不在本目录改——改了会破坏双孩平衡。
- 所有数值仍是 `[PLACEHOLDER]`，真机 playtest 后由家长在 `tuning-01` 统一调。
