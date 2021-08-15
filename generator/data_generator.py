from random import randrange
import csv
import random
import base64

posts = []

posts.append({'title': "Have you seen me? Spikey the golden retriever.", 'body': """Our beloved dog Spikey has gone missing! He is a disability assistance dog and so is an important part of our household. Please help us find him! Large male dog wearing a red leather collar. Please report sightings to Adeline Palmerston. Call night or day at 123-456-7890 or email hello@reallygreatsite.com. Reward will be given if found.""", 'img': "post_images/post1.png"})

posts.append({'title': "Making Money in Real Estate Investing", 'body': """We are a COMMUNITY of Real Estate Investors and are looking for like-minded individuals!! Whether you have no experience, little experience or you're a seasoned investor, we want to connect with you! The real estate investing opportunity that we will share with you is truly changing lives. What's in it for you? Are you looking to live a different lifestyle, spend more time with family and friends, learn proven systems that provide structure for your business, or see proof that financial freedom can be achieved, then come to our REI Introductory meeting and see the opportunity. You will learn how you can effectively implement REI strategies such as Fix and Flips, Buy and Holds, Lease Options, among others when you acquire the right knowledge. You will also learn how you can pay off your mortgage, car loan, and/or student loans in a fraction of the time.""", 'img': "post_images/post2.png"})

posts.append({'title': "How To Land Your Dream Job in 8 Weeks or Less (Without Applying Online)", 'body': """During this FREE Training, You'll Discover: The step-by-step gameplan to landing your dream job within 8 weeks...without submitting blind applications. The “insider secrets” only executive recruiters like myself know when it comes to getting callbacks and landing offers (HINT: It’s not about your resume). The “smartcut” for instantly winning the attention and interest of any hiring manager or decision maker without having to deal with the gatekeeper (HR). How to have hiring managers call you directly for “invite-only” six-figure jobs (wipes out the “competition” as 99% of job-seekers will never know these exist).How to develop bulletproof confidence knowing you can walk into any interview and get the offer...every time.How to crush your self-doubt and finally land your next position...even if nothing has worked so far""", 'img': "post_images/post3.png"})

posts.append({'title': "Vibrant Vibrations", 'body': """This is a restorative sound healing experience led me and my good friend Freeman! Allow the pure intentional vibration of the Gong, singing bowls, and more to drop you into a deeply relaxed and rejuvenating state of being! The studio has all the props you need, but feel free to bring your own. A Yoga Mat, blankets, bolsters, or whatever else you may need to get supremely comfortable.""", 'img': "post_images/post4.png"})

posts.append({'title': "Outdoor nature camp assistants and teachers needed", 'body': """Do you love working with children and being in nature? Would you like to learn more about local plants and animals, tracking, foraging, and primitive skills? Vilda nature programs is hiring assistant instructors for our nature summer camps running mid-June through August. Work alongside talented naturalists to help kids explore, enjoy and learn about nature as well as gain outdoor skills.""", 'img': "post_images/post5.png"})

posts.append({'title': "Goodguys 24th Speedway Motors Southwest Nationals", 'body': """Fill up your gas tank, grab your keys, and cruise on out to America’s Favorite Car Show for the last event of 2021! Satisfy your hot rod dreams with over 3,000 1987 & older hot rods, customs, classics, trucks, and muscle cars for our season finale! Don’t miss your chance to check out the “Goodguys Top 12” Cars and Trucks of the Year presented by Meguiar’s, a huge Vendor Midway, and the Goodguys AutoCross timed racing competition; featuring the 32-car “Duel in the Desert” Finals Shootout presented by Speedway Motors, OPTIMA Batteries, American Racing Wheels. K&N and Lecarra, where the Goodguys 2021 FAST AutoCrosser of the Year will be crowned! Watch the Burnout Competition, Nitro Thunderfest Vintage Dragster Exhibition, shop the massive Swap Meet and Cars 4 Sale Corral, enjoy the FREE Kids Zone, Model Car Show, Live Entertainment— and so much more! On Sunday November 21st bring out your American made or powered muscle cars, customs, and trucks for our All American Sunday celebration featuring the All American AutoCross Shootout! Don’t leave before we kick off our final Awards Ceremony of 2021 and celebrate a variety of winners and their bold and beautiful rides.""", 'img': "post_images/post6.png"})

posts.append({'title': "Silent Book Club Oakland", 'body': """Silent Book Club started in 2012 with a couple of friends reading in companionable silence at our neighborhood bar in San Francisco. We loved books, and reading with friends, but most of our previous attempts at book clubs had fizzled out. Often with traditional book clubs there's the scramble to finish the assigned book, and the pressure to have something smart to say. Wouldn't it be great to have a book club where you could just enjoy books, friends, and wine—without any homework?We started Silent Book Club because reading with friends enriches our lives and makes us happy. We love hearing about what people are reading (often in their other book clubs) and we think it's important to put down our phones and be social. Real, live, breathing-the-same-air social, not hearting-you-on-Instagram social. Join us as we: Discuss what we each are reading; Read in silence for 60 minutes; Read aloud a random or chosen section of one or more of our books for 1 minute; Discuss a general theme from one or more of our books; Socialize""", 'img': "post_images/post7.png"})

posts.append({'title': "FSP Summer Soccer Camp 2021", 'body': """FSP is ecstatic to announce our third annual summer soccer camp series! This soccer camp will be four days of high intensity, player-focused training that will provide an amazing experience for the youth soccer community, particularly in the West Valley. Each session will incorporate a speed mechanics, agility, and explosiveness period. Following this, players will be further segmented in specific age groups to rotate through skill-focused technical stations. These stations will cover areas like ball mastery, first touch, finishing, and off-the-ball movement. Sessions will then conclude with small-sided games. It is going to be a great way to bring players from all across the valley to compete and showcase their skills.""", 'img': "post_images/post8.png"})

posts.append({'title': "Bees on A Mountain - please avoid going there", 'body': """Hikers: Please avoid A Mountain through tomorrow morning. There have been reports of aggressive bees and stings today. The City is assessing the situation tomorrow morning. Bees have been swarming in the Valley lately. Here are some tips on what to do if you encounter a swarm anywhere or get stung: https://www.tempe.gov/government/fire-medical-rescue/community-risk-reduction/life-safety/bites-and-stings""", 'img': "post_images/post9.png"})

posts.append({'title': "Entertainment Center for sale", 'body': """This entertainment center has a place for everything!  89 1/2” tall X 75” wide with 6 adjustable shelves, 2 drawers, 2 cabinets, 2 roll out shelves for media, lights above each section highlight your knick-knacks and a place for technology.  Can be repainted to match your decor!  NOTE:  TV , speaker and cable box are NOT included.""", 'img': "post_images/post10.png"})

posts.append({'title': "Help with computer", 'body': """My computer has run into a problem that I’ve not been able to figure out. For some reason the computer is unable to start and is showing this blue screen (screenshot attached) every time I restart it. What I’d like to do is take it to someone local, but I don’t know who to trust. Is there someone around who is good with computers and can drop by to look into and maybe fix this issue for me. Reward for anyone who can fix this.""", 'img': "post_images/post11.png"})

tags_to_fetch = ["Real Estate", "Finance", "Pets & Animals", "Hobbies & Leisure", "Jobs & Education", "Health", "People & Society", "Autos & Vehicles", "Sports", "Books & Literature", "Home & Garden", "Computers & Electronics"]


# Img Base64 cache
img64 = {}

def read_image(filepath):
    print(filepath)
    if filepath in img64:
        return img64[filepath]
    img = None
    with open(filepath, 'rb') as img_file:
        file_content = img_file.read()
        base64img = base64.b64encode(file_content)
        base64img_str = base64img.decode('utf-8')
        img = f'data:image/png;base64,{base64img_str}'
        img64[filepath] = img
    return img


def generate_post(single_threaded=False):
    lines = list()
    with open('dummy_lats_longs_all_generator.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            lines.append(row)

    coordinate_indx = randrange(len(lines))
    post_indx = randrange(len(posts))

    post = posts[post_indx].copy()

    post['title'] = "Post " + lines[coordinate_indx][2] + ": " + post['title']
    post['longitude'] = lines[coordinate_indx][1]
    post['latitude'] = lines[coordinate_indx][0]

    post['img'] = read_image(post['img'])

    lines.pop(coordinate_indx)

    if single_threaded:
        with open("dummy_lats_longs_all_generator.csv", "w") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    return post


# Generates parameters for getting posts
def fetch_post():
    num_tags = randrange(len(tags_to_fetch)) + 1
    rand_tags = random.sample(tags_to_fetch, num_tags)
    
    rand_radius = randrange(5) + 1

    lines = list()
    with open('dummy_lats_longs_5000km_20.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                lines.append(row)

    coordinate_indx = randrange(len(lines))

    latitude = lines[coordinate_indx][0]
    longitude = lines[coordinate_indx][1]

    return latitude, longitude, rand_radius, rand_tags
    

if __name__ == "__main__":
    pass
    # post = generate_post()
    # print(post)
    
    # latitude, longitude, rand_radius, rand_tags = fetch_post()
    # print(latitude, longitude, rand_radius, rand_tags)



