"""turtle api."""
from importlib.metadata import version

from flask import Flask
from flask_restx import Api

# Create API instance (main entrypoint)
api = Api(
    title='turtle api',
    # NOTE: read version from package metadata, which is dynamically set in the
    # pyproject.toml file through our release workflow
    version=version('turtle'),  
    description='A RESTful API for turtle',
)

# Add namespaces to the API
# TODO: api.add_namespace(...)


def init_app(app: Flask) -> None:
    """Register the api with the Flask app."""
    # Configure docs url based on settings. We have to do this BEFORE the
    # app is registered with the API so that the API is correctly configured.
    api._doc = app.config.get('API_DOCS_URL', '/docs/')
    api.init_app(app)
