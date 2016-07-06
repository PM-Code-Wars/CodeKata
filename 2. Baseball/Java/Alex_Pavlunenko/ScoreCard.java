/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ckbaseball;

/**
 *
 * @author alex.pavlunenko
 */
public class ScoreCard {

    private final int MAX_OUTS = 3;
    private final int MIN_OUTS = 0;
    private final int STARTING_BASE = 1;
    private final int SCORE_MASK = 0x0F;

    private final int SINGLE_RUN = 1;
    private final int DOUBLE_RUN = 2;
    private final int TRIPLE_RUN = 3;
    private final int HOME_RUN = 4;

    private int homeScore;
    private int awayScore;
    private boolean homeAtBat;
    private int outs;
    private int bases;

    public ScoreCard() {
        homeScore = 0;
        awayScore = 0;
        homeAtBat = false;
        outs = MIN_OUTS;
        bases = STARTING_BASE;
    }

    /*
  * A public method accepting the result of an at-bat
  * @param {string} entry - The result of an at-bat 
  * Acceptable values: ('single', 'double', 'triple', 'homerun' or 'out') 
     */
    public void addEntry(String entry) throws Exception {

        switch (entry) {
            case "out":
                handleOut();
                break;

            case "single":
                handleScore(SINGLE_RUN);
                break;

            case "double":
                handleScore(DOUBLE_RUN);
                break;

            case "triple":
                handleScore(TRIPLE_RUN);
                break;

            case "homerun":
                handleScore(HOME_RUN);
                break;

            default:
                throw new Exception("Invalid entry!");
        }
    }

    /*
  * A public method returning the current score
  * Format: "Home: [HOME_SCORE] Away: [AWAY_SCORE]"
     */
    public String getScore() {
        return "Home: " + homeScore + " Away: " + awayScore;
    }

    private void handleOut() {
        outs++;
        if (outs == MAX_OUTS) {
            outs = MIN_OUTS;
            homeAtBat = !homeAtBat;
            bases = STARTING_BASE;
        }
    }

    private void handleScore(int score) {
        bases = bases << score;

        calculateScore();
        bases = bases & SCORE_MASK;
        bases = bases | 1;
    }

    private void calculateScore() {
       
        int scorers = bases >> 4;
        int score = Integer.bitCount(scorers); 

        if (homeAtBat) {
            homeScore += score;
        } else {
            awayScore += score;
        }
    }
}
