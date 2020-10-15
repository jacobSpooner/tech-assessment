import pytest
from  flask import Flask

app = Flask(__name__)

@pytest.fixture
def test_client():
    #create test client