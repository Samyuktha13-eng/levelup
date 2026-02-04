from flask import Flask, render_template, request, jsonify, redirect
from roadmap_generator import RoadmapGenerator

app = Flask(__name__)
generator = RoadmapGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roadmap')
def roadmap_page():
    role = request.args.get('role')
    level = request.args.get('level')
    
    if not role or not level:
        return redirect('/')
    
    roadmap = generator.generate_roadmap(role, level)
    if not roadmap:
        return redirect('/')
    
    return render_template('roadmap.html', role=role, level=level, roadmap=roadmap)

@app.route('/api/step-content')
def get_step_content():
    step = request.args.get('step')
    role = request.args.get('role')
    level = request.args.get('level')
    
    # Generate learning links based on role and step
    def get_learning_links(step_title, role):
        # Clean step title for search
        clean_step = step_title.lower().replace('(', '').replace(')', '').replace('&', 'and')
        
        # Role-specific base URLs and search terms
        if 'ui' in role.lower() or 'ux' in role.lower() or 'designer' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/ui-ux-design/"
            w3_search = f"https://www.w3schools.com/"
            youtube_query = f"{step_title} ui ux design tutorial"
        elif 'network' in role.lower() and 'engineer' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/computer-network-tutorials/"
            w3_search = f"https://www.w3schools.com/"
            youtube_query = f"{step_title} networking tutorial"
        elif 'cybersecurity' in role.lower() or 'security' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/cybersecurity/"
            w3_search = f"https://www.w3schools.com/cybersecurity/"
            youtube_query = f"{step_title} cybersecurity tutorial"
        elif 'data' in role.lower() and 'analytics' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/data-science-tutorial/"
            w3_search = f"https://www.w3schools.com/python/pandas/"
            youtube_query = f"{step_title} data analytics tutorial"
        elif 'mobile' in role.lower() or 'app developer' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/android-app-development-fundamentals-for-beginners/"
            w3_search = f"https://www.w3schools.com/"
            youtube_query = f"{step_title} mobile app development tutorial"
        elif 'full-stack' in role.lower() or 'web developer' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/web-development/"
            w3_search = f"https://www.w3schools.com/"
            youtube_query = f"{step_title} web development tutorial"
        elif 'rust' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/rust-programming-language-introduction/"
            w3_search = f"https://doc.rust-lang.org/book/"
            youtube_query = f"{step_title} rust programming tutorial"
        elif 'swift' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/swift-programming-language/"
            w3_search = f"https://developer.apple.com/swift/"
            youtube_query = f"{step_title} swift programming tutorial"
        elif 'kotlin' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/kotlin-programming-language/"
            w3_search = f"https://kotlinlang.org/docs/"
            youtube_query = f"{step_title} kotlin programming tutorial"
        elif 'php' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/php/"
            w3_search = f"https://www.w3schools.com/php/"
            youtube_query = f"{step_title} php tutorial"
        elif 'go' in role.lower() or 'golang' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/go-programming-language-introduction/"
            w3_search = f"https://www.w3schools.com/go/"
            youtube_query = f"{step_title} golang tutorial"
        elif 'typescript' in role.lower() or 'ts' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/typescript/"
            w3_search = f"https://www.w3schools.com/typescript/"
            youtube_query = f"{step_title} typescript tutorial"
        elif 'javascript' in role.lower() or 'js' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/javascript/"
            w3_search = f"https://www.w3schools.com/js/"
            youtube_query = f"{step_title} javascript tutorial"
        elif 'c#' in role.lower() or 'csharp' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/csharp-programming-language/"
            w3_search = f"https://www.w3schools.com/cs/"
            youtube_query = f"{step_title} c# tutorial"
        elif 'c++' in role.lower() or 'cpp' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/c-plus-plus/"
            w3_search = f"https://www.w3schools.com/cpp/"
            youtube_query = f"{step_title} c++ tutorial"
        elif 'java' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/java/"
            w3_search = f"https://www.w3schools.com/java/"
            youtube_query = f"{step_title} java tutorial"
        elif 'python' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"
            w3_search = f"https://www.w3schools.com/python/"
            youtube_query = f"{step_title} python tutorial"
        elif 'data scientist' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/data-science-{clean_step.replace(' ', '-')}/"
            w3_search = f"https://www.w3schools.com/python/pandas/"
            youtube_query = f"{step_title} data science tutorial"
        elif 'devops' in role.lower():
            gfg_search = f"https://www.geeksforgeeks.org/{clean_step.replace(' ', '-')}/"
            w3_search = f"https://www.w3schools.com/"
            youtube_query = f"{step_title} devops tutorial"
        else:
            gfg_search = f"https://www.geeksforgeeks.org/{clean_step.replace(' ', '-')}/"
            w3_search = f"https://www.w3schools.com/"
            youtube_query = f"{step_title} programming tutorial"
        
        youtube_url = f"https://www.youtube.com/results?search_query={youtube_query.replace(' ', '+')}"
        
        return {
            'geeksforgeeks': gfg_search,
            'w3schools': w3_search,
            'youtube': youtube_url
        }
    
    links = get_learning_links(step, role)
    
    # Generate comprehensive content
    content = {
        'overview': f'Master {step} - a crucial skill for {role} at {level} level. This step covers fundamental concepts and practical applications.',
        'key_concepts': [
            'Core theoretical understanding',
            'Practical implementation techniques', 
            'Industry best practices',
            'Real-world applications',
            'Common pitfalls and solutions'
        ],
        'learning_objectives': f'By completing this step, you will understand how to effectively use {step} in professional {role} projects and build confidence in your {level}-level skills.',
        'examples': 'Interactive coding exercises, step-by-step tutorials, hands-on projects, and real-world case studies to reinforce your learning.',
        'resources': [
            'Official documentation and guides',
            'Interactive coding platforms',
            'Community forums and discussions',
            'Professional development courses',
            'Open-source project examples'
        ],
        'links': links
    }
    
    return jsonify({'success': True, 'content': content})

@app.route('/api/roles')
def get_roles():
    return jsonify(generator.get_available_roles())

@app.route('/api/roadmap', methods=['POST'])
def get_roadmap():
    data = request.json
    role = data.get('role')
    level = data.get('level')
    
    roadmap = generator.generate_roadmap(role, level)
    if roadmap:
        return jsonify({
            'success': True,
            'roadmap': roadmap,
            'role': role,
            'level': level
        })
    else:
        return jsonify({'success': False, 'error': 'Invalid role or level'})

if __name__ == '__main__':
    app.run(debug=True)