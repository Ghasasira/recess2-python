
#exercise
name=input('Can we please get your name:')
print(f"you're welcome,{name}")

feedback_messages = {
        1: "I'm really sorry to hear that. It's important to reach out to someone you trust for support.",
        2: "I'm sorry to hear that you're not doing well. Remember, you don't have to face it alone.",
        3: "I understand that you're struggling. It might be helpful to talk to a professional about how you're feeling.",
        4: "I'm sorry to hear that you're feeling down. Take care of yourself and seek support if needed.",
        5: "I hope you feel better soon. Remember to practice self-care and reach out to loved ones.",
        6: "It sounds like you're doing okay, but there's always room for improvement. Take time for yourself.",
        7: "That's a good rating! Keep up the positive mindset and continue taking care of your mental health.",
        8: "Great to hear that you're doing well! Stay focused on self-care and maintaining your well-being.",
        9: "That's wonderful! You're in a really good place mentally. Keep up the positive outlook.",
        10: "Congratulations on a perfect rating! You're doing fantastic. Keep up the great work!"
    }


try:
    rating = int(input("On a scale of 1 to 10, how would you rate your mental health? "))
    if rating in range(10):
        feedback_message = feedback_messages[rating]
        print(feedback_message)
    if(rating<1 or rating>10):
        print('enter a number between 1 and 10')       
    
    
except Exception as exc:
    print(f'{exc.__class__.__name__} has occured ')
    print('please enter a valid number')
finally:
    print('thanks for coming')
    
 #summary of the content taught in lecture 2   
print('\n\n\n\n\n')   
print('my summary for the whole lecture')


numbers=[]
while len(numbers)<5:
    try:
        x=int(input('enter a number:'))
        if x%2==0:
            print (f'{x} is a even number')
            numbers.append(x)
        else:
            print (f'{x} is an odd number')
            continue


    except Exception as exc:
        print(f'{exc.__class__.__name__} has occured ')
        print('please enter a valid number')
    finally:
        print('continue')
else:
    print ('all the elements are added to the list')
    for number in numbers:
        print(number)
