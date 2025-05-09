import time
import pandas as pd
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def lay_thong_tin_chi_tiet(driver, url):
    """Truy cập trang chi tiết để lấy mô tả và diện tích"""
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    time.sleep(3)

    try:
        mo_ta = driver.find_element(By.CSS_SELECTOR, ".detail.text-content").text.strip()
    except:
        mo_ta = "Không có thông tin"

    try:
        div_dientich = driver.find_element(By.CLASS_NAME, "ct_dt")
        dien_tich = div_dientich.text.replace("Diện tích:", "").strip()
    except:
        dien_tich = "Không có thông tin"

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return mo_ta, dien_tich

def lay_du_lieu(trang_bat_dau=1, trang_ket_thuc=1):
    """Hàm chính để thu thập dữ liệu"""
    driver = webdriver.Chrome()
    du_lieu = []

    for trang in range(trang_bat_dau, trang_ket_thuc + 1):
        print(f" Đang lấy dữ liệu trang {trang}")
        url = f"https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/3/da-nang/trang--{trang}.html"
        driver.get(url)

        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "content-item")))

        except:
            print(f" Trang {trang} không tải được.")
            continue

        tin_dang = driver.find_elements(By.CLASS_NAME, "content-item")

        for tin in tin_dang:
            try:
                tieu_de_el = tin.find_element(By.CSS_SELECTOR, ".ct_title a")
                tieu_de = tieu_de_el.text.strip()
                link = tieu_de_el.get_attribute("href")

                gia = tin.find_element(By.CLASS_NAME, "ct_price").text.replace("Giá:", "").strip() \
                    if tin.find_elements(By.CLASS_NAME, "ct_price") else "Không có thông tin"
                dia_chi = tin.find_element(By.CLASS_NAME, "ct_dis").text.strip() \
                    if tin.find_elements(By.CLASS_NAME, "ct_dis") else "Không có thông tin"

                mo_ta, dien_tich = lay_thong_tin_chi_tiet(driver, link)

                du_lieu.append({
                    "tieu_de": tieu_de,
                    "gia": gia,
                    "dia_chi": dia_chi,
                    "dien_tich": dien_tich,
                    "mo_ta": mo_ta
                })

                print(f" {tieu_de} | Giá: {gia} | DT: {dien_tich} | Địa chỉ: {dia_chi}")

            except Exception as e:
                print(f" Lỗi khi xử lý tin đăng: {e}")

    # Đóng trình duyệt
    driver.quit()

    # Lưu vào file Excel
    df = pd.DataFrame(du_lieu)  
    df.to_excel("BTL.xlsx", index=False)  
    print("Lưu thành công vào BTL.xlsx")

    return du_lieu



def thu_thap_va_luu():
    du_lieu = lay_du_lieu(trang_bat_dau=1, trang_ket_thuc=1)
    print(f"Đã thu thập và lưu {len(du_lieu)} tin đăng.")

if __name__ == "__main__":
    schedule.every().day.at("13:50").do(thu_thap_va_luu)
    print(" Đã lên lịch chạy lúc 6:00 sáng mỗi ngày.")

    while True:
        schedule.run_pending()
        time.sleep(60)
