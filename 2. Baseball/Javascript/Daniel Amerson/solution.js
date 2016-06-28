/*
* Scorecard Constructor
*/
var ScoreCard = function() {
  this.outCount = 0;
  this.teamRuns = [0, 0];
  this.baseStatus = 0;
}

/*
* A public method accepting the result of an at-bat
* @param {string} entry - The result of an at-bat 
* Acceptable values: ('single', 'double', 'triple', 'homerun' or 'out') 
*/
ScoreCard.prototype.addEntry = function(entry) {
  var runnersCrossingHome = 0;

  if (entry === "out") {
    this.outCount++;
    if (this.outCount % 3 === 0) {
      this.baseStatus = 0;
    }
  } else {
    switch(entry) {
      case "single":
        this.baseStatus = (this.baseStatus << 1) + 1;
        break;
      case "double":
        this.baseStatus = (this.baseStatus << 2) + 2;
        break;
      case "triple":
        this.baseStatus = (this.baseStatus << 3) + 4;
        break;
      case "homerun":
        this.baseStatus = (this.baseStatus << 4) + 8;
        break;
    }
        
    runnersCrossingHome = this.getScoredRuns(Math.floor(this.baseStatus / 8));
    this.baseStatus = this.baseStatus % 8;
    
    this.teamRuns[Math.floor(this.outCount / 3) % 2] += runnersCrossingHome;
  }
}

ScoreCard.prototype.getScoredRuns = function(status) {
  var scored = 0;
  
  while (status !== 0) {
    if (status % 2 === 1) {
      scored ++;
    }
    
    status = status >> 1;
  }
  
  return scored;
}

/*
* A public method returning the current score
* Format: "Home: [HOME_SCORE] Away: [AWAY_SCORE]"
*/
ScoreCard.prototype.getScore = function() {
  return "Home: " + this.teamRuns[1] + " Away: " + this.teamRuns[0];
}