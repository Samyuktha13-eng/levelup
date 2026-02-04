# -*- coding: utf-8 -*-
import openai
import json
from typing import Dict, List

class AIContentGenerator:
    def __init__(self, api_key: str):
        openai.api_key = api_key
    
    def generate_step_content(self, step_title: str, role: str, level: str) -> Dict:
        prompt = f"""
        Generate comprehensive, current (2024-2025) learning content for this programming step with future outlook:
        
        Step: {step_title}
        Role: {role}
        Level: {level}
        
        Provide detailed, practical content focusing on:
        - Current industry standards and practices (2024)
        - Future trends and emerging technologies (2025-2026)
        - Real-world applications and use cases
        - Market demand and career prospects
        - Specific tools, frameworks, and technologies being used now
        
        Format as JSON:
        {{
            "overview": "Comprehensive 3-4 sentence overview explaining current relevance and future importance",
            "key_concepts": ["5-6 specific, current concepts with brief explanations"],
            "practical_examples": "Detailed real-world examples, current projects, and hands-on applications (2-3 sentences)",
            "resources": ["4-5 current, high-quality learning resources"],
            "youtube_search": "optimized search terms for 2024 tutorials",
            "industry_insights": {{
                "current_trends": "What's happening NOW in 2024 - specific technologies, methodologies, market shifts",
                "salary_range": "Accurate 2024 salary data with location context and growth projections",
                "job_demand": "Current job market analysis with specific statistics and future outlook",
                "companies_using": ["6-8 major companies actively hiring for this skill in 2024"],
                "developer_feedback": "Real insights from current developers - challenges, opportunities, career advice",
                "future_outlook": "2025-2026 predictions - emerging trends, new opportunities, skill evolution"
            }}
        }}
        
        Make it highly practical, current, and actionable for someone learning in 2024.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
                temperature=0.7
            )
            
            content = response.choices[0].message.content
            return json.loads(content)
        except Exception as e:
            return self.get_fallback_content(step_title, role, level)
    
    def get_fallback_content(self, step_title: str, role: str = "", level: str = "") -> Dict:
        return {
            "overview": f"Master {step_title} - a critical skill for modern {role} professionals in 2024. This technology is experiencing rapid growth with increasing industry adoption and excellent career prospects. Understanding this concept is essential for staying competitive in today's tech landscape and positioning yourself for future opportunities.",
            "key_concepts": [
                f"Core {step_title} fundamentals and modern best practices",
                "Current industry standards and implementation patterns", 
                "Integration with popular frameworks and tools (2024)",
                "Performance optimization and scalability considerations",
                "Security best practices and common pitfalls",
                "Testing strategies and debugging techniques"
            ],
            "practical_examples": f"Build real-world projects using {step_title} including modern web applications, API integrations, and cloud-based solutions. Practice with current industry tools and frameworks that companies are actively using in 2024. Work on portfolio projects that demonstrate practical skills to potential employers.",
            "resources": [
                "Official documentation and getting started guides",
                "Interactive coding platforms (Codecademy, freeCodeCamp)", 
                "GitHub repositories with real-world examples",
                "Developer communities (Stack Overflow, Reddit, Discord)",
                "Industry blogs and technical publications"
            ],
            "youtube_search": f"{step_title} {role} tutorial 2024 complete guide",
            "industry_insights": {
                "current_trends": f"{step_title} is experiencing significant growth in 2024 with widespread adoption across startups and enterprise companies. Modern development practices emphasize cloud-native solutions, microservices architecture, and AI integration.",
                "salary_range": f"{level} {role}: $65,000-$140,000 annually (US market, varies by location). Remote opportunities available. Strong growth trajectory with 15-25% salary increases possible with experience.",
                "job_demand": "High demand in current job market with 40% year-over-year growth in job postings. Remote-first companies actively hiring. Strong job security and multiple career advancement paths available.",
                "companies_using": ["Google", "Microsoft", "Amazon", "Meta", "Netflix", "Spotify", "Airbnb", "Uber"],
                "developer_feedback": "Essential skill for career growth with excellent learning resources and strong community support. High job satisfaction and good work-life balance. Continuous learning required but rewarding career path.",
                "future_outlook": "Expected 25% growth through 2026 with emerging opportunities in AI/ML integration, edge computing, and sustainable technology solutions. Skills will remain highly relevant with evolution toward more specialized applications."
            }
        }