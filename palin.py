def palindrome(list):
    if (len(list) == 1 or len(list) == 0):
        return True
    front = 0
    end = len(list)-1
    while (front < end):
        if (list[front] != list[end]):
            return False
        front = front + 1
        end = end - 1
    return True

