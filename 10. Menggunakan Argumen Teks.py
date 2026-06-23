import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_echo(self, line):
        """Echo: Mengulangi input yang diberikan."""
        print(line)

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Mengulangi teks yang diberikan pengguna.
# Kondisi: Ketika Anda ingin berinteraksi dan melihat respon langsung.