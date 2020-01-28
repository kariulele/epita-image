import requests, zipfile, io

import xml.etree.ElementTree as ET
import pandas as pd
import dateutil as du

def get_gaz_price():
    gaz_url = 'https://donnees.roulez-eco.fr/opendata/jour'
    req = requests.get(gaz_url)
    z = zipfile.ZipFile(io.BytesIO(req.content))
    root = ET.XML(z.read(z.filelist[0].filename))
    res = []
    for element in root:
        cp = element.attrib['cp']
        try:
            lat = float(element.attrib['latitude'])
            lon = float(element.attrib['longitude'])
        except ValueError as ve:
            continue
        adresse = element.find('adresse').text
        ville = element.find('ville').text
        for p in element.findall('prix'):
            prix = int(p.attrib['valeur']) / 1000
            essence = p.attrib['nom']
            maj = du.parser.parse(p.attrib['maj'])
            res.append([adresse, cp, ville, lat, lon, essence, prix, maj])
    df = pd.DataFrame(res, columns=['adresse','cp','ville', 'latitude',
                                    'longitude', 'essence', 'prix', 'maj'])
    df = df[(df.latitude > 1000) & (df.longitude > 1000)]
    df.latitude /= 100000.
    df.longitude /= 100000.
    return df
