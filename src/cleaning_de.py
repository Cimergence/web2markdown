import os, re
from functools import reduce
import shutil


# Define directories
# Directory containing the Markdown files
original_dir = "/home/bibiicekill/code-projects/web2markdown/src/scraped_markdown_pages/original de"
test_dir = "/home/bibiicekill/code-projects/web2markdown/src/scraped_markdown_pages/clean de" # Replace with the path to /test

# Ensure the /test directory exists
os.makedirs(test_dir, exist_ok=True)

pattern_1 = """![logo]()

[](https://www.cookiebot.com/en/what-is-behind-powered-by-cookiebot/)

  * [Consent](#)
  * [Details](#)
  * [[#IABV2SETTINGS#]](#)
  * [About](#)



## This website uses cookies

We use cookies to personalise content and ads, to provide social media features and to analyse our traffic. We also share information about your use of our site with our social media, advertising and analytics partners who may combine it with other information that you’ve provided to them or that they’ve collected from your use of their services. 

Consent Selection

**Necessary**

**Preferences**

**Statistics**

**Marketing**

[Show details](#)

  * Necessary  15

Necessary cookies help make a website usable by enabling basic functions like page navigation and access to secure areas of the website. The website cannot function properly without these cookies.

    * [Cookiebot2](#)[Learn more about this provider![]()](https://www.cookiebot.com/goto/privacy-policy/ "Cookiebot's privacy policy")

**1.gif** Used to count the number of sessions to the website, necessary for optimizing CMP product delivery. 

**Maximum Storage Duration** : Session**Type** : Pixel Tracker

**CookieConsent** Stores the user's cookie consent state for the current domain

**Maximum Storage Duration** : 1 year**Type** : HTTP Cookie

    * [Google1](#)[Learn more about this provider![]()](https://business.safety.google/privacy/ "Google's privacy policy")

Some of the data collected by this provider is for the purposes of personalization and measuring advertising effectiveness.

**test_cookie** Used to check if the user's browser supports cookies.

**Maximum Storage Duration** : 1 day**Type** : HTTP Cookie

    * [Hubspot4](#)[Learn more about this provider![]()](https://legal.hubspot.com/privacy-policy "Hubspot's privacy policy")

**__cf_bm [x2]** This cookie is used to distinguish between humans and bots. This is beneficial for the website, in order to make valid reports on the use of their website.

**Maximum Storage Duration** : 1 day**Type** : HTTP Cookie

**_cfuvid [x2]** This cookie is a part of the services provided by Cloudflare - Including load-balancing, deliverance of website content and serving DNS connection for website operators. 

**Maximum Storage Duration** : Session**Type** : HTTP Cookie

    * [LinkedIn2](#)[Learn more about this provider![]()](https://www.linkedin.com/legal/privacy-policy "LinkedIn's privacy policy")

**bcookie** Used in order to detect spam and improve the website's security. 

**Maximum Storage Duration** : 1 year**Type** : HTTP Cookie

**li_gc** Stores the user's cookie consent state for the current domain

**Maximum Storage Duration** : 180 days**Type** : HTTP Cookie

    * [Wix.com2](#)[Learn more about this provider![]()](http://parastorage.com/ "Wix.com's privacy policy")

**connect.sid** The cookie is necessary for secure log-in and the detection of any spam or abuse of the website.

**Maximum Storage Duration** : Session**Type** : HTTP Cookie

**bSession** Necessary for measuring and reporting of website performance. 

**Maximum Storage Duration** : 1 day**Type** : HTTP Cookie

    * [www.swiss-interim-management.ch4](#)

**hs** Ensures visitor browsing-security by preventing cross-site request forgery. This cookie is essential for the security of the website and visitor. 

**Maximum Storage Duration** : Session**Type** : HTTP Cookie

**ssr-caching** This cookie is necessary for the cache function. A cache is used by the website to optimize the response time between the visitor and the website. The cache is usually stored on the visitor’s browser.

**Maximum Storage Duration** : 1 day**Type** : HTTP Cookie

**svSession** This cookie is necessary for the login function on the website. 

**Maximum Storage Duration** : 400 days**Type** : HTTP Cookie

**XSRF-TOKEN** Ensures visitor browsing-security by preventing cross-site request forgery. This cookie is essential for the security of the website and visitor. 

**Maximum Storage Duration** : Session**Type** : HTTP Cookie

  * Preferences  2

Preference cookies enable a website to remember information that changes the way the website behaves or looks, like your preferred language or the region that you are in.

    * [LinkedIn1](#)[Learn more about this provider![]()](https://www.linkedin.com/legal/privacy-policy "LinkedIn's privacy policy")

**lidc** Registers which server-cluster is serving the visitor. This is used in context with load balancing, in order to optimize user experience. 

**Maximum Storage Duration** : 1 day**Type** : HTTP Cookie

    * [jobboard.online1](#)

**lang** Remembers the user's selected language version of a website

**Maximum Storage Duration** : Session**Type** : HTTP Cookie

  * Statistics  8

Statistic cookies help website owners to understand how visitors interact with websites by collecting and reporting information anonymously.

    * [Hubspot4](#)[Learn more about this provider![]()](https://legal.hubspot.com/privacy-policy "Hubspot's privacy policy")

**__hssc** Identifies if the cookie data needs to be updated in the visitor's browser.

**Maximum Storage Duration** : 1 day**Type** : HTTP Cookie

**__hssrc** Used to recognise the visitor's browser upon reentry on the website.

**Maximum Storage Duration** : Session**Type** : HTTP Cookie

**__hstc** Sets a unique ID for the session. This allows the website to obtain data on visitor behaviour for statistical purposes.

**Maximum Storage Duration** : 180 days**Type** : HTTP Cookie

**hubspotutk** Sets a unique ID for the session. This allows the website to obtain data on visitor behaviour for statistical purposes.

**Maximum Storage Duration** : 180 days**Type** : HTTP Cookie

    * [Wix2](#)[Learn more about this provider![]()](https://www.wix.com/about/privacy "Wix's privacy policy")

**_wixAB3** This cookie is used by the website’s operator in context with multi-variate testing. This is a tool used to combine or change content on the website. This allows the website to find the best variation/edition of the site. 

**Maximum Storage Duration** : 6 months**Type** : HTTP Cookie

**_wixAB3|#-#-#-#-#** This cookie is used by the website’s operator in context with multi-variate testing. This is a tool used to combine or change content on the website. This allows the website to find the best variation/edition of the site. 

**Maximum Storage Duration** : Session**Type** : HTTP Cookie

    * [Wix.com1](#)[Learn more about this provider![]()](http://parastorage.com/ "Wix.com's privacy policy")

**fedops.logger.sessionId** Registers statistical data on users' behaviour on the website. Used for internal analytics by the website operator. 

**Maximum Storage Duration** : Persistent**Type** : HTML Local Storage

    * [jobboard.online1](#)

**rememberme** Pending

**Maximum Storage Duration** : 14 days**Type** : HTTP Cookie

  * Marketing  7

Marketing cookies are used to track visitors across websites. The intention is to display ads that are relevant and engaging for the individual user and thereby more valuable for publishers and third party advertisers.

    * [Google6](#)[Learn more about this provider![]()](https://business.safety.google/privacy/ "Google's privacy policy")

Some of the data collected by this provider is for the purposes of personalization and measuring advertising effectiveness.

**IDE** Pending

**Maximum Storage Duration** : 400 days**Type** : HTTP Cookie

**pagead/1p-conversion/#/** Pending

**Maximum Storage Duration** : Session**Type** : Pixel Tracker

**pagead/1p-user-list/#** Tracks if the user has shown interest in specific products or events across multiple websites and detects how the user navigates between sites. This is used for measurement of advertisement efforts and facilitates payment of referral-fees between websites.

**Maximum Storage Duration** : Session**Type** : Pixel Tracker

**_ga** Used to send data to Google Analytics about the visitor's device and behavior. Tracks the visitor across devices and marketing channels.

**Maximum Storage Duration** : 2 years**Type** : HTTP Cookie

**_ga_#** Used to send data to Google Analytics about the visitor's device and behavior. Tracks the visitor across devices and marketing channels.

**Maximum Storage Duration** : 2 years**Type** : HTTP Cookie

**_gcl_au** Used by Google AdSense for experimenting with advertisement efficiency across websites using their services. 

**Maximum Storage Duration** : 3 months**Type** : HTTP Cookie

    * [Hubspot1](#)[Learn more about this provider![]()](https://legal.hubspot.com/privacy-policy "Hubspot's privacy policy")

**__ptq.gif** Sends data to the marketing platform Hubspot about the visitor's device and behaviour. Tracks the visitor across devices and marketing channels.

**Maximum Storage Duration** : Session**Type** : Pixel Tracker

  * Unclassified 0

Unclassified cookies are cookies that we are in the process of classifying, together with the providers of individual cookies.

We do not use cookies of this type.




[Cross-domain consent[#BULK_CONSENT_DOMAINS_COUNT#]](#) [#BULK_CONSENT_TITLE#]

List of domains your consent applies to: [#BULK_CONSENT_DOMAINS#]

Cookie declaration last updated on 11/13/24 by [Cookiebot](https://www.cookiebot.com "Cookiebot")

## [#IABV2_TITLE#]

[#IABV2_BODY_INTRO#]

[#IABV2_BODY_LEGITIMATE_INTEREST_INTRO#]

[#IABV2_BODY_PREFERENCE_INTRO#]

[#IABV2_LABEL_PURPOSES#]

[#IABV2_BODY_PURPOSES_INTRO#]

[#IABV2_BODY_PURPOSES#]

[#IABV2_LABEL_FEATURES#]

[#IABV2_BODY_FEATURES_INTRO#]

[#IABV2_BODY_FEATURES#]

[#IABV2_LABEL_PARTNERS#]

[#IABV2_BODY_PARTNERS_INTRO#]

[#IABV2_BODY_PARTNERS#]

Cookies are small text files that can be used by websites to make a user's experience more efficient.The law states that we can store cookies on your device if they are strictly necessary for the operation of this site. For all other types of cookies we need your permission.This site uses different types of cookies. Some cookies are placed by third party services that appear on our pages.You can at any time change or withdraw your consent from the Cookie Declaration on our website.Learn more about who we are, how you can contact us and how we process personal data in our [Privacy Policy](https://www.swiss-interim-management.ch/privacy).Please state your consent ID and date when you contact us regarding your consent.

**Do not sell or share my personal information**

Deny Allow selection Customize Allow all

top of page

  * Expertise

    * [Case Studies ](https://www.swiss-interim-management.ch/de/case-studies)
    * [Journal](https://www.swiss-interim-management.ch/de/blog)
    * [Für Interim Manager](https://www.swiss-interim-management.ch/de/for-interim-managers)
    * [Unser Unternehmen ](https://www.swiss-interim-management.ch/de/our-company)
    * [Unser Ansatz](https://www.swiss-interim-management.ch/de/our-approach)
    * [Unsere Werte](https://www.swiss-interim-management.ch/de/our-values)
    * [Unsere Interim Manager ](https://www.swiss-interim-management.ch/de/interim-managers)
    * [Unsere Kunden ](https://www.swiss-interim-management.ch/de/our-clients)

  * [Branchen](https://www.swiss-interim-management.ch/de/industries)

    * [Interim Management Finanzen](https://www.swiss-interim-management.ch/de/industries/finance-interim-management)
    * [Interim Management Marketing](https://www.swiss-interim-management.ch/de/industries/interim-marketing-management)
    * [Interim Management im Bereich Sales](https://www.swiss-interim-management.ch/de/industries/sales-interim-management)
    * [Interim Management Energie](https://www.swiss-interim-management.ch/de/industries/energy-interim-management)
    * [Pharma Interim Management ](https://www.swiss-interim-management.ch/de/industries/pharma-interim-management)
    * [ CEO / COO Interim Management](https://www.swiss-interim-management.ch/de/industries/ceo-coo-interim-management)
    * [IT-Interim Management](https://www.swiss-interim-management.ch/de/industries/it-interim-management)
    * [HR-Interim Management](https://www.swiss-interim-management.ch/de/industries/hr-interim-management)
    * [Interim Management Lebensmittel Branche](https://www.swiss-interim-management.ch/de/industries/food-industry-interim-management)
    * [Interim Management Medizintechnik](https://www.swiss-interim-management.ch/de/industries/medtech-interim-management)

  * [Jobs](https://www.swiss-interim-management.ch/de/jobs)
  * [Kontakt](https://www.swiss-interim-management.ch/de/contact)



[![SIM-Logo-2022-02.png](https://static.wixstatic.com/media/0eb0e4_23c480b39ebd4969815e6f233b3f0f40~mv2.png/v1/fill/w_185,h_59,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/SIM-Logo-2022-02.png)](https://www.swiss-interim-management.ch/de)"""

pattern_2 = """![SIM-Logo-2022-White.png](https://static.wixstatic.com/media/0eb0e4_1b83d6cfd303426385cad69fc0f9c64c~mv2.png/v1/fill/w_195,h_62,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/SIM-Logo-2022-White.png)

[Kontakt](https://www.swiss-interim-management.ch/de/contact)

Dienstleistung

Unternehmen

Follow us

[Jobs](https://www.swiss-interim-management.ch/de/jobs)

[Impressum](https://www.swiss-interim-management.ch/de/imprint)

[Datenschutz](https://www.swiss-interim-management.ch/de/privacy)

[Rechtlicher Hinweis](https://www.swiss-interim-management.ch/de/legal)

[Branchen](https://www.swiss-interim-management.ch/de/industries)

[Case Studies](https://www.swiss-interim-management.ch/de/case-studies)

[Journal](https://www.swiss-interim-management.ch/de/blog)

[Für Interim Manager](https://www.swiss-interim-management.ch/de/for-interim-managers-former)

[Unser Unternehmen](https://www.swiss-interim-management.ch/de/our-company)

[Unser Ansatz](https://www.swiss-interim-management.ch/de/our-approach)

[Unsere Werte](https://www.swiss-interim-management.ch/de/our-values)

[Unsere Interim Manager](https://www.swiss-interim-management.ch/de/interim-managers)

[![logo-linkedin-white.png](https://static.wixstatic.com/media/0eb0e4_093e65b093ac4d5384924fb35351fdfb~mv2.png/v1/crop/x_81,y_135,w_1944,h_1863/fill/w_30,h_30,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logo-linkedin-white.png)](https://www.linkedin.com/company/662551/admin/)

[![x-twitter-white.png](https://static.wixstatic.com/media/0eb0e4_1eb860bca16e4ad5bfd5b8b78a335bb5~mv2.png/v1/crop/x_54,y_0,w_1008,h_1008/fill/w_24,h_24,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/x-twitter-white.png)](https://twitter.com/SIM_GmbH)

[![xing icon white.png](https://static.wixstatic.com/media/0eb0e4_fe10aa433faa45b39da70a7a9f46bde8~mv2.png/v1/fill/w_30,h_30,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/xing%20icon%20white.png)](https://www.xing.com/pages/swiss-interim-management)

[Unsere Kunden](https://www.swiss-interim-management.ch/de/our-clients)

© 2024 by Swiss Interim Management GmbH

bottom of page
"""
pattern_3 = """![Cookiebot session tracker icon loaded](https://imgsct.cookiebot.com/1.gif?dgi=f2d1508e-cdf0-49bf-85a2-33d27b3e19cb)"""

patterns = [pattern_1, pattern_2, pattern_3]




def update_link_descriptions(content):
    """
    Replace image descriptions like '[Discover more.jpg]' with '[DES]'.
    """
    file_extensions = ('.jpg', '.png', '.gif', '.jpeg', '.bmp', '.svg')
    description_pattern = re.compile(r"\[.*?\.(jpg|png|gif|jpeg|bmp|svg)\]")

    return description_pattern.sub("[DES]", content)

def remove_patterns(content, patterns):
    """
    Remove all specified patterns from the content.
    """
    # import pdb; pdb.set_trace()
    for pattern in patterns:
        content = content.replace(pattern, "")
    return content

def replace_links(content):
    """
    Replace all links matching the pattern with a placeholder.
    """
    link_pattern = r"https://[^\s)]+"
    return re.sub(link_pattern, "LINK", content)

def remove_exclamation_from_links(content):
    """
    Replace all occurrences of '![' with '['.
    """
    return content.replace("![", "[")

# Copy original files to the test directory
for filename in os.listdir(original_dir):
    if filename.endswith(".md"):  # Only process Markdown files
        src_path = os.path.join(original_dir, filename)
        dest_path = os.path.join(test_dir, filename)
        shutil.copy(src_path, dest_path)

# Read and update all Markdown files in the /test directory
for filename in os.listdir(test_dir):
    if filename.endswith(".md"):  # Only process Markdown files
        filepath = os.path.join(test_dir, filename)
        
        # Read file content
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Remove patterns
        content = remove_patterns(content, patterns)
        # Replace links
        content = replace_links(content)
        # Replace links
        content = update_link_descriptions(content)

        content = remove_exclamation_from_links(content)
        
        # Write updated content back to the file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Patterns removed from all Markdown files in /test.")