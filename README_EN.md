# 📚 Book Methodology Extractor / Book Methodology Extractor

[![GitHub license](https://img.shields.io/github/license/dearhans/book-methodology-extractor)](https://github.com/dearhans/book-methodology-extractor/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/dearhans/book-methodology-extractor)](https://github.com/dearhans/book-methodology-extractor/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/dearhans/book-methodology-extractor)](https://github.com/dearhans/book-methodology-extractor/issues)

An intelligent tool that extracts core methodologies from books and automatically generates structured **Hermes Agent skills**, transforming knowledge into actionable AI workflows.

A smart tool that extracts core methodologies from books and automatically generates structured **Hermes Agent skills**, turning knowledge into executable AI workflows.

---

## 🌟 Features

- **📖 Dual Input Mode** - Supports book title search and document upload
- **🧠 Intelligent Extraction** - Automatically identifies methodologies, principles, and practices
- **⚡ One-Click Generation** - Quickly creates Hermes Agent compatible SKILL.md
- **✅ Compliance Checking** - Built-in validation script for quality assurance
- **🎨 Templated** - Provides GitHub publishing templates
- **🔒 Secure & Reliable** - Focuses on privacy protection and data security

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Hermes Agent environment
- Internet connection (for book search)

### Installation

```bash
# Clone the repository
git clone https://github.com/dearhans/book-methodology-extractor.git
cd book-methodology-extractor

# Ensure skills directory exists
mkdir -p ~/.hermes/skills/knowledge/

# Link to Hermes Agent
ln -s $(pwd)/SKILL.md ~/.hermes/skills/knowledge/book-methodology-extractor/SKILL.md
```

### Usage

#### Method 1: Using Hermes Agent

```bash
# Invoke the skill in Hermes Agent
Use book-methodology-extractor skill
```

#### Method 2: Direct Execution

```bash
# View the skill documentation
cat SKILL.md

# Run compliance check
python scripts/compliance_check.py
```

## 📂 Project Structure

```
book-methodology-extractor/
├── SKILL.md                          # Core skill definition
├── scripts/
│   └── compliance_check.py           # Compliance validation script
├── templates/
│   ├── concise-skill-template.md     # Concise skill template
│   └── github-project-template.md    # GitHub project template
└── references/
    ├── session-20260512-compliance-lessons.md      # Compliance lessons
    ├── session-20260512-content-preferences.md     # Content preferences
    ├── session-20260512-github-publishing-workflow.md  # Publishing workflow
    └── session-20260512-summary.md                 # Session summary
```

## 🎯 Core Functions

### 1. Methodology Extraction

- Identifies core concepts and frameworks from books
- Extracts practical principles and operational steps
- Generates executable workflow definitions

### 2. Skill Generation

- Automatically creates SKILL.md compliant with Hermes Agent standards
- Includes complete YAML frontmatter
- Provides usage examples and best practices

### 3. Compliance Checking

- Validates skill definition completeness
- Checks security and privacy protection
- Ensures service terms compliance

## 💡 Use Cases

- **📚 Knowledge Management** - Convert reading notes into executable skills
- **🤖 Workflow Automation** - Quickly build AI-driven task flows
- **📊 Data Analysis** - Extract quantitative analysis methods
- **🔍 Research Assistant** - Create domain-specific research tools

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hermes Agent](https://github.com/nousresearch/hermes) - Powerful AI assistant platform
- All contributors and testers

---

## 📮 Contact

- GitHub: [@dearhans](https://github.com/dearhans)
- Issue Tracker: [GitHub Issues](https://github.com/dearhans/book-methodology-extractor/issues)

## 🌐 Language Support

- 🇨🇳 Chinese (中文)
- 🇺🇸 English

---

**Transform knowledge into action, let intelligence happen** ✨

*让知识流动，让智能发生*