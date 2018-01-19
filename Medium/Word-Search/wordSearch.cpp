/* 

Problem from LeetCode - https://leetcode.com/problems/word-search/description/

@author - Brendon Murthum
@version - January 2018

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where 
"adjacent" cells are those horizontally or vertically neighboring. The same 
letter cell may not be used more than once.

Example:

  Given a board symbolically represented as the following...
 
  board = [['A','B','C','E'],
           ['S','F','C','S'],
           ['A','D','E','E']]
        
  word = "ABCCED", returns TRUE.
  word = "SEE", returns TRUE.
  word = "ABCB", returns FALSE.

My Performance Test Cases:

  Case 1: 3 x 3 board. Showing simple functionality.
  
    board = [['A','B','C'],
             ['D','E','F'],
             ['G','H','I']]
    word = "ABC", returns TRUE.
    word = "EHI", returns TRUE.
    word = "AEI", returns FALSE. No diagonals.
    word = "ABD", returns FALSE. "B" and "D" not connected.
    word = "ABA", returns FALSE. No repeated characters.
    word = "ZAB", returns FALSE. No "Z" in the board.
    word = "GHH", returns FALSE. No second "H" in the board.

  Case 2: 7 x 7 board. Showing complex solutions, edge cases.
    word = "AHOVCJQRSTUVWPIBU..", the entire board, returns TRUE.
    word = "AHOVCJQRSTUVWPIBU..", but with several repeat-R's, returns False
      due to a preliminary search to see if each letter of the word can at least
      be found within the board.

  Case 3: 20 x 20 board. Showing variety of speeds to solution.
    word = "TEST", returns FALSE.
    word = "ABCDEFGHIJKLMNOPQ..", 64-letter word, returns TRUE.
    word = "ABCDEFGHIJKLMNOPQ..", but last letter incorrect, returns FALSE.
    word = "ABCDEFGHIJKLMNOPQ..", but last letter as repeated "A" to see 
      efficiency difference with a case where the word's letters are not all on
      the board.

*/

#include <string.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <cstdlib>

using namespace std;

/* This class is in format of LeetCode's assigned problem. */
class Solution {
public:
    /** Searches for a word within a matrix of letters. */
    bool exist(vector<vector<char> > &board, string &word) {
        
        /* 
         If the letters are not all in the board, do not take time to allocate
         memory, or run any recursive-searches.
         
         Case 1, 3x3 Board:
           With "ABA", runtime went from 0.005ms to <0.001ms
         Case 2, 7x7 Board:
           With "AHO...RR", runtime went from 0.176ms to 0.007ms.
         Case 3, 20x20 Board:
           With 63-letter string, runtime went from 2.667ms to 0.117ms.
         
        */
        if (!lettersAvailable(board, word)) {
            return false;
        }
        
        /* First letter of the given word. */
        char firstLetter = word[0];
        /** Number of columns in board. */
        int boardRows = board.size();
        /** Number of rows in board. */
        int boardColumns = board[0].size();

        /* In the case of a 1-letter given. */
        if (word.length() == 1 && lettersAvailable(board, word)) {
            return true;
        }
        
        /** 
         Board of booleans for searching. Everything is initially false, then
         upon entering a position, it is marked true, so to not revisit.
        */
        vector<vector<bool> > boolBoard(boardRows, vector<bool>(boardColumns)); 
        for (int i=0; i < boardRows; i++) {
            for (int j=0; j < boardColumns; j++) {
                boolBoard[i][j] = false;
            }
        }
        
        /** 
         Iterate through the board for first-letters, to initiate a recursive
         search that will look for the entire word as a snake. 
        */
        for (int i = 0; i < boardRows; i++) {
            for (int j = 0; j < boardColumns; j++) {
                /* On finding a firstletter, initiate the search. */
                if (board[i][j] == firstLetter) {
                    /* Remove the first letter from the possible for search. */
                    boolBoard[i][j] = true;
                    if (recursiveSearch(board,boolBoard,word.substr(1),i,j)) {
                        return true;
                    }
                    /* Add that first letter back for next search. */
                    boolBoard[i][j] = false;
                }
            }
        }
        return false;
        
    }
    
    /** A search method used within the exist() method. */
    bool recursiveSearch( vector<vector<char> > &board, 
                          vector<vector<bool> > previouslySearched, 
                          string smallerWord, 
                          int currentRow, 
                          int currentColumn) {
        
        // cout << "  Recursive Search... \n";
        
        // cout << "    smallerWord: " << smallerWord << "\n";
        // cout << "    currentRow: " << currentRow << "\n";
        // cout << "    currentColumn: " << currentColumn << "\n";
        
        /** Number of columns in board. */
        int boardRows = board.size();
        /** Number of rows in board. */
        int boardColumns = board[0].size();
        
        /* Coordinates of the potential positions to search next. */
        int upRow = currentRow - 1;
        int upCol = currentColumn;
        int downRow = currentRow + 1;
        int downCol = currentColumn;
        int rightRow = currentRow;
        int rightCol = currentColumn + 1;
        int leftRow = currentRow;
        int leftCol = currentColumn - 1;;
        
        /* Initiate new recursive searches */
        
        /* Check the upper box from current position. */
        if (upRow >= 0 
                  && previouslySearched[upRow][upCol] == false 
                  && board[upRow][upCol] == smallerWord[0]) {
            /* Found the last letter! */
            if (smallerWord.size() == 1) {
                return true;
            } 
            else {
                previouslySearched[currentRow][currentColumn] = true;
                // cout << "    searching UP... \n";
                if (recursiveSearch(board, previouslySearched, 
                                         smallerWord.substr(1), upRow, upCol)) {
                    return true;
                }
            }
        }
        /* Check the below box. */
        if (downRow < boardRows
            && previouslySearched[downRow][downCol] == false 
            && board[downRow][downCol] == smallerWord[0]) {
            /* Found the last letter! */
            if (smallerWord.size() == 1) {
                return true;
            } 
            else {
                // cout << "    searching DOWN... \n";
                previouslySearched[currentRow][currentColumn] = true;
                if (recursiveSearch(board, previouslySearched, 
                                     smallerWord.substr(1), downRow, downCol)) {
                    return true;
                }
            }
        }
        /* Check the right box. */
        if (rightCol < boardColumns
            && previouslySearched[rightRow][rightCol] == false 
            && board[rightRow][rightCol] == smallerWord[0]) {
            /* Found the last letter! */
            if (smallerWord.size() == 1) {
                return true;
            } 
            else {
                // cout << "    searching RIGHT... \n";
                previouslySearched[currentRow][currentColumn] = true;
                if (recursiveSearch(board, previouslySearched, 
                                   smallerWord.substr(1), rightRow, rightCol)) {
                    return true;
                }
            }
        }
        /* Check the left box. */
        if (leftCol >= 0
            && previouslySearched[leftRow][leftCol] == false 
            && board[leftRow][leftCol] == smallerWord[0]) {
            /* Found the last letter! */
            if (smallerWord.size() == 1) {
                return true;
            } 
            else {
                // cout << "    searching RIGHT... \n";
                previouslySearched[currentRow][currentColumn] = true;
                if (recursiveSearch(board, previouslySearched, 
                                     smallerWord.substr(1), leftRow, leftCol)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    /** Sees if the letters in the "word" match a count in the board. */
    bool lettersAvailable(vector<vector<char> >& board, string &word) {
    
        /* This code limits CPU processes in the cases of invalid searches. */
        
        /** Number of columns in board. */
        int boardRows = board.size();
        /** Number of rows in board. */
        int boardColumns = board[0].size();
        /** The length of the given word. */
        int wordLength = word.size();
        /** Each letter of the word, in a char array. */
        char wordLetters[wordLength + 1];
        /** Each letter position has a boolean. */
        bool boolLetters[wordLength + 1];
        
        /* Initialize each of these arrays. */
        for (int i = 0; i < wordLength; i++) {
            wordLetters[i] = word[i];
            boolLetters[i] = false;
        }
        
        /* Makes sure every letter is seen at least for the amount necessary. */
        for (int i = 0; i < boardRows; i++) {
            for (int j = 0; j < boardColumns; j++) {
                for (int k = 0; k < wordLength; k++) {
                    /* If match, mark the letter as counted. */
                    if ( (board[i][j] == wordLetters[k]) 
                         && (boolLetters[k] == false) ) {
                        boolLetters[k] = true;
                        break;
                    }
                }
            }
        }
        
        /* Return false if a single letter is missing. */
        for (int i = 0; i < wordLength; i++) {
            if (boolLetters[i] == false) {
                return false;
            }
        }
        return true;
    }
};

/** Displays the board to the terminal. */
void displayBoard(vector<vector<char> > &board) {
    
    /** Number of columns in board. */
    int boardRows = board.size();
    /** Number of rows in board. */
    int boardColumns = board[0].size();
    
    /* Iterate through the two-dimensional vector. */
    cout << "\n";
    cout << " Board: \n";
    for (int i=0; i < boardRows; i++) {
        cout << " [";
        for (int j=0; j < boardColumns; j++) {
            if (j == boardColumns - 1) {
                cout << board[i][j] << "]\n";
            } else {
                cout << board[i][j] << ", ";   
            }
        }
    }
}

/** For testing the LeetCode methods. */
int main(int argc, char** argv) {

    /* Initial text given to the terminal. */
    cout << "\n" << "Initializing the board word-finder.." << "\n";
    cout << "\n";
    cout << "This program will run each test a multitude of times, each \n" <<
            "within the period of a second. This is to find the runtime \n" <<
            "in an order of milliseconds. \n";
    cout << "\n";

    /** Initialize an object for testing. This uses leetcode's format. */
    Solution solutionObject;
    /** Columns in a board. */
    int cols;
    /** Rows in a board. */
    int rows;
    /** Total characters in a board. */
    int totalCharacters;
    /** Iterator for adding characters. */
    int x;
    /* Timer of a case-test. */
    clock_t t;
    /* Time converted to milliseconds. */
    float timeInMilliseconds;
    /* Counted iterations of the line to be tested. */
    int iterationsOfLines;
    /* Output of exist() function to display. */
    bool output;
    
    /** Case-1 Board Vector. */
    /*
      ['A','B','C']
      ['D','E','F']
      ['G','H','I']
    */
    
    /** Case-1 Test Word A. */
    string board1_testWordA = "ABC";
    /** Case-1 Test Word B. */
    string board1_testWordB = "EHI";
    /** Case-1 Test Word C. */
    string board1_testWordC = "AEI";
    /** Case-1 Test Word D. */
    string board1_testWordD = "ABD";
    /** Case-1 Test Word E. */
    string board1_testWordE = "ABA";
    /** Case-1 Test Word F. */
    string board1_testWordF = "ZAB";
    /** Case-1 Test Word G. */
    string board1_testWordG = "GHH";
    
    /* Generate the board. */
    cols = 3;
    rows = 3;
    vector<vector<char> > board1(rows, vector<char>(cols)); 
    char addingCharacters[10] = "ABCDEFGHI";
    x = 0;
    for (int i=0; i < rows; i++) {
        for (int j=0; j < cols; j++) {
            board1[i][j] = addingCharacters[x];
            x++;
        }
    }
    
    /* Running Case-1 */
    cout << "Showing Case #1: ";
    /* Display the board on terminal. */
    displayBoard(board1);
    cout << "\n";
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board1_testWordA << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board1, board1_testWordA))
        cout << "True\n";
    else
        cout << "False\n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board1, board1_testWordA);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board1_testWordB << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board1, board1_testWordB))
        cout << "True\n";
    else
        cout << "False\n";

    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board1, board1_testWordB);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board1_testWordC << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board1, board1_testWordC))
        cout << "True\n";
    else
        cout << "False\n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board1, board1_testWordC);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board1_testWordD << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board1, board1_testWordD))
        cout << "True\n";
    else
        cout << "False\n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board1, board1_testWordD);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board1_testWordE << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board1, board1_testWordE))
        cout << "True\n";
    else
        cout << "False\n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board1, board1_testWordE);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board1_testWordF << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board1, board1_testWordF))
        cout << "True\n";
    else
        cout << "False\n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board1, board1_testWordF);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board1_testWordG << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board1, board1_testWordG))
        cout << "True\n";
    else
        cout << "False\n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board1, board1_testWordG);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    cout << "\n";
    
    
    /** Case-2 Board Vector. */
    /*
      ['A','B','C','D','E','F','G']
      ['H','I','J','K','L','M','N']
      ['O','P','Q','R','S','T','U']
      ['V','W','X','Y','Z','A','B']
      ['C','D','E','F','G','H','I']
      ['J','K','L','M','N','O','P']
      ['Q','R','S','T','U','V','W']
    */

    /** Case-2 Test Word A. */
    string board2_testWordA = "AHOVCJQRSTUVWPIBUNGFEDCBIPWDKLMNOHATMLKJQXEFGZSRY";
    /** Case-2 Test Word B. */
    string board2_testWordB = "AHOVCJQRSTUVWPIBUNGFEDCBIPWDKLMNOHATMLKJQXEFGZSRR";
    
    /* Generate the board. */
    cols = 7;
    rows = 7;
    totalCharacters = cols * rows;
    vector<vector<char> > board2(rows, vector<char>(cols));
    char addingCharacters2[totalCharacters];
    strcpy (addingCharacters2,"ABCDEFG");
    strcat (addingCharacters2,"HIJKLMN");
    strcat (addingCharacters2,"OPQRSTU");
    strcat (addingCharacters2,"VWXYZAB");
    strcat (addingCharacters2,"CDEFGHI");
    strcat (addingCharacters2,"JKLMNOP");
    strcat (addingCharacters2,"QRSTUVW");
    x = 0;
    for (int i=0; i < rows; i++) {
        for (int j=0; j < cols; j++) {
            board2[i][j] = addingCharacters2[x];
            x++;
        }
    }
    
    
    /* Running Case-2 */
    cout << "Showing Case #2: ";
    /* Display the board on terminal. */
    displayBoard(board2);
    cout << "\n";
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board2_testWordA << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board2, board2_testWordA))
        cout << "True\n";
    else
        cout << "False\n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board2, board2_testWordA);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board2_testWordB << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board2, board2_testWordB))
        cout << "True\n";
    else
        cout << "False\n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board2, board2_testWordB);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    cout << "\n";
    
    
    /** Case-3 Board Vector. 20x20 Board. */
    
    /** Case-3 Test Word A. */
    string board3_testWordA = "TEST";
    /** Case-3 Test Word B. */
    string board3_testWordB = "ABCDEFGHIJKLMNOPQRSTNHBVPJDXRLFZTNHBVPJIHGFEDCBAGHIJKLMNOUAGMSYE";
    /** Case-3 Test Word C. */
    string board3_testWordC = "ABCDEFGHIJKLMNOPQRSTNHBVPJDXRLFZTNHBVPJIHGFEDCBAGHIJKLMNOUAGMSYD";
    /** Case-3 Test Word D. */
    string board3_testWordD = "ABCDEFGHIJKLMNOPQRSTNHBVPJDXRLFZTNHBVPJIHGFEDAAAAAAAAAAAAAAAAAAA";
    
    /* Generate the board. */
    cols = 20;
    rows = 20;
    totalCharacters = cols * rows;
    vector<vector<char> > board3(rows, vector<char>(cols));
    char addingCharacters3[totalCharacters];
    strcpy (addingCharacters3,"ABCDEFGHIJKLMNOPQRST");
    strcat (addingCharacters3,"UVWXYZABCDEFGHIJKLMN");
    strcat (addingCharacters3,"OPQRSTUVWXYZABCDEFGH");
    strcat (addingCharacters3,"IJKLMNOPQRSTUVWXYZAB");
    strcat (addingCharacters3,"CDEFGHIJKLMNOPQRSTUV");
    strcat (addingCharacters3,"WXYZABCDEFGHIJKLMNOP");
    strcat (addingCharacters3,"QRSTUVWXYZABCDEFGHIJ");
    strcat (addingCharacters3,"KLMNOPQRSTUVWXYZABCD");
    strcat (addingCharacters3,"EFGHIJKLMNOPQRSTUVWX");
    strcat (addingCharacters3,"YZABCDEFGHIJKLMNOPQR");
    strcat (addingCharacters3,"STUVWXYZABCDEFGHIJKL");
    strcat (addingCharacters3,"MNOPQRSTUVWXYZABCDEF");
    strcat (addingCharacters3,"GHIJKLMNOPQRSTUVWXYZ");
    strcat (addingCharacters3,"ABCDEFGHIJKLMNOPQRST");
    strcat (addingCharacters3,"UVWXYZABCDEFGHIJKLMN");
    strcat (addingCharacters3,"OPQRSTUVWXYZABCDEFGH");
    strcat (addingCharacters3,"IJKLMNOPQRSTUVWXYZAB");
    strcat (addingCharacters3,"CDEFGHIJKLMNOPQRSTUV");
    strcat (addingCharacters3,"WXYZABCDEFGHIJKLMNOP");
    strcat (addingCharacters3,"QRSTUVWXYZABCDEFGHIJ");
    x = 0;
    for (int i=0; i < rows; i++) {
        for (int j=0; j < cols; j++) {
            board3[i][j] = addingCharacters3[x];
            x++;
        }
    }
    
    /* Running Case-3 */
    cout << "Showing Case #3: ";
    /* Display the board on terminal. */
    displayBoard(board3);
    cout << "\n";
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board3_testWordA << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board3, board3_testWordA))
        cout << "True \n";
    else
        cout << "False \n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board3, board3_testWordA);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board3_testWordB << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board3, board3_testWordB))
        cout << "True \n";
    else
        cout << "False \n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board3, board3_testWordB);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board3_testWordC << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board3, board3_testWordC))
        cout << "True \n";
    else
        cout << "False \n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board3, board3_testWordC);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    
    /* Display the searched-for word. */
    cout << " Given Word: \"" << board3_testWordD << "\"\n";
    cout << "  Letters Available: ";
    if (solutionObject.lettersAvailable(board3, board3_testWordD))
        cout << "True \n";
    else
        cout << "False \n";
        
    t = clock();
    iterationsOfLines = 0;
    while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board3, board3_testWordD);
        iterationsOfLines++;
    }
    t = clock() - t;
    timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    if (output == true) {
        cout << "  Solution Found: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "True \n";
    } else {
        cout << "  Program Run: " << iterationsOfLines << " times. \n";
        cout << "  Result: " << "False \n";
    }
    if (timeInMilliseconds == 0) {
        cout << "  Runtime: <0.001ms" << "\n";
    } else {
        cout << "  Runtime: " << timeInMilliseconds << "ms" << "\n";
    }
    
    cout << "\n";
    
    return 0;
}
