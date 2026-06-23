import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def __init__(self):
        super().__init__()
        self.values = []

    def do_clear(self, line):
        """Clear: Menghapus semua nilai dalam kumpulan."""
        self.values.clear()
        print("Kumpulan nilai telah dihapus.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menghapus semua nilai dari kumpulan saat diminta.
# Kondisi: Ketika Anda perlu memulai ulang data tanpa mematikan aplikasi.