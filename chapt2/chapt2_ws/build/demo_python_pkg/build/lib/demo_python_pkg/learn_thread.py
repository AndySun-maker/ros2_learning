import threading
import requests

class Download:
    def download(self, url, callback):
        print(f'Thread:{threading.get_ident()} begin to load:{url}')
        response = requests.get(url)
        response.encoding = 'uft-8'
        callback(url, response.text)

    def start_download(self, url, callback):
        thread = threading.Thread(target=self.download, args=(url, callback))
        thread.start()

def download_finish_callback(url, result):
    print(f'{url} download successfully,all:{len(result)} word, the content is:{result[:5]}...')

def main():
    d = Download()
    d.start_download('http://localhost:8000/novel1.txt', download_finish_callback)
    d.start_download('http://localhost:8000/novel2.txt', download_finish_callback)
    d.start_download('http://localhost:8000/novel3.txt', download_finish_callback)