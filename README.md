# AlienWorldsBot
www.alienworlds.io

# Version_3.0 PSEUDO CODE NOTES

## Bot_Brain + folder "bad_decisions" with measures
* Keep track of last decision made (or last 2-3 decisions)
* Keep a dict with each decision mapped to a decision file/section/category of the program.
* If a bot is stuck repeating a decision for X amounts of seconds. Backtrack.
* What was the last 1-3 decisions made?
  * What file/section/category of decisions do they belong? 
* For each decision file/section/category, write up scenarios when the bot might fail and keep a dict mapped to what specific decision or sequence of 1-3 decisions has highest probability of failing which specific scenarios.
* If Bot Brain notices that it can't go forward. ->
* Backtrack, check the mappings, and try a different approach.
* If Bot tried all possible approaches and still couldn't go forward, could be network error or unforeseen fail-scenario.
* If so, put Bot to sleep for 5minutes in order to not disturb the other bots. Then try again. 
* If it still doesn't work after sleeping 5minutes. -> Kill the Bot and restart it.
* Make sure to Log to Console exactly at what decision and what place in the code it broke down.


