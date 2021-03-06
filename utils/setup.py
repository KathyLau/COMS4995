import sqlite3
import csv
from geopy.geocoders import Nominatim

conn = sqlite3.connect('./data/shops.db', check_same_thread=False)
c = conn.cursor()


def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS shops
             (ID INT,
             NAME TEXT,
             IMAGE TEXT,
             TEXT TEXT,
             SERVICE TEXT,
             LOCATION TEXT,
             LAT INT,
             LON INT,
             TYPE TEXT);''')
    return True


def geo_loc(address):
    geolocator = Nominatim(user_agent="http")
    location = geolocator.geocode(address)
    try:
        return [location.latitude, location.longitude]
    except BaseException:  # dirty data
        return []


def generate_list(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        id = 0

        images = [
            "https://cdn.vox-cdn.com/thumbor/dIgp2rTgRWVe5RqZxsS6n2aWIik=/"
            "0x0:3200x2400/570x428/filters:focal(1344x944:1856x1456):no_up"
            "scale()/cdn.vox-cdn.com/uploads/chorus_image/image/63728608/Taco"
            "MapLittleTacoHouse.0.jpg",
            "https://cdn.vox-cdn.com/thumbor/7N-ELwR-aMgG-8gl8YmBE5YlZGY=/"
            "0x0:3200x2400/870x653/filters:focal(1344x944:1856x1456):no_ups"
            "cale()/cdn.vox-cdn.com/uploads/chorus_image/image/63728607/Taco"
            "MapGlorias.0.jpg",
            "https://cdn.vox-cdn.com/thumbor/9WZva7Fg4TeIWXDkzZSSK71y0UE=/"
            "0x0:2048x1360/870x653/filters:focal(861x517:1187x843):no_ups"
            "cale()/cdn.vox-cdn.com/uploads/chorus_image/image/66162713/Bi"
            "rriaTacos.0.jpg",
            "https://cdn.vox-cdn.com/thumbor/KcZGARj7ZLfVN_i9NHeziKdnkSk=/"
            "0x0:2048x1360/720x540/filters:focal(861x517:1187x843):no_ups"
            "cale()/cdn.vox-cdn.com/uploads/chorus_image/image/63728603/Taco"
            "MapSinaloense.0.jpg"]

        for row in reader:
            if row['Restaurant'] != "":
                address = geo_loc(row['Address'])
                if (len(address) == 0):
                    address = [0, 0]
                insert(id, row['Restaurant'], images[id % 4], row['Website'],
                       row['Service'], row['Borough'], address[0], address[1])
                id += 1


def countShopsInDB():
    c.execute('''SELECT COUNT(*) FROM shops''')
    num = c.fetchall()[0][0]
    return num


def insert(id, name, image, text, service, location, lat, lon):
    values = "INSERT INTO shops (ID, NAME, IMAGE, TEXT, SERVICE, LOCATION, LAT, LON, TYPE) \
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
    c.execute(values, (id, name, image, text, service, location, lat, lon,
                       "Restaurant"))
    conn.commit()


def selectdefaultshops():
    searchlist = []
    c.execute('SELECT * FROM shops WHERE ID <= 10;')
    rows = c.fetchall()
    for shop in rows:
        searchlist.append({
            "address": [shop[6], shop[7]],
            "id": shop[0],
            "image": shop[2],
            "name": shop[1],
            "service": shop[4],
            "text": shop[3],
            "location": shop[5],
            "type": "Restaurant"
        })
    return searchlist


def selectshopbyname(name):
    term = "%" + name + "%"
    c.execute('SELECT * FROM shops WHERE LOWER(name) LIKE ?', (term,))
    rows = c.fetchall()
    return rows


def selectshops(borough):
    term = "%" + borough + "%"
    c.execute('SELECT * FROM shops WHERE LOWER(location) LIKE ?', (term,))
    rows = c.fetchall()
    return rows


def selectshopbyid(id):
    c.execute('SELECT * FROM shops WHERE ID = ?', (id,))
    row = c.fetchone()
    return row


def updateshopbyname(id, newname):
    c.execute('UPDATE shops SET NAME = ? WHERE ID = ?', (newname, id,))
    conn.commit()


def updateshopbyservice(id, service):
    c.execute('UPDATE shops SET SERVICE = ? WHERE ID = ?', (service, id,))
    conn.commit()


def updateshopbytext(id, text):
    c.execute('UPDATE shops SET TEXT = ? WHERE ID = ?', (text, id,))
    conn.commit()


def updateshopbyimage(id, img):
    c.execute('UPDATE shops SET IMAGE = ? WHERE ID = ?', (img, id,))
    conn.commit()
