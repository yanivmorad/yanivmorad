import argparse
import os
import pickle
from g1 import VTAnalyzer

if __name__ == '__main__':

    if not os.path.exists('VT_website.pickle'):
        save_website = VTAnalyzer()
    else:
        with open('VT_website.pickle', 'rb') as fh:
            save_website = pickle.load(fh)

    parser = argparse.ArgumentParser(
        prog='Virus Total',
        description='The program allow you send api to virus total',
        epilog='Text at the bottom to help'
    )

    #definr arguments
    parser.add_argument('url', help='url to scan')
    parser.add_argument('-k', '--apikey')
    parser.add_argument('-s', '--scan', action='store_true')
    args = parser.parse_args()
    try:
        urls = args.url.split(",")
        if not args.apikey:
            if args.scan:
                print("Sorry for the delay, it will take about 20 seconds" )
                save_website.multi_scan(urls)
                print(save_website.get_urls_reputation(urls))
            else:
                print(save_website.get_urls_reputation(urls))
        else:
            if args.scan:
                print("Sorry for the delay, it will take about 20 seconds")
                save_website.multi_scan(urls,args.apikey)
                print(save_website.get_urls_reputation(urls, args.apikey))
    except Exception as e:
        print(e)
    with open('VT_website.pickle', 'wb') as fh:
        pickle.dump(save_website, fh)
