import cmd
import json

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_save(self, setting):
        """Save: Menyimpan pengaturan dalam file JSON."""
        with open('settings.json', 'w') as file:
            json.dump({'setting': setting}, file)
            print("Pengaturan disimpan.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menyimpan pengaturan konfigurasi pengguna ke dalam file JSON.
# Kondisi: Ketika Anda ingin menyimpan status atau preferensi pengguna untuk digunakan nanti.