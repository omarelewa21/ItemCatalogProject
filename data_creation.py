from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from database import Accessory, AccessorySection, SectionItem

engine = create_engine('sqlite:///mobilystore.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Accessories item categories
mobile_category = Accessory(name='MOBILE ACCESSORIES')
Computer_category = Accessory(name='COMPUTER ACCESSORIES')

session.add_all([mobile_category, Computer_category])
session.commit()

# Mobile accessory items
cables = AccessorySection(
    name='Cables', accessory=mobile_category)
chargers = AccessorySection(
    name='Chargers', accessory=mobile_category)
headsets = AccessorySection(
    name='Headsets', accessory=mobile_category)

session.add_all([cables, chargers, headsets])
session.commit()

# Computer accessory items
mouses = AccessorySection(
    name='Mouses', accessory=Computer_category)
keyboards = AccessorySection(
    name='Keyboards', accessory=Computer_category)
flash_drivers = AccessorySection(
    name='Flash Drivers', accessory=Computer_category)

session.add_all([mouses, keyboards, flash_drivers])
session.commit()

# Mobile Accessories
# Cables
cable1 = SectionItem(
    name='Remax',
    price='$3.99',
    description='AUX Metal Cable - 3.5mm - 100Cm Male To Male',
    image_url='img/cables/cable1.jpg',
    category=cables
    )
cable2 = SectionItem(
    name='Tronsmart',
    price='$9.99',
    description='Micro USB Cable - Black - 3 Pcs',
    image_url='img/cables/cable2.jpg',
    category=cables
    )
cable3 = SectionItem(
    name='Anker',
    price='$8.99',
    description='Powerline Micro USB 90 Cm - Black',
    image_url='img/cables/cable3.jpg',
    category=cables
    )
cable4 = SectionItem(
    name='Generic',
    price='$4.99',
    description='Cable Data And Charger USB For The C Mobile',
    image_url='img/cables/cable4.jpg',
    category=cables
    )
cable5 = SectionItem(
    name='Fashion',
    price='$4.99',
    description='3-IN-1 Quick Charger & Data Universal Cable - Silver',
    image_url='img/cables/cable5.jpg',
    category=cables
    )
cable6 = SectionItem(
    name='YK-S07',
    price='$11.99',
    description='YK-S07 Mobile Phone Cable - 1 M',
    image_url='img/cables/cable6.jpg',
    category=cables
    )

session.add_all([cable1, cable2, cable3, cable4, cable5, cable6])
session.commit()

# Chargers
charger1 = SectionItem(
    name='Generic',
    price='$7.99',
    description='Fast Charger Output 9V=2A USB Type C',
    image_url='img/chargers/charger1',
    category=chargers
    )
charger2 = SectionItem(
    name='LDNIO',
    price='$8.45',
    description='Charger - 6 Ports - 5.4amp',
    image_url='img/cables/cable2',
    category=chargers
    )
charger3 = SectionItem(
    name='Generic',
    price='$5.45',
    description='Wall Charger And Cable - Black',
    image_url='img/cables/cable3',
    category=chargers
    )
charger4 = SectionItem(
    name='Teeba',
    price='$5.45',
    description='Mobile Chager With 2 Ports',
    image_url='img/cables/cable4',
    category=chargers
    )
charger5 = SectionItem(
    name='LDNIO',
    price='$4.99',
    description='Dual USB Port Home Charger',
    image_url='img/cables/cable5',
    category=chargers
    )

session.add_all([charger1, charger2, charger3, charger4, charger5])
session.commit()

# Headsets
headset1 = SectionItem(
    name='Generic',
    price='$13.99',
    description='In Ear Hi-Res Audio Headphones With Mic - Black',
    image_url='img/headsets/headset1',
    category=headsets
    )
headset2 = SectionItem(
    name='Anker',
    price='$12.45',
    description='SoundBuds Verve Built-In Microphone',
    image_url='img/headsets/headset2',
    category=headsets
    )
headset3 = SectionItem(
    name='Remax',
    price='$6.99',
    description='RM-510 Concave-convex Design Earphone - Black',
    image_url='img/headsets/headset3',
    category=headsets
    )
headset4 = SectionItem(
    name='Generic',
    price='$7.45',
    description='Blutooth Earphone - Black',
    image_url='img/headsets/headset4',
    category=headsets
    )
headset5 = SectionItem(
    name='Remax',
    price='$19.99',
    description='RB-S10 Blutooth Sports Magnetic Headset - Black',
    image_url='img/headsets/headset5',
    category=headsets
    )
headset6 = SectionItem(
    name='Yison',
    price='$12.99',
    description='Celebrate A9 Wireless Headset Shocked Bass Headphone',
    image_url='img/headsets/headset6',
    category=headsets
    )

session.add_all([headset1, headset2, headset3, headset4, headset5, headset6])
session.commit()

# PC Accessories
# Mouses
mouse1 = SectionItem(
    name='zero',
    price='$3.99',
    description='USB Mouse',
    image_url='img/mouses/mouse1',
    category=mouses
    )
mouse2 = SectionItem(
    name='Acme',
    price='$6.99',
    description='MW10 sportfy Wireless Mouse',
    image_url='img/mouses/mouse2',
    category=mouses
    )
mouse3 = SectionItem(
    name='Atick',
    price='$5.00',
    description='Wireless Mouse - Red',
    image_url='img/mouses/mouse3',
    category=mouses
    )
mouse4 = SectionItem(
    name='zero',
    price='$2.99',
    description='ZR-150Mouse - Black',
    image_url='img/mouses/mouse4',
    category=mouses
    )
mouse5 = SectionItem(
    name='Microsoft',
    price='$10.00',
    description='Wireless Mobile Mouse 1850 - Blue',
    image_url='img/mouses/mouse5',
    category=mouses
    )

session.add_all([mouse1, mouse2, mouse3, mouse4, mouse5])
session.commit()

# Keyboards
keyboard1 = SectionItem(
    name='Microsoft',
    price='$16.00',
    description='Wireless All-in-one Media Keyboard',
    image_url='img/keyboards/keyboard1',
    category=keyboards
    )
keyboard2 = SectionItem(
    name='Generic',
    price='$13.45',
    description='G21 Gaming Keyboard Fast Like Mechanical Feeling USB Lighting',
    image_url='img/keyboards/keyboard2',
    category=keyboards
    )
keyboard3 = SectionItem(
    name='Fox',
    price='$11.00',
    description='ZYG-800-LED Back Light Gaming Keyboard',
    image_url='img/keyboards/keyboard3',
    category=keyboards
    )
keyboard4 = SectionItem(
    name='Golden King',
    price='$9.45',
    description='Gx-500 USB Keyboard & Mouse Combo',
    image_url='img/keyboards/keyboard4',
    category=keyboards
    )

session.add_all([keyboard1, keyboard2, keyboard3, keyboard4, keyboards])
session.commit()

# Flash Drivers
drive1 = SectionItem(
    name='Universal',
    price='$5.45',
    description='64GB USB 2.0 Flash Drive Memory Stick Pen Data Storage Thumb',
    image_url='img/flash-drivers/drive1',
    category=flash_drivers
    )
drive2 = SectionItem(
    name='Kingston',
    price='$7.65',
    description='32GB DataTraveler SWIVL USB 3.0 Flash Drive - DTSWIVL/32GB',
    image_url='img/flash-drivers/drive2',
    category=flash_drivers
    )
drive3 = SectionItem(
    name='Kingston',
    price='$5.00',
    description='16GB DataTraveler DTIG4 USB 3.0 Flash - DTIG4/16GB',
    image_url='img/flash-drivers/drive3',
    category=flash_drivers
    )
drive4 = SectionItem(
    name='Excepro',
    price='$17.45',
    description='''2 IN 1 OTG USB Flash Drive -
                    32GB For PC/IPhone With Touch Screen''',
    image_url='img/flash-drivers/drive4',
    category=flash_drivers
    )
drive5 = SectionItem(
    name='Kingston',
    price='$5.00',
    description='16GB DataTraveler 50 USB 3.1 Flash Drive',
    image_url='img/flash-drivers/drive5',
    category=flash_drivers
    )

session.add_all([drive1, drive2, drive3, drive4, drive5])
session.commit()
