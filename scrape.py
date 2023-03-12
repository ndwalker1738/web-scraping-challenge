def scrape_all():

    from splinter import Browser 

    from bs4 import BeautifulSoup
    import pandas as pd
    import time 

    from webdriver_manager.chrome import ChromeDriverManager

    executable_path = { 'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text

    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    results = soup.find_all('a', class_="fancybox-thumbs")
    imageurls = []

    for result in results:
        imageurls.append(image_url+result['href'])
        imageurls

    featured_image_url = image_url+results[0]['href']
    featured_image_url

    facts_url = 'https://galaxyfacts-mars.com/'

    facts_table = pd.read_html(facts_url)

    mars_facts = facts_table[0]

    mars_facts

    mars_html = mars_facts.to_html()

    hemi_url = 'https://marshemispheres.com/'

    browser.visit(hemi_url)

    html = browser.html 

    soup = BeautifulSoup(html, "html.parser")

    results = soup.find_all('div', class_='item')

    hemisphere_image_urls=[]

    for result in results:
        title = result.find('h3').get_text()
        img_url = result.find('img', class_='thumb')['src']
        hemisphere_image_urls.append([
        {"title": "Valles Marineris Hemisphere", "img_url": img_url},
        {"title": "Cerberus Hemisphere", "img_url": img_url},
        {"title": "Schiaparelli Hemisphere", "img_url": img_url},
        {"title": "Syrtis Major Hemisphere", "img_url": img_url},
])

    return {"article":news_title, "paragraph":news_p, "image":image_url, "featured":featured_image_url, "mars":mars_html, "hemispheres":hemisphere_image_urls}
