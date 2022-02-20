from flask import Flask
from rest_api import create_app

app = create_app()


if __name__ == "__main__":
    """main method
        
    """
    Flask.run(app, threaded=True, debug=True, port=2030)
    
    