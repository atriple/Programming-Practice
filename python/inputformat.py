t = int(input())
for i in range (1, t+1):
    # WRITE YOUR INPUT SETUP, below will be some of its examples
    x = input() # Single Input, you can assign it to int() function if you want to ensure it is integer
    a, b = [int(s) for s in input().split(" ")] # input 2 integer in a line that separated with space, assign it to a and b
    list = [int(s) for s in input().split(" ")]  # read whatever many integer you write in a line

    # Trivia : Most of the time you either will handle Integer or String input in Competitive Programming

    # WRITE YOUR CODE HERE

    print("Case #{}: {}".format(i, output)) #OUTPUT, you might need to modify it if it produce >1 output