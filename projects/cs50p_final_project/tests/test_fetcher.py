import pytest
import requests
from unittest.mock import patch, Mock
from fetcher import Fetcher, FetchError


def test_invalid_url():
    with pytest.raises(ValueError):
        Fetcher("cat")


def test_valid_url():
    Fetcher("https://example.com")


def test_fetch_returns_response():
    with patch("fetcher.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.raise_for_status = Mock()
        fetcher = Fetcher("https://example.com")
        response = fetcher.fetch()
        assert response is not None


def test_fetch_caches_response():
    with patch("fetcher.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.raise_for_status = Mock()
        fetcher = Fetcher("https://example.com")
        fetcher.fetch()
        fetcher.fetch()
        assert mock_get.call_count == 1


def test_fetch_raises_on_failure():
    with patch("fetcher.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("failed")
        fetcher = Fetcher("https://example.com")
        with pytest.raises(FetchError):
            fetcher.fetch()


def test_title_returns_page_title():
    with patch("fetcher.requests.get") as mock_get:
        mock_get.return_value.raise_for_status = Mock()
        mock_get.return_value.text = "<html><title>Example</title></html>"
        fetcher = Fetcher("https://example.com")
        assert fetcher.title == "Example"
