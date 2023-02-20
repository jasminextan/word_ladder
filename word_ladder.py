#!/bin/python3


from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony',
    'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because
    the outputs are not unique.)
    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    HINT:
    See <https://github.com/mikeizbicki/cmc-csci046/issues/472>
    for a discussion about a common memory
    management bug that causes the
    generated word ladders to be too long in some cases.
    '''
    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)
    if start_word == end_word:
        return stack
    with open('words5.dict') as f:
        dictionary_file = [word.strip() for word in f]

    while len(queue) != 0:
        current_stack = queue.popleft()
        copy_dictionary = copy.copy(dictionary_file)
        for word in copy_dictionary:
            if _adjacent(word, current_stack[-1]) is True:
                if word == end_word:
                    current_stack.append(word)
                    return current_stack
                else:
                    copy_stack = copy.copy(current_stack)
                    copy_stack.append(word)
                    queue.append(copy_stack)
                    dictionary_file.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    adjacent = []
    for count, word in enumerate(ladder):
        if count == 0:
            adjacent.append(word)
        else:
            if _adjacent(word, ladder[count - 1]) is True:
                adjacent.append(word)
            else:
                return False
    if adjacent == ladder and len(ladder) != 0:
        return True
    else:
        return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) == len(word2):
        different = []
        for count, char in enumerate(word1):
            if word2[count] != char:
                different.append(word2[count])
        if len(different) == 1:
            return True
        else:
            return False
    else:
        return False
