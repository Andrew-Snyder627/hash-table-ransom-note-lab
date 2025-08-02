def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    mag_counts = {}
    for char in magazine:
        mag_counts[char] = mag_counts.get(char, 0) + 1
    
    for char in ransomNote:
        if mag_counts.get(char, 0) == 0:
            return False
        mag_counts[char] -= 1

    return True


# Create an empty mag_counts dict
# Loop through magazine and count each letter
# Loop thorugh ransomNote:
    # If the letter is not in mag_counts or count is 0 -> return False
    # Otherwise, decrement the count in mag_counts
# Return True if all letters were accounted for.