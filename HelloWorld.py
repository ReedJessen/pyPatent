from Models import Patent

if __name__ == "__main__":

    #create new empty patent object
    example_patent = Patent()
    #set one of its unique identifiers
    example_patent.grant_number = 6857069
    #populate the rest of the patent data
    example_patent.populate()


    #see what is there
    print(example_patent.__dict__)


