import time

target_time = 180  # seconds

print("เริ่มทอดไข่ดาว")
for second in range(1, target_time + 1):
    print(f"เวลา: {second} วินาที")
    time.sleep(1)

print("ครบเวลา 3 นาที ตรวจสอบความสุกของไข่")