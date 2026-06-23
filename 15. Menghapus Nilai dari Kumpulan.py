import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def __init__(self):
        super().__init__()
        self.values = []

    def do_remove(self, value):
        """Remove: Menghapus nilai dari kumpulan."""
        if value in self.values:
            self.values.remove(value)
            print(f"Nilai {value} dihapus.")
        else:
            print(f"Nilai {value} tidak ditemukan.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menghapus nilai dari daftar berdasarkan masukan pengguna.
# Kondisi: Ketika Anda ingin memungkinkan pengguna mengelola kumpulan data secara interaktif.