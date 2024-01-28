from pathlib import Path
from typing import Literal
from zipfile import ZipFile

PATH_SUFFIX = '.zip'


class ZipFileManager:
    def __init__(self, filename: str):
        self.path = Path(filename)

    def compress(self):
        with self._get_zipfile_with_mode('w') as zip_archive:
            zip_archive.write(self.path)

    def decompress(self, extract_at: str = None):
        extract_at_path = None
        if extract_at:
            extract_at_path = Path(extract_at)
            if extract_at_path.is_file():
                raise ValueError("El valor de extract_at debe ser un directorio, no un archivo.")

        with self._get_zipfile_with_mode('r') as zip_archive:
            zip_archive.extractall(extract_at_path)

    def _get_path_with_suffix(self) -> Path:
        return self.path.with_suffix(PATH_SUFFIX)

    def _get_zipfile_with_mode(self, mode: Literal["r", "w", "x", "a"]) -> ZipFile:
        return ZipFile(self._get_path_with_suffix(), mode=mode)
