from data.group import Group
from data.scraping_from_kpop import ScrapingFromKPop
from window.main_window import MainWindow

if __name__ == "__main__":
    classKpop = ScrapingFromKPop()

    profile_categories = list(classKpop.get_all_profile_category())
    for i in range(len(profile_categories)):
        print("\t" + str(i+1) + ".\t" + profile_categories[i])

    chosen = int(input("Please choose a number to work on: ")) - 1
    print(classKpop.get_link(profile_categories[chosen]))
