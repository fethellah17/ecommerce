from django import forms
from .models import ShippingAddress

# Algeria Wilayas (States)
ALGERIA_WILAYAS = [
    ('', 'Select Wilaya'),
    ('01', '01 - Adrar'),
    ('02', '02 - Chlef'),
    ('03', '03 - Laghouat'),
    ('04', '04 - Oum El Bouaghi'),
    ('05', '05 - Batna'),
    ('06', '06 - Béjaïa'),
    ('07', '07 - Biskra'),
    ('08', '08 - Béchar'),
    ('09', '09 - Blida'),
    ('10', '10 - Bouira'),
    ('11', '11 - Tamanrasset'),
    ('12', '12 - Tébessa'),
    ('13', '13 - Tlemcen'),
    ('14', '14 - Tiaret'),
    ('15', '15 - Tizi Ouzou'),
    ('16', '16 - Alger'),
    ('17', '17 - Djelfa'),
    ('18', '18 - Jijel'),
    ('19', '19 - Sétif'),
    ('20', '20 - Saïda'),
    ('21', '21 - Skikda'),
    ('22', '22 - Sidi Bel Abbès'),
    ('23', '23 - Annaba'),
    ('24', '24 - Guelma'),
    ('25', '25 - Constantine'),
    ('26', '26 - Médéa'),
    ('27', '27 - Mostaganem'),
    ('28', '28 - M\'Sila'),
    ('29', '29 - Mascara'),
    ('30', '30 - Ouargla'),
    ('31', '31 - Oran'),
    ('32', '32 - El Bayadh'),
    ('33', '33 - Illizi'),
    ('34', '34 - Bordj Bou Arréridj'),
    ('35', '35 - Boumerdès'),
    ('36', '36 - El Tarf'),
    ('37', '37 - Tindouf'),
    ('38', '38 - Tissemsilt'),
    ('39', '39 - El Oued'),
    ('40', '40 - Khenchela'),
    ('41', '41 - Souk Ahras'),
    ('42', '42 - Tipaza'),
    ('43', '43 - Mila'),
    ('44', '44 - Aïn Defla'),
    ('45', '45 - Naâma'),
    ('46', '46 - Aïn Témouchent'),
    ('47', '47 - Ghardaïa'),
    ('48', '48 - Relizane'),
    ('49', '49 - El M\'Ghair'),
    ('50', '50 - El Meniaa'),
    ('51', '51 - Ouled Djellal'),
    ('52', '52 - Bordj Badji Mokhtar'),
    ('53', '53 - Béni Abbès'),
    ('54', '54 - Timimoun'),
    ('55', '55 - Touggourt'),
    ('56', '56 - Djanet'),
    ('57', '57 - In Salah'),
    ('58', '58 - In Guezzam'),
]

# Delivery prices by Wilaya (in DA)
DELIVERY_PRICES = {
    '01': 1200,  # Adrar - far south
    '02': 600,   # Chlef
    '03': 900,   # Laghouat
    '04': 700,   # Oum El Bouaghi
    '05': 700,   # Batna
    '06': 600,   # Béjaïa
    '07': 800,   # Biskra
    '08': 1100,  # Béchar
    '09': 400,   # Blida - close to Algiers
    '10': 500,   # Bouira
    '11': 1200,  # Tamanrasset - far south
    '12': 800,   # Tébessa
    '13': 800,   # Tlemcen
    '14': 700,   # Tiaret
    '15': 500,   # Tizi Ouzou
    '16': 400,   # Alger - capital
    '17': 800,   # Djelfa
    '18': 600,   # Jijel
    '19': 600,   # Sétif
    '20': 800,   # Saïda
    '21': 700,   # Skikda
    '22': 800,   # Sidi Bel Abbès
    '23': 700,   # Annaba
    '24': 700,   # Guelma
    '25': 600,   # Constantine
    '26': 500,   # Médéa
    '27': 700,   # Mostaganem
    '28': 700,   # M'Sila
    '29': 700,   # Mascara
    '30': 1000,  # Ouargla
    '31': 700,   # Oran
    '32': 1000,  # El Bayadh
    '33': 1200,  # Illizi - far south
    '34': 600,   # Bordj Bou Arréridj
    '35': 400,   # Boumerdès - close to Algiers
    '36': 800,   # El Tarf
    '37': 1200,  # Tindouf - far west
    '38': 700,   # Tissemsilt
    '39': 900,   # El Oued
    '40': 800,   # Khenchela
    '41': 800,   # Souk Ahras
    '42': 400,   # Tipaza - close to Algiers
    '43': 600,   # Mila
    '44': 500,   # Aïn Defla
    '45': 1000,  # Naâma
    '46': 800,   # Aïn Témouchent
    '47': 1000,  # Ghardaïa
    '48': 700,   # Relizane
    '49': 1000,  # El M'Ghair
    '50': 1100,  # El Meniaa
    '51': 900,   # Ouled Djellal
    '52': 1200,  # Bordj Badji Mokhtar - far south
    '53': 1100,  # Béni Abbès
    '54': 1100,  # Timimoun
    '55': 900,   # Touggourt
    '56': 1200,  # Djanet - far south
    '57': 1200,  # In Salah - far south
    '58': 1200,  # In Guezzam - far south
}

# Municipalities by Wilaya (sample - main communes for each wilaya)
MUNICIPALITIES = {
    '01': ['Adrar', 'Reggane', 'Aoulef', 'Timimoun', 'Zaouiet Kounta'],
    '02': ['Chlef', 'Ténès', 'El Karimia', 'Oued Fodda', 'Boukadir'],
    '03': ['Laghouat', 'Aflou', 'Ksar El Hirane', 'Hassi R\'Mel'],
    '04': ['Oum El Bouaghi', 'Aïn Beïda', 'Aïn M\'lila', 'Sigus'],
    '05': ['Batna', 'Barika', 'Aïn Touta', 'N\'Gaous', 'Merouana'],
    '06': ['Béjaïa', 'Akbou', 'El Kseur', 'Sidi Aïch', 'Kherrata'],
    '07': ['Biskra', 'Tolga', 'Ouled Djellal', 'Sidi Okba', 'El Kantara'],
    '08': ['Béchar', 'Kenadsa', 'Abadla', 'Beni Ounif'],
    '09': ['Blida', 'Boufarik', 'El Affroun', 'Mouzaïa', 'Oued El Alleug'],
    '10': ['Bouira', 'Lakhdaria', 'Sour El Ghozlane', 'M\'Chedallah'],
    '11': ['Tamanrasset', 'In Salah', 'In Guezzam', 'Abalessa'],
    '12': ['Tébessa', 'Bir El Ater', 'Cheria', 'El Aouinet', 'Ouenza'],
    '13': ['Tlemcen', 'Maghnia', 'Ghazaouet', 'Remchi', 'Nedroma'],
    '14': ['Tiaret', 'Frenda', 'Sougueur', 'Mahdia', 'Ksar Chellala'],
    '15': ['Tizi Ouzou', 'Azazga', 'Draâ El Mizan', 'Larbaâ Nath Irathen', 'Aïn El Hammam'],
    '16': ['Alger Centre', 'Bab El Oued', 'Hussein Dey', 'El Harrach', 'Bir Mourad Raïs', 'Kouba', 'Hydra', 'Dély Ibrahim', 'Chéraga', 'Draria', 'Bab Ezzouar', 'Dar El Beïda', 'Rouiba', 'Reghaia'],
    '17': ['Djelfa', 'Messaad', 'Aïn Oussera', 'Hassi Bahbah'],
    '18': ['Jijel', 'El Milia', 'Taher', 'Chekfa', 'Ziama Mansouriah'],
    '19': ['Sétif', 'El Eulma', 'Aïn Oulmene', 'Bougaa', 'Aïn Arnat'],
    '20': ['Saïda', 'Aïn El Hadjar', 'Youb', 'El Hassasna'],
    '21': ['Skikda', 'Azzaba', 'El Harrouch', 'Collo', 'Tamalous'],
    '22': ['Sidi Bel Abbès', 'Telagh', 'Aïn El Berd', 'Sfisef'],
    '23': ['Annaba', 'El Bouni', 'El Hadjar', 'Berrahal', 'Seraïdi'],
    '24': ['Guelma', 'Oued Zenati', 'Bouchegouf', 'Héliopolis'],
    '25': ['Constantine', 'El Khroub', 'Aïn Smara', 'Hamma Bouziane', 'Didouche Mourad'],
    '26': ['Médéa', 'Berrouaghia', 'Ksar El Boukhari', 'Tablat'],
    '27': ['Mostaganem', 'Aïn Tédelès', 'Sidi Ali', 'Hassi Mameche'],
    '28': ['M\'Sila', 'Bou Saâda', 'Sidi Aïssa', 'Aïn El Melh'],
    '29': ['Mascara', 'Sig', 'Mohammadia', 'Tighennif', 'Ghriss'],
    '30': ['Ouargla', 'Hassi Messaoud', 'Touggourt', 'Taibet'],
    '31': ['Oran', 'Es Sénia', 'Bir El Djir', 'Aïn Turk', 'Arzew', 'Bethioua'],
    '32': ['El Bayadh', 'Bougtob', 'El Abiodh Sidi Cheikh'],
    '33': ['Illizi', 'Djanet', 'In Amenas', 'Bordj Omar Driss'],
    '34': ['Bordj Bou Arréridj', 'Ras El Oued', 'Bir Kasdali', 'El Achir'],
    '35': ['Boumerdès', 'Bordj Menaïel', 'Dellys', 'Khemis El Khechna', 'Thénia'],
    '36': ['El Tarf', 'El Kala', 'Bouteldja', 'Ben M\'Hidi'],
    '37': ['Tindouf'],
    '38': ['Tissemsilt', 'Bordj Bou Naama', 'Theniet El Had', 'Lardjem'],
    '39': ['El Oued', 'Guemar', 'Debila', 'Robbah', 'Bayadha'],
    '40': ['Khenchela', 'Kaïs', 'Chechar', 'El Hamma'],
    '41': ['Souk Ahras', 'Sedrata', 'M\'Daourouch', 'Taoura'],
    '42': ['Tipaza', 'Cherchell', 'Koléa', 'Hadjout', 'Bou Ismaïl'],
    '43': ['Mila', 'Chelghoum Laïd', 'Ferdjioua', 'Grarem Gouga'],
    '44': ['Aïn Defla', 'Khemis Miliana', 'El Attaf', 'Miliana'],
    '45': ['Naâma', 'Mécheria', 'Aïn Sefra', 'Moghrar'],
    '46': ['Aïn Témouchent', 'El Malah', 'Hammam Bou Hadjar', 'Beni Saf'],
    '47': ['Ghardaïa', 'Metlili', 'Berriane', 'El Guerrara'],
    '48': ['Relizane', 'Oued Rhiou', 'Mazouna', 'Mendes'],
    '49': ['El M\'Ghair', 'Djamaa', 'Sidi Khellil'],
    '50': ['El Meniaa', 'Hassi Gara'],
    '51': ['Ouled Djellal', 'Sidi Khaled', 'Doucen'],
    '52': ['Bordj Badji Mokhtar', 'Timiaouine'],
    '53': ['Béni Abbès', 'El Ouata', 'Igli'],
    '54': ['Timimoun', 'Charouine', 'Ouled Saïd'],
    '55': ['Touggourt', 'Temacine', 'Megarine'],
    '56': ['Djanet', 'Bordj El Haouès'],
    '57': ['In Salah', 'In Ghar', 'Foggaret Ezzaouia'],
    '58': ['In Guezzam', 'Tin Zaouatine'],
}


class ShippingForm(forms.ModelForm):
    state = forms.ChoiceField(
        choices=ALGERIA_WILAYAS,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_state'
        })
    )
    
    city = forms.ChoiceField(
        choices=[('', 'Select Municipality')],
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_city'
        })
    )
    
    class Meta:
        model = ShippingAddress
        fields = ['phone', 'state', 'city']
        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '0XX XX XX XX XX',
                'type': 'tel'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # If form has data, populate city choices
        if 'state' in self.data:
            state_code = self.data.get('state')
            if state_code in MUNICIPALITIES:
                self.fields['city'].choices = [('', 'Select Municipality')] + [
                    (m, m) for m in MUNICIPALITIES[state_code]
                ]
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.country = 'Algeria'
        instance.address = ''  # Set empty address
        if commit:
            instance.save()
        return instance
