import random
import time

class Bot:
    def __init__(self, bot_id, proxy, ip):
        self.bot_id = bot_id
        self.proxy = proxy
        self.ip = ip
        self.active = True

    def watch_live(self, stream_url):
        while self.active:
            print(f'Bot {self.bot_id} menonton {stream_url} dengan IP {self.ip} melalui proxy {self.proxy}')
            time.sleep(random.randint(5,10))

    def stop(self):
        self.active = False

def load_proxies():
    with open('viewer_bot/proxy_list.txt') as f:
        return [line.strip() for line in f.readlines()]

def generate_random_ip():
    return '.'.join(str(random.randint(0,255)) for _ in range(4))

def create_bots(num_bots):
    proxies = load_proxies()
    bots = []
    for i in range(num_bots):
        proxy = random.choice(proxies)
        ip = generate_random_ip()
        bots.append(Bot(bot_id=i, proxy=proxy, ip=ip))
    return bots
