      # The main function
def main():
    print("Even" if is_even else "Odd")

def is_even(n):
    # could be more simpler
    if n % 2 == 0:
        return True     # is even
    else:
        return False

# don't call main
