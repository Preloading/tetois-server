# Version v0.0.1 (beta-3.5)
import signal
from flask import Flask
import config
from waitress import serve
import homepage

# init
app = Flask(__name__)

# # register seperate paths
app.register_blueprint(homepage.homepage)
# app.register_blueprint(playlist)
# app.register_blueprint(video)
# app.register_blueprint(channel)
# if config.CLIENT_TEST:
#     app.register_blueprint(client_videos)


# Catch sigterm for docker
def catch_docker_stop(*args):
    exit()

# config
if __name__ == "__main__":
    signal.signal(signal.SIGTERM, catch_docker_stop)
    if config.DEBUG:
        app.run(port=config.PORT, host="0.0.0.0", debug=True)
    else:
        serve(app, port=config.PORT, host="0.0.0.0")