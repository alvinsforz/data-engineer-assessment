#load libraries for web crawling
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import request
import re

#feed the list of addresses which contains targeted information into string array
siteName=['https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Ff2cc5978-e45c-4f28-b859-7f89221b0505&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fc6a26e11-bdf1-47a1-849d-fdcf819d458d&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F9bf4c8ea-e814-4772-ae31-0f29672dc497&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fc6e5e0e7-fa99-4f71-9fc1-9889d85282a5&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fe4c915ff-6c9c-4fa9-a8fb-09d0c67e30d4&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F7696b15a-c52e-4ac5-b38d-9eeb010c5fa3&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fbbd1fe06-1b55-4937-9317-fc162311ab38&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fb864c9a3-ef6e-46a0-a40c-66188f74dfa7&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F0b1d8dcb-d941-4d79-99bf-fc10c1806c43&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fb223f402-0318-4e27-8691-df6e7f7295d2&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F262f21a3-ae78-46f4-a5f9-5a1f502caa90&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fe44b2459-af5e-492d-9c57-d9c2e62944e7&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fcb3b2662-774a-4e6f-841e-f120244d7031&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F1de91afd-9da2-47ab-a7e7-19bf931709a4&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F86c892cf-09a3-44c8-b9d1-814d93dbcbb4&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fc94dc5b2-6b23-4915-8de5-a4e6ae86d802&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F4a3f40a8-0587-494c-b8d3-7098b8c5992f&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Ffdc8adfb-1807-4146-98ae-3a26fbe19996&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fbd5a2f44-fc06-45fd-909b-3a4001c8b8a3&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F35e67944-231e-4bc9-8c69-560f203167ff&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F555235ce-8c45-409b-a6c9-83e69c2d2bce&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F555235ce-8c45-409b-a6c9-83e69c2d2bce&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F404a50e9-61ce-448d-a695-bbfc697a0727&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F6cee3765-2b3b-48b0-af2b-1eb512d071fd&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fd63789ac-74b5-40e3-b890-685513c38e12&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F0ee67d5e-8de9-48f0-97c5-ba23d486b1e9&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F73c3f018-71ce-4dc1-abdd-14cea7873717&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F9e4269d5-e10e-4f49-ac99-65c833f933a2&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fa8d05b64-f60b-4dd9-91c2-e2e63d82f2f5&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F1fb92021-9576-4c85-8759-f6918e9f0ad4&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F190ec9a5-938c-45a5-bd9c-c12b1af33353&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fa2494c65-11a8-4853-9371-c89333c33be1&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Ff2413988-f76a-4636-a4b1-9952517aa21f&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F2ae275fe-4f11-4a38-9e95-d466d74b42a3&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F0752ed49-03e7-4d75-8314-a051b3771a1d&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F5c5b153e-4bf8-4f3d-973d-12fabf306d12&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fe9cf8b24-6b8b-47cc-9dd3-b601aa135960&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F93dfef83-579c-4bef-b0ba-d41ee9cbda85&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F544cd9cf-e2ee-4ac0-8a02-7147af6b97d7&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F0917ab6b-18a8-4cfd-8e7a-843b88cf9457&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F6c3fd65e-2d24-47d8-bc22-9e93512bdcc2&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F4be4ea31-1211-4f0c-82bb-f6fe10791f4d&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fc64a6e4e-5b38-4f93-b26d-aded817aeaf3&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F30f3ea93-882a-4525-841c-1d5b4b64076f&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Ff605bcd2-90b6-45a0-a558-d05016d68a77&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F7a3996d8-b90d-4b81-bd5e-e37f005b2683&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fd00b4607-c4fe-4f3e-8974-29401e23223c&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F4f49df98-98b8-4a9e-98ad-9c5557817eba&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fe246eca2-2cec-45b4-ae76-aa1f37d07bc5&conceptLanguage=en&full=true',
          'https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2Fc94f3565-d987-431f-a46b-6f4e018e0bd7&conceptLanguage=en&full=true']

#write data into csv file
filename = "joblist.csv"
f = open(filename, "w")
#create header for csv file
headers = "job_title, job_skills\n"
f.write(headers)

#loop the addresses
for s in siteName:
    #request to read the html
    uClient = uReq(s)
    page_html = uClient.read()
    uClient.close()
    #parse the html content
    page_soup = soup(page_html, "html.parser")
    #get the data inside the html body that contains content-container class
    containers = page_soup.findAll("div", {"class":"content-container"})
    #get the first element of the class
    container = containers[0]
    #get the data inside the container that contains has-tooltip class
    jobtitle_container = container.findAll("a", {"class":"has-tooltip"})
    #get the data inside the container that contains show-hand show-underline class
    skill_container = container.findAll("a", {"class":"show-hand show-underline"})
    #write the jobtitle and ten required skills
    f.write(jobtitle_container[4].text + "," + skill_container[0].text + "\n")
    f.write(jobtitle_container[4].text + "," + skill_container[1].text + "\n")
    f.write(jobtitle_container[4].text + "," + skill_container[2].text + "\n")
    f.write(jobtitle_container[4].text + "," + skill_container[3].text + "\n")
    f.write(jobtitle_container[4].text + "," + skill_container[4].text + "\n")
    f.write(jobtitle_container[4].text + "," + skill_container[5].text + "\n")
    f.write(jobtitle_container[4].text + "," + skill_container[6].text + "\n")
    f.write(jobtitle_container[4].text + "," + skill_container[7].text + "\n")
    f.write(jobtitle_container[4].text + "," + skill_container[8].text + "\n")
    f.write(jobtitle_container[4].text + "," + skill_container[9].text + "\n")
#close the file
f.close()
