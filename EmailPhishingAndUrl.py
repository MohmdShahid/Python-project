# phishing_emails = ["Phishing@ryuk.com", "phishing@conti.com","phishing@lockbit.com","spam@revil.com","shahid"]

# email = input("Enter the Email Address")

# if email in phishing_emails:
#     print("Beware this email is from the Ransomware group.")
# else:
#     print("this email does not appear to be from a known phisher")
phishing_urls = ["revil.ru","conti.ru","nso.il","doubledragon.cn","ryuk.ru","spam.com"]

url = input("Enter a URL:")

domain = url.split("//")[-1].split("/")[0]

if domain in phishing_urls:
    print("Beware baachho issee")
else:
    print("This URL not appear to be known phishign url")
