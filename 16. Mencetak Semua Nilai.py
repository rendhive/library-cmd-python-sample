import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def __init__(self):
        super().__init__()
        self.values = []

    def do_list(self, line):
        """List: Menampilkan semua nilai dalam kumpulan."""
        print("Daftar nilai:", self.values)

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menampilkan semua nilai dalam kumpulan saat diminta.
# Kondisi: Ketika Anda ingin melihat data terkait saat ini.