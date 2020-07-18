# uni2anthydic

- unicode emoji convert to anthy dictonary.

## purpose

- anthy's dictionary is cannadic format.
- this program convert to anthy's dictionary format from unicode.org emoji-sequences.
- If set output of this program your anthy's dictionary, you can input emoji at anthy.


## usage

`$ ./uni2anthydic.py unicode.org/Public/emoji/13.0/emoji-sequences.txt


## format of anthy's dictionary file.

- anthy's dictionarys format is cannadic.

    - 3 columns with space padding.
    - column 0
        - 読み（ひらがな）
    - column 1
        - 品詞
            - 例：#T35 #T30 #KK #JN #CN
    - column 2
        - 単語

- example

    - りんご #T35 🍏

## reference

- https://unicode.org/emoji/format.html
- https://unicode.org/emoji/charts/full-emoji-list.html
- https://unicode.org/Public/emoji/13.0/
