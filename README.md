# NBA-COVID-19-Investigation

## Background
On March 11, 2020, Utah Jazz center Rudy Gobert tested positive for COVID-19, prompting suspension of the 2019-2020 NBA Season


Since that time there have been 240 instances of 189 players being placed in the NBA’s “COVID-19 Health and Safety Protocols”  (H&S Protocols)


Due to HIPAA privacy laws it is not public knowledge  whether a player is placed in the H&S Protocols due to a positive CV-19 test or close contact with someone else with a positive CV-19 test

## Data Sources
Initially wrote program to scrape every daily Injury Report pdf published by the NBA, but that data was very messy since reports often covered multiple days causing overlap


Found a site with injury data already tabularized prosportstransactions.com and scraped injury data from March 11, 2020 to present


Since 2019-20 was discontinuous due to the stoppage, I focused on players in H&S Protocols during the 2020-21 season


Scraped basketball-reference.com to obtain 2020-21 game logs for players using a algorithm I created to generate the bball-ref id from the player names in the injury table


Ran into issues getting certain names to match up for things like accents on letters, similar names and sons of former players with the same name

## Data Summary
To obtain consistent parameters I chose to focusing on players that entered the H&S Protocols during the 2020-21 and played a minimum of 5 games before and after entering the protocols 

Focusing on those parameters, the number of instances and players went from 240 instances from 189 players to 128 instances from 119 players

After exploring the data and characteristics of multiple statistical categories, I decide to focus on Game Score (GmSc), a statistic created by John Hollinger that combines all of a players statistics and gives a measure of a players productivity in a given single game. Formula:
```
GmSc = PTS + 0.4*FG - 0.7*FGA - 0.4*(FTA - FT) + 0.7*ORB + 0.3*DRB + STL + 0.7*AST + 0.7*BLK - 0.4*PF - TOV
```
(GmSc of 10 is average and 40 is outstanding)

From there I turned GmSc into a rate by dividing it by the number of minutes the player played in the given game. (Roughly GmSc Rate of 0.28 is average and greater than 1.0 is outstanding)

Then looked at the mean GmSc Rate of the 5 games prior to and returning from H&S Protocols

## EDA
See [eda.ipynb](https://github.com/MLvtt/NBA-COVID-19-Investigation/tree/main/code/eda.ipynb)

## Hypothesis Testing

Null Hypothesis:
```
H0: Mean GmSc Rate 5gms Prior = Mean GmSc Rate5 gms After 

⇒ H0: |Mean GmSc Rate 5gms After - Mean GmSc Rate 5gms Prior| = 0
```

Alt Hypothesis:
```
Ha: Mean GmSc Rate 5gms Prior  ≠ Mean GmSc Rate 5gms After

⇒ Ha: |Mean GmSc Rate 5gms After - Mean GmSc Rate 5gms Prior| ≠ 0
```

Where ```|Mean GmSc Rate 5gms After - Mean GmSc Rate 5gms Prior| ```
is the Difference in Mean GmSc Rate

Parameters from Samples of Difference in Mean GmSc Rate 
```
Sample Size: n = 128
Sample Mean: x̅  = 0.024
Sample Std Dev:	𝜎 = 0.230
Std Error: SE = 0.020
T-Statistic: t-stat = 1.197
p-value: p = 0.234
```
p > 𝛼 (= 0.05)

Therefore we cannot reject the Null Hypothesis:

H0: |Mean GmSc Rate 5gms After - Mean GmSc Rate 5gms Prior| = 0

### Further Hypothesis Testing
Since all we know is that the player was in H&S Protocols and not if they actually had COVID or not, I attempted to look at Difference in Mean GmSc Rate with respect to games missed.

Divided the data into 2 categories:
- Players that missed a week or less in H&S Protocols 
- Players that missed more than a week in H&S Protocols

Hypotheses:
```
H0:  Mean GmSc Rate≤7days = Mean GmSc Rate>7days 
Ha:  Mean GmSc Rate≤7days ≠ Mean GmSc Rate>7days 
```
T-test performed resulting in p-value of 0.55 therefore again we cannot reject the Null Hypothesis


