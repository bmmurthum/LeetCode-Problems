/* 

Problem from LeetCode - https://leetcode.com/problems/longest-palindromic-substring/

@author - Brendon Murthum
@version - January 2018

Given a string, this program returns a longest substring within that is a
valid palindrome. The program returns the first longest palindrome that it
finds. The program starts by searching through long substring possibilities
first, then immediately stopping upon finding a valid output.

- The program searches down to a given length of letter-length-combinations, 
  such as "bb" for a lowest length of 2, or "aba" for a lowest length of 3. For 
  the sake of LeetCode compliance to instruction, the lowest-length is set to 1.
  A valid palindrome set by another user may be set to higher limits.

Example:
Given "apple", the program returns "pp" because starting from longer potential
palindromes within the string, "pp" is the first valid palindrome that it found.

Case 1: Multiple palindromes.
  Given "dadijmom",
  Return "dad".

Case 2: No palindromes.
  Given "abcdefghi",
  Return "NULL".
  
Case 3: 2-letter palindrome only.
  Given "bbatom",
  Return "bb".

Case 4: 3-letter palindrome only.
  Given "tatabc",
  Return "tat".

Case 5: 4-letter palindrome only, to test even and odd difference.
  Given "tootsieroll",
  Return "toot".

Case 6: 20-letter given, with only one 3-letter palindrome.
  Given "dadabcdefghijklmnopq",
  Return "dad".

Case 7: 30-letter given, with only one 3-letter palindrome.
  Given "momabcdefghijklmnopqrstuvwxyza",
  Return "mom".

Case 8: 31-letter given, with only one 3-letter palindrome.
  Given "momabcdefghijklmnopqrstuvwxyzab",
  Return "mom".

Case 9: 945-letter given. Issue with Leetcode, "Time Limit Exceeded" at 71ms. 
Changing isPalindrome() to accept a reference, cut this to 37ms. This is due to 
the friction caused by interacting with memory.
  Given "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksno",
  Return "yvvy".

Case 10: 1000-letter given.
  Given "esbtzjaaijqk...",
  Return "yvvy".

*/

#include <string>
#include <iostream>
#include <time.h>
#include <math.h>

using namespace std;

/* This class is in format of LeetCode's assigned problem. */
class Solution {
    public:
        /* This returns the longest palindrome within the string. */
        string longestPalindrome(string s) {
            /** The length of the input string. */
            int stringLength = s.length();
            /** Helper string in the following loop. */
            string tempString;
            /** The lowest valid length of palindrome to search for. */
            int lowestValidLength = 2;
            
            /* Trialing smaller substrings, starting at largest. */
            /* "i" is equal to the length of string to search for possibles. */
            for (int i = stringLength; i >= lowestValidLength; i--) {
            
                /* "j" is the index of the character to start on. */
                for (int j = 0; j < (stringLength - i + 1); j++) {
                    
                    /* Grabs the string starting at j, length i. */
                    tempString = s.substr(j,i);
                
                    if (isPalindrome(tempString)) {
                        return tempString;
                    }
                }
            }
            
            /*
             As per my desire. If no valid combination at the length of the
             given "lowestValidLength", this program the string "NULL" to 
             signify no palindromes within the original string. 
            */
            return "NULL";
        }
        
        /* Returns TRUE if the string is a palindrome. FALSE, otherwise. */
        bool isPalindrome(string &t) {
            /** The length of the given string. */
            int stringLength = t.length();
            
            /* 
             See if the first letter matches the last letter. Come inwards from
             there. If one doesn't match, stop searching, return false.
            */
            for (int i = 0; i < (stringLength / 2); i++) {
                if (t[i] != t[stringLength - 1 - i]) {
                    /* For debugging. */
                    // cout << "Failure: " << t << "\n";
                    return false;
                }
            }
            /* For debugging. */
            // cout << "Success: " << t << "\n"     ;
            return true;
        }
};


int main(int argc, char** argv) {

    /* Initial text given to the terminal. */
    cout << "\n" << "Initializing the palindrome finder.." << "\n";
    cout << "\n";
    cout << "This program will run each test a multitude of times, each \n" <<
            "within the period of a second. This is to find the runtime \n"<<
            "in an order of milliseconds. \n"; 
    cout << "\n";
    
    /** Case-1 String. */
    string testString1("dadijmom");
    /** Case-2 String. */
    string testString2("abcdefghi");
    /** Case-3 String. */
    string testString3("bbatom");
    /** Case-4 String. */
    string testString4("tatabc");
    /** Case-5 String. */
    string testString5("tootsieroll");
    /** Case-6 String. */
    string testString6("dadabcdefghijklmnopq");
    /** Case-7 String. */
    string testString7("momabcdefghijklmnopqrstuvwxyza");
    /** Case-8 String. */
    string testString8("momabcdefghijklmnopqrstuvwxyzab");
    /** Case-9 String. */
    string testString9("esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksno");
    /** Case-10 String. */
    string testString10("esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnovpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquh");

    /* Used for showing results of tests. */
    string output;
    /* Initialize an object for testing. This uses leetcode's format. */
    Solution solutionObject;
    /* Timer of a case-test. */
    clock_t t;
    /* Time converted to milliseconds. */
    float timeInMilliseconds;
    /* Counted iterations of the line to be tested. */
    int iterationsOfLines;
    
    
    // Case 1
    cout << "Case 1: " << testString1 << "\n";
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.longestPalindrome(testString1);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    cout << "Iterations: " << iterationsOfLines << "\n"; 
    cout << "Output: " << output << "\n";
    cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
    
    
    // Case 2
    cout << "Case 2: " << testString2 << "\n";
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.longestPalindrome(testString2);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    cout << "Iterations: " << iterationsOfLines << "\n"; 
    cout << "Output: " << output << "\n";
    cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
    
    
    // Case 3
    cout << "Case 3: " << testString3 << "\n";
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.longestPalindrome(testString3);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    cout << "Iterations: " << iterationsOfLines << "\n"; 
    cout << "Output: " << output << "\n";
    cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
    
    
    // Case 4
    cout << "Case 4: " << testString4 << "\n";
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.longestPalindrome(testString4);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    cout << "Iterations: " << iterationsOfLines << "\n"; 
    cout << "Output: " << output << "\n";
    cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
    
    
    // Case 5
    cout << "Case 5: " << testString5 << "\n";
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.longestPalindrome(testString5);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    cout << "Iterations: " << iterationsOfLines << "\n"; 
    cout << "Output: " << output << "\n";
    cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
    
    
    // Case 6
    cout << "Case 6: " << testString6 << "\n";
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.longestPalindrome(testString6);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    cout << "Iterations: " << iterationsOfLines << "\n"; 
    cout << "Output: " << output << "\n";
    cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
    
    
    // Case 7
    cout << "Case 7: " << testString7 << "\n";
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.longestPalindrome(testString7);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    cout << "Iterations: " << iterationsOfLines << "\n"; 
    cout << "Output: " << output << "\n";
    cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
    
    
    // Case 8
    cout << "Case 8: " << testString8 << "\n";
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.longestPalindrome(testString8);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    cout << "Iterations: " << iterationsOfLines << "\n"; 
    cout << "Output: " << output << "\n";
    cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
    
    
    // Case 9
    cout << "Case 9: " << "esbtzjaaij..." << "\n";
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.longestPalindrome(testString9);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    cout << "Iterations: " << iterationsOfLines << "\n"; 
    cout << "Output: " << output << "\n";
    cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
    
    
    // Case 10
    cout << "Case 10: " << "esbtzjaaij..." << "\n";
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.longestPalindrome(testString10);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    cout << "Iterations: " << iterationsOfLines << "\n"; 
    cout << "Output: " << output << "\n";
    cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
}







