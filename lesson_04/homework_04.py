import string


adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with-and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 01-03
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())

# task 04
print("Task 04")
print(adwentures_of_tom_sawer.count("h"))

# task 05
capitalized_words_count = 0

for word in adwentures_of_tom_sawer.split():
    cleaned_word = word.strip(string.punctuation)

    if cleaned_word and cleaned_word[0].isupper():
        capitalized_words_count += 1

print("\nTask 05")
print(capitalized_words_count)

# task 06
first_tom_position = adwentures_of_tom_sawer.find("Tom")
second_tom_position = adwentures_of_tom_sawer.find("Tom", first_tom_position + 1)

print("\nTask 06")
print(second_tom_position)

# task 07
adwentures_of_tom_sawer_sentences = [
    sentence.strip()
    for sentence in adwentures_of_tom_sawer.split(".")
    if sentence.strip()
]

# task 08
print("\nTask 08")
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
starts_with_by_the_time = any(
    sentence.startswith("By the time")
    for sentence in adwentures_of_tom_sawer_sentences
)

print("\nTask 09")
print(starts_with_by_the_time)

# task 10
last_sentence_words_count = len(adwentures_of_tom_sawer_sentences[-1].split())

print("\nTask 10")
print(last_sentence_words_count)
