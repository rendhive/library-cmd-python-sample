import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_greet(self, line):
        """Greet NAME: Menyapa pengguna dengan namanya."""
        print(f"Halo, {line}!")

    def do_exit(self, line):
        """Exit: Keluar dari aplikasi."""
        print("Keluar dari program.")
        return True

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Membuat perintah dengan penjelasan bantuan ketika pengguna meminta bantuan.
# Kondisi: Ketika Anda ingin memberikan dokumentasi interaktif kepada pengguna.