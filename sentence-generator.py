# sentence-generator to generate simple sentences
# By Hannah Newman <HN860433@wcupa.edu>

import random
                                    # These are types of vocabulary for which I was unable to find
                                    # a reasonably long and useful list online.
verbs_tr = ["ate","killed","exploded","painted","loved","slapped","held","created","fed","opened","grabbed","admired","hugged","held","taught","poked","broke"]
verbs_itr = ["sang","ran","wrote","smiled","flew","studied","accelerated","screamed","laughed","floated","slept","played","died","painted","cried","worked"]
determiners = ["a(n)","the","her","his","that","their","this","some","our","your"]
prepositions = ["in","outside","through","for","against","above","below","around","despite","along"]

                                    # vocab lists from https://github.com/janester/mad_libs
adjFile = open("adjectives.txt")    # get adjectives
adjectives = adjFile.read().split("\n")

nounFile = open("nouns.txt")        # get nouns
nouns = nounFile.read().split("\n")

                                    # S() is the top-level sentence function
def S():
    res = NP() + " " + VP()         # every sentence has a noun phrase and a verb phrase
    if random.random() > 0.2:       # ~80% of the time, a prepositional phrase is added
        if random.random() > 0.5:
            res = res + " " + PP()  # ~50% of prepositional phrases come after the NP+VP
        else:
            res = PP() + ", " + res # ~50% of prepositional phrases come before
    return res.capitalize() + "."   # capitalizes sentence and adds period

def NP():                           # NP() creates a noun phrase
    res = ""
    if random.random() > .01:       # ~99% of noun phrases have a determiner
        res += det() + " "
    if random.random() > .7:        # ~30% of noun phrases have an adjective
        res += adj() + " "
    res += n()                      # adds the central noun to every noun phrase
    if random.random() > .95:       # ~5% of noun phrases have a recursive prepositional phrase
        res += " " +PP()
    return res                      # returns the result and ends the function

def VP():                           # VP() creates a verb phrase
    if random.random() > .5:        # ~50% of verb phrases are transitive and include a noun phrase
        return v_tr() + " " + NP()  # returns transitive verb + noun phrase
    else:
        return v_itr()              # returns intransitive verb by itself

def PP():                           # PP() creates a prepositional phrase
    return prep() + " " + NP()      # all prepositional phrases consist of a preposition and a noun phrase

def v_itr():                        # returns random intransitive verb
    return verbs_itr[random.randint(0,len(verbs_itr)-1)]
def v_tr():                         # returns random transitive verb
    return verbs_tr[random.randint(0,len(verbs_tr)-1)]
def n():                            # returns random noun
    return nouns[random.randint(0,len(nouns)-1)]
def adj():                          # returns random adjective
    return adjectives[random.randint(0,len(adjectives)-1)]
def det():                          # returns random determiner
    return determiners[random.randint(0,len(determiners)-1)]
def prep():                         # returns random preposition
    return prepositions[random.randint(0,len(prepositions)-1)]

for x in range(100):
    print(S())                      # generates and prints 100 sentences

