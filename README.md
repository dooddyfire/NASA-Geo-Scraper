# NASA-Geo-Scraper

# ถ้าอยากตั้งให้ script run ตามเวลาที่กำหนดทุกวัน ให้เปลี่ยนไปใช้คำสั่งนี้

เดิม (ตั้งให้รันทุกๆ 10 วินาที)
schedule.every(10).seconds.do(first_file)
schedule.every(20).seconds.do(second_file)

ใหม่ (ตั้งให้รันทุกๆ 10.30 น. ของทุกวัน)

schedule.every().day.at("10:30").do(first_file)
schedule.every().day.at("10:33").do(second_file)
