import random
from typing import Dict, List

class LocalAIGenerator:
    def __init__(self):
        self.templates = {
            'overview': [
                "Learn the fundamentals of {topic} and understand its core concepts",
                "Master {topic} through practical examples and hands-on exercises", 
                "Explore {topic} and its real-world applications in programming"
            ],
            'concepts': {
                'python basics': ['Syntax', 'Variables', 'Data types', 'Control structures'],
                'functions': ['Function definition', 'Parameters', 'Return values', 'Scope'],
                'oop': ['Classes', 'Objects', 'Inheritance', 'Polymorphism'],
                'default': ['Core concepts', 'Best practices', 'Common patterns', 'Error handling']
            },
            'examples': [
                "Interactive coding exercises with step-by-step guidance",
                "Real-world projects and practical implementations",
                "Code examples with detailed explanations and comments"
            ]
        }
    
    def generate_content(self, step_title: str, role: str, level: str) -> Dict:
        topic = step_title.lower()
        
        # Generate overview
        overview_template = random.choice(self.templates['overview'])
        overview = overview_template.format(topic=step_title)
        
        # Generate key concepts
        concepts = self._get_concepts(topic)
        
        # Generate examples
        examples = random.choice(self.templates['examples'])
        
        # Generate resources
        resources = [
            f"Official {role} documentation",
            f"{level} level tutorials",
            "Interactive coding platforms",
            "Community forums and discussions"
        ]
        
        return {
            'overview': overview,
            'key_concepts': concepts,
            'practical_examples': examples,
            'resources': resources,
            'youtube_search': f"{step_title} {role} {level} tutorial"
        }
    
    def _get_concepts(self, topic: str) -> List[str]:
        for key in self.templates['concepts']:
            if key in topic:
                return self.templates['concepts'][key]
        return self.templates['concepts']['default']