
class Word:
    def __init__(self, pinyin, chinese, definition):
        input_list = [pinyin, chinese, definition]
        decoded_list = [self.decode(val) for val in input_list]
        self.pinyin, self.chinese, self.definition = input_list
        self.pinyin_d, self.chinese_d, self.definition_d = decoded_list
        self.pinyin_l, self.chinese_l, self.definition_l = [len(val) for val in decoded_list]

    @classmethod
    def decode(cls, word):
        return word.decode("utf-8")

    @classmethod
    def min_lenght(cls, word, min_len=0):
        return word if min_len == 0 else word + " "*(min_len - len(word))

    def str_all(self, min_len=[0, 0]):
        pinyin = self.min_lenght(self.pinyin_d, min_len[0])
        chinese = self.min_lenght(self.chinese_d, min_len[1])
        space_before = " "*(min_len[1] - len(self.chinese_d))
        space_after = " "*len(self.chinese_d)
        string = '%s %s %s"%s"%s' % (pinyin, chinese, space_before, self.definition_d, space_after)
        return string

    def str_pinyin(self):
        return self.pinyin_d

    def str_chinese(self):
        return self.chinese_d + " "*len(self.chinese_d)

    def str_definition(self):
        return self.definition_d
