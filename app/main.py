import platform
import time


from flask import jsonify

START_TIME = time.time()


def register_routes(app):
        @app.get("/health")
        def health():
              return jsonify({
                  "status": "healthy",
                  "service": "system-health-api"
               }), 200
        @app.get("/status")
        def status():
            return jsonify({
                 "service": "system-health-api",
                 "python_version": platform.python_version(),
                 "platform": platform.system(),
                 "uptime_seconds": int(time.time() - START_TIME)                                                    }), 200        

