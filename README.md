# DiskDeetz

**DiskDeetz** is a Python script that automates the entry of CD metadata when ripping CDs using XLD (X Lossless Decoder) for Mac OS X.

While XLD uses databases FreeDB and MusicBrainz to provide metadata for CDs, there are still CDs that do not appear in these databases.
In many cases, these CDs and their metadata are available at Discogs.com.

For these CDs, DiskDeetz automates the entry of metadata by retrieving metadata from Discogs.com and automatically filling out metadata fields in XLD.

## Installation

1. Clone the repository (double check):
   ```bash
   git clone https://github.com/yourusername/DiskDeetz.git cd DiskDeetz
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv source venv/bin/activate # On macOS/Linux venv\Scripts\activate # On Windows
   ```
3. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
4. Obtain a user token to access the Discogs API
    - Sign in to your Discogs account. If you don't have one, you can create an account [here](https://login.discogs.com/u/signup?state=hKFo2SBBb0lTM01tNWVzaW5wekY1SmJMZE1GU0ZQXzB6Vmc3TKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIE02Z09oSjloQ3M1YmtXeXRkTmRXVW0xYmp2LWw2aHVno2NpZNkgMDg2SDEyQklDVzFiZnRlMVUwQ056NmV4UVFtSk56SGg).
    - Once logged in, navigate to Settings, then to Developer. [Here](https://www.discogs.com/settings/developers) is a direct link.
    - Click Generate New Token and then copy the generated token.
5. Configure the script
    - Open the disk_deetz.py file.
    - Locate the following line:
      ```bash
      d = discogs_client.Client('DiskDeetz/1.0', user_token='YOUR_TOKEN_HERE')
      ```
    - Replace 'YOUR_TOKEN_HERE' with your token.

## Usage

1. Run the script with:
   ```bash
   python disk_deetz.py
   ```
2. When prompted, enter the URL of the Discogs page of the release

## Running Tests

Run the tests with:
   ```bash
   python -m pytest tests/test_disk_deetz.py
   ```
## Dependencies

 * `discogs-client`
 * `pytest`

## License

This project is licensed under the MIT License.