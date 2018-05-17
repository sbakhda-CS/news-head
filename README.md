# Top Headlines Skill

## Developer pre-requisites
  * Obtain a Cortex account
  * Install Cortex CLI
  * For python3 use python > 3.6
  * For nodejs use nodejs > 8.x

## What does this skill do? 
I created this skill to get familiar with writing skill functions and use features such as properties and routes. 

### Inputs
*source*: the news source. Check out 
https://newsapi.org/sources
for the complete list of sources.

*n*: the number of top headlines from the source

### Ouputs
*route*: the route taken by the skill

*top_head*: array of the article titles and urls of the top headlines

*api*: the api token used for the skill

### Properties
*token*: the api token for newsapi.org


## How to test this skill on Cortex?

There are 4 stages to testing: 
1. `deploy-skill.sh`: this deploys the skill definition to Cortex
2. `build-function.sh`: packages the function in build/function.zip
3. `deploy-function.sh`: builds and deploys the function(s) 
4. `test-function.sh`: test the function with an input json

The 2nd step is optional because `deploy-function.sh` includes both building and deploying

For more information: https://docs.cortex.insights.ai
