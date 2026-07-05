from app.core.markdown_reader import MarkdownReader


class ContextEngine:

    KERNEL_FILES = [
        "01_Kernel/00_North_Star.md",
        "01_Kernel/01_Principles.md",
        "01_Kernel/02_Kernel.md",
        "01_Kernel/03_Rule_of_Three.md",
        "01_Kernel/04_Skill_Dependency_Graph.md",
        "01_Kernel/05_AI_Manager.md",
        "01_Kernel/06_Context_Engine.md",
        "01_Kernel/07_Session_Workflow.md",
        "01_Kernel/08_State_Management.md",
        "01_Kernel/09_Session_Templates.md",
        "01_Kernel/10_Dynamic_Prompt_Generator.md",
        "01_Kernel/11_Runtime_Engine.md",
        "01_Kernel/12_OS_Controller.md",
        "01_Kernel/13_Current_Runtime.md",
    ]

    def __init__(self, project_root):
        self.reader = MarkdownReader(project_root)

    def load_kernel(self):

        print("\nLoading Kernel...\n")

        kernel = {}

        for file in self.KERNEL_FILES:

            kernel[file] = self.reader.read(file)

            print(f"[✓] {file}")

        return kernel