# Barcelona Stadium Impact Hypothesis Testing

## Context

As a passionate FC Barcelona fan, this season has been particularly challenging, despite winning the league last year. Reflecting on what went wrong, I noticed Barcelona played home games at Montjuïc instead of Camp Nou, due to renovations.

Given Camp Nou's fortress-like reputation and the known impact of home advantage, I explored whether the stadium change significantly affected Barcelona's home performance.

## Data Collection

To analyze the impact, I scraped Barcelona’s result data for the 2022/2023 and 2023/2024 seasons from Understat using its API. This data includes:
- Date
- Opponent
- Goals scored by Barcelona
- Expected goals (xG)
- Goals conceded
- Final outcome
- Opponent's expected goals

## Analysis

### EDA Insights

- **Goal Scoring**: Barcelona scored slightly more goals on average at Montjuïc than at Camp Nou, despite a higher average xG at Camp Nou.
  
  ![Average Goals by Stadium](https://github.com/Abdul-AA/Barcelona-Stadium-Impact-Hypothesis-Testing/blob/eef1798752cb3bbf5ce154c92fc30047324819b3/Plots/G.png)
  
  ![Average xG by Stadium](https://github.com/Abdul-AA/Barcelona-Stadium-Impact-Hypothesis-Testing/blob/eef1798752cb3bbf5ce154c92fc30047324819b3/Plots/xG.png)

- **Goals Conceded**: Barcelona conceded substantially fewer goals at Camp Nou than at Montjuïc.

  ![Average Goals Conceded by Stadium](https://github.com/Abdul-AA/Barcelona-Stadium-Impact-Hypothesis-Testing/blob/eef1798752cb3bbf5ce154c92fc30047324819b3/Plots/GC.png)

- **Match Outcomes**: Barcelona won 15 home games in both stadiums. However, at Montjuïc, they lost three and drew one, while at Camp Nou, they lost only one and drew three.

  ![Result Distribution by Stadium](https://github.com/Abdul-AA/Barcelona-Stadium-Impact-Hypothesis-Testing/blob/eef1798752cb3bbf5ce154c92fc30047324819b3/Plots/Dis.png)

- **xG vs. Actual Goals Over Time**: At Camp Nou, actual goals often fell short of xG, indicating some inefficiency. At Montjuïc, actual goals sometimes exceeded xG, particularly in September and October 2023.

  ![Temporal Analysis](https://github.com/Abdul-AA/Barcelona-Stadium-Impact-Hypothesis-Testing/blob/eef1798752cb3bbf5ce154c92fc30047324819b3/Plots/Temp.png)
  ![Temporal Analysis](https://github.com/Abdul-AA/Barcelona-Stadium-Impact-Hypothesis-Testing/blob/eef1798752cb3bbf5ce154c92fc30047324819b3/Plots/Temp2.png)

- **Consistency Over Time**: Barcelona maintained a more consistent xG at Camp Nou, while Montjuïc showed more abrupt changes, especially in late 2023 and early 2024.

### Hypothesis Testing

To assess if observed differences were due to the stadium change or random chance, I performed hypothesis tests on various metrics.

#### Result Distribution

- **Test**: Chi-square test
- **Result**: p-value = 0.37 (no significant difference)

#### Proportion of Losses

- **Test**: Chi-square test
- **Result**: p-value = 0.60 (no significant difference)

#### Average Goals Scored

- **Test**: Two-tailed t-test
- **Result**: p-value = 0.45 (no significant difference)

#### Average xG

- **Test**: Two-tailed t-test
- **Result**: p-value = 0.57 (no significant difference)

#### Average Goals Conceded

- **Test**: Two-tailed t-test
- **Result**: p-value = 0.02, t-stat = -2.37 (significant difference)

## In Closing

This analysis suggests that Barcelona's defense was notably affected by the stadium change, conceding more goals at Montjuïc. Other performance aspects remained consistent with the previous season. The temporary relocation had a tangible impact on our defensive solidity.

As we prepare to return to the iconic Spotify Camp Nou, other teams should brace for a supercharged Barcelona!
