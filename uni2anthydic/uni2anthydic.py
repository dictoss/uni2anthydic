#!/usr/bin/env python3
#
# Copyright (C) 2020 Norimitsu Sugimoto
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import sys
from emoji_trans_ja import EMOJI_KANA_TRANS_TABLE

# emoji_trans_ja.EMOJI_KANA_TRANS_TABLE INDEX
EMOJI_KANA_TRANS_INDEX_SHORT_NAME = 0
EMOJI_KANA_TRANS_INDEX_JA_WORD_TYPE = 1
EMOJI_KANA_TRANS_INDEX_JA_WORD_KANA = 2

class EmojiCannaDic(object):
    def __init__(self):
        # emoji file
        self.codepoints_str = ""
        self.type_field = ""
        self.cldr_short_name = ""

        # cannadic format parameter
        self.japanese_kana = ""
        self.japanese_type = ""
        self.emoji = ""

        self.codepoints = []
        self.plane = 0

    def __init__(self, line):
        # emoji file
        self.codepoints_str = ""
        self.type_field = ""
        self.cldr_short_name = ""

        # cannadic format parameter
        self.japanese_kana = ""
        self.japanese_type = ""
        self.emoji = ""

        self.codepoints = []
        self.plane = 0

        #
        # parse line
        #
        _cols = line.split(";")
        
        # remove padding space.
        self.codepoints_str = _cols[0].strip()
        self.type_field = _cols[1].strip()
        
        # remove comment
        _tmp = _cols[2].strip().split("#")
        self.cldr_short_name = _tmp[0].strip()

        if ".." in self.codepoints_str:
            _pos = self.codepoints_str.split("..")

            if 4 < len(_pos[0]):
                self.plane = int(_pos[0][0])

            _start = int(_pos[0], 16)
            _end = int(_pos[1], 16)
            #print("{}, {}".format(_start, _end))

            for i in range(_start, _end + 1, 1):
                self.codepoints.append(i)
        elif " " in self.codepoints_str:
            # not yet implemented.
            pass
        else:
            self.codepoints.append(int(self.codepoints_str, 16))

    def __str__(self):
        return "{} {} {}".format(self.japanese_kana, self.japanese_type, self.emoji)

    def pickup_sequences(self):
        for c in EMOJI_KANA_TRANS_TABLE:
            if self.cldr_short_name == c[EMOJI_KANA_TRANS_INDEX_SHORT_NAME]:
                self.japanese_type = c[EMOJI_KANA_TRANS_INDEX_JA_WORD_TYPE]
                self.japanese_kana = c[EMOJI_KANA_TRANS_INDEX_JA_WORD_KANA]
                return True

        return False

    def dump_codepoints(self):
        for c in self.codepoints:
            # convert unicode to utf8.
            if 0 < c:
                _emoji = chr(c)
                print("{} {} {}".format(self.japanese_kana, self.japanese_type, _emoji))


def main(unicode_file_path):
    try:
        with open(unicode_file_path, "r", encoding="utf8") as f:
            while True:
                _line = f.readline()
                if _line:
                    _line = _line.strip()
                    if 0 == len(_line) or '#' == _line[0]:
                        continue
                    else:
                        #print(_line)
                        _canna_emoji = EmojiCannaDic(_line)

                        _b = _canna_emoji.pickup_sequences()
                        if _b:
                            _canna_emoji.dump_codepoints()
                else:
                    break
    except Exception as e:
        print(e)
        
    return 0


if '__main__' == __name__:
    _file_path = "./emoji-sequences.txt"

    if 1 < len(sys.argv):
        _file_path = sys.argv[1]

    _ret = main(_file_path)

    sys.exit(_ret)
