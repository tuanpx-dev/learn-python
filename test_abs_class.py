'''
ワクワクで取り扱うエラー定義全般
'''


class WakpyError(Exception):
    CODE = 'E9999'
    MESSAGE = 'サーバーでエラーが発生しました'

    def __init__(self, *args, **kwargs):
        self.code = kwargs.pop('code', self.CODE)
        self.msg = kwargs.pop('msg', self.MESSAGE)

    def as_dict(self):
        '''辞書型に変換する'''
        return dict(code=self.code, msg=self.msg)

    def __str__(self):
        return 'Error: {}, Message: {}'.format(self.code,
                                               self.msg)


class ServerError(WakpyError):
    '''予期せぬエラー'''
    pass


class CompoundError(Exception):
    '''複数のエラーを表現するクラス'''

    def __init__(self, *exceptions):
        self._inner_exceptions = []
        for e in exceptions:
            self.append(e)

    def has(self, exception_type):
        '''
        該当するエラー型が存在するか

        :param exception_type: エラー型（オブジェクトではない）
        :return: True：存在する, False：存在しない
        '''
        return self.get(exception_type) is not None

    def get(self, exception_type):
        '''
        該当するエラー型が存在したら取り出す

        :param exception_type: エラー型（オブジェクトではない）
        :return: None：存在しない場合、WakpyError：存在する場合
        '''

        def _has_exception_type(e):
            return isinstance(e, exception_type)

        hits = filter(_has_exception_type, self._inner_exceptions)
        return next(hits) if len(hits) > 0 else None

    def exists(self):
        '''エラーが存在するか確認する'''
        return len(self._inner_exceptions) > 0

    def append(self, exception):
        '''返却エラーを付け足す。

        .. code::

            errors = CompondError()
            if validation1:
                errors.append(NanigashiError())
            if validation2:
                errors.append(SoregashiError())
            if errors.exists():
                # エラーが1つでも存在したらスローする
                raise errors
        '''
        self._inner_exceptions.append(exception)
        return self

    def as_array_dict(self):
        '''
        辞書型でエラー配列を返す。
        JSONレスポンス生成に利用。
        '''
        return [e.as_dict() for e in self._inner_exceptions if hasattr(e, 'as_dict')]

    def __str__(self):
        return '\t'.join([str(e) for e in self._inner_exceptions])


class AbstractTest(object):

    def __init__(self):
        self._errors = []

    @property
    def expire_at(self):
        return None

    @property
    def created_at(self):
        return None

    @property
    def member(self):
        return None

    @property
    def errors(self):
        return [e.as_dict() for e in self._errors]


class AuthTokenInvalidError(WakpyError):
    '''不正トークンエラー'''
    CODE = 'E00003'
    MESSAGE = '不正なアクセスです。'


class UnauthorizedToken(AbstractTest):

    def __init__(self, *errors):
        self._errors = errors


auth = None
if auth is None:
    print(UnauthorizedToken(AuthTokenInvalidError()))
