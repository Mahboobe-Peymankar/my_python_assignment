import instaloader
import getpass


L = instaloader.Instaloader()

username = input ( "enter your username:   " )
password = getpass.getpass ( "enter your password:   ")

old_followers = []
f = open ( "followers.txt" , "r" )
for line in f :
    old_followers.append ( line )
f.close()
print ( old_followers )


L.login ( username , password )
print ( "entered successful" )

account = input ( "enter an account which  you want to check his/her followers..." )
profile = instaloader.Profile.from_username ( L.context , account)

new_followers = []
for follower in profile.get_followers () :
    new_followers.append ( follower )

f = open ( "newfollowers.txt" , "w" )
for follower in new_followers:
    f.write (follower + "\n")
f.close()

for new_follower in new_followers :
    if new_follower not in old_followers :
        print (new_follower)
