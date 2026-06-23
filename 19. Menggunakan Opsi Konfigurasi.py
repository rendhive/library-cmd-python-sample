import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def __init__(self):
        super().__init__()
        self.config = {'verbose': False}

    def do_set_verbose(self, line):
        """Set Verbose: Mengaktifkan atau menonaktifkan mode verbose."""
        if line.lower() in ['true', 'yes']:
            self.config['verbose'] = True
            print("Mode verbose diaktifkan.")
        elif line.lower() in ['false', 'no']:
            self.config['verbose'] = False
            print("Mode verbose dinonaktifkan.")
        else:
            print("Masukkan 'true' atau 'false'.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Mengatur opsi konfigurasi untuk mode verbose.
# Kondisi: Ketika Anda ingin memberikan opsi kustomisasi kepada pengguna.