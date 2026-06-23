import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_version(self, line):
        """Version: Menampilkan versi aplikasi."""
        print("Aplikasi CLI versi 1.0")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menampilkan informasi versi untuk aplikasi.
# Kondisi: Ketika Anda ingin memberikan informasi pemeliharaan kepada pengguna.