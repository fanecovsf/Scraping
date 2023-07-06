import time
import os
import shutil

from link import Link

download_path = r'C:\Users\Catedral Barbearia\Downloads'

reports_path = r'C:\Users\Catedral Barbearia\OneDrive\Relatórios - BI'


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

time.sleep(10)

files_list = os.listdir(download_path)

report_list = os.listdir(reports_path)

for file in report_list:
    if 'rankingDeProfissionais.csv' in file:
        delete_path = os.path.join(reports_path, file)
        os.remove(delete_path)

    else:
        pass

for file in files_list:
    if 'rankingDeProfissionais.csv' in file:
        old_path = os.path.join(download_path, file)
        new_path = os.path.join(reports_path, file)
        shutil.move(old_path, new_path)
    
    else:
        pass

link.quitSite()
