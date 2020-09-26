def feedbackReview(feedback, size):
    return [feedback[i:i+size] for i in range(0,len(feedback),size)]

print(feedbackReview("This is an example feedback",8))
print(feedbackReview("This is an example feedback",4))