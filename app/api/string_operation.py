class string_operation:
    def __init__(self):
        pass
    @classmethod
    def find_a_string(cls,string,sub_string):    #https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
        len_group = len(sub_string)
        counter = 0
        for i in range(0, len(string)):
            each_group = string[i:i + len_group]
            if each_group == sub_string:
                counter += 1
        return counter
    @staticmethod
    def merge_the_tools(input_string, k):   #https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

        new_list = []
        list_group = []
        start_over = 0
        for i in list(input_string):
            list_group.append(i)

            start_over += 1
            if start_over == int(k):
                start_over = 0
                new_list.append(list_group)
                list_group = []

        for each_group in new_list:
            each_line = []
            for each_letter in each_group:
                if each_letter not in each_line:
                    each_line.append(each_letter)
                    a = "".join(each_line)
            print(a)
    @classmethod
    def the_minion_game(cls,input_string):  #https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
        vowels = "AEIOU"
        kevin_score = 0
        stuart_score = 0
        length = len(input_string)

        for i in range(0,length):
            if input_string[i] in vowels:
                kevin_score += length - i
            else:
                stuart_score += length - i

        if stuart_score > kevin_score:
            print("Stuart", stuart_score)
        elif kevin_score > stuart_score:
            print("Kevin", kevin_score)
        else:
            print("Draw")






if __name__ == "__main__":
    #print(string_operation.find_a_string("ABCDCDC","CDC"))
    print(string_operation.merge_the_tools("AABCAAADA", 3))
    print(string_operation.the_minion_game("BANANA"))

