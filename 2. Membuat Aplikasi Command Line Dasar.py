import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_hello(self, line):
        print(f"Halo, {line}!")

    def do_exit(self, line):
        print("Keluar dari program.")
        return True

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Membuat CLI dasar dengan dua perintah: hello dan exit.
# Kondisi: Ketika Anda ingin membuat aplikasi yang memberikan umpan balik interaktif.