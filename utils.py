"""
This file stores the prompts and some helper dictionaries and functions.
"""


def swap_words(s, x, y):
    return y.join(part.replace(y, x) for part in s.split(x))


fits_domain_renaming = {
    'Celebrity': 'Celebrities', 
    'Literature': 'Literature', 
    'Psychology': 'Psychology', 
    'Food/Nutrition': 'Nutrition', 
    'History': "History", 
    'Cooking Recipes': "Cooking",
    'Politics': "Politics", 
    'Skincare': "Skincare",
    'Shopping': "Shopping",
    'Music songs': "Music",
    'Clothing/Crocheting/Knitting': "Knitting",
    'Art': "Art",
    'Games': "Games",
    'Gardening': "Gardening",
    'Finance': "Finance",
    'Beauty': "Beauty",
    'Health/Nutrition': "Health",
    'Writing': "Writing",
    'Medical': "Medicine",
    'Car': "Cars", 
    'Gifts': "Gifts", 
    'Education': "Education", 
    'Sports': "Sports", 
    'Math': "Math", 
    'Clothing': " Clothes", 
    'Clothing/Crocheting/knitting': "Knitting", 
    'Travel': "Travel", 
    'Pets': "Pets", 
    'Environment': "The Environment", 
    'Gaming': "Gaming", 
    'Philosophy/Psychology': "Philosophy", 
    'Fitness': "Fitness", 
    'Philosophy': "Philosophy", 
    'Food/Drink': "Food", 
    'Movies': "Movies", 
    'Anime': "Anime", 
    'Petting': "Petting", 
    'Home deco/repairs': "Home Renovation", 
    'Society/Law': "Law", 
    'Music': "Music", 
    'Health': "Health", 
    'Relationship': "Relationships", 
    'Tech': "Technology", 
    'Science/STEM': "Science", 
    'Business': "Business",
    'Fintness': "Fitness", 
    'Clothes': "Clothes", 
    'Movie/TV': "Entertainment", 
    'Food/Drinks': "Food", 
    'Movie': "Movies", 
    'Personal investment': "Personal Investments", 
    'Parenting': "Parenting", 
    'Education/Career planning': "Education", 
    'Tech/Electronics': "Technology", 
    'Pet': "Pets"
    }

conversation_pool = [
    """The following is a conversation between Alice and Bob about past travel experiences. Alice has been to Japan and Bob is considering flying there.
Alice: Hi!
Bob: Hey, how are you doing?
Alice: I'm doing well! I just got back from my vacation in Japan.
Bob: Wow that's awesome! What did you think of it?
Alice: Japan was such an amazing place to visit!
Bob: Wow! What was your favorite part?
Alice: I really enjoyed the food in Tokyo.
Bob: Which airline did you take?
Alice: I flew using Japan Airlines.""",
    """The following is a conversation between Alice and Bob about their hobbies. Alice enjoys tennis and Bob likes playing soccer.
Alice: What do you like to do for fun?
Bob: I used to play soccer in college, so I still like to play for fun on the weekends!
Alice: That's great. Soccer is a great way to stay in good shape.
Bob: I agree - it's really good cardio. What about you?
Alice: I love to play tennis. I've been taking lessons for a few months now!
Bob: Tennis is fun too!""",
    """The following is a conversation between Alice and Bob about their favorite movies. Bob loved the new Batman movie. Alice really liked watching Pride and Prejudice.
Alice: I just saw Pride and Prejudice for the fifth time!
Bob: That's a lot of times! What do you like so much about that movie?
Alice: Well, as a teenager I really liked the book. But I just really loved Keira Knightley's portrayal of Elizabeth.
Bob: I see. I haven't seen the movie myself. I prefer action films.
Alice: What's your favorite action movie?
Bob: Hm, I really liked the Batman movie that just came out.
Alice: I haven't seen it yet. I heard it got pretty good reviews.""",
    """The following is a conversation between Alice and Bob about their hometowns. Alice is from New York City. Bob grew up in Seattle.
Alice: Hello! How are you doing?
Bob: Hi, I'm doing great! What about yourself?
Alice: I'm doing well! Where are you from?
Bob: I'm originally from Seattle, but now I live in Palo Alto.
Alice: Oh cool! I live in Palo Alto too. Do you like Seattle or California more?
Bob: Well, Seattle is always going to be home for me. Even if the weather in California is nicer.
Alice: Haha, I get that! I miss New York City - there's no place like home.
Bob: What is your favorite neighborhood of New York City?
Alice: I love going to Chelsea. The Highline has a great view, and Little Island is close by too! Have you ever been?
Bob: Unfortunately I have not. I have never been to the East Coast!""",
    """The following is a conversation between Alice and Bob about art. Alice's favorite artist is Michelangelo. Bob does not know much about art.
Alice: Hi, how's it going?
Bob: It's going well, what about you?
Alice: I'm doing great! I've been really interested in art recently.
Bob: What got you interested in art?
Alice: Art can be so breathtaking!
Bob: I feel like I don't know how to properly appreciate art, but certain pieces of artwork certainly look very complex.
Alice: Have you ever heard of Michelangelo?
Bob: I have heard of him, but I don't know anything that he has created.
Alice: Michelangelo is really famous for his statue of David.
Bob: Huh? Who is David?
Alice: David is a Biblical figure who was a king of Israel. Michelangelo built a really magnificent statue of him in Florence.""",
    """The following is a conversation between Alice and Bob about drinks. Alice is a wine expert, whereas Bob prefers cocktails.
Alice: How are you doing?
Bob: Pretty great! I'm planning to go to a brewery this weekend.
Alice: Do you know much about alcohol?
Bob: Yeah, I really like beer! I drink a lot of IPAs.
Alice: Oh - what do you like about IPAs? I can't get over the bitter taste.
Bob: Well, I don't think it's just bitter. Sometimes there are really interesting citrusy or herbal flavor notes.
Alice: I see. That kind of reminds me of wine tasting.
Bob: There's definitely a lot of depth to it like there is with wine. Do you know much about wine?
Alice: Yeah, I took several classes on wine tasting back in the day. I really love Pinot Noir.
Bob: Oh I love red wines too.
Alice: Right? I love the dryness and fruity notes of Pinot Noir.""",
    """The following is a conversation between Alice and Bob about relationships. Bob recently got engaged.
Alice: Congrats on your engagement! When do you think you will have your wedding?
Bob: Thank you!! We're thinking of having it in November.
Alice: That's amazing! Will you pick a fancy destination?
Bob: I wanted to! I was thinking of having it somewhere in Europe, but my partner and I ultimately decided we wanted to have it close to home so our friends could all make it.
Alice: That's a good point. My husband and I had similar thoughts when we were planning our wedding.
Bob: What did you plan in the end?
Alice: We had a small ceremony in my hometown!""",
    """The following is a conversation between Alice and Bob about their jobs. Alice works in the financial industry and Bob is a musician.
Alice: I'm so burnt out from my work! I just want to quit already!
Bob: Whoa - what do you do for work? 
Alice: I'm an investment banker. It's been four years at this company and I'm absolutely exhausted.
Bob: That sounds intense. Is there anything you actually like about the job?
Alice: Well, the money is good.
Bob: It sounds like you could use a break. Maybe you could use some of that money to go travel.
Alice: I really want to go to South America, but I don't have a lot of time.""",
    """The following is a conversation between Alice and Bob about their pets. Alice has a dog and Bob prefers cats.
Alice: Do you have any pets?
Bob: No, but I really want to get a cat.
Alice: What, why a cat? Cats seem so boring. They never want to play.
Bob: Yeah, but cats are so cute! They also are a lot easier to take care of. They can clean themselves. What do you prefer?
Alice: Well, I have a dog. He is a corgi and his name is Bo.
Bob: Aww that's cute! I'm not usually a dog person, but corgis are adorable.
Alice: Haha, thank you! Bo is a really friendly dog.
Bob: How old is he?
Alice: Bo is one year old now.""",
    """The following is a conversation between Alice and Bob about grocery shopping. Alice has a shopping list for Bob.
Alice: Could you run to the grocery store and pick up some bananas for me?
Bob: Will do - how many do you need?
Alice: Oh, I don't know, maybe ten bananas. I'm planning to make banana bread, but I also want to save some for us to eat at home.
Bob: That sounds delicious! I'll head out in a second. Is there anything else you need?"""
]

triadic_conversation_pool = [
    """The following is a conversation between Alice and Bob and Claire about past travel experiences. Alice has been to Japan and Bob is considering flying there. Claire has been to Taiwan and Korea, but not Japan.
Alice: Hi!
Bob: Hey, how are you doing?
Alice: I'm doing well! I just got back from my vacation in Japan.
Bob: Wow that's awesome! What did you think of it?
Alice: Japan was such an amazing place to visit!
Claire: Wow, I've always wanted to visit Japan!
Bob: What was your favorite part?
Alice: I really enjoyed the food in Tokyo. I had the best sushi of my life!
Bob: Which airline did you take?
Alice: I flew using Japan Airlines.
Claire: How expensive are tickets these days?
""",
    """The following is a conversation between Alice and Bob about their hobbies. Alice enjoys tennis and Bob likes playing soccer. Claire plays football.
Alice: What do you like to do for fun?
Bob: I used to play soccer in college, so I still like to play for fun on the weekends!
Claire: Oh wow! Did you play varsity soccer?
Bob: Yeah, I was a four-year starter!
Alice: That's great. Soccer is a great way to stay in good shape.
Bob: I agree - it's really good cardio. What about you all?
Claire: I'm in a flag football league! We play every Saturday afternoon.
Alice: I love to play tennis. I've been taking lessons for a few months now!
Bob: Cool, football and tennis are fun too!""",
    """The following is a conversation between Alice and Bob and Claire about their favorite movies. Claire is looking for movie recommendations. Bob loved the new Batman movie. Alice really liked watching Pride and Prejudice.
Alice: I just saw Pride and Prejudice for the fifth time!
Claire: Would you recommend watching it? I've never seen it!
Bob: Yeah, five times is a lot of times! What do you like so much about that movie?
Alice: Well, as a teenager I really liked the book. But I just really loved Keira Knightley's portrayal of Elizabeth.
Bob: I see. I haven't seen the movie myself. I prefer action films.
Alice: What's your favorite action movie?
Bob: Hm, I really liked the Batman movie that just came out.
Alice: I haven't seen it yet. I heard it got pretty good reviews.""",
    """The following is a conversation between Alice and Bob and Claire about their hometowns. Alice is from New York City. Bob grew up in Seattle. Claire is from Boston and would like to visit New York City.
Alice: Hello! How are you doing?
Claire: I'm doing good!
Bob: Hi, I'm doing great! What about yourself?
Alice: I'm doing well! Where are you both from?
Claire: I'm from Boston! I'm just visiting the Bay Area.
Bob: I'm originally from Seattle, but now I live in Palo Alto.
Alice: Oh cool! I live here in Palo Alto. Do you like Seattle or California more?
Bob: Well, Seattle is always going to be home for me. Even if the weather in California is nicer.
Alice: Haha, I get that! I miss New York City - there's no place like home.
Claire: Oh you're from New York? I've always wanted to visit!
Bob: Me too! What is your favorite neighborhood of New York City?
Alice: I love going to Chelsea. The Highline has a great view, and Little Island is close by too! Have you ever been?
Bob: Unfortunately I have not. I have never been to the East Coast!""",
    """The following is a conversation between Alice and Bob and Claire about art. Alice's favorite artist is Michelangelo. Bob does not know much about art. Claire is a painter.
Alice: Hi, how's it going?
Bob: It's going well, what about you?
Alice: I'm doing great! I've been really interested in art recently.
Claire: Oh that's great to hear! I love art as well.
Bob: What got you interested in art?
Alice: Art can just be so breathtaking!
Bob: I feel like I don't know how to properly appreciate art, but certain pieces of artwork certainly look very complex.
Alice: Have you ever heard of Michelangelo?
Bob: I have heard of him, but I don't know anything that he has created.
Claire: Michelangelo has some truly magnificent paintings, such as The Creation of Adam.
Alice: Michelangelo is also really famous for his statue of David.
Bob: Huh? Who is David?
Alice: David is a Biblical figure who was a king of Israel. Michelangelo built a really magnificent statue of him in Florence.""",
    """The following is a conversation between Alice and Bob and Claire about drinks. Alice is a wine expert, whereas Bob prefers cocktails. Claire likes to drink beer.
Alice: How are you doing?
Bob: Pretty great! I'm planning to go to a brewery this weekend.
Alice: Do you know much about alcohol?
Bob: Yeah, I really like beer! I drink a lot of IPAs.
Claire: Oh, beers are my favorite type of drink! I can really appreciate the taste of a good IPA.
Alice: Oh - what do you like about IPAs? I can't get over the bitter taste.
Bob: Well, I don't think it's just bitter. Sometimes there are really interesting citrusy or herbal flavor notes.
Claire: Yeah, there's a whole science to the hops used in making IPAs!
Alice: I see. That kind of reminds me of wine tasting.
Claire: The science behind tasting is similar for sure.
Bob: I agree, there's definitely a lot of depth to it like there is with wine. Do you know much about wine?
Alice: Yeah, I took several classes on wine tasting back in the day. I really love Pinot Noir.
Bob: Oh I love red wines too.
Alice: Right? I love the dryness and fruity notes of Pinot Noir.""",
    """The following is a conversation between Alice and Bob and Claire about relationships. Bob recently got engaged.
Alice: Congrats on your engagement! 
Claire: Yes, congrats! When do you think you will have your wedding?
Bob: Thank you! We're thinking of having it in November.
Alice: That's amazing! Will you pick a fancy destination?
Bob: I wanted to! I was thinking of having it somewhere in Europe, but my partner and I ultimately decided we wanted to have it close to home so our friends could all make it.
Claire: Oh wow, that is very considerate of you.
Alice: Yeah, that's a good point. My husband and I had similar thoughts when we were planning our wedding.
Bob: What did you plan in the end?
Alice: We had a small ceremony in my hometown!
Claire: It turned out nicely! It was such a beautiful ceremony.""",
    """The following is a conversation between Alice and Bob and Claire about their jobs. Alice works in the financial industry and Bob is a musician. Claire is an architect.
Alice: I'm so burnt out from my work! I just want to quit already!
Bob: Whoa - what do you do for work? 
Alice: I'm an investment banker. It's been four years at this company and I'm absolutely exhausted.
Bob: That sounds intense. Is there anything you actually like about the job?
Alice: Well, the money is good.
Claire: That doesn't sound like a healthy relationship with your job!
Bob: It sounds like you could use a break. Maybe you could use some of that money to go travel.
Alice: I really want to go to South America, but I don't have a lot of time.
Claire: Don't you have vacation days? I think breaks are important.
Alice: Yes, but I really want to get promoted this year.""",
    """The following is a conversation between Alice and Bob and Claire about their pets. Alice has a dog and Bob prefers cats. Claire has a pet hamster.
Alice: Do you have any pets?
Claire: I have a pet hamster! He is so adorable. What about you two?
Bob: I don't, but I really want to get a cat.
Alice: What, why a cat? Cats seem so boring. They never want to play.
Bob: Yeah, but cats are so cute! They also are a lot easier to take care of. They can clean themselves. What do you prefer?
Alice: Well, I have a dog. He is a corgi and his name is Bo.
Claire: That's so adorable! How old is he?
Alice: He just turned one!
Bob: Aww that's cute! I'm not usually a dog person, but corgis are adorable.
Alice: Haha, thank you! Bo is a really friendly dog.""",
    """The following is a conversation between Alice and Bob and Claire about grocery shopping. Alice has a shopping list for Bob. Claire is helping Alice cook at home.
Alice: Could you run to the grocery store and pick up some bananas for me?
Bob: Will do - how many do you need?
Alice: Oh, I don't know, maybe ten bananas. We are planning to make banana bread, but I also want to save some for us to eat at home.
Bob: That sounds delicious! I'll head out in a second. Is there anything else you need?
Claire: Oh, could you also pick up some more eggs? I think we're running low here."""
]

dyda_topic_map = {
    1: "Ordinary Life",
    2: "School Life",
    3: "Culture & Education",
    4: "Attitude & Emotion",
    5: "Relationship",
    6: "Tourism",
    7: "Health",
    8: "Work",
    9: "Politics",
    10: "Finance"
}
