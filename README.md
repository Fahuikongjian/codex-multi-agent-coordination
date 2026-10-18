# Codex 多代理协作 Skill

让 Codex 的主代理与子代理围绕同一目标工作，减少重复实现、互改文件、审查拉扯和旧方案覆盖新方案。

适合多 agent 联合实现、并行审查，以及已经出现“左右脑互搏”的任务。普通小改动仍由一个代理直接完成。技能以中文编写，提供英文检索描述，不绑定模型或操作系统。

## 解决哪些冲突

| 常见问题 | 采用的协作方式 |
| --- | --- |
| 多个代理各自重做整件事 | 主代理统一目标，子任务有明确交付边界 |
| 两个代理同时修改一个文件 | 单写入负责人；其他代理只提案，或停写后交接 |
| 实现者和审查者反复推翻 | 用需求和复现裁定；无新证据沿用已定方案 |
| 旧任务结果晚到，覆盖新需求 | 任务 epoch 与输入基线复核；旧结果先验证再采用 |
| 中断旧代理后立即让新人接手 | 核实代理、工具及后台进程停写，再转移所有权 |
| worktree 分开了仍抢端口、数据库 | 同时分配共享资源与文件所有权 |
| 子代理完成后主代理只拼报告 | 集成实际产物，检查最终版本，再统一交付 |

本技能提供提示和协作协议，不是调度服务、文件锁或权限系统，无法保证所有代理始终遵守。涉及真实并发写入时仍需要实际隔离和状态核实。

## 安装

在 Codex 中使用内置安装器：

```text
使用 $skill-installer 安装这个技能：
https://github.com/Fahuikongjian/codex-multi-agent-coordination/tree/main/skills/codex-multi-agent-coordination
```

也可以复制仓库中的 `skills/codex-multi-agent-coordination/` 到项目的 `.agents/skills/`，或当前客户端使用的个人技能目录。当前官方文档列出的个人目录为 `~/.agents/skills/`；部分既有环境及安装器使用 `~/.codex/skills/`。以本机技能列表和安装器为准，不必同时安装两份。

技能允许正常的自动发现，也可显式调用。客户端未刷新时重启 Codex。不会修改你的全局 `AGENTS.md`、模型配置或并发限制。

## 使用

直接委派一个实现任务：

```text
使用 $codex-multi-agent-coordination 完成这个功能。
由主代理确定接口和验收，只把能独立推进的工作交给子代理。
明确各自的文件与共享资源所有权，完成实际集成和必要检查。
```

解决正在发生的冲突：

```text
使用 $codex-multi-agent-coordination 接管当前多代理协作。
两个代理正在改同一个文件，审查意见也在反复推翻。
先核实当前任务、写入者和产物，停止受影响的重叠写入，
再按证据裁定争点并完成交接；继续推进不受影响的工作。
```

并行审查：

```text
使用 $codex-multi-agent-coordination 审查当前改动。
按互不重复的关注点分配只读审查，使用同一个稳定版本。
主代理核实发现并去重，不让审查者直接修改实现文件。
```

运行时需要提供真正的子代理工具。若没有，技能按依赖顺序直接推进，不会创建新的用户聊天来模拟并行。实际发送、发布等操作仍须在原有授权范围内。

## 文件结构

```text
skills/codex-multi-agent-coordination/
  SKILL.md                         核心规则与工作流
  agents/openai.yaml               Codex 界面元数据
  references/task-contracts.md     委派、回报和决策模板
  references/conflict-recovery.md  冲突恢复与停写交接
  references/codex-tools.md        运行时能力适配与官方资料
evals/scenarios.md                行为评估输入与判定标准
```

只读入口后按实际问题加载相应参考文件。无需安装额外 Python 包、MCP 服务或后台程序。

## 验证与维护

技能应通过 Codex 内置 skill-creator 的 `quick_validate.py`，并检查 YAML、相对链接和委派行为。格式校验只能证明结构有效；行为评估输入和判定标准见 [evals/scenarios.md](evals/scenarios.md)。

格式与安装依据：[OpenAI Skills 文档](https://developers.openai.com/codex/skills)；子代理适配依据：[OpenAI Subagents 文档](https://developers.openai.com/codex/multi-agent)。工具名只作能力映射示例，以当前会话工具契约为准。

采用 [MIT License](LICENSE)。
