# Braverman Personality Test
# Determining your dominant nature, 200 questions total.

import random
import csv

print("\nBraverman Personality Test\n\n"
      "INSTRUCTIONS: Please answer each question by typing \"y\" for Yes, or \"n\" for No, then \n"
      "press Enter on the keyboard. Please answer each question based on how you feel most of \n"
      "the time on an average day.\n\n"
      "Total of 200 questions.\n"
      "Loading questions...\n\n"
)


# N=8
dopamineMemoryAttention = [
    ["I find it easy to process my thoughts: "],
    ["I concentrate effectively: "],
    ["I am a deep thinker: "],
    ["I am a quick thinker: "],
    ["I become distracted, because I do so many tasks at once: "],
    ["I enjoy intense debate: "],
    ["I have a good imagination: "],
    ["I tend to criticize and analyze my thoughts: "],
]

# N=14
dopaminePhysical = [
    ["I have a lot of energy most of the time: "],
    ["My blood pressure is often elevated: "],
    ["Sometimes in my life, I have had episodes of extreme energy: "],
    ["I have insomnia: "],
    ["I find exercising invigorating: "],
    ["I don't ordinarily need coffee to jump-start me in the morning: "],
    ["My veins are visible and tend to look as though they might pop out of my skin: "],
    ["I tend to have a high body temperature: "],
    ["I eat my lunch while I'm working: "],
    ["I engage in sexual intercourse any change I get: "],
    ["I have a temper: "],
    ["I eat only to re-energize my body: "],
    ["I love action movies: "],
    ["Exercising makes me feel powerful: "],
]

# N=21
dopaminePersonality = [
    ["I am a very domineering individual: "],
    ["I sometimes don't notice my feelings: "],
    ["I often have trouble listening to others, because my own ideas dominate: "],
    ["I have been in many fights: "],
    ["I tend to be future-oriented"],
    ["I am sometimes speculative: "],
    ["Most people view me as thinking-oriented: "],
    ["I daydream and often fantasize: "],
    ["I like to read history and other non-fiction books: "],
    ["I admire ingenuity: "],
    ["I can be slow in identifying how people can cause trouble: "],
    ["I don't usually get tricked by people who say they need my help: "],
    ["Most people view me as innovative: "],
    ["People have thought I have had some strange ideas, but I can always explain the basis for them rationally: "],
    ["I am often agitated or irritated: "],
    ["Little things make me anxious or upset: "],
    ["I have fantasies of unlimited power: "],
    ["I love spending money: "],
    ["I dominate others in relationships: "],
    ["I am very hard on myself: "],
    ["I react aggressively to criticism, often becoming defensive in front of others: "],
]

# N=7
dopamineCharacter = [
    ["Some individuals view me as tough-minded: "],
    ["Most people view me as achievement-oriented: "],
    ["Some people say that I am irrational: "],
    ["I will do anything to reach a goal: "],
    ["I value a religious philosophy: "],
    ["Incompetence makes me angry: "],
    ["I have high standards for myself and others: "],
]

# N=9
acetylcholineMemoryAttention = [
    ["My memory is very strong: "],
    ["I am an excellent listener: "],
    ["I am good at remembering stories: "],
    ["I usually do not forget a face: "],
    ["I am very creative: "],
    ["I have an excellent attention span and rarely miss a thing: "],
    ["I have many good hunches: "],
    ["I notice everything going on around me: "],
    ["I have a good imagination: "],
]

# N=9
acetylcholinePhysical = [
    ["I tend to have a slow pulse: "],
    ["My body has excellent tone: "],
    ["I have a great figure/build: "],
    ["I have really low cholesterol: "],
    ["When I eat, I love to experience the aromas and the beauty of food: "],
    ["I love yoga and stretching my muscles: "],
    ["During sex, I am very sensual: "],
    ["I have had an eating disorder at some point in my life: "],
    ["I have tried many alternative remedies: "],
]

# N=23
acetylcholinePersonality = [
    ["I am a perpetual romantic: "],
    ["I am in touch with my feelings: "],
    ["I tend to make decisions based on hunches: "],
    ["I like to speculate: "],
    ["Some people say I have my head in the clouds: "],
    ["I love reading fiction: "],
    ["I have a rich fantasy life: "],
    ["I am creative when solving people problems: "],
    ["I am very expressive; I like to talk about what's bothering me: "],
    ["I am buoyant: "],
    ["I believe that it is possible to have a mystical experience: "],
    ["I believe in being a soul mate: "],
    ["Sometimes the mystical can excite me: "],
    ["I tend to overreact to my body: "],
    ["I find it easy to change things; I am not set in my ways: "],
    ["I am deeply in touch with my emotions: "],
    ["I tend to love someone one minute and hate him/her the next: "],
    ["I am flirtatious: "],
    ["I don't mind spending money if it benefits my relationships: "],
    ["I tend to fantasize when I'm having sex: "],
    ["My relationships tend to be filled with romance: "],
    ["I love watching romantic movies: "],
    ["I take risks in my love life: "],
]

# N=9
acetylcholineCharacter = [
    ["I foresee a better future: "],
    ["I am inspired to help other people: "],
    ["I believe that all things are possible, particularly for those who are devoted: "],
    ["I am good at creating harmony between people: "],
    ["Charity and altruism come from the heart, and I have plenty of both: "],
    ["Others think me of as having vision: "],
    ["My thoughts on religion often change: "],
    ["I am an idealist, but not a perfectionist: "],
    ["I'm happy with someone who just treats me right: "],
]

# N=7
gabaMemoryAttention = [
    ["I have a stable attention span and can follow other's logic: "],
    ["I enjoy reading people more than books: "],
    ["I retain most of what I hear: "],
    ["I can remember facts people tell me: "],
    ["I learn from my experiences: "],
    ["I am good at remembering names: "],
    ["I can focus very well on tasks and people's stories: "],
]

# N=13
gabaPhysical = [
    ["I find it easy to relax: "],
    ["I am a calm person: "],
    ["I find it easy to fall asleep at night: "],
    ["I tend to have high physical endurance: "],
    ["I have low blood pressure: "],
    ["I do not have a family history of stroke: "],
    ["When it comes to sex, I am not very experimental: "],
    ["I have little muscle tension: "],
    ["Caffeine has little effect on me: "],
    ["I take my time eating my meals: "],
    ["I sleep well: "],
    ["I don't have many harmful food cravings such as sugar: "],
    ["Exercising is a regimented habit for me: "],
]

# N=19
gabaPersonality = [
    ["I am not very adventurous: "],
    ["I do not have a temper: "],
    ["I have a lot of patience: "],
    ["I don't enjoy philosophy: "],
    ["I love watching sitcoms about families: "],
    ["I dislike movies about other worlds or universes: "],
    ["I am not a risk-taker: "],
    ["I keep past experiences in mind before I make decisions: "],
    ["I am a realistic person: "],
    ["I believe in closure: "],
    ["I like facts and details: "],
    ["When I make a decision, it's permanent: "],
    ["I like to plan my day, week, month, etc.: "],
    ["I collect things: "],
    ["I am a little sad: "],
    ["I am afraid of confrontations and altercations: "],
    ["I save up a lot of money in the event of a crisis: "],
    ["I tend to create strong, lasting bonds with others: "],
    ["I am a stable pillar in people's lives: "],
]

# N=11
gabaCharacter = [
    ["I believe in the adage, \"Early to bed, early to rise\": "],
    ["I believe in meeting deadlines: "],
    ["I try to please others the best I can: "],
    ["I am a perfectionist: "],
    ["I am good at maintaining long-lasting relationships: "],
    ["I pay attention to where my money goes: "],
    ["I believe that the world would be more peaceful if people would improve upon their morals: "],
    ["I am very loyal and devoted to my loved ones: "],
    ["I have high ethical standards that I live by: "],
    ["I pay close attention to laws, principles, and policies: "],
    ["I believe in participating in service for the community: "],
]

# N=8
serotoninMemoryAttention = [
    ["I can easily concentrate on manual-labor tasks: "],
    ["I have a good visual memory: "],
    ["I am very perceptive: "],
    ["I am an impulsive thinker: "],
    ["I live in the here and now: "],
    ["I tend to say, \"Tell me the bottom line, straight\": "],
    ["I am a slow book learner, but I learn easily from experience: "],
    ["I need to experience something or work at it hands-on in order to understand it: "],
]

# N=11
serotoninPhysical = [
    ["I sleep too much: "],
    ["When it comes to sex, I am very experimental: "],
    ["I have low blood pressure: "],
    ["I am very action-oriented: "],
    ["I am very handy around the house: "],
    ["I am very active outdoors: "],
    ["I engage in daring activities such as skydiving and motorcycle riding: "],
    ["I can solve problems spontaneously: "],
    ["I rarely have carbohydrate cravings: "],
    ["I usually grab a quick meal on the run: "],
    ["I'm usually not very consistent with my exercise routine. "
    "I may exercise daily for 3 weeks, then skip it for a month: "],
]

# N=21
serotoninPersonality = [
    ["I live life in the immediate moment: "],
    ["I like to perform/entertain in public: "],
    ["I tend to gather facts in an unorganized manner: "],
    ["I am very flexible: "],
    ["I am a great negotiator: "],
    ["I often just like to \"eat, drink, and be merry\": "],
    ["I am dramatic: "],
    ["I am very artistic: "],
    ["I am a good craftsman: "],
    ["I'm a risk taker when it comes to sports: "],
    ["I believe in psychics: "],
    ["I can easily take advantage of others: "],
    ["I am cynical of others' philosophies: "],
    ["I like to have fun: "],
    ["My favorite type of movies are horror flicks: "],
    ["I am fascinated with weapons: "],
    ["I rarely stick to a plan or agenda: "],
    ["I have trouble remaining faithful: "],
    ["I am easily able to separate and move on when relationships with loved ones end: "],
    ["I don't pay much attention to how I spend my money: "],
    ["I have many frivolous relationships: "],
]

# N=10
serotoninCharacter = [
    ["I always keep my options open in case something better comes up: "],
    ["I don't like working hard for long periods of time: "],
    ["I believe things should have a function and purpose: "],
    ["I am optimistic: "],
    ["I live in the moment: "],
    ["I pray only when I'm in need of spiritual support: "],
    ["I don't have particularly high morals and ethical values: "],
    ["I do what I want, when I want to: "],
    ["I don't care about being perfect; I just live my life: "],
    ["Savings are for suckers: "],
]

def tagList(list, string):
    for i in list:
        i.append(string)


# Tag all questions with the associated neurotransmitter
tagList(dopamineMemoryAttention, "dopamine")
tagList(dopaminePhysical, "dopamine")
tagList(dopaminePersonality, "dopamine")
tagList(dopamineCharacter, "dopamine")
tagList(acetylcholineMemoryAttention, "acetylcholine")
tagList(acetylcholinePhysical, "acetylcholine")
tagList(acetylcholinePersonality, "acetylcholine")
tagList(acetylcholineCharacter, "acetylcholine")
tagList(gabaMemoryAttention, "gaba")
tagList(gabaPhysical, "gaba")
tagList(gabaPersonality, "gaba")
tagList(gabaCharacter, "gaba")
tagList(serotoninMemoryAttention, "serotonin")
tagList(serotoninPhysical, "serotonin")
tagList(serotoninPersonality, "serotonin")
tagList(serotoninCharacter, "serotonin")


# Tag all questions with the associated section
tagList(dopamineMemoryAttention, "MemoryAttention")
tagList(dopaminePhysical, "Physical")
tagList(dopaminePersonality, "Personality")
tagList(dopamineCharacter, "Character")
tagList(acetylcholineMemoryAttention, "MemoryAttention")
tagList(acetylcholinePhysical, "Physical")
tagList(acetylcholinePersonality, "Personality")
tagList(acetylcholineCharacter, "Character")
tagList(gabaMemoryAttention, "MemoryAttention")
tagList(gabaPhysical, "Physical")
tagList(gabaPersonality, "Personality")
tagList(gabaCharacter, "Character")
tagList(serotoninMemoryAttention, "MemoryAttention")
tagList(serotoninPhysical, "Physical")
tagList(serotoninPersonality, "Personality")
tagList(serotoninCharacter, "Character")


# Clump neurotransmitters by section
onlyMemoryAttention = dopamineMemoryAttention + acetylcholineMemoryAttention + gabaMemoryAttention + serotoninMemoryAttention
onlyPhysical = dopaminePhysical + acetylcholinePhysical + gabaPhysical + serotoninPhysical
onlyPersonality = dopaminePersonality + acetylcholinePersonality + gabaPersonality + serotoninPersonality
onlyCharacter = dopamineCharacter + acetylcholineCharacter + gabaCharacter + serotoninCharacter

# Clump all sections into one master pool of questions
grandPoolQuestions = onlyMemoryAttention + onlyPhysical + onlyPersonality + onlyCharacter



# Shuffle each section
random.shuffle(onlyMemoryAttention)
random.shuffle(onlyPhysical)
random.shuffle(onlyPersonality)
random.shuffle(onlyCharacter)



# Shuffle all questions
random.shuffle(grandPoolQuestions)


"""
# Attempt at adding input validation
def validateInput(userAnswer):
    userAnswer = ""
    if userAnswer != "y" and userAnswer != "n":
        return True
#    if userAnswer not in "yn":
#        return True
    else:
        return False

def runBravermanTest(questionSet):
    dopamineTally = 0
    acetylcholineTally = 0
    gabaTally = 0
    serotoninTally = 0
    consolidatedTally = []
    answer = ""
    for question in questionSet:
        rawAnswer = input(question[0]).lower()
        #validatedInput = validateInput(str(rawAnswer))
        #while validatedInput:
            #print("Invalid answer. Please type \"y\" for yes, or \"n\" for no, then press Enter.")
            #continue
        if rawAnswer == "y" and question[1] == "dopamine":
            dopamineTally += 1
            continue
        elif rawAnswer == "y" and question[1] == "acetylcholine":
            acetylcholineTally += 1
            continue
        elif rawAnswer == "y" and question[1] == "gaba":
            gabaTally += 1
            continue
        elif rawAnswer == "y" and question[1] == "serotonin":
            serotoninTally += 1
            continue
        elif rawAnswer == "n":
            continue
    consolidatedTally.append(dopamineTally)
    consolidatedTally.append(acetylcholineTally)
    consolidatedTally.append(gabaTally)
    consolidatedTally.append(serotoninTally)
    print("*********************\n"
          "Your results, tallied by neurotransmitter:\n"
          "Dopamine: " + str(dopamineTally) + "\n"
          "Acetylcholine: " + str(acetylcholineTally) + "\n"
          "GABA: " + str(gabaTally) + "\n"
          "Serotonin: " + str(serotoninTally) + "\n"
          "*********************"
          )
    if consolidatedTally[0] == max(consolidatedTally):
        print("Your dominant personality is DOPAMINE")
    elif consolidatedTally[1] == max(consolidatedTally):
        print("Your dominant personality is ACETYLCHOLINE")
    elif consolidatedTally[2] == max(consolidatedTally):
        print("Your dominant personality is GABA")
    elif consolidatedTally[3] == max(consolidatedTally):
        print("Your dominant personality is SEROTONIN")
"""


# Does not yet validate input
def runBravermanTest(questionSet):
    dopamineTally = 0
    acetylcholineTally = 0
    gabaTally = 0
    serotoninTally = 0
    consolidatedTally = []
    questionNumber = 1
    for question in questionSet:
        answer = input("Question #" + str(questionNumber) + "...... " + question[0])
        questionNumber += 1
        answer.lower()
        question.append(answer)
        if answer == "y" and question[1] == "dopamine":
            dopamineTally += 1
            continue
        elif answer == "y" and question[1] == "acetylcholine":
            acetylcholineTally += 1
            continue
        elif answer == "y" and question[1] == "gaba":
            gabaTally += 1
            continue
        elif answer == "y" and question[1] == "serotonin":
            serotoninTally += 1
            continue
        elif answer == "n":
            continue
        elif answer != "y" and answer != "n":
            print("***********Invalid input. Please enter either \"y\" or \"n\", then press Enter...*********")
            print("Moving on to next question...")
            continue
    consolidatedTally.append(dopamineTally)
    consolidatedTally.append(acetylcholineTally)
    consolidatedTally.append(gabaTally)
    consolidatedTally.append(serotoninTally)
    print("\n\n\n*********************\n"
          "Your results, tallied by neurotransmitter:\n"
          "Dopamine: " + str(dopamineTally) + "\n"
          "Acetylcholine: " + str(acetylcholineTally) + "\n"
          "GABA: " + str(gabaTally) + "\n"
          "Serotonin: " + str(serotoninTally) + "\n"
          "*********************"
          )
    if consolidatedTally[0] == max(consolidatedTally):
        print("Your dominant personality is DOPAMINE")
    elif consolidatedTally[1] == max(consolidatedTally):
        print("Your dominant personality is ACETYLCHOLINE")
    elif consolidatedTally[2] == max(consolidatedTally):
        print("Your dominant personality is GABA")
    elif consolidatedTally[3] == max(consolidatedTally):
        print("Your dominant personality is SEROTONIN")


nameInitials = input("Please type in your initials: ")
faveAnimal = input("Please type in your favorite animal: ")
#runBravermanTest(grandPoolQuestions)
runBravermanTest(onlyPhysical[0:3])



newPath = "C:\\Users\\moreforles\\Desktop\\LAVC_schoolwork\\CoSci802\\LAVC_CoSci802_in_Python_3p7\\" + "bravermanPersonality_" + nameInitials + "_" + faveAnimal + ".csv"
csvFile = open(newPath, 'w', newline = '')
csvContent = csv.writer(csvFile)
csvContent.writerow(["Question", "Neurotransmitter", "Section", "Answer"])
[csvContent.writerow(i) for i in grandPoolQuestions]
csvFile.close()





# Try and Except statements for input answers y/n
# What happens to ties?
