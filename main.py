def clean_string(dirty_str):
  cleaned_string = ""
  for element in dirty_str:
    if element.isalpha():
      cleaned_string = cleaned_string + element.lower()
  return cleaned_string


def isPalindrome(input_str):
  # considering only alphanumeric characters and ignoring cases
  #determine if the string is a palindrome
  cleaned_string = clean_string(input_str)# O(n)

  # is the string the same forward and backwards?
  if cleaned_string == cleaned_string[::-1]:# O(n)
    return 1
  
  return 0 # O(2n) with 4x space complexity

print(isPalindrome("otto"))
print(isPalindrome("abc"))
print(isPalindrome("A man, a plan, a canal, Panama."))