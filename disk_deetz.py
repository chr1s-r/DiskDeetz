import discogs_client
import re

d = discogs_client.Client('DiskDeetz/1.0', user_token='YOUR_TOKEN_HERE')


# Gets URL input from user and prompts for re-entry if invalid.
def validate_url_input():

    is_valid = False
    url = None

    while not is_valid:
        print("-" * 75)
        url = input("Enter Discogs URL: ").strip()

        if not url:
            print('No URL entered. Please try again.')

        is_valid, url_type = is_valid_url(url)

        if url_type == "master":
            print("This is a master release URL. Please use a specific release URL instead.")

        elif url_type == "invalid":
            print("Invalid URL format. Please enter a valid Discogs URL.")

        elif url_type == "other":
            print("This is not a release URL. Please enter a release URL.")

    return url


# Detects URL pattern and returns a boolean to indicate validity, and a label to indicate type of URL
def is_valid_url(url):
    # Pattern for a valid Discogs release URL
    release_pattern = re.compile(
        r'^(https?:\/\/)?(www\.)?discogs\.com\/release\/\d+.*$'
    )

    # Pattern for a Discogs master release URL
    master_pattern = re.compile(
        r'^(https?:\/\/)?(www\.)?discogs\.com\/master\/\d+.*$'
    )

    # Pattern for other (non-release) Discogs URLs
    non_release_pattern = re.compile(
        r'^(https?:\/\/)?(www\.)?discogs\.com\/(?!release\/|master\/)[^\/]+.*$'
    )

    if re.match(release_pattern, url):
        return True, "release"

    if re.match(master_pattern, url):
        return False, "master"

    if re.match(non_release_pattern, url):
        return False, "other"

    return False, "invalid"


# Extracts release number from full URL
def extract_release_number(url):

    pattern = r'release/(\d+)'

    match = re.search(pattern, url)

    if match:
        return match.group(1)
    else:
        return None


def main():

    valid_url = validate_url_input()

    release_number = extract_release_number(valid_url)
    release = d.release(release_number)

    # Currently, retrieved metadata is printed to console to confirm it has been correctly retrieved
    # TODO: enter in to metadata fields in XLD
    print(f"Artist: {release.artists[0].name}")
    print(f"Album: {release.title}")
    print(f"Tracklist: {', '.join([track.title for track in release.tracklist])}")


if __name__ == "__main__":
    main()
