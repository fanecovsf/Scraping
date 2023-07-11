import time

from link import Link

def trinks_extract():
    trinks = Link("https://www.trinks.com/Login", "Chrome", sleep=1, headless=False)

    trinks.openLink()

    trinks.maximize()

    trinks.sendKeys('//*[@id="fEmail"]', 'matheus.cavichione@hotmail.com')

    trinks.sendKeys('//*[@id="fSenha"]', '@mcdlemao0505')

    trinks.clickElement('//*[@id="login"]/div/div/form/div[3]/div[2]/button')

    trinks.clickElement('//*[@id="globalsite"]/section/nav/ul/li/div[5]/div[1]/a')

    trinks.clickElement('//*[@id="globalsite"]/section/nav/ul/li/div[5]/div[2]/ul[1]/li/a')

    trinks.clickElement('//*[@id="globalsite"]/section/nav/ul/li/div[5]/div[2]/ul[1]/li/ul/li[3]/a/span[2]')

    trinks.clickElement('/html/body/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/input')

    trinks.clickElement('//*[@id="ExportarRankingDeProfissionaisPopup"]/section/div/button[1]')

    trinks.clickElement('/html/body/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/input')

trinks_extract()
