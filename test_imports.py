try:
    from flask import Flask, render_template, request, jsonify
    print("Flask imports successful")
except ImportError as e:
    print(f"Flask import error: {e}")

try:
    from roadmap_generator import RoadmapGenerator
    print("RoadmapGenerator import successful")
except ImportError as e:
    print(f"RoadmapGenerator import error: {e}")

try:
    app = Flask(__name__)
    generator = RoadmapGenerator()
    print("App initialization successful")
except Exception as e:
    print(f"App initialization error: {e}")