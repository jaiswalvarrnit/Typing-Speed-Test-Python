from time import *
import random as rd

def mistakes(para, user):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] != user[i]:
                error += 1
        except:
            error += 1
    return error

def time_cal(time_start, time_end, user_input):
    time_delay = time_end - time_start
    time_round = round(time_delay, 2)
    speed = len(user_input)/ time_round
    return round(speed)


easy_test = ["A virtual assistant (typically abbreviated to VA) is generally self-employed and provides professional administrative, technical, or creative assistance to clients remotely from a home office.", "Closed captions were created for deaf or hard of hearing individuals to assist in comprehension. They can also be used as a tool by those learning to read, learning to speak a non-native language, or in an environment where the audio is difficult to hear or is intentionally muted.", "A teacher's professional duties may extend beyond formal teaching. Outside of the classroom teachers may accompany students on field trips, supervise study halls, help with the organization of school functions, and serve as supervisors for extracurricular activities. In some education systems, teachers may have responsibility for student discipline."]

inter_test = ["Words per minute (WPM) is a measure of typing speed, commonly used in recruitment. For the purposes of WPM measurement a word is standardized to five characters or keystrokes. Therefore, brown counts as one word, but accounted counts as two. The benefits of a standardized measurement of input speed are that it enables comparison across language and hardware boundaries. The speed of an Afrikaans-speaking operator in Cape Town can be compared with a French-speaking operator in Paris. (Wikipedia)","There are many idiosyncratic typing styles in between novice-style hunt and peck and touch typing. For example, many hunt and peck typists have the keyboard layout memorized and are able to type while focusing their gaze on the screen. Some use just two fingers, while others use 3-6 fingers. Some use their fingers very consistently, with the same finger being used to type the same character every time, while others vary the way they use their fingers.", "Proofreader applicants are tested primarily on their spelling, speed, and skill in finding errors in the sample text. Toward that end, they may be given a list of ten or twenty classically difficult words and a proofreading test, both tightly timed. The proofreading test will often have a maximum number of errors per quantity of text and a minimum amount of time to find them. The goal of this approach is to identify those with the best skill set."]

hard_test = ["Income before securities transactions was up 10.8 percent from $13.49 million in 1982 to $14.95 million in 1983. Earnings per share (adjusted for a 10.5 percent stock dividend distributed on August 26) advanced 10 percent to $2.39 in 1983 from $2.17 in 1982. Earnings may rise for 7 years. Hopefully, earnings per share will grow another 10 percent. Kosy, Klemin, and Bille began selling on May 23, 1964. Their second store was founded in Renton on August 3, 1965. From 1964 to 1984, they opened more than 50 stores through-out the country. As they expanded, 12 regional offices had to be organized. Each of these 12 regional offices had to be organized. Each of these 12 regions employs from 108 to 578 people. National headquarters employs 1,077 people. Carole owns 118 stores located in 75 cities ranging as far west as Seattle and as far east as Boston. She owns 46 stores south of the Mason-Dixon line and 24 stores north of Denver. Carole buys goods from 89 companies located in 123 countries and all 50 states. Carole started in business on March 3, 1975. She had less than $6,000 in capital assets.","Two members of the 1984 class of Jefferson High School are chairing a group of 18 to look for a resort for the 20-year class reunion. A lovely place 78 miles from the city turns out to be the best. It has 254 rooms and a banquet hall to seat 378. It has been open 365 days per year since opening on May 30, 1926. They will need 450 to reserve the resort. Debbie Holmes was put in charge of buying 2,847 office machines for the entire firm. Debbie visited more than 109 companies in 35 states in 6 months. She will report to the board today in Room 2784 at 5 p.m. The board will consider her report about those 109 firms and recommend the top 2 or 3 brands to purchase. Debbie must decide before August 16. Lynn Greene said work started on the project March 27, 2003. The 246 blueprints were mailed to the office 18 days ago. The prints had to be 100 percent accurate before they were acceptable. The project should be finished by May 31, 2025. At that time there will be 47 new condominiums, each having at least 16 rooms. The building will be 25 stories.","Word processors evolved dramatically once they became software programs rather than dedicated machines. They can usefully be distinguished from text editors, the category of software they evolved from. Word processing added to the text editor the ability to control type style and size, to manage lines (word wrap), to format documents into pages, and to number pages. Functions now taken for granted were added incrementally, sometimes by purchase of independent providers of add-on programs. Spell checking, grammar checking and mail merge were some of the most popular add-ons for early word processors. Word processors are also capable of hyphenation, and the management and correct positioning of footnotes and endnotes. Later desktop publishing programs were specifically designed with elaborate pre-formatted layouts for publication, offering only limited options for changing the layout, while allowing users to import text that was written using a text editor or word processor, or type the text in themselves."]

diff_input = int(input("Choose '1' for easy level, '2' for intermediate level and press '3' for hard level :=> "))

if diff_input == 1:
    testing = rd.choice(easy_test)
elif diff_input == 2:
    testing = rd.choice(inter_test)
elif diff_input == 3:
    testing = rd.choice(hard_test)

print()
print("************ TYPING SPEED TEST ************* \n")
print(testing)
print()
print()

time_1 = time()

user_input = input("Start Entering :=> ")

time_2 = time()

print("Speed is ", time_cal(time_1, time_2, testing), "words/ seconds")
print("Number of errors are ", mistakes(testing, user_input))



