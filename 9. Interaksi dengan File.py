import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_read(self, filename):
        """Read: Membaca dan menampilkan isi file."""
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"File '{filename}' tidak ditemukan.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Membaca dan menampilkan isi dari file yang diberikan.
# Kondisi: Ketika Anda ingin memudahkan pengguna untuk membaca file dari CLI.