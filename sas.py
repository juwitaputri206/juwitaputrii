from datetime import datetime

# Kelas Reminder untuk menyimpan informasi pengingat
class Reminder:
    def __init__(self, title: str, description: str, reminder_time: datetime):
        self.title = title
        self.description = description
        self.reminder_time = reminder_time

    def __str__(self):
        return (f"Reminder: {self.title}\n"
                f"Description: {self.description}\n"
                f"Time: {self.reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Kelas ReminderManager untuk mengelola daftar pengingat
class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, reminder: Reminder):
        self.reminders.append(reminder)
        print(f"Reminder '{reminder.title}' berhasil ditambahkan.")

    def list_reminders(self):
        if not self.reminders:
            print("Tidak ada pengingat.")
        else:
            print("Daftar Pengingat:")
            for i, reminder in enumerate(self.reminders, start=1):
                print(f"{i}. {reminder}")

    def remove_reminder(self, index: int):
        if 0 <= index < len(self.reminders):
            removed = self.reminders.pop(index)
            print(f"Reminder '{removed.title}' berhasil dihapus.")
        else:
            print("Indeks tidak valid!")

    def check_reminders(self):
        now = datetime.now()
        due_reminders = [r for r in self.reminders if r.reminder_time <= now]

        if due_reminders:
            print("Pengingat yang sudah jatuh tempo:")
            for reminder in due_reminders:
                print(reminder)
            self.reminders = [r for r in self.reminders if r.reminder_time > now]
        else:
            print("Tidak ada pengingat yang jatuh tempo.")

# Fungsi untuk memastikan input waktu benar
def input_datetime(prompt):
    while True:
        time_str = input(prompt)
        try:
            # Coba parsing waktu
            return datetime.strptime(time_str, '%Y-%m-%d %H:%M')
        except ValueError:
            print("Format waktu tidak valid. Harap gunakan format: YYYY-MM-DD HH:MM.")
            print("Contoh: 2024-12-08 14:30")

# Fungsi utama
def main():
    manager = ReminderManager()

    while True:
        print("\nMenu:")
        print("1. Tambah pengingat")
        print("2. Lihat daftar pengingat")
        print("3. Hapus pengingat")
        print("4. Cek pengingat jatuh tempo")
        print("5. Keluar")

        try:
            choice = int(input("Pilih menu (1-5): "))
            if choice == 1:
                title = input("Judul pengingat: ")
                description = input("Deskripsi pengingat: ")
                reminder_time = input_datetime("Waktu pengingat (YYYY-MM-DD HH:MM): ")

                reminder = Reminder(title, description, reminder_time)
                manager.add_reminder(reminder)

            elif choice == 2:
                manager.list_reminders()

            elif choice == 3:
                manager.list_reminders()
                index = int(input("Masukkan nomor pengingat yang ingin dihapus: ")) - 1
                manager.remove_reminder(index)

            elif choice == 4:
                manager.check_reminders()

            elif choice == 5:
                print("Terima kasih telah menggunakan aplikasi pengingat!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan angka sesuai menu.")

if __name__ == "__main__":
    main()
