from module.handler.enemy_searching import EnemySearchingHandler as EnemySearchingHandler_
from module.os_handler.assets import *


class EnemySearchingHandler(EnemySearchingHandler_):
    def is_in_map(self):
        return self.appear(IN_MAP) or self.appear(IN_MAP_OBSCURED)
