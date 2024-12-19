from enum import Enum

class standardactions(Enum):
    FEAR : 0
    PUSH : 1
    GATHER : 2
    DAMAGE : 3
    DEFEND : 4
    REMOVE_ENTITY : 5 #ex: sacriface a dahan
    ADD_ENTITY : 6
    DAMAGE_PER_ENTITY : 7
    SKIP_ATTACK : 8
    CONDITION_LAND : 9 #action conditional of land
    REPLACE_ENTITY : 10
    DAMAGE_PER_ADJACENT_ENTITY : 11 #X amount of damage per entity adjacent to targe land
    DAMAGE_TO_EACH_INVADER: 12
    IF_CONDITION : 13
    OR_CONDITION : 14
