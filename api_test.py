"""
to install a package to a global interpreter (i.e. python 3.7..)
Palette: Create New Integrated Terminal 
"""

"""
to install a package for a specific virtual environment

1 - Create a virtual environment (use the Python Terminal at the bottom)
py -3 -m venv .mleproject_test_venv
2 - Activate it
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.mleproject_test_venv\scripts\activate
3 - Select your new environment from the Palette:Python: Select Interpreter (might need to refresh)
4 - Install the packages
python -m pip install matplotlib
5 - pip freeze > requirements.txt 
===> requests==2.26.0
"""
import os
import requests
from requests.auth import HTTPBasicAuth
import sys
'''script paremeters:
The script will necessarily be called with 6 parameters, set them to "" if no value
1: "127.0.0.1" (ip address)
2: "8000" (port)
3: "permissions"(endpoint)
4: (sentence)
5: (model_index)
6: (username)
7: (password)
'''
lst_sentences = ["Visited 21 5 2014. This park is a joke, three main rides were closed in one park and one in the other and two broken which means the huge crowds made for 2 hour wait times. At $150 for a one day hopper this turned out to be an expensive crowded walk. Google Disneyland to see what a shameful joke this place is, oh...$17 to park a car. I have been to Disney Florida for 29 years so I am not naive about wait times, this park is a disgrace."
, "if walt disney is currently in a cryogenic chamber above the fire station in disneyland   s main street, he must be wanting to pull the plug. having been a fan and visitor of orlando   s walt disney world, disneyland was a disappointment. most of the staff seems to hate working there, it was hard to receive a smile. i don   t blame them, they have recently had disputes with they   re salary. the park was mostly dirty, and the bathrooms in 7 eleven were cleaner that most of the restrooms across the parks. about 40% of the rides had issues midway through. and they were unannounced closures throughout the day.one good thing was the 3 day passes that included maxpass (for fast passes) and photo pass, which were a great value. i went in trying to feel like a kid, but they brought the adult side of me."
, "I've to been to Disneyland Japan, and compare to this, Disney HK is much smaller, especially the Sleeping Beauty Castle. I visited during weekdays but still the crowd is so many. Mostly the people are from mainland China. Maybe this is summer holiday and the China crowd came. I'm not sure. Very hot and humid during this time of the year. I will go again only if   the place is expanding (there is this new attraction call 'mystic' coming soon next to Toy Story land ; and will only go during cooler season such as autumn or end on winter. Overall, good place to bring your kids."
, "Hahaha, title says it all. Ridiculous prices, but do you get what you pay for? Eh, maybe yes, maybe no. I went alone so I could do what I wanted to do. This is the first time I've actually paid to go because usually I get free tickets by winning them or knowing people who work there who need to use their extra tickets, and go with family. Prices are ridiculous, but I knew that before going. This is technically a review for both Disney parks. Cons1) Ticket lines are sooooooooooo slow. There were only a couple of people ahead of me and it took forever for my turn. Then I went up, told the lady exactly what I wanted, had my cash out, and it still took her forever. A snail could have done it faster.2) Walking in the gate with the ticket you just bought is just as slow and painful. They take pictures of you now so if you buy a multi day ticket you can't sell it off to someone else (fine, whatever, I get it) but it just makes the lines horrendously long and slow just to get in. The people behind me complained,  They should have a line for season passholders.  I don't have a season pass, obviously, but he's right. Why make them wait through the photo sessions?3) No real discounts for SoCal residents. If you want a one day pass you don't really get a discount. Discounts maybe for two or three days, but I don't need two or three days, and quite frankly if I used that I'd have to drive home and back and one drive up to Anaheim every few months in the crummy CA traffic is more than enough. If I stayed in Anaheim then I'd have to pay extra for a hotel, so there really wouldn't be savings.4) Soooooooooo many people. They should cut off the number somewhere, but obviously they won't because of $$$$$$$$$. Oh, and this wasn't considered a  Peak Day . I'd hate to see how many people are there on those days. 5) Single Ply Toilet Paper? That seriously wasn't a joke. Why do you pay so much for tickets and then use the restrooms to find out they only buy single ply toilet paper? Cheapskates. (Yeah, I can't believe I even had that thought, but I did.)6) Disney is great at line deception. You see the time, then look at the line and think,  Oh, that's not so bad.  Then you get in line and it just goes back and forth and back and forth and around and down and up and in places you didn't even know existed getting into the line..... Yikes. It's amazing how well they can hide a line of a gazillion people.7) Dirty. Dirty. Dirty. Usually Disney is pretty clean, but this time it was just gross. Food all over the ground. Almost squished my feet in several discarded food items including popcorn, ice cream sandwiches, and who knows what else. And there were random things lying around in ride lines *cough cough* tampon *cough cough*. EW. 8) People start lining up for the parade like two hours early and then there are just people in the way. Everywhere. Oh, and for those of use pathetic souls there by ourselves, who might want to go on rides that normally have lines out the wazoo with parents and little kids in Fantasyland.... Parade time might be a good time to do that except, oh yeah, they shut everything down in Fantasyland at that time. Now I'm not sure of the real reasoning behind this because at this point, I left and went to Downtown Disney until after the parade and fireworks crowd cleared out, but yeah, that sucks. I can't for the life of me figure out why the ride for the Peter Pan ride is so massively long, even when I've gone to  night parties  with radio stations. Fourth or fifth time here and FINALLY got on it   with a  Short  time of 30 mins, and this was at 11:00pm. 9) People are rude as can be. Cutting in line, trying to ram you with their stroller if you aren't moving fast enough (trust me, I move as fast as possible, but can't do that if there are a million people in the way). Just randomly stop in the middle of walkways to check their phone or map. 10) Disney used to have lines down to a science. What happened? Fast pass lines longer than the regular line. People seemed to be having trouble having their phones scan using that option for their fast passes, so that slowed things down. Employees urging people to get fast passes for that CURRENT TIME so the people already in line have to wait longer (why??). Single rider line over on Screamin' is a joke (Universal does this very well, Disney does NOT. Maybe it's done poorly on purpose?) 11) There are issues with the lines in the restaurants. The main one I went to was Rockett's whatever over in Tomorrowland. Choices of Salad, Pasta, or Pizza. The employee flat out said Salad and Pasta were one line, Pizza was separate. Then he disappeared, so while the rest of us waited for pasta in a non moving salad line, people were cutting ahead of us and getting grumpy behind us. Food didn't appear to be coming out, and the line was at a stand still. 12) Parking. Due to the number of people you park all the way out in the Timbuktu Lot, and then you get the fun of waiting in a long line (for the shuttles)   before you even get to the parks!13) Star WarsPros1) Long Hours. The day I went the hours at DL were 8am to 12am (till 10pm at CA). I had hoped to get there earlier, but to avoid the worst of the traffic on the expressways, I didn't leave until about 8:30am and got there by about 10:15am. This actually worked out better for me. I ended up staying there later that evening and I got in a good number of rides AFTER the fireworks crowd left. If I had gotten there earlier, I probably would have left the parks earlier and not come back. 2) Due to the close Proximity of the parks, I was able to go to DL, do a bunch of stuff, head over to CA and do many things I wanted to do, then head back to DL and get in some more fun. I was also able to  escape  for a bit and grab dinner at Downtown Disney, then head back yet again. 3) Was happy with what I managed to fit into my day. I fit in my favorites. Did a bunch of extras. Saw some of those street shows. Got to both parks. And this was with a million people there. If you're able to use the Fast Passes properly (I only used one all day, by the way   and didn't pay extra for whatever the cell phone thing is, since I don't have a cell phone) and pay attention to the slow areas you'll get in quite a bit. If you go on an off day you can probably squeeze a lot more into a one day ticket. 4) Employees   All were nice and super helpful, no matter how stupid my question. Hey, it's Disney!5) Free Water   Managed to get through the day buying only one drink. With my meals and even the ice cream I had, I just got a nice cup of ice water. At the right places they'll give you nice big cups too, rather than those dinky little things, to stay cool and hydrated! And trust me, on a mid summer day in SoCal, you'll appreciate it.6) First Aid area was a lifesaver. I had a massive headache I had been battling all day and despite drinking tons of water and doing everything I knew how to get rid of it without taking anything, I finally decided to get something so I could fully enjoy the rest of the day. I thought it might take awhile but I simply asked if they had anything, wrote down my name, and they handed me a two pack of some sort of headache relieving awesomeness. Easy peasy. Overall it was a decent day, but I think I'll stick with my original belief that it's only best to go to places like this in the off season. It was good for the day it was, but could have been a lot less stressful and lot more enjoyable when it's not as packed."
,"Went to Disneyland Paris, 4 8 September. All I can say is that whatever price you have budgeted for this holiday, treble it at least and that is how much money you are likely to spend.My advice is save up and go to Florida. The food and drink are way over priced, all the fast food is the same. The Queues are ridiculous, 30 minutes every time you want to buy a drink, 2.59 euros for a small cup of tea.The staff have no idea of what customer service is, for example at Casey's Corner, I wanted 5 teas, Queued for ages to be told they had no milk but I could have hot milk in my tea and then was told I would have to pay for the hot milk on top of the 2.59 for the tea, what a joke, I told them to shove it.The Americans fall over themselves backwards to help,the Disney staff need to get some serious tips on customer service. 95% don't crack a smile and couldn't care less if you enjoy your day or not, as long as you are paying the money that's all they seem bothered about.The Queues for rides are terrible, especially weekends, 120 minutes for the main rides, half the time the fast passes were not working. Every day at least one of the main rides wasn't working.Than goodness we had been there for two days before else would have only managed 3 rides in the day.They let far too many people in for the size of the park and the amount of staff they employ.The pushing in, has to be seen to be believed. The Europeans have no manners at all, I can't believe I had forgotten this fact.Was in one Queue and up to 20 people pushed in before we got to the ride, my daughter spoke to one Spanish family and asked them to go to the back of the queue, only for the father to shout shut up in my daughter's face. Very intimidating and very rude.The staff ignore all the pushing and shoving in the queues, they have no queue management at all.I gave the park two stars for the park itself and the late night show and even that was a bun fight at night. People shoving and pushing to get a position to see the castle. On the Saturday night, a bunch of French teens were throwing their rubbish at an English couple standing at the front and kept shouting out are you English and even though French staff were standing around the edge, they did nothing. This was the same every evening, as every night there were nearly fights amongst the crowd but staff always turned a blind eye.Six of us went to Disneyland Paris and none of us will go back. Give me Florida any day and in the end, the food, drink, and merchandise is so much cheaper."
]
lst_queries = [("","","","","")
, ("text_to_sentiment",lst_sentences[0],1,"alice1","wonderland")
, ("text_to_sentiment",lst_sentences[0],1,"alice","wonderland1")
, ("text_to_sentiment",lst_sentences[0],6,"alice","wonderland")
, ("text_to_sentiment",lst_sentences[0],1,"alice","wonderland")
, ("text_to_sentiment",lst_sentences[1],1,"alice","wonderland")
, ("text_to_sentiment",lst_sentences[2],2,"alice","wonderland")
, ("text_to_sentiment",lst_sentences[3],3,"alice","wonderland")
, ("text_to_sentiment",lst_sentences[4],4,"alice","wonderland")
]
print(str(len(sys.argv))+ " argument(s) are sent")
if __name__ == "__main__":
    if (len(sys.argv) < 8):
    #just for debugging
        index_tested_query=7
        api_address = '127.0.0.1'#'disneyreviews.azurewebsites.net'
        api_port = '8000'#'80'
        api_endpoint = lst_queries[index_tested_query][0]
        test_sentence = lst_queries[index_tested_query][1]
        test_model_index = lst_queries[index_tested_query][2]
        test_username = lst_queries[index_tested_query][3]
        test_password = lst_queries[index_tested_query][4]
    else:
        """
        "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe" api_test.py "127.0.0.1" "8000" "text_to_sentiment" "Visited 21 5 2014. This park is a joke, three main rides were closed in one park and one in the other and two broken which means the huge crowds made for 2 hour wait times. At $150 for a one day hopper this turned out to be an expensive crowded walk. Google Disneyland to see what a shameful joke this place is, oh...$17 to park a car. I have been to Disney Florida for 29 years so I am not naive about wait times, this park is a disgrace." 1 alice wonderland
        """
        api_address = sys.argv[1]
        api_port =sys.argv[2]
        api_endpoint = sys.argv[3]
        test_sentence = sys.argv[4]
        test_model_index = sys.argv[5]
        test_username = sys.argv[6]
        test_password = sys.argv[7]

#a dictionnary will contain the expected result for each set of parameters
#the key will be formatted from {endpoint}#{sentence}#{model_index}#{username}#{password}
#the value will be a tuple with (status_code, model_score)
dict_tests_expected_results ={
    '####': (200, '1'), #test index
    'text_to_sentiment#{sentence}#1#alice1#wonderland'.format(sentence=lst_sentences[0]): (401, ''), #test => bad username
    'text_to_sentiment#{sentence}#1#alice#wonderland1'.format(sentence=lst_sentences[0]): (401, ''), #test => bad password
    'text_to_sentiment#{sentence}#6#alice#wonderland'.format(sentence=lst_sentences[0]): (422, ''),  #test bad model_index=6 => status 422
    'text_to_sentiment#{sentence}#1#alice#wonderland'.format(sentence=lst_sentences[0]): (200, '[1]'), #test => score = 
    'text_to_sentiment#{sentence}#1#alice#wonderland'.format(sentence=lst_sentences[1]): (200, '[3]'), #test => score = 
    'text_to_sentiment#{sentence}#2#alice#wonderland'.format(sentence=lst_sentences[2]): (200, '[4]'), #test => score = 
    'text_to_sentiment#{sentence}#3#alice#wonderland'.format(sentence=lst_sentences[3]): (200, '[3]'), #test => score = 
    'text_to_sentiment#{sentence}#4#alice#wonderland'.format(sentence=lst_sentences[4]): (200, '[2]') #test => score = 
}

#REQUEST
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}
url='http://{address}:{port}{endpoint}'.format(address=api_address, port=api_port
    , endpoint=("" if api_endpoint== "" else "/" + api_endpoint + "/")
    #, sentence=("" if test_sentence== "" else "/" + test_sentence)
    #, model=("" if test_model_index== "" else "/" + test_model_index)
    )
if (test_sentence != "" and test_model_index != ""):
    myparams={"text": "", "model": 0}#.format(test_sentence=test_sentence, test_model_index=str(test_model_index))
    myparams["text"]=test_sentence
    myparams["model"]=test_model_index
else:
    myparams=None
#if endpoint is "" then no authentication needed
if api_endpoint != "":
    myauth=HTTPBasicAuth(test_username, test_password)
    r = requests.post(url, auth= myauth, json = myparams, headers=headers)
else:
    myauth=None
    r = requests.get(url, auth= myauth, json = myparams, headers=headers)

# get request HTTP status (200, 401..)
request_status = r.status_code
response=r.json()
# get the expected tuple (status_code, score) matching the current parameters of the script from the dictionnary
expected_result = dict_tests_expected_results[api_endpoint+"#"+test_sentence+"#"+str(test_model_index)+"#"+test_username+"#"+test_password]
    
try:
    request_score=response["score"]
except:
    request_score=""

if request_status == expected_result[0] and request_score == expected_result[1]:
    test_status = 'success'
else:
    test_status = '!!FAILURE!!!'

output = '''
============================
    API test
============================
Request done at "/{endpoint}"
| sentence={sentence}
| model_index={model_index}
| username="{username}"
| password="{password}"
=> Test(expected vs actual) / HTTP Status: {expected_status} vs {request_status} / Score: {expected_score} vs {request_score} ==> {test_status}
'''

stroutput=(output.format(sentence=(test_sentence if len(test_sentence) < 80 else test_sentence[0:80] + "..."), expected_status=expected_result[0], expected_score=expected_result[1], username=test_username, password=test_password, endpoint=api_endpoint, request_status=request_status, test_status=test_status, request_score=request_score, model_index=test_model_index))
print(stroutput)

'''
# impression dans un fichier
#if os.environ.get('LOG') == 1:
with open('/home/api_test.log', 'a') as file:
    file.write(stroutput)
    file.close() 
'''