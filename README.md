# 📚 Book Methodology Extractor / 书籍方法论提取器

[![GitHub license](https://img.shields.io/github/license/dearhans/book-methodology-extractor)](https://github.com/dearhans/book-methodology-extractor/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/dearhans/book-methodology-extractor)](https://github.com/dearhans/book-methodology-extractor/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/dearhans/book-methodology-extractor)](https://github.com/dearhans/book-methodology-extractor/issues)

一个智能工具，可以从书籍中提取核心方法论并自动生成结构化的 **Hermes Agent 技能**，让知识快速转化为可执行的 AI 工作流。

An intelligent tool that extracts core methodologies from books and automatically generates structured **Hermes Agent skills**, transforming knowledge into actionable AI workflows.

---

## 🌟 特性 / Features

- **📖 双模式输入** - 支持书名搜索和文档上传
- **🧠 智能提取** - 自动识别方法论、原则和实践
- **⚡ 一键生成** - 快速创建 Hermes Agent 兼容的 SKILL.md
- **✅ 合规验证** - 内置合规性检查脚本
- **🎨 模板化** - 提供 GitHub 发布模板
- **🔒 安全可靠** - 注重隐私保护和数据安全

## 🚀 快速开始 / Quick Start

### 前提条件 / Prerequisites

- Python 3.8+
- Hermes Agent 环境
- 网络连接（用于书籍搜索）

### 安装 / Installation

```bash
# 克隆仓库
git clone https://github.com/dearhans/book-methodology-extractor.git
cd book-methodology-extractor

# 确保技能目录存在
mkdir -p ~/.hermes/skills/knowledge/

# 链接到 Hermes Agent
ln -s $(pwd)/SKILL.md ~/.hermes/skills/knowledge/book-methodology-extractor/SKILL.md
```

### 使用方法 / Usage

#### 方式一：通过 Hermes Agent 使用

```bash
# 在 Hermes Agent 中调用技能
使用 book-methodology-extractor 技能
```

#### 方式二：直接运行

```bash
# 查看技能文档
cat SKILL.md

# 运行合规性检查
python scripts/compliance_check.py
```

## 📂 项目结构 / Project Structure

```
book-methodology-extractor/
├── SKILL.md                          # 核心技能定义
├── scripts/
│   └── compliance_check.py           # 合规性验证脚本
├── templates/
│   ├── concise-skill-template.md     # 简洁技能模板
│   └── github-project-template.md    # GitHub 项目模板
└── references/
    ├── session-20260512-compliance-lessons.md      # 合规性经验
    ├── session-20260512-content-preferences.md     # 内容偏好
    ├── session-20260512-github-publishing-workflow.md  # 发布工作流
    └── session-20260512-summary.md                 # 会话总结
```

## 🎯 核心功能 / Core Functions

### 1. 方法论提取 / Methodology Extraction

- 从书籍中识别核心概念和框架
- 提取实践原则和操作步骤
- 生成可执行的工作流定义

### 2. 技能生成 / Skill Generation

- 自动创建符合 Hermes Agent 规范的 SKILL.md
- 包含完整的 YAML 前置元数据
- 提供使用示例和最佳实践

### 3. 合规检查 / Compliance Checking

- 验证技能定义的完整性
- 检查安全性和隐私保护
- 确保符合服务条款

## 💡 应用场景 / Use Cases

- **📚 知识管理** - 将阅读笔记转化为可执行技能
- **🤖 自动化工作流** - 快速构建 AI 驱动的任务流程
- **📊 数据分析** - 提取量化分析方法
- **🔍 研究助手** - 创建领域特定的研究工具

## 🤝 贡献 / Contributing

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证 / License

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢 / Acknowledgments

- [Hermes Agent](https://github.com/nousresearch/hermes) - 强大的 AI 助手平台
- 所有贡献者和测试者

---

## 📧 联系 / Contact

- GitHub: [@dearhans](https://github.com/dearhans)
- Issue Tracker: [GitHub Issues](https://github.com/dearhans/book-methodology-extractor/issues)

## 🌐 多语言支持 / Language Support

- 🇨🇳 中文 (Chinese)
- 🇺🇸 English

---

**让知识流动，让智能发生** 🌟

*Transform knowledge into action, let intelligence happen.*