import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_read_multiple(self, files):
        """Read Multiple: Membaca isi beberapa file."""
        for filename in files.split(','):
            try:
                with open(filename.strip(), 'r') as f:
                    print(f"Isi {filename}:\n{f.read()}")
            except FileNotFoundError:
                print(f"File '{filename}' tidak ditemukan.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Membaca isi beberapa file yang diberikan secara bersamaan.
# Kondisi: Ketika Anda ingin memudahkan pengguna untuk membaca beberapa file dengan sekali perintah.