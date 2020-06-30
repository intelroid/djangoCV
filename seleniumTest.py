from selenium import webdriver



browser = webdriver.Firefox()
browser.get("https://sxh1066.pythonanywhere.com")
assert "Seonghee Han's CV" in browser.title


browser.get("https://sxh1066.pythonanywhere.com/about")

	
html_source = browser.page_source
if "Name" in html_source:
    print("name present in about me")
else:
    assert False


browser.get("https://sxh1066.pythonanywhere.com/skills")
html_source = browser.page_source
if "Tech Skills" in html_source:
    print("Tech Skills present in skills")
else:
    assert False

browser.get("https://sxh1066.pythonanywhere.com/education")
html_source = browser.page_source
if "Education" in html_source:
    print("Education present in Education")
else:
    assert False



browser.get("https://sxh1066.pythonanywhere.com/contact")
html_source = browser.page_source
if "Email Address" in html_source:
    print("Email address present in contact")
else:
    assert False



browser.get("https://sxh1066.pythonanywhere.com/posts")
html_source = browser.page_source
if "Posts" in html_source:
    print("Contact present in Post")
else:
    assert False



browser.get("https://sxh1066.pythonanywhere.com/posts/create/")
html_source = browser.page_source
if "Title" in html_source:
    print("successfully get create post page")
else:
    assert False
