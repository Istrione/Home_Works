# Задание №2

class Solution(object):

    def find_root(self, word, dict_set):
        for head in range(1, len(word)):
            if word[:head] in dict_set:
                return word[:head]
        return word

    def replace_words(self, dictionary, sentence):
        set_dict = set(dictionary)
        sentence_in_list = sentence.split(" ")

        return_list = [self.find_root(w, set_dict) for w in sentence_in_list]

        return " ".join(return_list)


sol = Solution()
print(sol.replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
