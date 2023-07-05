import time

from link import Link


link = Link("https://www.trinks.com/Login", "Chrome", sleep=1, headless=False)

link.openLink()

link.maximize()

link.sendKeys('//*[@id="fEmail"]', 'matheus.cavichione@hotmail.com')

link.sendKeys('//*[@id="fSenha"]', '@mcdlemao0505')

link.clickElement('//*[@id="login"]/div/div/form/div[3]/div[2]/button')

link.clickElement('//*[@id="globalsite"]/section/nav/ul/li/div[5]/div[1]/a')

link.clickElement('//*[@id="globalsite"]/section/nav/ul/li/div[5]/div[2]/ul[1]/li/a')

link.clickElement('//*[@id="globalsite"]/section/nav/ul/li/div[5]/div[2]/ul[1]/li/ul/li[3]/a/span[2]')

link.clickElement('/html/body/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/input')

link.clickElement('//*[@id="ExportarRankingDeProfissionaisPopup"]/section/div/button[1]')

link.clickElement('/html/body/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/input')

time.sleep(3000)
