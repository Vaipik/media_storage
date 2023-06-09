from pathlib import Path

from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

from src.config import GDrive
BASE_DIR = Path(__file__).parent


class GoogleDrive:

    def __init__(
            self,
            *,
            settings: GDrive,
            api_version: str = "v3",
    ):
        """
        :param scopes: A list auth scopes to authorize for the application.
        :param key_file_location: The path to a valid service account JSON key file.
        :param api_version: he api version to connect to.
        """
        self.api_version = api_version
        self.settings = settings
        self._api_name = "drive"
        self._service = self._get_service()

    def _get_service(self) -> Resource:
        """Get a service that communicates to a Google API.
        Returns:
            A service that is connected to the specified API.
        """
        # credentials = service_account.Credentials.from_service_account_file(self.key_file_location)  # type: ignore
        credentials = service_account.Credentials.from_service_account_info(self.settings.credentials)
        scoped_credentials = credentials.with_scopes(self.settings.scopes)
        service = build(self._api_name, self.api_version, credentials=scoped_credentials)
        return service

    def get_files(self) -> list | None:
        results = self._service.files().list(
            pageSize=10).execute()

        items = results.get('files')
        if not items:
            print('No files found.')
            return

        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

    def upload_file(self, filename: Path):
        __file = self._service.files()
        file_metadata = {
            "name": filename.name,
            "parents": [self.settings.folder],  # Google Drive folder id
        }

        media = MediaFileUpload(
            filename,
            mimetype=None,
        )
        try:
            __drive_file = __file.create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            return __drive_file.get("id")
        except Exception as err:
            return str(err)
