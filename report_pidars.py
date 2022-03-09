from webpage_elements import *
from css_selectors import bcolors
from helpers import *
import argparse

parser = argparse.ArgumentParser(description='Report Pidars')
parser.add_argument(
    "-u",
    "--username",
    type=str,
    required=True,
    metavar="USERNAME",
    help="username or email"
)
parser.add_argument(
    "-p",
    "--password",
    type=str,
    required=True,
    metavar="PASSWORD",
    help="Password"
)
args = parser.parse_args()

displayChant()
dolboebi, driver = init("./dolboebi.json")
driver.get("https://www.instagram.com")

# accept_cookies & log in
accept_cookies(driver)
log_in(driver, args.username, args.password)

# report pidars
posts_counter = 0
user_counter = 0
for index in dolboebi:
    dolboeb = dolboebi[index]
    follow(driver, dolboeb['username'])
    for post in dolboeb["posts"]:
        if report_post(driver, post):
            posts_counter += 1
    if report_user(driver, dolboeb['username']):
        user_counter += 1
    unfollow(driver, dolboeb['username'])
    print("Going to the next dolboeb\n")
print("\n",
      f"\n{bcolors.OKGREEN}Posts reported in total: {user_counter}{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}Posts reported in total: {posts_counter}{bcolors.ENDC}")
driver.quit()
