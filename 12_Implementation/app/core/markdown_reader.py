from pathlib import Path


class MarkdownReader:

    def __init__(self, project_root: Path):
        self.project_root = project_root

    def read(self, relative_path: str) -> str:
        file_path = self.project_root / relative_path

        if not file_path.exists():
            raise FileNotFoundError(f"{relative_path} not found.")

        return file_path.read_text(encoding="utf-8")