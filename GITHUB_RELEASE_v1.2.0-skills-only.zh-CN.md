# Game Superpowers v1.2.0 — Skills-Only Release

这个版本正式把项目收敛为一个面向 Claude Code 和 Codex 的、**以 skills 为核心** 的开源系统。

## 这次改了什么

- 项目叙事从“插件分发”改成“skills collection”
- 新增 `using-game-superpowers` 作为整套技能库的总入口
- 安装文档改成 Claude / Codex 的原生 skills 方案
- 新增 Claude / Codex 的安装与卸载脚本
- 开源文档重新围绕 build track + audit track 整理

## 为什么重要

Game Superpowers 的真正价值在于：
- 游戏领域工作流逻辑
- UI/UX 和反馈感知的路由方式
- 基于项目状态的 build / audit 流程
- 容易 fork、容易改、容易组合的 skills

用 skills collection 的方式发布，意味着它会更容易：
- 本地使用
- 开源协作
- 团队定制
- 跨宿主兼容

## 亮点

- skills-first 分发
- build track 和 audit track
- collection bootstrap skill
- Claude 的 `--add-dir` 使用方式
- Codex 的 symlink 安装方式

## 说明

以后仍然可以有人基于这个仓库再打成插件，但插件不再是这个项目的 source of truth。
