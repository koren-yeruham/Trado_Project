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
products_table = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]"
products_search = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]")

products_tab = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[2]")
products_kebab = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[1]/span[1]/i[1]")

products_1st_tab = (By.XPATH, "//tbody/tr[1]")
products_1st_price = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[5]/span[1]/div[1]/input[1]")
products_1st_next = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[4]/input[1]")

products_1st_tab_price = (By.XPATH, "//tbody/tr[1]/td[5]")
products_1st_tab_name = (By.XPATH, "//tbody/tr[1]/td[1]")
products_1st_tab_MKT = (By.XPATH, "//tbody/tr[1]/td[3]")
products_1st_tab_supercategory = (By.XPATH, "//tbody/tr[1]/td[17]")
products_1st_tab_store = (By.XPATH, "//tbody/tr[1]/td[22]")

products_add_user = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]")
products_add_MKT = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[3]/span[1]/div[1]/input[1]")
products_add_name = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[1]/span[1]/div[1]/input[1]")
products_add_price = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[5]/span[1]/div[1]/input[1]")
products_add_submit_btn = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[4]/input[1]")
products_add_submit_btn2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[4]/input[2]")
products_add_supercategory = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[2]/div[1]/span[1]/div[1]/input[1]")
products_add_store = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[6]/div[1]/span[1]/div[1]/input[1]")
products_add_store_dropdown_1st = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[6]/div[1]/span[1]/div[2]/div[1]/div[1]")
products_add_supercategory_dropdown = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/span[1]/form[1]/div[2]/div[2]/div[1]/span[1]/div[2]/div[1]/div[1]")
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
#לכל טסט etrado_tab
etrado_tab = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/nav/div[2]/a[17]/span[2]')
btn_more_option_menu_etrado = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/div/span/i')
btn_add = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[1]')
field_sum = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div/span/div/input')
#כפתורים בתהליך הוספה לטסט 4.6.1
btn_next_sum = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input')
btn_next_details = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input[2]')
btn_next_results = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input[2]')
btn_add_etrado_payment = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/input')
#
text_creation_date_etrado = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[1]/table/tbody/tr[17]/td[4]/div')
#כפתורים
btn_update_sum = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/input')
btn_next_detail_etrado = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input[2]')
btn_next_result_etrado = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/input')
btn_update_etrado_payment = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/input')
btnn_next_etrado_sum = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input')
sum_element_etrado = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[1]/table/tbody/tr[17]/td[1]')
#
#test-4.6.4
field_ID_etrado = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[1]/span/div/input')
###test-4.6.5
Payment_period_element = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[2]/span/div/input')
Account_Number_element = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[3]/span/div/input')
bank_name_element = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[4]/div[1]/span[1]/div[1]')
bank_leumi_element = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[4]/div[1]/span[1]/div[2]/div/div')
bank_name_input = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[4]/div[1]/span[1]/div/input')
Bank_code_element = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[5]/span/div/input')
Branch_element = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[6]/span/div/input')
Remarks_element = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[7]/span/div/input')


"stores Locators"
stores_tab = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/nav/div[2]/a[21]')
stores_more_option_menu_btn = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[1]/span[1]/i[1]")
add_store_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[1]')
store_name_field = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[2]/span/div/input')
store_phone_field = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div/input')
store_city_field = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[8]/div[1]/div[1]/span/div/input')
store_street_field = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[8]/div[1]/div[2]/span/div/input')
store_building_field = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[8]/div[1]/div[3]/span/div/input')
stores_add_store_btn= (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/input')
stores_btn1_arrow_sign = (By.XPATH , '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/span[4]/i')
stores_btn2_arrow_sign = (By.XPATH , '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/span[6]/i')
# החנות הספציפית שנבחרה בשורה מתחת היא חנות עם מספר עוסק 145828122
stores_specialty_store_row = (By.XPATH , '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[1]/table/tbody/tr[22]')
stores_specialty_store_row_name = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[2]/span/div/input')
stores_update_store_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/input')
store_name_tab = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[1]/table/tbody/tr[22]/td[2]')
stores_specialty_store_field_name = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[2]/span/div/input')
stores_specialty_store_field_phone = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div/input')
stores_specialty_store_field_phone_country = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div/div[2]/div')
stores_specialty_store_field_phone_country_IL = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div/div[2]/ul/li[1]')
store_phone_tab = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[1]/table/tbody/tr[22]/td[4]')
stores_add_store_field_phone_country = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div/div[2]/div')
stores_add_store_field_phone_country_IL = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div/div[2]/ul/li[1]')
store_search_bar = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/span/span/div/input')
stores_specialty_store_field_city = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[8]/div[1]/div[1]/span/div/input')
stores_specialty_store_row_search = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[1]/table/tbody/tr')
stores_specialty_store_field_street = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[8]/div[1]/div[2]/span/div/input')
stores_specialty_store_field_building = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[8]/div[1]/div[3]/span/div/input')
store_search_name_tab = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')
count_store = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[2]/div[2]')

"users Locators"
users_tab = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[22]")
users_kebab = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[1]/span[1]/i[1]")
users_kebab_add = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]")
users_kebab_add2 = (By.XPATH, "//*[@id='root']/div[1]/div[4]/div/div/form/input")
users_add_phone = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[6]/div[1]/div[1]/input[1]")
users_add_store = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[9]/span[1]/div[2]/input[1]")
users_add_store_dropdown = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[9]/span[1]/div[3]/div[1]/div[1]")
users_add_submit = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/input[1]")


























"System users"
system_user_tab = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[23]")
searchbarsystem = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]")
system_user_submit = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/input[1]")
system_user_1st_row = (By.XPATH, "//tbody//tr")
system_user_kebab = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[1]/span[1]/i[1]")
system_user_add_btn = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]")

system_user_firstname = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]")
system_user_lastname = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]/div[1]/input[1]")
system_user_email = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[3]/span[1]/div[1]/input[1]")
system_user_store = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[7]/span[1]/div[2]/input[1]")
system_user_store_1st = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[7]/span[1]/div[3]/div[1]/div[1]")
system_user_phone = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/input[1]")

"Tab asserts"
system_user_name_tab = (By.XPATH, "//tbody/tr[1]/td[1]")
system_user_lastname_tab = (By.XPATH, "//tbody/tr[1]/td[2]")
system_user_email_tab = (By.XPATH, "//tbody/tr[1]/td[3]")
system_user_stores_tab = (By.XPATH, "//tbody/tr[1]/td[7]")