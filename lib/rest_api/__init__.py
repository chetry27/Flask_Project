from flask import Flask

def create_app():
    
    app = Flask('Bhaskar API')
        
    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"
    
    return app

    
    
    
    