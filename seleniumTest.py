from selenium import webdriver



browser = webdriver.Chrome()
browser.get("http'//localhost:8000")
assert 'Home' in browser.title


browser.get("http'//localhost:8000/about")
assert 'About' in browser.title

browser.get("http'//localhost:8000/skills")
assert 'Tech' in browser.title

browser.get("http'//localhost:8000/education")
assert 'Education' in browser.title


browser.get("http'//localhost:8000/contact")
assert 'Contact' in browser.title


browser.get("http'//localhost:8000/posts")
assert 'posts' in browser.title


browser.get("http'//localhost:8000/posts/create/")
assert 'Title' in browser.title
