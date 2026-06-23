import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '

    def do_divide(self, line):
        """Divide: Membagi angka."""
        try:
            numerator, denominator = map(int, line.split())
            print(f"Hasil: {numerator / denominator}")
        except ZeroDivisionError:
            print("Kesalahan: Pembagian dengan nol.")
        except ValueError:
            print("Kesalahan: Mohon masukkan dua angka.")

if __name__ == "__main__":
    MyCLI().cmdloop()
# Fungsi: Menangani kesalahan dalam operasi pembagian.
# Kondisi: Ketika Anda ingin memastikan bahwa pengguna tidak dapat memasukkan input yang menyebabkan kesalahan runtime.