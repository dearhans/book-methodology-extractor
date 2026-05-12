# GitHub Project Template for Book Methodology Skills

## Repository Structure

```
{repository-name}/
├── README.md                    # Project overview and quick start
├── SKILL.md                     # Core skill definition
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore patterns
├── setup-github.sh              # Automated deployment script
├── GITHUB_PUBLISH_GUIDE.md      # Detailed publishing guide
├── examples/
│   └── basic-usage.md          # Usage examples
└── templates/
    └── skill-templates.md      # Skill templates for different domains
```

## README.md Template

```markdown
# {book-title} Methodology Skills

> Automated extraction of core methodologies from "{book-title}" by {author}, implemented as Hermes Agent skills.

## Overview

This repository contains {N} Hermes Agent skills extracted from the book "{book-title}". Each skill represents a core methodology or framework from the book, implemented as a standalone, reusable skill.

## Skills Included

{skills_list}

## Quick Start

### Prerequisites

- Hermes Agent CLI installed
- Node.js (for some advanced features)

### Installation

#### Method 1: Automated Deployment (Recommended)

```bash
./setup-github.sh
```

This script will:
1. Create a new GitHub repository
2. Configure Git with your credentials
3. Push all skill files
4. Set up remote tracking

#### Method 2: Manual Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/{username}/{repository-name}.git
   cd {repository-name}
   ```

2. Install each skill:
   ```bash
   skill_manage(action='create', name='{skill-name}', ...)
   ```

## Usage

### Basic Example

```javascript
// Using a specific methodology
skill_view(name='{skill-name}')
```

### Integration with Other Skills

These skills can be combined with other Hermes Agent capabilities:

- **Search and Discovery**: Use with search tools to find relevant methodologies
- **Automation**: Chain multiple skills for complex workflows
- **Documentation**: Generate comprehensive guides from skill outputs

## Skill Details

{skill_details}

## Examples

See the `examples/` directory for detailed usage examples.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.
```

## SKILL.md Template

```markdown
---
name: {methodology-name}
description: {trigger-description}. When user {trigger-condition} use this skill.
category: knowledge
---

# {methodology-chinese-name}

{methodology-description}

## Source

This methodology comes from "{book-title}" by {author}, Chapter {chapter}.

## Applicable Scenarios

- {scenario-1}
- {scenario-2}
- {scenario-3}

## Execution Steps

### Step 1: {step-1-name}
{step-1-description}

### Step 2: {step-2-name}
{step-2-description}

### Step 3: {step-3-name}
{step-3-description}

## Output Format

{output-description}

**Example Output:**

```
{example-output}
```

## Notes

- {note-1}
- {note-2}

## Real-World Application

{application-example}
```

## setup-github.sh Template

```bash
#!/bin/bash

# GitHub Repository Setup Script
# Automated deployment for Book Methodology Skills

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Book Methodology Skills - GitHub Setup ===${NC}"

# Function to print colored messages
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check prerequisites
print_info "Checking prerequisites..."

if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install Git first."
    exit 1
fi

if ! command -v gh &> /dev/null; then
    print_warn "GitHub CLI (gh) is not installed."
    print_info "You can install it from: https://cli.github.com/"
    print_info "Alternatively, you can create the repository manually."
fi

# Get user input
read -p "Enter your GitHub username: " GITHUB_USERNAME
read -p "Enter repository name (default: book-methodology-skills): " REPO_NAME

REPO_NAME=${REPO_NAME:-book-methodology-skills}

# Check if repository already exists locally
if [ -d ".git" ]; then
    print_warn "Git repository already initialized."
    read -p "Do you want to reinitialize? (y/N): " REINIT
    if [[ ! $REINIT =~ ^[Yy]$ ]]; then
        print_info "Skipping reinitialization."
    else
        rm -rf .git
        git init
    fi
else
    git init
fi

# Configure Git
print_info "Configuring Git..."
git config user.name "$GITHUB_USERNAME"
git config user.email "$GITHUB_USERNAME@users.noreply.github.com"

# Create .gitignore if it doesn't exist
if [ ! -f .gitignore ]; then
    cat > .gitignore << EOF
# Dependencies
node_modules/
__pycache__/
*.pyc

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Hermes
.hermes/skills/generated/

# Temporary files
*.tmp
*.log
temp/
EOF
    print_info "Created .gitignore"
fi

# Create initial commit
print_info "Creating initial commit..."
git add .
git commit -m "Initial commit: Book methodology skills

- Core skill definitions
- Usage examples
- Templates for different domains
- Automated deployment scripts" || print_warn "Nothing to commit or already committed"

# Create GitHub repository
if command -v gh &> /dev/null; then
    print_info "Creating GitHub repository..."
    if gh repo create "$REPO_NAME" --public --source=. --remote=origin --push; then
        print_info "Repository created and code pushed successfully!"
    else
        print_error "Failed to create repository. You may need to authenticate first."
        print_info "Run: gh auth login"
        exit 1
    fi
else
    print_warn "GitHub CLI not available."
    print_info "Please create the repository manually:"
    echo "  1. Go to https://github.com/new"
    echo "  2. Name it: $REPO_NAME"
    echo "  3. Make it public"
    echo "  4. Do not initialize with README"
    echo ""
    echo "Then run these commands:"
    echo "  git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
    echo "  git push -u origin main"
fi

print_info "Setup complete!"
echo ""
echo -e "${GREEN}Next steps:${NC}"
echo "1. View your skills in the repository"
echo "2. Share the repository with others"
echo "3. Install skills using skill_manage()"
echo ""
echo -e "${GREEN}Repository URL:${NC}"
echo "https://github.com/$GITHUB_USERNAME/$REPO_NAME"
```

## GITHUB_PUBLISH_GUIDE.md Template

```markdown
# GitHub Publishing Guide

## Overview

This guide explains how to publish your Book Methodology Skills to GitHub.

## Prerequisites

1. **GitHub Account**: You need a GitHub account
2. **Git Installed**: Git should be installed on your system
3. **Hermes Agent**: Hermes Agent CLI should be installed

## Method 1: Automated Deployment (Recommended)

### Step 1: Run the Setup Script

```bash
./setup-github.sh
```

### Step 2: Follow the Prompts

The script will ask for:
- Your GitHub username
- Repository name (defaults to `book-methodology-skills`)

### Step 3: Authenticate (if needed)

If you haven't authenticated with GitHub CLI before, you'll need to run:

```bash
gh auth login
```

Follow the prompts to authenticate.

### Step 4: Verify

After the script completes, visit:
```
https://github.com/{username}/{repository-name}
```

## Method 2: Manual Deployment

### Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Enter a repository name
3. Choose public or private
4. **Do not** initialize with README, .gitignore, or license
5. Click "Create repository"

### Step 2: Add Remote

```bash
git remote add origin https://github.com/{username}/{repository-name}.git
```

### Step 3: Push Code

```bash
git push -u origin main
```

## Method 3: Import Existing Repository

If you have an existing repository:

1. Go to https://github.com/new/import
2. Enter the URL of your existing repository
3. Follow the import process

## Post-Deployment

### Install Skills

After deployment, you can install skills:

```javascript
skill_manage(
    action='create',
    name='{skill-name}',
    category='knowledge',
    content=skill_content
)
```

### Update Skills

To update skills:

```bash
# Make changes
git add .
git commit -m "Update skills"
git push
```

### Share with Others

Share the repository URL with others so they can:
1. Clone the repository
2. Install the skills
3. Use the methodologies

## Troubleshooting

### Authentication Issues

If you get authentication errors:

```bash
gh auth login
```

### Permission Denied

Make sure you have write access to the repository.

### Repository Already Exists

If the repository already exists, you can push to it:

```bash
git push -u origin main
```

## Best Practices

1. **Commit Often**: Make small, frequent commits
2. **Write Good Messages**: Use descriptive commit messages
3. **Use Branches**: Create branches for new features
4. **Review Changes**: Review changes before pushing
5. **Keep Updated**: Regularly update your skills

## Additional Resources

- [GitHub Documentation](https://docs.github.com/)
- [Git Documentation](https://git-scm.com/doc)
- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs)
```

## License Template

```
MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## .gitignore Template

```
# Dependencies
node_modules/
__pycache__/
*.pyc

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Hermes
.hermes/skills/generated/

# Temporary files
*.tmp
*.log
temp/
*.bak

# Environment
.env
.env.local

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/

# nyc test coverage
.nyc_output

# Dependency directories
jspm_packages/

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Microbundle cache
.rpt2_cache/
.rts2_cache_cjs/
.rts2_cache_es/
.rts2_cache_umd/

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# parcel-bundler cache (https://parceljs.org/)
.cache/

# Next.js build output
.next/

# Nuxt.js build / generate output
.nuxt/

# Gatsby files
.cache/
public

# vuepress build output
.vuepress/dist

# Serverless directories
.serverless/

# FuseBox cache
.fusebox/

# DynamoDB Local files
.dynamodb/

# TernJS port file
.tern-port

# Stores VSCode versions used for testing VSCode extensions
.vscode-test
```

## Examples Directory Structure

```
examples/
├── basic-usage.md          # Basic usage examples
├── advanced-usage.md       # Advanced usage examples
├── integration.md          # Integration with other tools
└── troubleshooting.md      # Common issues and solutions
```

## Templates Directory Structure

```
templates/
├── skill-templates.md      # Templates for different skill types
├── domain-templates.md     # Templates for specific domains
└── example-templates.md    # Example templates for common scenarios
```

## Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `{book-title}` | Title of the book | "Atomic Habits" |
| `{author}` | Author name | "James Clear" |
| `{repository-name}` | GitHub repository name | "atomic-habits-skills" |
| `{username}` | GitHub username | "johndoe" |
| `{skill-name}` | Name of the skill | "habit-loop" |
| `{N}` | Number of skills | 4 |
| `{year}` | Current year | 2026 |
| `{skills_list}` | List of skills | See template above |
| `{skill_details}` | Detailed skill information | See template above |

## Quick Start Commands

```bash
# 1. Clone the repository
git clone https://github.com/{username}/{repository-name}.git
cd {repository-name}

# 2. Run automated setup
./setup-github.sh

# 3. Install a skill
skill_manage(
    action='create',
    name='{skill-name}',
    category='knowledge',
    content=skill_content
)

# 4. Use the skill
skill_view(name='{skill-name}')
```

## Support

For issues or questions:
1. Check the troubleshooting guide
2. Review the examples
3. Check the Hermes Agent documentation
4. Create an issue in the repository
