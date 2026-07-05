class OSContext:

    def __init__(self, kernel):
        self.kernel = kernel

    def get_north_star(self):

        return self.kernel["01_Kernel/00_North_Star.md"]

    def get_kernel(self):

        return self.kernel["01_Kernel/02_Kernel.md"]