/*
 * Brendon Murthum. August 2020.
 * Java 1.8.0
 * Leetcode Problem - Perfect Squares
 * https://leetcode.com/problems/perfect-squares/
 *
 * GOAL: Given a positive integer n, find the least number of perfect square
 *   numbers (for example, 1, 4, 9, 16, ...) which sum to n.
 *
 * OVERVIEW:
 */


// For use of sqrt() function.
import java.lang.Math;


/** To test the algorithm of finding sums of squares. */
public class perfectSquares {

    // Set the test cases.
    static int[][] testCases = {
        {0,0},      {16,1},     {100,1},    {232,2},
        {1,1},      {27,3},     {101,2},    {277,2},
        {2,2},      {29,2},     {102,3},    {384,3},
        {3,3},      {34,2},     {103,4},    {572,4},
        {4,1},      {37,2},     {104,2},    {733,2},
        {5,2},      {50,2},     {115,3},    {799,4},
        {6,3},      {58,2},     {154,3},    {1022,3},
        {10,2},     {61,2},     {159,4},    {1337,3},
        {12,3},     {62,3},     {173,2},    {2645,2},
        {13,2},     {99,3},     {181,2},    {5655,4}
    };

    /** Runs the program. */
    public static void main(String[] args){
        // Run the test cases.
        testCase(testCases);
        return;
    }

    /** Returns the minimum number of squares that can be summed to the given
        number. */
    public static int numSquares(int n) {
        return 2;
    }

    /** Runs each test-case through the algorithm. */
    public static void testCase(int[][] testList) {
        int numberOfTests = testList.length;
        int numberOfSuccesses = 0;
        double percentSuccess;
        for (int i = 0; i < numberOfTests; i++) {
            if(numSquares(testList[i][0]) != testList[i][1]) {
                System.out.println("FAILURE: " + testList[i][0] + " != " +
                    numSquares(testList[i][0]) + ", should be: " +
                    testList[i][1]);
            } else {
                numberOfSuccesses += 1;
            }
        }
        percentSuccess = Math.floor(((double)numberOfSuccesses / (double)numberOfTests) * 100);
        System.out.println(percentSuccess + "% Success " + numberOfSuccesses + "/" + numberOfTests + " Cases");
    }
}
