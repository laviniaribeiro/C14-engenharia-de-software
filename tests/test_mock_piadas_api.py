from unittest.mock import patch, Mock
import pytest
import piadas_api

@pytest.mark.parametrize("joke_text", [f"Chuck joke {i}" for i in range(1, 21)])
def test_fetch_random_joke_success(joke_text):
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"value": joke_text}
    mock_resp.raise_for_status = Mock()

    with patch("piadas_api.requests.get", return_value=mock_resp) as mocked_get:
        result = piadas_api.fetch_random_joke()
        assert result == joke_text
        mocked_get.assert_called_once_with(piadas_api.API_URL, timeout=5)

def test_fetch_random_joke_http_error():
    mock_resp = Mock()
    mock_resp.raise_for_status.side_effect = Exception("HTTP error")
    with patch("piadas_api.requests.get", return_value=mock_resp):
        with pytest.raises(Exception):
            piadas_api.fetch_random_joke()
