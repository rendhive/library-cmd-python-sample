import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_square(self, line):
        """Square a number: Menghitung kuadrat angka."""
        try:
            number = float(line)
            print(f"Kuadrat dari {number} adalah {number ** 2}")
        except ValueError:
            print("Silakan masukkan angka yang valid.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menghitung kuadrat dari angka yang diberikan oleh pengguna.
# Kondisi: Ketika Anda ingin melakukan operasi matematis pada input pengguna.