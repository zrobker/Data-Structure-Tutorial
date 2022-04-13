def undo_button(sentence,quantity):
    stack = []
    
    for word in sentence.split(' '):
        stack.append(word)

    if quantity <= len(stack):
        while quantity > 0:
            stack.pop()
            quantity -= 1
        return print(stack)
    else:
        return print("Quantity Error")

sentence = "Larry waved to Susan as he drove off into the distance."
quantity = 7
undo_button(sentence,quantity) #['Larry', 'waved', 'to', 'Susan']

sentence = "We went to the ball to dance with our friends."
quantity = 3
undo_button(sentence,quantity) #['We', 'went', 'to', 'the', 'ball', 'to', 'dance']

sentence = "After she left the party, I went home."
quantity = 10
undo_button(sentence,quantity) #Quantity Error