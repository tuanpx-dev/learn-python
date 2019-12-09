class Gurunavi:
    """
           店舗名     #ten cua hang
           郵便番号      #ma buu dien
           住所    #di chi
           電話番号 #so dien thoai
           FAX番号
           HP    #url
           メールアドレス
           営業時間
           定休日
           平均予算
           座席数
           最大宴会人数
           貸しきり人数
           個室情報
           追加メールアドレス
           追加電話番号
           追加FAX番号
       """

    __attrs__ = [
        '店舗名', '郵便番号', '住所', '電話番号', 'FAX番号',
        'HP', 'メールアドレス', '営業時間', '定休日', '平均予算',
        '座席数', '最大宴会人数', '貸しきり人数', '個室情報',
        '追加メールアドレス', '追加電話番号', '追加FAX番号'
    ]

    __object_import = ('店舗名', '住所', '電話番号', 'HP', 'メールアドレス')

    def __init__(self, **kwargs):
        adv = kwargs.get('adv', None)
        self.name = adv.get('店舗名')
        self.address = adv.get('住所')
        self.phone_number = adv.get('電話番号')
        self.url = adv.get('HP')
        self.email = adv.get('メールアドレス')
        self.csv_additional = self._csv_additional(adv)

    def _csv_additional(self, o):
        csv_external_fields = o
        for key in self.__object_import:
            csv_external_fields.pop(key, None)

        return csv_external_fields

    def __getstate__(self):
        return {
            attr: getattr(self, attr, None) for attr in self.__attrs__
        }


A = {
    "店舗名": "ten cua hang",
    "住所": "dia chi",
    "郵便番号": "ma buu dien",
    "電話番号": "sdt",
    "FAX番号": "so phach",
    "HP": "URL",
    "メールアドレス": "email",
    "営業時間": "thoi gian lam viec",
    "定休日": "ngay nghi",
    "平均予算": "ytuyt",
    "座席数": "huhuhu",
    "最大宴会人数": "dahsjd",
    "貸しきり人数": "dasdas",
    "個室情報": "dasdasd",
    "追加メールアドレス": "asdgsad",
    "追加電話番号": "dasda",
    "追加FAX番号": "dasdasd"
}

gu = Gurunavi(adv=A)

print(gu.csv_additional)
