#import flask - from the package import a module
from flask import Flask 
from flask_bootstrap import Bootstrap

#create a function that creates a web application
# a web server will run this web application
def create_app():
    print(__name__)  #let us be curious - what is this __name__ 
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.secret_key='anythingyoulike'
    bootstrap = Bootstrap(app)
    from . import views
    app.register_blueprint(views.mainbp)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import destinations
    app.register_blueprint(destinations.bp)

    return app
