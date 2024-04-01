from selenium.webdriver.common.by import By

"Locators"
input_phone_field = (By.CSS_SELECTOR, "div.login_login div.login_panel form.form_form div.form_items div.form_formItem.undefined.undefined.formItem_phone div.phoneInput_phoneInputContainer:nth-child(2) div.react-tel-input > input.form-control")
submit_btn = (By.CSS_SELECTOR, "div.login_login div.login_panel span:nth-child(2) form.form_form > input.form_submitBtn")
code_submit = (By.CSS_SELECTOR, "div.login_login div.login_panel form.form_form div.form_items div.form_formItem.undefined.undefined.formItem_code:nth-child(1) span.input_input:nth-child(2) div.input_relative > input:nth-child(1)")
login_button = (By.CSS_SELECTOR, "div.login_login div.login_panel span:nth-child(2) form.form_form > input.form_submitBtn")
trado_button = (By.CSS_SELECTOR, "div.login_login div.login_panel div.storesList_storesList:nth-child(2) div.storesList_list:nth-child(2) > div.storesList_store:nth-child(1)")


"DB connection info"
username = "qa_agency"
password = "!5szveK7$TE$93u"
database_name = "trado_qa"
