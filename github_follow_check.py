from github import Github
import os
import keyboard


def check_unfollowers(username, access_token):
    # Initialize GitHub client
    g = Github(access_token)
    
    try:
        # Get authenticated user
        user = g.get_user()
        
        # Get followers and following
        followers = set(follower.login for follower in user.get_followers())
        following = set(followed.login for followed in user.get_following())
        
        # Find users who don't follow back
        non_followers = following - followers
        
        # Print results
        if non_followers:
            print(f"You're following: {len(following)} accounts")
            print(f"You have: {len(followers)} followers")
            print(f"The number of villians who don't follow you back are ({len(non_followers)}):")         
                
        else:
            print("\nAll users you follow also follow you back!")
            

        # Display message if no non-follower to unfollow
        if not non_followers:
            print("\nNo users to unfollow.")
        
        else:
            # Ask if the user wants to unfollow non-followers
            print("\nKindly select an option(e.g 1)...")
            print("1. Unfollow all non-followers")
            print("2. Choose specific users to unfollow")
            print("3. Don't unfollow any")
            print("4. Enter any other key to exit")
            unfollow_choice = input("\nEnter option: ").strip().lower()
            
            match unfollow_choice:
                case '1':
                    for nf in non_followers:
                        try:
                            user_to_unfollow = g.get_user(nf)
                            user.remove_from_following(user_to_unfollow)
                            print(f"\nUnfollowed {nf}")
                        except Exception as e:
                            print(f"Failed to unfollow {nf}: {str(e)}")
                    print("\nJustice is served!\n")
                    
                case '2':
                    print("\nEnter the numbers of the users you want to unfollow, separated by commas: (e.g., 1,2,3)")
                    for idx, nf in enumerate(sorted(non_followers), start=1):
                        print(f"{idx}. {nf}")
                    try:
                        choices = input("\nYour choices: ").strip()
                        indices = [int(i) for i in choices.split(',') if i.isdigit()]
                        for idx in indices:
                            if 1 <= idx <= len(non_followers):
                                nf = sorted(non_followers)[idx - 1]
                                try:
                                    user_to_unfollow = g.get_user(nf)
                                    user.remove_from_following(user_to_unfollow)
                                    print(f"\nUnfollowed {nf}")
                                except Exception as e:
                                    print(f"Failed to unfollow {nf}: {str(e)}")
                            else:
                                print(f"\nInvalid choice: {idx}")
                    except Exception as e:
                        print(f"Error processing choices: {str(e)}")
                    
                    print("\nJustice is served!\n")
                    
                case '3':
                    print("\nNo users were unfollowed...")
                    print("Very generous\n")

                case _:
                    print("\nInvalid response. Exiting...\n")
   
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Start a key listener for the 'Esc' key
def exit_program():
    print("\nEsc key pressed. Exiting the program...")
    os._exit(0)  # Force exit the program


def main():
    # Set up a listener for the 'Esc' key
    print("Press 'Esc' at any time to exit the program.\n")
    keyboard.add_hotkey('esc', exit_program)

    # Get GitHub credentials
    print("Welcome to the GitHub Unfollowers Checker!")
    print("Please provide your GitHub username and personal access token.")

    username = input("GitHub username: ")
    access_token = os.getenv("GITHUB_TOKEN") or input("GitHub personal access token: ")

    print(f"\nCounting the bad nuts in {username}'s soup...\n")

    # Check for unfollowers
    check_unfollowers(username, access_token)      
    

if __name__ == "__main__":
    main()