from project import run_app, get_text_from_url, exception_message
import pytest


def test_run_app():
    with pytest.raises(TypeError):
        e = "value"
        run_app(e)
    

def test_get_text_from_url():
    returned_text = get_text_from_url("https://pt.wikipedia.org/wiki/Brasil")
    assert "Bandeira do Brasil" in returned_text  
    assert get_text_from_url("not_url") == "Sadly, BAB3L can't access that url. Try another one! 👹"


def test_exception_message():
    with pytest.raises(AttributeError):
        e = "value"
        exception_message(e)
