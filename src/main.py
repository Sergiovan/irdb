import urllib.request, imghdr, argparse, tempfile, shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="It's a secret to everybody...")
    parser.add_argument('--path', help="Path to image")
    parser.add_argument('--url', help="Url to image")

    params = parser.parse_args()

    print(vars(params))

    print(imghdr.what(params.path))

    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    req = urllib.request.Request(params.url, headers=hdr)

    with tempfile.TemporaryDirectory() as dir:
        tf = open(dir + '/000', 'w+b')
        imgbin = urllib.request.urlopen(req).read()
        tf.write(imgbin)
        print(imghdr.what(tf.name))
        tf.close()

        shutil.copy(tf.name, 'data/000')
