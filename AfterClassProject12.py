def shutdown(choice):
    if choice.lower() == "yes":
        print("Shutting down...")
    elif choice.lower() == "no":
        print("Shutdown cancelled.")
    else:
        print("Please enter Yes or No.")

answer = input("Do you want to shut down? Yes/No: ")
shutdown(answer)