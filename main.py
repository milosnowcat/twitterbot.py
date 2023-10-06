#                      .                    .                           
#                 :-:--=:-:::.             :=-**##*=:                   
#                  :=----------.         .-%@@@@@@@@@%:                 
#                 :-------------:        :@@@@@@@@@@@@%.                
#                :-=-----------==:       +@@@@@@@@@@@@@#                
#              .------------=------.     =@@@@@@@@@@@@@#                
#               :=-=-------===-=--      .+%@@@@@@@@@@@#=                
#                --=--------==-=-.       -*%@@@@@@@@@*-.                
#                   ::----===+-             .#%@@@@*.                   
#                      -+++=: .               :+##+                     
#                     -+=====.              .=%@@%%%#=                  
#                  :-----------:.        :+#%%%@@@@@%@%+-               
#                -----------------      -%%%%%@@@%@@%%@%%*              
#               .-==----------==--:     #%%%@%@@@@@@@@@@%%.             
#               :-=+----------*=---    =%%%@@%%@@@%%@@@%%%=             
#               ---=----------*----:  .#%%%@@%%@@@%@%@@%%%%             
#              :-===----------+=---=  -#%%%@@%%@%@%@%@@%%%%=            
#                --=----------=#==+.   ==+%@@%%@@@%@%@@*++.             
#                --=-----------*=---  :===#@@%%@@@%@%%%--=              
#                -==-----------++--=  ---:#@%@@@%%%@@@%--=              
#                -=------------=:--=. =-- %@%%%%%%@%%%@=-=              
#               .-+-------------.:---.--: %%%%%%%%@%%@@+==              
#               :-++*++++++*+***. --=+--  *###########**-=              
#               --*+++++++++*+++: :--*-: :------=------*-=              
#               =-*++++++++*+***- .--*-. :-------------+-=              
#              .--*+++=+*++*+***+ :==*=: -------=------===:             
#              :=+++++==+++*++**+ -*++=. -------+-------+=:             
#               -++++=+==**+++***  :-:   -------+-------+.              
#                -+++=++=****+**#        -------+=------=               
#                .++==*=---=*+**+        =------+*------=               
#                 ----=    :---=          ====-.::+====                 
#            :**#==---=:   ----= ..   .:::=--=+*%#*--=+***. .--:..      
#            .=+**#=--==   :=--=%@*:.-=+%%*--=: ::+=--+***+=#@%*-=-::.  
#                :+=--=. :::=--=:.-*#%*--=*---+-+**=--=--=+**+*=**%@%=  
#                  =--= .#%%=--=.  +*#%#= +---#%++#=---.+%@%+  .+++*+-  
#                  ====   .:+===:   -==+= :===*+: -==== .--:.      ..   
#                  =--=     ----:         .----   :=---                 
#                  ----     :---:         .=---   .=---                 
#                  ----     :---:         .=---    =---                 
#                  ---:     :---:         .=---    +---                 
#                  +##%.    =*##-         -%%#:    %%%#                 
#                 :@@@@-    #@@@+         %@@@*   :@@@%:                
#                 .====.    -++=:         =+==-    --==.                

# @milosnowcat

import os
import tweepy
from dotenv import load_dotenv
import utils

def api():
    """
    The `api()` function returns an instance of the `tweepy.API` class with the necessary authentication
    credentials.
    :return: The function `api()` returns an instance of the `tweepy.API` class, which is authenticated
    using the provided API key, API secret, access token, and access token secret.
    """
    load_dotenv()
    
    api_key = os.environ.get('Api_Key')
    api_secret = os.environ.get('Api_Secret')
    token = os.environ.get('Access_Token')
    token_secret = os.environ.get('Access_Token_Secret')
    
    auth = tweepy.OAuthHandler(
        consumer_key=api_key,
        consumer_secret=api_secret
    )

    auth.set_access_token(token, token_secret)
    
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str):
    """
    The function `tweet` takes in an instance of the `tweepy.API` class and a string `message`, and uses
    the API to update the user's status with the given message.
    
    :param api: The `api` parameter is an instance of the `tweepy.API` class. It is used to interact
    with the Twitter API and perform actions such as updating the status (tweeting)
    :type api: tweepy.API
    :param message: The message parameter is a string that represents the content of the tweet you want
    to post
    :type message: str
    """
    api.update_status(message)
    print('Tweeted successfully! ')

def main():
    """
    The main function retrieves a quote and its author using the utils module, and then tweets the quote
    and author using the api module.
    """
    quote, author = utils.get_quote()
    tweet(api(), f'{quote} ~ {author}')

main()
