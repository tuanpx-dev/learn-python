class LookupDict(dict):
    """Dictionary lookup object."""

    def __init__(self, name=None):
        self.name = name
        super(LookupDict, self).__init__()

    def __repr__(self):
        return '<lookup \'%s\'>' % (self.name)

    def __getitem__(self, key):
        # We allow fall-through here, so values default to None

        return self.__dict__.get(key, None)

    def get(self, key, default=None):
        return self.__dict__.get(key, default)


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

a = LookupDict(A)
print(a)
print(a.__getitem__('店舗名'))
