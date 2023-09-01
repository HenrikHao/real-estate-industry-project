import zipfile, urllib.request, shutil
import contextlib
import os

''' https://abs.gov.au/census/find-census-data/datapacks/download/2021_GCP_all_for_VIC_short-header.zip'''
import urllib.request
import shutil
import zipfile
import contextlib
import os

def download_and_extract_zip(url, destination_folder, zip_file_name=None):
    """
    Download and extract a ZIP file from a given URL to a specified destination folder.

    Args:
    - url (str): The URL of the ZIP file to be downloaded.
    - destination_folder (str): The folder where the ZIP contents should be extracted.
    - zip_file_name (str, optional): The name of the temporary ZIP file. If not provided, the name will be inferred from the URL.

    Returns:
    None
    """

    # If no file name is provided, infer from the URL.
    if zip_file_name is None:
        zip_file_name = url.split('/')[-1]
    
    print("Starting download...")

    with urllib.request.urlopen(url) as response, open(zip_file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        with zipfile.ZipFile(zip_file_name) as zf:
            zf.extractall(destination_folder)

    # Remove the zip file from the directory
    with contextlib.suppress(FileNotFoundError):
        os.remove(zip_file_name)

    print('Download complete.')

# Example usage:
# url = 'https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip'
# download_and_extract_zip(url, '../data/Statistical_area_level2')
