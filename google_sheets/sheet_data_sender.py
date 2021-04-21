import gspread
import flipkart
import json

cpu_url = 'CPU', 'https://www.flipkart.com/electrobot-core-2-duo-4-gb-ram-intel-onboard-graphics-graphics-160-hard-disk-windows-7-ultimate-mid-tower/p/itm1110a9ccee07f?pid=CPUF5CN2HQKWRQ4E&lid=LSTCPUF5CN2HQKWRQ4EKLBXKA&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=SEARCH&iid=93141204-f5a1-4991-99f7-29ef1939a778.CPUF5CN2HQKWRQ4E.SEARCH&ppt=hp&ppn=homepage&ssid=q36nsm5fao0000001614507473661&qH=d9747e2da342bdb9'
keyboard_url = 'Keyboard', 'https://www.flipkart.com/zebronics-judwaa-555-combo-mouse-wired-usb-laptop-keyboard/p/itmeuefxxu2x3pcq?pid=ACCEUEFXZEKWUM7Q&lid=LSTACCEUEFXZEKWUM7Q99YTQI&marketplace=FLIPKART&fm=productRecommendation%2Fattach&iid=R%3Aa%3Bp%3ACPUF5CN2HQKWRQ4E%3Bl%3ALSTCPUF5CN2HQKWRQ4EKLBXKA%3Bpt%3App%3Buid%3A3a97cffe-79ae-11eb-ae02-dba6f60d6454%3B.ACCEUEFXZEKWUM7Q&ssid=6flsb02tj40000001614507478016&otracker=pp_reco_Frequently%2BBought%2BTogether_2_Frequently%2BBought%2BTogether_ACCEUEFXZEKWUM7Q_productRecommendation%2Fattach_2&otracker1=pp_reco_PINNED_productRecommendation%2Fattach_Frequently%2BBought%2BTogether_NA_productCard_cc_2_NA_view-all&cid=ACCEUEFXZEKWUM7Q'
monitor_url = 'Monitor', 'https://www.flipkart.com/enter-15-4-inch-hd-led-backlit-monitor-e-m16b/p/itmcbeb7bfe73a4a?pid=MONFMBSPP7AVNGQ4&lid=LSTMONFMBSPP7AVNGQ4JZTZ07&marketplace=FLIPKART&fm=productRecommendation%2Fattach&iid=R%3Aa%3Bp%3ACPUF5CN2HQKWRQ4E%3Bl%3ALSTCPUF5CN2HQKWRQ4EKLBXKA%3Bpt%3App%3Buid%3A3a97cffe-79ae-11eb-ae02-dba6f60d6454%3B.MONFMBSPP7AVNGQ4&ssid=6flsb02tj40000001614507478016&otracker=pp_reco_Frequently%2BBought%2BTogether_1_Frequently%2BBought%2BTogether_MONFMBSPP7AVNGQ4_productRecommendation%2Fattach_1&otracker1=pp_reco_PINNED_productRecommendation%2Fattach_Frequently%2BBought%2BTogether_NA_productCard_cc_1_NA_view-all&cid=MONFMBSPP7AVNGQ4'

gc = gspread.service_account(filename='rich-channel-311405-64e076c9a55d.json')
sheet = gc.open('PythonSheets').sheet1

product_data = flipkart.get_price_log(cpu_url, keyboard_url, monitor_url)

for data in product_data:
    sheet.append_row(data)
