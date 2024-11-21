class TodoList:
    # این کلاس نمایانگر یک لیست کارهاست
    def __init__(self):
        # سازنده، که یک لیست خالی برای ذخیره کارها ایجاد می‌کند
        self.tasks = []

    def add_task(self, task):
        # متدی برای اضافه کردن کار به لیست
        self.tasks.append(task)  # کار جدید به لیست اضافه می‌شود
        print(f'Task "{task}" added.')  # پیغام تأیید اضافه کردن کار

    def view_tasks(self):
        # متدی برای نمایش کارهای موجود در لیست
        if not self.tasks:
            print("No tasks in the list.")  # اگر لیست خالی باشد
        else:
            print("To-Do List:")  # نمایش عنوان لیست
            for index, task in enumerate(self.tasks, start=1):
                # نمایش هر کار با شماره آن
                print(f"{index}. {task}")

    def remove_task(self, task_number):
        # متدی برای حذف کار از لیست بر اساس شماره آن
        if 0 < task_number <= len(self.tasks):
            # اگر شماره کار معتبر باشد
            removed_task = self.tasks.pop(task_number - 1)  # کار حذف می‌شود
            print(f'Task "{removed_task}" removed.')  # پیغام تأیید حذف کار
        else:
            print("Invalid task number.")  # اگر شماره کار نامعتبر باشد

def main():
    # تابع اصلی برنامه
    todo_list = TodoList()  # ایجاد یک نمونه از کلاس TodoList
    
    while True:
        # حلقه بی‌پایان برای نمایش منو
        print("\nOptions:")
        print("1. Add task")  # گزینه برای اضافه کردن کار
        print("2. View tasks")  # گزینه برای مشاهده کارها
        print("3. Remove task")  # گزینه برای حذف کار
        print("4. Exit")  # گزینه برای خروج

        choice = input("Choose an option (1-4): ")  # دریافت ورودی از کاربر

        if choice == '1':
            # اگر کاربر گزینه 1 را انتخاب کند
            task = input("Enter the task: ")  # دریافت نام کار از کاربر
            todo_list.add_task(task)  # اضافه کردن کار
        elif choice == '2':
            # اگر کاربر گزینه 2 را انتخاب کند
            todo_list.view_tasks()  # نمایش کارها
        elif choice == '3':
            # اگر کاربر گزینه 3 را انتخاب کند
            task_number = int(input("Enter the task number to remove: "))  # دریافت شماره کار
            todo_list.remove_task(task_number)  # حذف کار
        elif choice == '4':
            # اگر کاربر گزینه 4 را انتخاب کند
            print("Exiting the To-Do List application.")  # پیغام خروج
            break  # خروج از حلقه
        else:
            print("Invalid choice. Please try again.")  # اگر انتخاب نامعتبر باشد

if __name__ == "__main__":
    main()  # فراخوانی تابع اصلی