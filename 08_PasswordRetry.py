# Password မှန်တဲ့အထိ ထပ်ထည့်ခိုင်းမယ်
password = ""
attempt = 0

while password != "abc123":
    password = input("Password ထည့်ပါ: ")
    attempt += 1

print(f"မှန်ပါပြီ။ (တစ်ကြိမ် {attempt} ကြိမ် သွင်းခဲ့တယ်)")
