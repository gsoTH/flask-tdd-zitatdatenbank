import pytest
from precision_box import create_app                    # Verweis auf Factory-Pattern unserer App
import sqlite3


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    
    #yield app.test_client()                            # Unterschied zu return unklar
    return app.test_client()


