# Assignment 2
## Exploring the Trends in COVID-19 Cases and COVID-19 related Death in 2020

#### Data Selection
For this assignment, the dataset used was obtained from [Kaggle](https://www.kaggle.com/sudalairajkumar/covid19-in-usa?select=us_states_covid19_daily.csv "Dataset").
This dataset had a usability score of 9.7. 
The data described the number of COVID-19 cases and related deaths across the United States by state and counties in 2020.

#### Goals
The aim of this interactive application is to analyze trends in COVID-19 cases and related deaths across the United States. 
Understanding the regional trends can provide better insight into the patterns of changes in COVID-19 cases. 
Moreover, a regional analysis can help develop a stronger understanding of the patterns and make future predictions. For instance, if the number of COVID-19 cases increased in **state A** from the beginning of 2020 to the end of 2020 and the number of COVID-19 cases increases in **state B** only for a few months and then plateaues, this gives us an insight into how well the state has the situation under control. 
Moreover, identifying states that are better handling the COVID-19 situation and have been able to successfully reduce or prevent increases in the number of COVID-19 cases can encourage other states to adopt policies that have helped improve public health.

In order to allow users to identify trends in changes of COVID-19 cases and related deaths, this applications enable to analyze both cases and related deaths. In each case, users can view the changes in average monthly cases/deaths across all states through an animated map. This animation highlights regions with dramatic changes. To further observe those changes in detail for a particular state, users can click on the state. 
This generates a follow-up graph for that state allowing users to visualize the trends in the absolute number of COVID-19 cases/deaths. Users can also view the realtive changes in the number of COVID-19 cases/deaths by observing the relative plot.

#### Rationale Behind Decisions
The first aim was to allow user to analyze both COVID-19 cases and related deaths. Since both of them can be seperately visualized, I added the option to switch between the two using a dropdown menu. This reduced the clutter on the page.

The next aim was to visualize the trends in the changes across all the states in the US. Maps usually help visualize geographic information. Consequently, I colored the states in the map depending on the number of COVID-19 cases/deaths. However, the time component still had to be integrated. Placing maps side by side made it difficult to see the changes. So I decided to animate the map to make it easier to view the changes over the months.

Once we saw a pattern, the next step would be to allow users to visualize the trend for the specific state. Since there were to many states, making a dropdown menu seemed infeasible. Instead, the map was designed to be interactive, so that selecting a state on the map would generate plots for that specific state and allow users to further explore the trend. For this visualization, I added two types of plots - absolute and relative trends. Absolute trends make it easier to see the number of cases/deaths while relative trends make it easier to analyze the percentage change in cases/deaths.

#### Development Process
I did the project by myself. It took me an hour to select the dataset. Once I had that, creating the map plots was challenging. It took me 5 hours to successfully install the relevant libraries and have a baseline map. Next, making that map interactive took me over 3 hours. Once I had the pictoral components ready, it took me two hours to set up the pipeline, clean and process the data and write the code. Most of the time was spend on learning new features of the code and implementing them. Debugging took a long time too. Altogether, I spent over 12 hours project.
