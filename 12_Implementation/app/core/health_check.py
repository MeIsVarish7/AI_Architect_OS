from pathlib import Path

from app.core.constants import REQUIRED_FOLDERS


class HealthCheck:

    def __init__(self, project_root: Path):
        self.project_root = project_root.parent
        self.required_folders = REQUIRED_FOLDERS

    def run(self):
        print("System Health Check\n")

        healthy = True

        for folder in self.required_folders:
            path = self.project_root / folder

            if path.exists():
                print(f"[✓] {folder}")
            else:
                print(f"[✗] {folder}")
                healthy = False

        print()

        if healthy:
            print("System Status : HEALTHY")
        else:
            print("System Status : ERROR")