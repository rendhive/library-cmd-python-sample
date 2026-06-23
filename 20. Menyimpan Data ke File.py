import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_save(self, filename):
        """Save: Menyimpan beberapa nilai ke file."""
        with open(filename, 'w') as f:
            f.write("Ini adalah data yang disimpan.\n")
        print(f"Data disimpan di {filename}.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menyimpan informasi dari aplikasi ke dalam file.
# Kondisi: Ketika Anda perlu membuat hasil simpanan dari aplikasi ke file untuk diakses di lain waktu.