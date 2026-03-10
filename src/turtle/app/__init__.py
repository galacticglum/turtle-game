"""Entrypoint for the Flask app."""
from typing import Any

from flask import Flask
from werkzeug.debug import DebuggedApplication
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app(settings_override: Any = None) -> Flask:
    """Create a new Flask app.

    Args:
        settings_override: A map-like object that can be passed to the 
            :func:`app.config.update` function.

    Returns:
        A Flask application
    """
    app = Flask(__name__)
    app.config.from_object('config.app_settings')
    if settings_override:
        app.config.update(settings_override)

    init_middleware(app)

    # Register extensions with the app
    from turtle.app.extensions.db import db
    db.init_app(app)

    # Register api with the app
    import turtle.app.api as api
    api.init_app(app)

    # Register blueprints
    from turtle.app import blueprints
    blueprints.register(app)

    return app


def init_middleware(app: Flask) -> None:
    """Register 0 or more middleware (mutates the app passed in).

    Args:
        app: A Flask application instance.
    """
    # Enable the Flask interactive debugger in the browser for development.
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    # Set the real IP address into request.remote_addr when behind a proxy.
    app.wsgi_app = ProxyFix(app.wsgi_app)
    return None