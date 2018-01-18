# Longest-Palindromic-Substring

**Description:**

Given a string, this program returns a longest substring within that is a
valid palindrome. The program returns the first longest palindrome that it
finds. The program starts by searching through long substring possibilities
first, then immediately stopping upon finding a valid output.

The program searches down to a given length of letter-length-combinations, 
such as "bb" for a lowest length of 2, or "aba" for a lowest length of 3. For 
the sake of LeetCode compliance to instruction, the lowest-length is set to 1.
A valid palindrome set by another user may be set to higher limits.

**Example:** 
```
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
```

## Additional Details

The program runs through the test cases with a timer to check for efficiency.

## Sample Inputs and Runtimes

The run-time required to find the solution included is particular to the case involved, not particularly to sizes of problems. As programmed, each test-case below completes at an identical runtime each time, as tested on the system. The measurement in milliseconds represents the time for the goal-function of `longestPalindrome()` to return a palindrome.

**Case 1:** Multiple palindromes (0.001ms)
```
Given "dadijmom",
Return "dad".
```
**Case 2:** No palindromes (0.002ms)
```
Given "abcdefghi",
Return "NULL".
```
**Case 3:** 2-letter palindrome only (0.001ms)
```
Given "bbatom",
Return "bb".
```
**Case 4:** 3-letter palindrome only (0.001ms)
```
Given "tatabc",
Return "tat".
```
**Case 5:** 4-letter palindrome only. Shows even and odd palindromes (0.002)
```
Given "tootsieroll",
Return "toot".
```
**Case 6:** 20-letter given, with only one 3-letter palindrome (0.009ms)
```
Given "dadabcdefghijklmnopq",
Return "dad".
```
**Case 7:** 30-letter given, with only one 3-letter palindrome (0.02ms)
```
Given "momabcdefghijklmnopqrstuvwxyza",
Return "mom".
```
**Case 8:** 31-letter given, with only one 3-letter palindrome (0.022ms)
```
Given "momabcdefghijklmnopqrstuvwxyzab",
Return "mom".
```
**Case 9:** 945-letter given, with one 4-letter palindrome (37.037ms)
```
Given "esbtzjaaijqkgmtaajpsdfiqtvxsgfv...",
Return "yvvy".
```
**Case 10:** 1000-letter given, with one 4-letter palindrome (41.667ms)
```
Given "esbtzjaaijqkgmtaajpsdfiqtvxsgfv...",
Return "yvvy".
```

## Further Inquiry

- To develop this with an intent to have these methods be easily used within broader programs, such as pattern finding within very large sets.
- To count the number of palindromes.
- To remove or scramble the palindromes.
