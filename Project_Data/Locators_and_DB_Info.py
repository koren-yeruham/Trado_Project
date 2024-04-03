from selenium.webdriver.common.by import By



"Login Locators"
site_url = "http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/"
input_phone_field = (By.CSS_SELECTOR, "div.login_login div.login_panel form.form_form div.form_items div.form_formItem.undefined.undefined.formItem_phone div.phoneInput_phoneInputContainer:nth-child(2) div.react-tel-input > input.form-control")
submit_btn = (By.CSS_SELECTOR, "div.login_login div.login_panel span:nth-child(2) form.form_form > input.form_submitBtn")
code_submit = (By.CSS_SELECTOR, "div.login_login div.login_panel form.form_form div.form_items div.form_formItem.undefined.undefined.formItem_code:nth-child(1) span.input_input:nth-child(2) div.input_relative > input:nth-child(1)")
login_button = (By.CSS_SELECTOR, "div.login_login div.login_panel span:nth-child(2) form.form_form > input.form_submitBtn")
trado_button = (By.CSS_SELECTOR, "div.login_login div.login_panel div.storesList_storesList:nth-child(2) div.storesList_list:nth-child(2) > div.storesList_store:nth-child(1)")


"Dashboard Locators"
dashboard_orders_btn = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/a[1]")



"Products Locators"
products_tab = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[2]")
products_kebab = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[1]/span[1]/i[1]")

products_1st_tab = (By.XPATH, "//tbody/tr[1]")
products_1st_price = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[5]/span[1]/div[1]/input[1]")
products_1st_next = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[4]/input[1]")

products_1st_tab_price = (By.XPATH, "//tbody/tr[1]/td[5]")
products_1st_tab_name = (By.XPATH, "//tbody/tr[1]/td[1]")
products_1st_tab_MKT = (By.XPATH, "//tbody/tr[1]/td[3]")

products_add_user = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]")
products_add_MKT = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[3]/span[1]/div[1]/input[1]")
products_add_name = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[1]/span[1]/div[1]/input[1]")
products_add_price = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[5]/span[1]/div[1]/input[1]")
products_add_submit_btn = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[4]/input[1]")
products_add_submit_btn2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[4]/input[2]")
products_add_supercategory = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[2]/div[1]/span[1]/div[1]/input[1]")
products_add_store = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[6]/div[1]/span[1]/div[1]/input[1]")
products_add_country = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[9]/div[1]/span[1]/div[1]/input[1]")


"DB connection info"
username = "qa_agency"
password = "!5szveK7$TE$93u"
database_name = "trado_qa"

"Orders Locators"
orders_tab = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/nav/div[2]/a[5]/span[2]')
btn_arrow_sign = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/span[4]/i')
btn2_arrow_sign = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/span[6]/i')

"eTrado Locators"
etrado_tab = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/nav/div[2]/a[17]/span[2]')
btn_more_option_menu_etrado = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/div/span/i')
btn_add = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[1]')
btn_sum = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div/span/div/input')
btn_next_sum = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input')
btn_next_details = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input[2]')
btn_next_results = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input[2]')
btn_add_etrado_payment = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/input')
text_creation_date_etrado = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[1]/table/tbody/tr[17]/td[4]/div')
btn_update_sum = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/input')
btn_next_detail_etrado = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input[2]')
btn_next_result_etrado = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input[2]')
btn_update_etrado_payment = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/input')