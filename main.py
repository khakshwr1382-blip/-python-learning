     # برنامه محاسبه مانده حساب و پس‌انداز روزانه - نسخه ۱.۰
name = "رضا"
daily_income = 2000000  # مثلا درآمد فرضی یک روز (تومان)
expenses = [150000, 85000, 200000]  # لیست هزینه‌های روزانه: غذا، رفت‌وآمد و غیره

# محاسبه مجموع هزینه‌ها با تابع توکار sum
total_expense = sum(expenses)
remaining_money = daily_income - total_expense

print(f"سلام {name} عزیز!")
print(f"کل درآمد امروز: {daily_income:,} تومان")
print(f"مجموع هزینه‌ها: {total_expense:,} تومان")
print(f"پس‌انداز خالص امروز: {remaining_money:,} تومان")

# شرط بررسی وضعیت مالی
if remaining_money > 1000000:
    print("وضعیت عالیه! نرخ انباشت سرمایه مثبت است.")
else:
    print("باید هزینه‌ها را کنترل کنی.")
