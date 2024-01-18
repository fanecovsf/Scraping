import time
import os
import shutil
import datetime

from link import Link


download_path = r'C:\Users\Catedral Barbearia\Downloads'

reports_path = r'C:\Users\Catedral Barbearia\OneDrive - Catedral Barbearia\Relatórios - BI'

def trinks_extract():
    hoje = datetime.date.today()
    hoje = datetime.date.strftime(hoje, '%d/%m/%Y')
    primeiro_dia = f"01/{str(hoje).split('/')[1]}/{str(hoje).split('/')[2]}"

    if str(hoje).split('/')[0] == '01':
        execute = False

    else:
        ultimo_dia = datetime.date.today() - datetime.timedelta(days=1)
        ultimo_dia = datetime.date.strftime(ultimo_dia, "%d/%m/%Y")
        data = f"{primeiro_dia}   {ultimo_dia}"
        execute = True

    if execute == True:
        trinks = Link("https://www.trinks.com/Login", "Chrome", sleep=1, headless=False)

        trinks.openLink()

        trinks.maximize()

        trinks.sendKeys('//*[@id="fEmail"]', 'matheus.cavichione@hotmail.com')

        trinks.sendKeys('//*[@id="fSenha"]', '@mcdlemao0505')

        trinks.clickElement('//*[@id="login"]/div/form/div[4]/button')

        time.sleep(5)

        trinks.clickElement('//*[@id="globalsite"]/section/nav/ul/li/div[5]/div[1]/a')

        trinks.clickElement('//*[@id="globalsite"]/section/nav/ul/li/div[5]/div[2]/ul[1]/li/a')

        trinks.clickElement('//*[@id="globalsite"]/section/nav/ul/li/div[5]/div[2]/ul[1]/li/ul/li[4]/a')

        trinks.clickElement('//*[@id="formFiltro"]/div/div[2]/div/button[1]')

        time.sleep(1)

        trinks.clearText('//*[@id="mapa-calor-filtro-periodo"]')
        trinks.clearField('//*[@id="mapa-calor-filtro-periodo"]')

        time.sleep(3)

        trinks.sendKeys('//*[@id="mapa-calor-filtro-periodo"]', data)

        trinks.clickElement('//*[@id="ext-gen1009"]/div[6]/div[4]/button[2]')

        trinks.clickElement('//*[@id="modalFiltro"]/div/div/div/div[5]/button[2]')

        time.sleep(3)

        trinks.clickElement('/html/body/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/input')

        trinks.clickElement('//*[@id="ExportarRankingDeProfissionaisPopup"]/section/div/button[1]')

        trinks.clickElement('/html/body/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/input')

        time.sleep(300)
        for file in os.listdir(reports_path):
            if 'rankingDeProfissionais' in file:
                os.remove(os.path.join(reports_path, file))

            else:
                pass

        time.sleep(2)

        for file in os.listdir(download_path):
            if 'rankingDeProfissionais' in file:
                shutil.move(os.path.join(download_path,file), reports_path)
                break

            else:
                pass

        trinks.quitSite()

    elif execute == False:
        pass



trinks_extract()
