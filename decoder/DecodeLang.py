class DecodeLang:
    
    alphabet_ordered = ('s','x','o','c','q','n','m','w','p','f','y','h','e','l','j','r','d','g','u','i')
    foo_letters = ('u','d','x','s','m','p','f')
    bar_letters = ('o','c','q','n','w','y','h','e','l','j','r','g','i')
    words = []
    
    def __init__(self, text):
        if text:
            self.words = text.lower().split()
            
    # prepositions are the words of exactly 6 letters which end in a foo letter and do not contain the letter u.
    def count_prepositions(self):
        try:
            filter_prepositions = filter(lambda x: len(x) == 6 and x.endswith(self.foo_letters) and 'u' not in x, self.words)
            print("1) There are %d prepositions in the text" % len(filter_prepositions))
            
        except Exception as e:
            raise e

    # verbs are words of 6 letters or more that end in a bar letter. 
    def is_verb(self, word):
        return True if len(word) >= 6 and word.endswith(self.bar_letters) else False

    # if a verb starts in a bar letter, then the verb is inflected in its subjunctive form
    def is_subjunctive_verb(self, word):
        return self.is_verb(word) and word.startswith(self.bar_letters)
        
    # verbs are words of 6 letters or more that end in a bar letter. Furthermore,
    # if a verb starts in a bar letter, then the verb is inflected in its subjunctive form
    def count_subjunctive_and_verbs(self):
        try:
            filter_subjunctive_forms = filter(self.is_subjunctive_verb, self.words)
            filter_verbs = filter(self.is_verb, self.words)
            print("2) There are %d verbs in the text" % len(filter_verbs))
            print("3) There are %d subjunctive verbs in the text" % len(filter_subjunctive_forms))
            
        except Exception as e:
            raise e

    # text are ordered by heroku's alphabetical language order
    def ordered_alphabetical(self):
        try:
            text_ordered = sorted(self.words, key=lambda x: [self.alphabet_ordered.index(c) for c in x])            
            print("4) Vocabulary list: %s " % text_ordered)
            
        except Exception as e:
            raise e
    
    # filter pretty numbers and count
    def count_distinct_pretty_numbers(self):
        try:
            word_to_numbers = map(self.word_to_number, self.words)
            #  Heruits consider a number to be pretty if it satisfies all of the following properties:
            # - it is greater than or equal to 81827
            # - it is divisible by 3
            filter_pretty_numbers = filter(lambda n: n >= 81827 and n % 3 == 0, word_to_numbers)
            print("5) There are %d distinct pretty numbers in the text" % len(filter_pretty_numbers))
            
        except Exception as e:
            raise e

    # alphabet starts with 0 and ends at 19 
    # words also represent numbers given in base 20, where each letter is a digit. The
    # digits are ordered from the least significant to the most significant, which is the opposite of
    # our system. That is, the leftmost digit is the unit, the second digit is worth 20, the third one is
    # worth 400, and so on and so forth.
    # value starts at 1, getting the position from character and multiply starting with value (1) after multiply the value by (x20)
    def word_to_number(self, word):
        number = 0
        value = 1
        try: 
            for char in word:
                number += self.alphabet_ordered.index(char) * value
                #print(char, number, str(self.alphabet_ordered.index(char)) + " * "+ str(value))
                value *= 20
            return number
        
        except Exception as e:
            raise e
        