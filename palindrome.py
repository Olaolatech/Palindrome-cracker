import string
def punct_free(world):
    # Turn all to lower case and remove extra space from the begining and the end
    world_n = world.strip().lower()
    excess_world = string.punctuation + " " # world and letters to remove
    punct_remove = "" # Subject it empty string
    for letter in world_n:
        if letter not in excess_world:
            punct_remove += letter
    return punct_remove

def panlindrome(world):
    reverse_world = punct_free(world)[::-1] # Calling the punct_free function & store the reverse in a variable
    return reverse_world == punct_free(world)
sent = "A man, a plan, a canal: Panama"
print(panlindrome(sent))