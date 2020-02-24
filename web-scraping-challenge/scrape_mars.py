from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    slide_elem = news_soup.select_one('ul.item_list li.slide')
    title = slide_elem.find("div", class_="content_title").get_text()
    paragraph = slide_elem.find("div", class_="article_teaser_body").get_text()
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')
    img_source = image_soup.select_one('figure.lede a img').get("src")
    img_source
    final_url = 'https://www.jpl.nasa.gov' + img_source
    final_url
    mars_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather)
    html = browser.html
    twitter_soup = BeautifulSoup(html, 'html.parser')
    mars_tweet = twitter_soup.find('span', attrs={"class": "css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"})
    mars_text = mars_tweet.find('p', "tweet-text").get_text()
    mars_tweet
    mars_text
    mars_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemi)
    links = browser.find_by_css("a.product-item h3")
    hemi_images = []
    for i in range(len(links)):
        hemisphere = {}
        browser.find_by_css("a.product-item h3")[i].click()
        sample_elem = browser.find_link_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
        hemisphere['title'] = browser.find_by_css("h2.title").text
        hemi_images.append(hemisphere)
        browser.back()
    hemi_images
    df = pd.read_html('https://space-facts.com/mars/')[0]
    df.columns=['description', 'value']
    df.set_index('description', inplace=True)
    df
    # Store data in a dictionary
    mars_data = {
        "sloth_img": sloth_img,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
