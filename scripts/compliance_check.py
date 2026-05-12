#!/usr/bin/env python3
"""
Compliance Check Script for Book Methodology Skills

This script validates that generated skills meet quality standards
and comply with legal/ethical guidelines.
"""

import json
import re
import os
import sys
from datetime import datetime

class ComplianceChecker:
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.passed = []
        
    def check_skill_file(self, file_path):
        """Check a single skill file for compliance."""
        print(f"\n{'='*60}")
        print(f"Checking: {file_path}")
        print(f"{'='*60}")
        
        if not os.path.exists(file_path):
            self.issues.append(f"File not found: {file_path}")
            return False
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Parse YAML frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if not yaml_match:
            self.issues.append("Missing or invalid YAML frontmatter")
            return False
            
        yaml_content = yaml_match.group(1)
        body_content = yaml_match.group(2)
        
        # Check required fields
        required_fields = ['name', 'description', 'category']
        for field in required_fields:
            if field not in yaml_content:
                self.issues.append(f"Missing required field: {field}")
            else:
                self.passed.append(f"✓ Required field present: {field}")
                
        # Check category
        if 'category: knowledge' not in yaml_content:
            self.warnings.append("Category should be 'knowledge' for methodology skills")
        else:
            self.passed.append("✓ Category is 'knowledge'")
            
        # Check description length
        desc_match = re.search(r'description: (.+)', yaml_content)
        if desc_match:
            desc = desc_match.group(1)
            if len(desc) < 20:
                self.warnings.append("Description is too short (< 20 chars)")
            elif len(desc) > 200:
                self.warnings.append("Description is quite long (> 200 chars)")
            else:
                self.passed.append(f"✓ Description length is appropriate ({len(desc)} chars)")
                
        # Check for trigger condition in description
        if 'when user' in desc.lower() or '当用户' in desc:
            self.passed.append("✓ Description includes trigger condition")
        else:
            self.warnings.append("Description should include when to use this skill")
            
        # Check body content
        checks = [
            ('来源/Source section', r'#\s*来源|#\s*Source'),
            ('适用场景/Applicable Scenarios', r'#\s*适用场景|#\s*Applicable Scenarios'),
            ('执行步骤/Execution Steps', r'#\s*执行步骤|#\s*Execution Steps'),
            ('输出格式/Output Format', r'#\s*输出格式|#\s*Output Format'),
            ('示例输出/Example Output', r'```\s*\n.*?\n```', re.DOTALL),
        ]
        
        for check_name, pattern, *flags in checks:
            regex_flags = flags[0] if flags else 0
            if re.search(pattern, body_content, regex_flags):
                self.passed.append(f"✓ Contains {check_name}")
            else:
                self.warnings.append(f"Missing {check_name}")
                
        # Check for legal/compliance mentions
        compliance_patterns = [
            r'法律|legal|合规|compliance',
            r'隐私|privacy|机密|confidential',
            r'服务条款|terms of service|ToS',
            r'授权|authorization|permission',
        ]
        
        has_compliance_mention = any(
            re.search(pattern, body_content, re.IGNORECASE) 
            for pattern in compliance_patterns
        )
        
        if has_compliance_mention:
            self.passed.append("✓ Contains legal/compliance considerations")
        else:
            self.warnings.append("Consider adding legal/compliance notes")
            
        # Check for sensitive data placeholders
        if '[REDACTED]' in content:
            self.passed.append("✓ Uses [REDACTED] placeholder for sensitive data")
        else:
            # Not required, but good practice
            pass
            
        # Check for excessive length
        if len(content) > 10000:
            self.warnings.append("Content is very long (> 10KB), consider splitting")
        elif len(content) < 1000:
            self.warnings.append("Content is quite short (< 1KB), may need more detail")
        else:
            self.passed.append(f"✓ Content length is appropriate ({len(content)} chars)")
            
        # Check for code examples
        code_blocks = len(re.findall(r'```', content))
        if code_blocks >= 2:
            self.passed.append(f"✓ Contains code examples ({code_blocks//2} blocks)")
        else:
            self.warnings.append("Consider adding code examples")
            
        return len(self.issues) == 0
        
    def check_directory(self, directory):
        """Check all skill files in a directory."""
        print(f"\n{'#'*60}")
        print(f"Compliance Check for: {directory}")
        print(f"{'#'*60}")
        
        skill_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file == 'SKILL.md':
                    skill_files.append(os.path.join(root, file))
                    
        if not skill_files:
            print(f"No SKILL.md files found in {directory}")
            return
            
        print(f"\nFound {len(skill_files)} skill file(s) to check\n")
        
        all_passed = True
        for skill_file in skill_files:
            self.issues = []
            self.warnings = []
            self.passed = []
            
            passed = self.check_skill_file(skill_file)
            all_passed = all_passed and passed
            
            # Print results
            if self.passed:
                print(f"\n✓ Passed checks:")
                for item in self.passed:
                    print(f"  {item}")
                    
            if self.warnings:
                print(f"\n⚠ Warnings:")
                for item in self.warnings:
                    print(f"  {item}")
                    
            if self.issues:
                print(f"\n✗ Issues:")
                for item in self.issues:
                    print(f"  {item}")
                    
        # Summary
        print(f"\n{'#'*60}")
        print("SUMMARY")
        print(f"{'#'*60}")
        
        if all_passed:
            print("✓ All skills passed compliance checks!")
            return 0
        else:
            print("✗ Some skills have issues that need to be addressed")
            return 1
            
def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        # Default to checking the book-methodology-extractor skills
        target = os.path.expanduser('~/.hermes/skills/knowledge/book-methodology-extractor')
        
    if not os.path.exists(target):
        print(f"Error: Path does not exist: {target}")
        print(f"Usage: {sys.argv[0]} [path]")
        return 1
        
    checker = ComplianceChecker()
    
    if os.path.isfile(target):
        passed = checker.check_skill_file(target)
        return 0 if passed else 1
    else:
        return checker.check_directory(target)
        
if __name__ == '__main__':
    sys.exit(main())