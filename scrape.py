import requests
from bs4 import BeautifulSoup

def weather(n : str):
    url_lat_long = "https://in.search.yahoo.com/search;_ylt=AwrPhmmmGZxebzkAoxK6HAx.;_ylc=X1MDMjExNDcyMzAwMg" \
                "RfcgMyBGZyAwRncHJpZANxWEgwMnJhR1FBZWlGM01WSmhHaWpBBG5fcnNsdAMwBG5fc3VnZwMxBG9yaWdpbgNpbi5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmw" \
                "DBHFzdHJsAzE5BHF1ZXJ5AzI0MzEyMiUyMHRlbXByYXR1cmUEdF9zdG1wAzE1ODcyODg0OTQ-?fr2=sb-top-in.search&p={}+temprature&fr=sfp&iscqry=".format(n)
    page = requests.get(url = url_lat_long)
    soup = BeautifulSoup(page.content, "html.parser")
    find = soup.find(class_ = "main-temp")
    find_high_low = find.find(class_ = "temp-ctnt")
    find_curr = find.find_all_next(class_ = "currTemp")
    curr_loc = soup.find(class_ = "cptn-ctnt")
    loc_find = curr_loc.find(class_ = "txt")

    mydict = {
        "Your Location " : str(loc_find.get_text()) + " " + str(curr_loc.find(class_ = "subTxt").get_text()),
        "Today's Highest "  : find_high_low.find(class_ = "high").get_text(),
        "Today's Lowest "   : find_high_low.find(class_ = "low").get_text(),
        "Current Temprature "  : find_curr[0].get_text()
    }
    return mydict
