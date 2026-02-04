from flask import Flask, render_template, request, jsonify
from roadmap_generator import RoadmapGenerator

app = Flask(__name__)
generator = RoadmapGenerator()

# Add CORS headers manually
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def index():
    roles = generator.get_available_roles()
    return render_template('index.html', roles=roles)

@app.route('/api/roles', methods=['GET'])
def get_roles():
    try:
        roles = generator.get_available_roles()
        print(f"Available roles: {roles}")
        return jsonify(roles)
    except Exception as e:
        print(f"Error in get_roles: {e}")
        return jsonify([])

@app.route('/api/roadmap', methods=['POST', 'OPTIONS'])
def get_roadmap():
    if request.method == 'OPTIONS':
        return '', 200
        
    try:
        print(f"Request method: {request.method}")
        print(f"Request headers: {dict(request.headers)}")
        
        data = request.get_json(force=True)
        print(f"Request data: {data}")
        
        if not data:
            return jsonify({'success': False, 'error': 'No data received'})
            
        role = data.get('role')
        level = data.get('level')
        
        print(f"Received request - Role: {role}, Level: {level}")
        
        if not role or not level:
            return jsonify({'success': False, 'error': 'Role and level are required'})
        
        roadmap = generator.generate_roadmap(role, level)
        if roadmap:
            response = {
                'success': True,
                'roadmap': roadmap,
                'role': role,
                'level': level
            }
            print(f"Sending response: {len(roadmap)} steps")
            return jsonify(response)
        else:
            return jsonify({'success': False, 'error': 'Invalid role or level'})
    except Exception as e:
        print(f"Error in get_roadmap: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    print("Starting Flask app...")
    print("Available routes:")
    for rule in app.url_map.iter_rules():
        print(f"  {rule.endpoint}: {rule.rule} {list(rule.methods)}")
    app.run(debug=True, host='127.0.0.1', port=5000)