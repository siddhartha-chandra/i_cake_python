# Million Gazillion - Memory efficient web crawler
class Trie:

    def __init__(self):
        self.root_node = {}

    def check_present_and_add(self, word):
        current = self.root_node
        is_new_word = False

        for character in word:
            if character not in current:
                current[character] = {}
                is_new_word = True
            current = current[character]

        if '**' not in current:
            is_new_word = True
            current['**'] = {}

        return is_new_word


trie = Trie()
trie.root_node = {'w': {}}
trie.root_node['w']['w'] = {}
trie.root_node['w']['w']['h'] = {}
trie.root_node['w']['w']['w'] = {}
trie.root_node['w']['w']['w']['**'] = {}

print "Is new word: %s"  % trie.check_present_and_add('www')
