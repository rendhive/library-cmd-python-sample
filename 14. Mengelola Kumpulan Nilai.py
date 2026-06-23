import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def __init__(self):
        super().__init__()
        self.values = []

    def do_add(self, value):
        """Add: Menambah nilai ke dalam kumpulan."""
        self.values.append(value)
        print(f"Nilai {value} ditambahkan.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menambahkan nilai baru ke dalam daftar.
# Kondisi: Ketika Anda ingin memperbarui data secara dinamis berdasarkan masukan pengguna.