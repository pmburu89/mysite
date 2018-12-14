from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import QuizItem

def myView(request):
    all_quiz_items = QuizItem.objects.all()
    return render(request, 'quiz.html', 
        {'all_items': all_quiz_items})

def addQuiz(request):
    # create a new quiz all_items
    new_item = QuizItem(content = request.POST['content'])
    # save
    new_item.save()
    # redirect the browser to '/quiz/'
    return HttpResponseRedirect('/quiz/')

def deleteQuiz(request, quiz_id):
    item_to_delete = QuizItem.objects.get(id=quiz_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/quiz/')


import string
import random
 
 
class Question:
 
    def __init__( self, prompt = "", answers = [], \
                  correct_answer = None):
 
        self.prompt = prompt
        self.answers = answers
 
        self.correct_answer = correct_answer
 
        # If we are creating answers "in-line", use an index
        # to reference the correct answer
        if ( type(self.correct_answer) == type( int() ) ):
            self.correct_answer = self.answers[self.correct_answer]
 
 
 
class Answer:
    
    def __init__( self, text = "", point_value = 0 ):
 
        self.text = text
        self.point_value = point_value # expect it in 1...10
 
 
 
#------------------------------------------------
 
 
class Quiz:
 
    def __init__( self ):
 
        self.score = 0

        # JOHN: Adding this so we can know the range of your answer values....
        #       It allows us to determine the average.
        self.total_possible_score = 0
 
    def tell_current_score( self ):
 
        print ("Your current score is %d." % self.score)
 
        print ('='*30) # ==============================
        
 
 
 
    def ask_a_question( self, question ):
 
        answered = False
 
        print (question.prompt)
 
        number_of_possible_answers = len(question.answers)
 
        for index, answer in enumerate(question.answers):

            # JOHN: Adding up all the possible answer values, so we can
            #       tally the average later on
            self.total_possible_score += answer.point_value
            print (([index]), answer.text)
 
        while ( not answered ):
            their_answer = input('> ')
 
            # JOHN: It looks like you are suggesting possible answers with 
            #       numbers, so we should use string.digits instead
            # if (their_answer and their_answer in string.ascii_letters[:number_of_possible_answers]):
            if (their_answer and their_answer in string.digits[:number_of_possible_answers]):

                # JOHN: See comment above for this line change:
                # index_of_answer = string.ascii_letters.index(their_answer)
                index_of_answer = string.digits.index(their_answer)
                answer_they_give = question.answers[index_of_answer]
 
                # Optional feedback...
                #if ( answer_they_give.point_value <= 5 ):
                 #   print ("Bad answer!")
                #else:
                 #   print ("Good answer!")
               
                if ( answer_they_give == question.correct_answer ):
                    # JOHN: Commented these lines out because you said you didn't want it to display...
                    # print ("CORRECT! You got it right!")
                    # print ("Adding %d points to your score..." % question.correct_answer.point_value)
                    self.score += question.correct_answer.point_value
 
 
                else:
                    # JOHN: Commented these lines out because you said you didn't want it to display...
                    # print ("INCORRECT! You got it wrong!")
                    # print ("Adding %d points to your score..." % question.correct_answer.point_value)
                    self.score += question.correct_answer.point_value
                answered = True
 
            else:
                print ("That is not a valid answer!")
                answered = False
 
    def ask_many_questions( self, questions ):
 
        for question in questions:
            self.ask_a_question( question )

            # JOHN: Commented this out because you said you didn't want it to say anything..
            # self.tell_current_score()
 
    def ask_random_sample_of_questions( self, questions, number ):
 
        random_sample_of_questions = []
 
        for i in range( number ):
            new_question = random.choice(questions)
            random_sample_of_questions.append(new_question)
            questions.remove(new_question)
 
        self.ask_many_questions(random_sample_of_questions)


    # JOHN: Added a generic function to handle the averaging...
    def tell_results( self, average ):

        # JOHN: I put the key in as an array. It should be in order from 0-10 (like an average)...
        # So in this case, the HIGHER the score, the more likely to be a fuck boy.
        ORDERED_key = [
        "Fuck boy:  He is a great guy will probably propose in 3 months.  Equivalent to ciara’s prayer type of man.",
        "Fuck boy: Also a great guy will propose in 4 months.  Equivalent to meagan good’s prayer type of man.",
        "Fuck boy: Great guy.  Will claim your kids as his and take care of them.",
        "Fuck boy: Good guy.  He will have tendencies that annoy you but you will get through it. His good habits will rub off on you.  Even if you guys don’t make it.",
        "Fuck boy: Good guy.  Yall will fight a lot because even though he sees things your way.  He will play devil’s advocate by trying to get you to understand the other side",
        "Fuck boy: not a bad guy just doesn’t realize he is not ready for a relationship.  He will say he really likes you but doesn’t like labels.  You can flip him to a 5 or lower but its a coin toss.  This is the guy you think you can change. Will claim to be a fuck boy.  After you he will probably be a good guy.",
        "Fuck boy: doesn’t want to be in a relationship.  The way he hooks up with girls is by letting them think they have a future together without saying it.  Leads girls on and when confronted acts oblivious. Lives in the dms.  Brags about his body count",
        "Fuck boy: Every break up he swears the girl was the problem that is why it didn’t work out.  Has an explanation for why men should get paid more than women. ",
        "Fuck boy:  If his advances are shut down by a girl, he will call the girl names.  Will cancel on you and expect you to be available on his schedule. He thinks fuck boys are weak men",
        "Fuck boy: stay the fuck away.  He doesn’t think he is a fuck boy out of ignorance but out of arrogance.  "
        ]
    

        # Remember to subtract one because the key is index based:
        index = round(average * len(ORDERED_key)) - 0 # Map the average number to the possible size of this key.   

        print("="*30)
        print("The results are in! Your answers determined:\n" )
        
        print(ORDERED_key[index])

        print("\nThanks for playing!")

    def run( self ):
 
 
        # -------------------------------
 
        # JOHN: Setting this as a variable so we can take the average
        number_of_questions = 7

        # self.ask_many_questions(
        self.ask_random_sample_of_questions(
            [
                # List of question...
 
                Question( \
prompt = "Would you talk to a girl that made you wait a month before you had sex?",
answers =       [
                    Answer("Yes", 1),
                    Answer("No", 8),
                    ],
correct_answer = 1 # so "Yes" is the correct answer in this case.
                ),
 
                # more questions....
 
                Question( \
prompt = "Would you lie to your girl if the truth would break her heart?",
answers =       [
                    Answer("Yes", 8),
                    Answer("No", 3),                    
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),
 
 
                Question( \
prompt = "Would you sleep with a girl that u know has feelings for you even though you don’t like her?",
answers =       [
                    Answer("Yes", 8),
                    Answer("No", 1),
                    ],
correct_answer = 0 # so "No" is the correct answer in this case.
                ),
 
 
 
                Question( \
prompt = "If a boyfriend breaks up with his girlfriend because he no longer want to be with her.  And a few weeks later she invites him to her house and he has sex with her.  Whose fault is it?",
answers =       [
                    Answer("The boyfriend", 2),
                    Answer("The girlfriend", 7),
                    ],
correct_answer = 1 # so "The boyfriend" is the correct answer in this case.
                ),
 
                
                Question( \
prompt = "If u won a million dollars what would you buy first? A house or a car?",
answers =       [
                    Answer("House", 4),
                    Answer("Car", 6),
                    ],
correct_answer = 1 # so "House" is the correct answer in this case.
                ),

                Question( \
prompt = "What’s your credit score?",
answers =       [
                    Answer("0-400", 8),
                    Answer("401-700", 7),
                    Answer("701-800", 4),
                    ],
correct_answer = 1 # so "701-800" is the correct answer in this case.
                ),

                Question( \
prompt = "Are you a fuck boy?",
answers =       [
                    Answer("Yes", 4),
                    Answer("No", 8),
                    ],
correct_answer = 1 # so "Yes" is the correct answer in this case.
                ),

                Question( \
prompt = "Do you have fuck boy tendencies?",
answers =       [
                    Answer("Yes", 3),
                    Answer("No", 10),
                    ],
correct_answer = 1 # so "Yes" is the correct answer in this case.
                ),

                Question( \
prompt = "Did you achieve your new year's resolution last year?",
answers =       [
                    Answer("Yes", 2),
                    Answer("No", 6),
                    ],
correct_answer = 1 # so "Yes" is the correct answer in this case.
                ),

                Question( \
prompt = "Are you a cock blocker?",
answers =       [
                    Answer("Yes", 10),
                    Answer("No", 1),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "How many insta models are you following on instagram or snapchat?",
answers =       [
                    Answer("0-19", 3),
                    Answer("20-29", 5),
                    Answer("30+", 10),
                    ],
correct_answer = 1 # so "0-19" is the correct answer in this case.
                ),

                Question( \
prompt = "If you see a cute girl in front of your home boys do you ever call dibs?",
answers =       [
                    Answer("Yes", 8),
                    Answer("No", 4),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Do you think women should be paid as much as men?",
answers =       [
                    Answer("Yes", 4),
                    Answer("No", 10),
                    ],
correct_answer = 1 # so "Yes" is the correct answer in this case.
                ),

                Question( \
prompt = "Are most of your friends fuck boys?",
answers =       [
                    Answer("Yes", 10),
                    Answer("No", 4),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Do you support the slut walk?",
answers =       [
                    Answer("Yes", 5),
                    Answer("No", 8),
                    ],
correct_answer = 1 # so "Yes" is the correct answer in this case.
                ),

                Question( \
prompt = "Do you believe in the friend zone?",
answers =       [
                    Answer("Yes", 6),
                    Answer("No", 5),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "What do you think fuck boy means?",
answers =       [
                    Answer("A weak man", 10),
                    Answer("A man manipulates women and takes advantage of their feelings.", 1),
                    ],
correct_answer = 1 # so "A man manipulates women and takes advantage of their feelings." is the correct answer in this case.
                ),

                Question( \
prompt = "If a woman called you a “fuck boy” would you be mad?",
answers =       [
                    Answer("Yes", 8),
                    Answer("No", 1),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "If you break up with a girl, is it because the girl did something that caused you to break up with her?",
answers =       [
                    Answer("Yes", 10),
                    Answer("No", 5),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Your girl got mad at you for coming home late without calling to say you were fine; even though, you told her you would come home late.  Would you be mad?",
answers =       [
                    Answer("Yes", 10),
                    Answer("No", 1),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Have you ever call a vagina a 'box'?",
answers =       [
                    Answer("Yes", 7),
                    Answer("No", 3),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Do you kiss and tell?",
answers =       [
                    Answer("Yes", 6),
                    Answer("No", 3),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "In a given social gathering, what percentage of girls do you think you can leave home with?",
answers =       [
                    Answer("0-10%", 5),
                    Answer("11-30", 2),
                    Answer("31-70%", 6),
                    Answer("71-100", 9),
                    ],
correct_answer = 1 # so "11-30%" is the correct answer in this case.
                ),

                Question( \
prompt = "Have you ever cheated?",
answers =       [
                    Answer("Yes", 10),
                    Answer("No", 1),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Is it okay to flirt with other girls while in a relationship?",
answers =       [
                    Answer("Yes", 5),
                    Answer("No", 4),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Is a guy entitled to sex with a person they are in a relationship with?",
answers =       [
                    Answer("Yes", 10),
                    Answer("No", 1),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Do you generalize when talking about a woman’s trait? Ie 'All women…'",
answers =       [
                    Answer("Yes", 8),
                    Answer("No", 3),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Have you sent an unrequested dick pic?",
answers =       [
                    Answer("Yes", 7),
                    Answer("No", 3),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Have you requested nude pics from a woman you are not in a relationship with?",
answers =       [
                    Answer("Yes", 7),
                    Answer("No", 2),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Do you use the phrase 'bros before hoes?'",
answers =       [
                    Answer("Yes", 6),
                    Answer("No", 1),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Do you think women are scared of men most of the time?",
answers =       [
                    Answer("Yes", 2),
                    Answer("No", 8),
                    ],
correct_answer = 1 # so "Yes" is the correct answer in this case.
                ),

                Question( \
prompt = "Did you know some girls wake up early and put makeup on so that their man think they always look like that?",
answers =       [
                    Answer("Yes", 5),
                    Answer("No", 1),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Is your car leased?",
answers =       [
                    Answer("Yes", 8),
                    Answer("No", 4),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "How many times do you take the same pic before u decide it is good enough?",
answers =       [
                    Answer("0-3", 4),
                    Answer("4-6", 7),
                    Answer("7+", 10),
                    ],
correct_answer = 1 # so "0-3" is the correct answer in this case.
                ),

                Question( \
prompt = "Have you ever let a girl pay for the first date?",
answers =       [
                    Answer("Yes", 8),
                    Answer("No", 3),
                    ],
correct_answer = 1 # so "No" is the correct answer in this case.
                ),

                Question( \
prompt = "Do you communicate with your partner during sex?",
answers =       [
                    Answer("Yes", 1),
                    Answer("No", 10),
                    ],
correct_answer = 1 # so "Yes" is the correct answer in this case.
                ),


                
                
                # ...
 
            ]
        , number_of_questions) # only ask SEVEN random questions...

        average = float(self.score) / float(self.total_possible_score)

        self.tell_results(average)
 
 
if ( __name__ == "__main__" ):
 
    quiz = Quiz()
    quiz.run()