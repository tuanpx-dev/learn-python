from enum import Enum

from django.db import models


class Types(Enum):
    '''
    定義 = (action_type, limit_count)
    '''
    # action_typeの定義
    XmasCampaign2018 = (1, 1)
    NewYear2019 = (2, 1)
    ShowEncounterPopUp = (3, 1)
    FreeMailPopUp = (4, 1)
    XmasCampaign2019 = (5, 1)
    ShowBeautyFeaturePopUp = (8, 1)
    CommunityWebTutorial = (100, 1)

    @classmethod
    def from_action_type(cls, action_type):
        for v in cls.__members__.values():
            if v.value[0] == action_type:
                next(v)


action_type = Types.from_action_type(9)
print(action_type)
