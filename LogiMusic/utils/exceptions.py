#
# Copyright (C) 2021-2022 by Logi_Help@Github, < https://github.com/LOGI-LAB >.
# @logi-channel in telegram





class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
