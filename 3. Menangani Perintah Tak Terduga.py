import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_add(self, line):
        print(f"Menambahkan: {line}")

    def default(self, line):
        print(f"Perintah '{line}' tidak dikenali.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menangani perintah yang tidak terduga dengan metode default.
# Kondisi: Ketika Anda ingin memberikan umpan balik untuk input yang tidak valid.