BASE_URL = "https://guest:welcome2qauto@qauto2.forstudy.space/"


xpath_locators = [
    ("header", "//header[contains(@class, 'header')]"),
    ("logo link", "//header//a[@routerlink='/' and contains(@class, 'header_logo')]"),
    ("home nav link", "//nav[contains(@class, 'header_nav')]//a[text()='Home']"),
    ("about nav button", "//nav[contains(@class, 'header_nav')]//button[text()='About']"),
    ("contacts nav button", "//nav[contains(@class, 'header_nav')]//button[text()='Contacts']"),
    ("guest login button", "//div[contains(@class, 'header_right')]//button[text()='Guest log in']"),
    ("sign in button", "//div[contains(@class, 'header_right')]//button[text()='Sign In']"),
    ("hero title", "//section[contains(@class, 'hero')]//h1[text()='Do more!']"),
    ("hero signup button", "//section[contains(@class, 'hero')]//button[text()='Sign up']"),
    ("youtube iframe", "//div[contains(@class, 'hero-video')]//iframe[contains(@src, 'youtube.com/embed')]"),
    ("about section", "//div[@id='aboutSection' and contains(@class, 'about')]"),
    ("log fuel expenses title", "//div[@id='aboutSection']//p[text()='Log fuel expenses']"),
    ("instructions image", "//div[@id='aboutSection']//img[@alt='Instructions']"),
    ("contacts section title", "//div[@id='contactsSection']//h2[text()='Contacts']"),
    ("facebook link", "//div[@id='contactsSection']//a[@href='https://www.facebook.com/Hillel.IT.School']"),
    ("telegram link", "//div[@id='contactsSection']//a[contains(@href, 't.me/ithillel_kyiv')]"),
    ("site contacts link", "//div[@id='contactsSection']//a[text()='ithillel.ua']"),
    ("support email link", "//div[@id='contactsSection']//a[@href='mailto:developer@ithillel.ua']"),
    ("footer copyright", "//footer[contains(@class, 'footer')]//p[contains(text(), '2021 Hillel IT school')]"),
    ("login modal title", "//div[contains(@class, 'modal-header')]//h4[text()='Log in']"),
    ("login email input", "//app-signin-form//input[@id='signinEmail' and @name='email']"),
    ("login password input", "//app-signin-form//input[@id='signinPassword' and @type='password']"),
    ("remember me checkbox", "//app-signin-form//input[@id='remember' and @type='checkbox']"),
    ("forgot password button", "//app-signin-form//button[text()='Forgot password']"),
    ("registration modal button", "//div[contains(@class, 'modal-footer')]//button[text()='Registration']"),
]


css_locators = [
    ("header", "header.header.bg-basic-dark"),
    ("logo link", "header .header_left a.header_logo[routerlink='/']"),
    ("home nav link", "nav.header_nav a.header-link[routerlink='/']"),
    ("about nav button", "nav.header_nav button.header-link[appscrollto='aboutSection']"),
    ("contacts nav button", "nav.header_nav button.header-link[appscrollto='contactsSection']"),
    ("guest login button", ".header_right > button.header-link.-guest"),
    ("sign in button", ".header_right > button.btn.btn-outline-white.header_signin"),
    ("hero section", "section.section.hero"),
    ("hero title", "section.hero .hero-descriptor > h1.hero-descriptor_title"),
    ("hero signup button", "section.hero .hero-descriptor button.hero-descriptor_btn.btn-primary"),
    ("youtube iframe", ".hero-video iframe.hero-video_frame[src*='youtube.com/embed']"),
    ("about section", "div#aboutSection.section.about"),
    ("first about image", "#aboutSection .about-block:first-child img.about-picture_img[alt='Instructions']"),
    ("about block title", "#aboutSection .about-block .about-block_title.h2"),
    ("contacts section", "div#contactsSection.section.contacts"),
    ("contacts socials", "#contactsSection .contacts_socials.socials"),
    ("facebook link", "#contactsSection a.socials_link[href='https://www.facebook.com/Hillel.IT.School']"),
    ("telegram link", "#contactsSection a.socials_link[href*='t.me/ithillel_kyiv']"),
    ("support email link", "#contactsSection a.contacts_link[href='mailto:developer@ithillel.ua']"),
    ("footer", "footer.footer.d-flex.align-items-center"),
    ("login email input", "app-signin-form input#signinEmail[name='email'][formcontrolname='email']"),
    ("login password input", "app-signin-form input#signinPassword[type='password'][formcontrolname='password']"),
    ("remember me checkbox", "app-signin-form input#remember[type='checkbox'][formcontrolname='remember']"),
    ("sign-up name input", "app-signup-form input#signupName[name='name'][formcontrolname='name']"),
    ("sign-up repeat password input", "app-signup-form input#signupRepeatPassword[name='repeatPassword']"),
]


if __name__ == "__main__":
    print(f"Base URL: {BASE_URL}")
    print(f"XPath locators: {len(xpath_locators)}")
    print(f"CSS locators: {len(css_locators)}")
