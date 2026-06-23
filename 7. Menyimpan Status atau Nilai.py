import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def __init__(self):
        super().__init__()
        self.count = 0

    def do_increment(self, line):
        """Increment: Menambah nilai count."""
        self.count += 1
        print(f"Count saat ini: {self.count}")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menyimpan dan memperbarui status (count) di dalam aplikasi.
# Kondisi: Ketika Anda perlu melacak nilai antara perintah.