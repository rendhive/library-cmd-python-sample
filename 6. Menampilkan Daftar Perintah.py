import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_list(self, line):
        """List: Menampilkan daftar perintah yang tersedia."""
        print("Perintah yang tersedia adalah: greet, square, exit")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menampilkan semua perintah yang tersedia dalam aplikasi.
# Kondisi: Ketika Anda ingin menyediakan akses mudah ke daftar perintah untuk pengguna.