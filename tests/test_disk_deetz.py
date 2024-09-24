import pytest
from disk_deetz import is_valid_url


# Parametrized test for various URLs
@pytest.mark.parametrize("url, expected_valid, expected_type", [
    ("https://www.discogs.com/release/1692870-David-Bowie-Station-To-Station", True, "release"),  # Valid release URL
    ("discogs.com/release/1751997-Terje-Rypdal-After-The-Rain", True, "release"),  # Valid but abbreviated URL
    ("https://www.discogs.com/release/8153435", True, "release"),  # Valid but abbreviated URL
    ("https://www.discogs.com/release/23025515-宇多田ヒカル-Badモード", True, "release"),  # Special characters
    ("https://www.discogs.com/release/999998-Some-Album", True, "release"),  # Valid URL but non-existent album
    ("https://www.discogs.com/master/2994-Kraftwerk-Autobahn", False, "master"),  # Master instead of release URL
    ("https://www.discogs.com/settings/developers", False, "other"),  # Other Discogs page, not release or master page
    ("2907576", False, "invalid"),  # Release ID only, not a valid URL
    (1234, False, "invalid"),  # Integer, not string
    ("invalid-url", False, "invalid"),  # String that is not a URL
    ("", False, "invalid"),  # Empty string
    ("   ", False, "invalid"),  # White space string
    (None, False, "invalid"),  # Null value
    (True, False, "invalid")  # Boolean value
])
def test_is_valid_url(url, expected_valid, expected_type):
    if isinstance(url, str):
        is_valid, url_type = is_valid_url(url)
        assert is_valid == expected_valid
        assert url_type == expected_type
    else:
        with pytest.raises(TypeError):
            is_valid_url(url)


