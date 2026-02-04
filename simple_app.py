from flask import Flask, render_template_string, request, jsonify
from roadmap_generator import RoadmapGenerator

app = Flask(__name__)
generator = RoadmapGenerator()

# Embedded HTML template with roles hardcoded
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Learning Roadmap Generator</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .form-group { margin: 20px 0; }
        select, button { padding: 10px; font-size: 16px; width: 200px; }
        button { background: #007bff; color: white; border: none; cursor: pointer; }
        .roadmap { margin-top: 30px; }
        .step { padding: 10px; margin: 10px 0; background: #f8f9fa; border-left: 4px solid #007bff; }
    </style>
</head>
<body>
    <h1>Learning Roadmap Generator</h1>
    
    <div class="form-group">
        <label>Career Role:</label>
        <select id="role">
            <option value="">Choose career...</option>
            <option value="Python Developer">Python Developer</option>
            <option value="Software Developer">Software Developer</option>
            <option value="Data Scientist">Data Scientist</option>
            <option value="DevOps Engineer">DevOps Engineer</option>
        </select>
    </div>
    
    <div class="form-group">
        <label>Skill Level:</label>
        <select id="level">
            <option value="">Choose level...</option>
            <option value="Beginner">Beginner</option>
            <option value="Intermediate">Intermediate</option>
            <option value="Advanced">Advanced</option>
        </select>
    </div>
    
    <button onclick="generateRoadmap()">Generate Roadmap</button>
    
    <div id="roadmap" class="roadmap" style="display:none;">
        <h2 id="title"></h2>
        <div id="steps"></div>
    </div>

    <script>
        function generateRoadmap() {
            const role = document.getElementById('role').value;
            const level = document.getElementById('level').value;
            
            if (!role || !level) {
                alert('Please select both role and level!');
                return;
            }
            
            fetch('/api/roadmap', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ role, level })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById('title').textContent = `${data.role} - ${data.level}`;
                    const stepsDiv = document.getElementById('steps');
                    stepsDiv.innerHTML = '';
                    data.roadmap.forEach((step, i) => {
                        const div = document.createElement('div');
                        div.className = 'step';
                        div.textContent = `${i+1}. ${step}`;
                        stepsDiv.appendChild(div);
                    });
                    document.getElementById('roadmap').style.display = 'block';
                }
            });
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

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
    app.run(debug=True, port=5001)