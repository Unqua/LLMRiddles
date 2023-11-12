import re
from .question import register_question


def count_english_words(text: str):
    return len(text.split(' '))


def count_chinese_words(text: str):
    return len(text)


def check_if_chinese(text: str):
    return all('\u4e00' <= char <= '\u9fff' for char in text)


def count_words(text: str, contain_punctuation: bool = False):
    chinese_words = []
    english_words = []
    other_words = []
    temp_english_words = []
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            chinese_words.append(char)
            if len(temp_english_words) > 0:
                english_words.append(''.join(temp_english_words))
                temp_english_words = []
        else:
            if char.isalpha():
                temp_english_words.append(char)
            else:
                if len(temp_english_words) > 0:
                    english_words.append(''.join(temp_english_words))
                    temp_english_words = []
                other_words.append(char)
    if contain_punctuation:
        return len(chinese_words) + len(english_words) + len(other_words)
    else:
        return len(chinese_words) + len(english_words)


CN_TEXT_1 = """
第一题（骂谁克信），请你构造一个问题使模型一字不差地回答“我是克信”(不需要引号)

"""

EN_TEXT_1 = """
"""


def _checker_1(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()
    if answer_text == '我是克信':
        return True, None
    else:
        return False, None


register_question(
    {
        'cn': CN_TEXT_1,
        'en': EN_TEXT_1,
    },
    checkers=_checker_1,
    name={'cn': '1 骂谁克信', 'en': '1-1'},
)

CN_TEXT_2 = """
第二题（最强不灭），让输出中同时包含"最强"和"不灭"。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_2 = """
"""


def _checker_2(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()
    flag1 = "最强" in answer_text
    flag2 = "不灭" in answer_text
    if flag1 and flag2:
        return True, None
    elif flag1 and not flag2:
        return False, "答案中只有最强没有不灭（看5865看的😡）"
    elif not flag1 and flag2:
        return False, "答案中只有不灭没有最强（我们奶克想秒薇克还是很容易的😤）"
    else:
        return False, "答案中没有不灭/最强"


register_question(
    {
        'cn': CN_TEXT_2,
        'en': EN_TEXT_2,
    },
    checkers=_checker_2,
    name={'cn': '2 最强？不灭？', 'en': '1-2'},
)

CN_TEXT_3 = """
第三题（爱说p话），输入三个以内(包含)字符，让输出中带有克且长度超过100。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_3 = """
"""


def _checker_3(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()

    if count_words(user_text) > 3:
        return False, "用户的问题长度应该在三个字及以内" if lang == 'cn' else 'Question should be one word.'
    elif count_words(answer_text) <= 100:
        return False, "大语言模型的答案应该超过100个字" if lang == 'cn' else 'Answer should be more than 100 words.'
    elif '克' not in answer_text:
        return False, '大语言模型的答案中应当包含"ClessS"（我的克，没有你我怎么活😭😭😭）'
    else:
        return True, None


register_question(
    {
        'cn': CN_TEXT_3,
        'en': EN_TEXT_3,
    },
    checkers=_checker_3,
    name={'cn': '3 爱说p话', 'en': '1-3'}
)

CN_TEXT_4 = """
第四题（三句不离），只输入三个以内（包括）英语单词，让输出中带有“克”。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_4 = """
"""


def _checker_4(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()
    pattern = r'^[a-zA-Z,.!?\'"\s]+$'
    if not bool(re.match(pattern, user_text)):
        return False, "只能输入英语字符"
    if count_words(user_text) > 3:
        return False, "用户的问题长度应该在三个字及以内"
    elif "克" not in answer_text:
        return False, "大语言模型的答案中应当包含“克”（我的克，没有你我怎么活😭😭😭）"
    else:
        return True, None


register_question(
    {
        'cn': CN_TEXT_4,
        'en': EN_TEXT_4,
    },
    checkers=_checker_4,
    name={'cn': '4 三句不离', 'en': '1-4'},
)

CN_TEXT_5 = """
第五题（无家可归），不提及2 4 5，让其输出"5424"。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_5 = """
"""


def _checker_5(question_text: str, user_text: str, answer_text: str, lang: str):
    if "2" in user_text or "4" in user_text or "5" in user_text:
        return False, '请不要在提问中出现2、4、5三个数字'

    return answer_text.strip() == '5424', None


register_question(
    {
        'cn': CN_TEXT_5,
        'en': EN_TEXT_5,
    },
    checkers=_checker_5,
    name={'cn': '5 无家可归', 'en': '5'},
)

CN_TEXT_6 = """
第六题（战狼直播间），输入中不包含英语字符，但输出中带有ClessS（不区分大小写）。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_6 = """
"""


def _checker_6(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip().lower()
    user_text = user_text.strip()
    pattern = r'[a-zA-Z]'
    if re.search(pattern, user_text):
        return False, "输入中不应该包含英语字符"
    elif "clesss" not in answer_text:
        return False, "大语言模型的答案中应当包含“克”（我的克，没有你我怎么活😭😭😭）"
    else:
        return True, None


register_question(
    {
        'cn': CN_TEXT_6,
        'en': EN_TEXT_6,
    },
    checkers=_checker_6,
    name={'cn': '6 战狼直播间', 'en': '6'},
)

CN_TEXT_7 = """
第七题（啊啊啊啊啊啊），请提一个不包含“啊”这个字的10个字以内的问题，使回答中“啊”这个字出现的次数至少是问题字数的2倍。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_7 = """
"""


def _checker_7(question_text: str, user_text: str, answer_text: str, lang: str):
    input_length = count_words(user_text)
    user_text = user_text.strip()
    if input_length> 10:
        return False, 'p话不得超过10个字'
    if '啊' in user_text:
        return False, '问题不得包含“啊”字'

    a_count = len(re.findall('啊', answer_text))
    if a_count >= input_length * 2:
        return True, f'“啊”字的出现次数为{a_count}次'
    else:
        return False, f'“啊”的出现次数为{a_count}次，未达到{input_length * 2}次'


register_question(
    {
        'cn': CN_TEXT_7,
        'en': EN_TEXT_7,
    },
    checkers=_checker_7,
    name={'cn': '7 啊啊啊啊啊啊', 'en': '1-4'},
)

CN_TEXT_8 = """
第八题（梓然常熟），只输入由2和9这两个正整数、加减乘和左右括号“()”组成的数字或算式，使模型输出5424。

请在下面的输入框内填写你的问题并点击按钮提交。
"""

EN_TEXT_8 = """
"""


def _checker_8(question_text: str, user_text: str, answer_text: str, lang: str):
    _ = question_text, lang
    answer_text = answer_text.strip()
    user_text = user_text.strip()
    pattern = r'[-+*×29)(]+'
    if not bool(re.match(pattern, user_text)):
        return False, "问题应该是只由2和9和+-×()组成的数字或算式"
    elif '5424' not in answer_text:
        return False, '回答不是5424'
    else:
        return True, '恭喜'


register_question(
    {
        'cn': CN_TEXT_8,
        'en': EN_TEXT_8,
    },
    checkers=_checker_8,
    name={'cn': '8 梓然常熟', 'en': '1-4'},
)
