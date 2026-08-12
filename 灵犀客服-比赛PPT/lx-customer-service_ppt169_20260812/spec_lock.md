<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: zh-CN
- audience: 比赛评委与同行参赛者，熟悉 AI/Agent 概念，关注工程落地
- objective: 让评委记住多 Agent 客服闭环已真实跑通、全透明可干预安全可控、知识反哺是独特创新，并认可其可落地性
- core_message: 基于 AgentTeams 的 6 智能体客服闭环，从多渠道工单到知识沉淀全自动，已跑通端到端验证

## mode
- mode: custom
- mode_references: briefing
- mode_behavior: 结论先行式论证——每部分先亮出核心主张（"闭环已跑通""全透明可干预""知识反哺"），再分块展开支撑论据；标题采用断言式，页面节奏均匀，以事实和结构说服评委

## visual_style
- visual_style: custom
- visual_style_references: blueprint
- visual_style_behavior: 技术蓝图美学——浅冷白底 + 克莱因蓝主色，发丝线网格与直角色块构成版式骨架，mono 字体做章节标注，架构流程使用几何连线与框体（描边线条，非填充卡通），克制、精确、可投影，无渐变、无圆角、无阴影

## colors
- background: #F7F8FA
- secondary_bg: #EDEFF3
- primary: #002FA7
- accent: #0057FF
- secondary_accent: #B8C4D6
- body_text: #1A1D24

## typography
- font_family: "微软雅黑", "PingFang SC", "Noto Sans SC", Inter, sans-serif
- title_family: "微软雅黑", "PingFang SC", "Noto Sans SC", Inter, sans-serif
- body_family: "微软雅黑", "PingFang SC", "Noto Sans SC", Inter, sans-serif
- data_family: "JetBrains Mono", "Consolas", monospace
- body: 22
- title: 44
- subtitle: 30
- annotation: 18

## icons
- library: tabler-outline
- stroke_width: 2
- inventory: tabler-outline/users, tabler-outline/mail, tabler-outline/message-circle, tabler-outline/phone, tabler-outline/message, tabler-outline/brand-x, tabler-outline/layers, tabler-outline/git-branch, tabler-outline/check, tabler-outline/shield-check, tabler-outline/eye, tabler-outline/database, tabler-outline/tool, tabler-outline/api, tabler-outline/refresh, tabler-outline/calendar

## page_rhythm
- P01: anchor
- P02: anchor
- P03: dense
- P04: breathing
- P05: dense
- P06: dense
- P07: anchor
- P08: dense
- P09: dense
- P10: dense
- P11: anchor
- P12: breathing

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
