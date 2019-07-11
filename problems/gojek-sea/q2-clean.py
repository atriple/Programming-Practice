#function to count desired word in a string.
def count_all(str, word):
    count = 0
    itr = 0
    taken = set()
    while True :
        search = str.find(word, itr)
        taken.add(search)
        if search == -1:
            return count
        count = count + 1
        itr = search + 1
  
# TEST CASE
t = int(input())
for i in range(1, t + 1):
    N = int(input())
    M = int(input())

    # Adding word to grid
    words = []
    for j in range(0, N):
        words.append(input())

    W = input() #desired word to search
    not_palindrome = not(W == W[::-1]) #check 
    cnt = 0 # count total

    # Horizontal Search
    for str in words :
        cnt = cnt + count_all(str, W)
        if(not_palindrome):
            cnt = cnt + count_all(str[::-1], W) # reverse horizontal
    
    # Creating Vertical List
    v_words = []
    for x in range(0,M):
        v_word = ""
        for y in range(0,N):
            v_word = v_word + words[y][x]
        v_words.append(v_word)

    # Vertical Search
    for v_str in v_words :
        cnt = cnt + count_all(v_str, W)
        if (not_palindrome):
            cnt = cnt + count_all(v_str[::-1], W) # reverse vertical if it's not palindrome

    # Creating Diagonal List
    d_words = []
    # Upper echelon (including main diagonal if it's square grid)
    for x in range(0,M-1):
        itr_x = x
        itr_y = 0
        d_word = ""
        while (itr_x < M and itr_x >= 0) and (itr_y < N and itr_y >= 0):          
            d_word = d_word + words[itr_y][itr_x]
            itr_x = itr_x + 1
            itr_y = itr_y + 1
        d_words.append(d_word)

    # Opposite Upper Echelon
    for x in range(M-1,0,-1):
        itr_x = x
        itr_y = 0
        d_word = ""
        while (itr_x < M and itr_x >= 0) and (itr_y < N and itr_y >= 0):          
            d_word = d_word + words[itr_y][itr_x]
            itr_x = itr_x - 1 
            itr_y = itr_y + 1 
        d_words.append(d_word)

    # Lower echelon
    for y in range(1,N-1):
        itr_x = 0
        itr_y = y
        d_word = ""
        while (itr_x < M and itr_x >= 0) and (itr_y < N and itr_y >= 0):
            d_word = d_word + words[itr_y][itr_x]
            itr_x = itr_x + 1
            itr_y = itr_y + 1
        d_words.append(d_word)
    
    # Opposite Lower Echelon
    for y in range(1,N-1):
        itr_x = M-1
        itr_y = y
        d_word = ""
        while (itr_x < M and itr_x >= 0) and (itr_y < N and itr_y >= 0):
            d_word = d_word + words[itr_y][itr_x]
            itr_x = itr_x - 1
            itr_y = itr_y + 1
        d_words.append(d_word)

    # Diagonal Search
    for d_str in d_words :
        cnt = cnt + count_all(d_str, W)
        if (not_palindrome):
            cnt = cnt + count_all(d_str[::-1], W) # reverse vertical if it's not palindrome
    
    print("Case {}: {}".format(i, cnt))
        