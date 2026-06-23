import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_set_prompt(self, prompt):
        """Set Prompt: Mengubah prompt CLI."""
        self.prompt = f'({prompt}) '
        print(f"Prompt diubah menjadi: {self.prompt}")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Mengubah prompt command line interaktif.
# Kondisi: Ketika Anda ingin menyesuaikan antarmuka pengguna untuk memberikan konteks lebih lanjut.