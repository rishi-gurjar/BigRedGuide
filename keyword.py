import os
import requests
import json
<<<<<<< Updated upstream
# from dotenv import load_dotenv
=======
>>>>>>> Stashed changes

from request import course_request, getcourse_simple, get_all_courses

# load_dotenv()

# apikey = os.getenv('apikey')
# apiend = os.getenv('apiend')
apikey = "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"
apiend = "https://api.openai.com/v1/chat/completions"
#getcourse_simple(course_request("CS", [1000]))
#getcourse_simple(course_request("MATH", [1000]))
#getcourse_simple(course_request("PLHRT", [1000]))

<<<<<<< Updated upstream
def generate_chat_completion(messages, apikey, apiend, model="gpt-4", temperature=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + apikey,
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(apiend, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception("Error " + response.status_code + " : " + response.text)
 
def user_prompting():
    system_prompt = "The user will input a string of words that include their academic, intellectual, and personal interests. I need you to separate these interests in a list, and refer to the json below. ONLY Use the value from the json, never ever output a value that is not found in the json, but if the input is a specific topic like plant phylogenetics, use the broader field, like evolutionary biology. For example, if the user says 'computer science and moral philosophy', turn it into: {'CS': 'Computer Science', 'PHIL': 'Philosophy',}. Just output the JSON in THIS EXACT FORMAT, NOTHING ELSE [{'value': 'AAP', 'descr': 'Architecture, Art, and Plannin', 'descrformal': 'Architecture, Art, and Planning'}, {'value': 'AAS', 'descr': 'Asian American Studies', 'descrformal': 'Asian American Studies'}, {'value': 'AEM', 'descr': 'Applied Economics & Management', 'descrformal': 'Applied Economics & Management'}, {'value': 'AEP', 'descr': 'Applied & Engineering Physics', 'descrformal': 'Applied & Engineering Physics'}, {'value': 'AIIS', 'descr': 'American Indian & Indigenous', 'descrformal': 'American Indian and Indigenous Studies'}, {'value': 'AIRS', 'descr': 'Air Force Science', 'descrformal': 'Aerospace Studies'}, {'value': 'ALS', 'descr': 'Agriculture & Life Sciences', 'descrformal': 'Agriculture & Life Sciences'}, {'value': 'AMST', 'descr': 'American Studies', 'descrformal': 'American Studies'}, {'value': 'ANSC', 'descr': 'Animal Science', 'descrformal': 'Animal Science'}, {'value': 'ANTHR', 'descr': 'Anthropology', 'descrformal': 'Anthropology'}, {'value': 'ARAB', 'descr': 'Arabic', 'descrformal': 'Arabic'}, {'value': 'ARCH', 'descr': 'Architecture', 'descrformal': 'Architecture'}, {'value': 'ARKEO', 'descr': 'Archaeology', 'descrformal': 'Archaeology'}, {'value': 'ART', 'descr': 'Art', 'descrformal': 'Art'}, {'value': 'ARTH', 'descr': 'Art History', 'descrformal': 'History of Art'}, {'value': 'AS', 'descr': 'Arts & Sciences', 'descrformal': 'Arts & Sciences'}, {'value': 'ASIAN', 'descr': 'Asian Studies', 'descrformal': 'Asian Studies'}, {'value': 'ASL', 'descr': 'American Sign Language', 'descrformal': 'American Sign Language'}, {'value': 'ASRC', 'descr': 'Africana Studies & Res Center', 'descrformal': 'Africana Studies & Research Center'}, {'value': 'ASTRO', 'descr': 'Astronomy', 'descrformal': 'Astronomy'}, {'value': 'BCS', 'descr': 'Bosnian, Croatian, Serbian', 'descrformal': 'Bosnian, Croatian, Serbian'}, {'value': 'BEE', 'descr': 'Biological & Environmental Eng', 'descrformal': 'Biological & Environmental Engineering'}, {'value': 'BENGL', 'descr': 'Bengali', 'descrformal': 'Bengali'}, {'value': 'BIOAP', 'descr': 'Animal Physiology & Anatomy', 'descrformal': 'Animal Physiology & Anatomy'}, {'value': 'BIOCB', 'descr': 'Computational Biology', 'descrformal': 'Computational Biology'}, {'value': 'BIOEE', 'descr': 'Ecology & Evolutionary Biology', 'descrformal': 'Ecology & Evolutionary Biology'}, {'value': 'BIOG', 'descr': 'Biology: General Courses', 'descrformal': 'Biology: General Courses'}, {'value': 'BIOMG', 'descr': 'Molecular Biology and Genetics', 'descrformal': 'Molecular Biology and Genetics'}, {'value': 'BIOMI', 'descr': 'Microbiology', 'descrformal': 'Microbiology'}, {'value': 'BIOMS', 'descr': 'Bio Medical Science', 'descrformal': 'Biomedical Sciences'}, {'value': 'BIONB', 'descr': 'Neurobiology & Behavior', 'descrformal': 'Neurobiology & Behavior'}, {'value': 'BME', 'descr': 'Biomedical Engineering', 'descrformal': 'Biomedical Engineering'}, {'value': 'BSOC', 'descr': 'Biology & Society', 'descrformal': 'Biology & Society'}, {'value': 'BTRY', 'descr': 'Biometry & Statistics', 'descrformal': 'Biometry & Statistics'}, {'value': 'BURM', 'descr': 'Burmese', 'descrformal': 'Burmese'}, {'value': 'CAPS', 'descr': 'China & Asia Pacific Studies', 'descrformal': 'China & Asia Pacific Studies'}, {'value': 'CEE', 'descr': 'Civil & Environmental Engr', 'descrformal': 'Civil & Environmental Engineering'}, {'value': 'CHEM', 'descr': 'Chemistry', 'descrformal': 'Chemistry'}, {'value': 'CHEME', 'descr': 'Chemical Engineering', 'descrformal': 'Chemical Engineering'}, {'value': 'CHIN', 'descr': 'Chinese', 'descrformal': 'Chinese'}, {'value': 'CHLIT', 'descr': 'Chinese Literature', 'descrformal': 'Chinese Literature'}, {'value': 'CLASS', 'descr': 'Classics', 'descrformal': 'Classics'}, {'value': 'COGST', 'descr': 'Cognitive Science', 'descrformal': 'Cognitive Science'}, {'value': 'COLLS', 'descr': 'College Scholar Program', 'descrformal': 'College Scholar Program'}, {'value': 'COML', 'descr': 'Comparative Literature', 'descrformal': 'Comparative Literature'}, {'value': 'COMM', 'descr': 'Communication', 'descrformal': 'Communication'}, {'value': 'CRP', 'descr': 'City & Regional Planning', 'descrformal': 'City & Regional Planning'}, {'value': 'CS', 'descr': 'Computer Science', 'descrformal': 'Computer Science'}, {'value': 'CZECH', 'descr': 'Czech', 'descrformal': 'Czech'}, {'value': 'DEA', 'descr': 'Design & Environmental Analy', 'descrformal': 'Design & Environmental Analysis'}, {'value': 'DESIGN', 'descr': 'Design Tech', 'descrformal': 'Design Tech'}, {'value': 'DUTCH', 'descr': 'Dutch', 'descrformal': 'Dutch'}, {'value': 'EAS', 'descr': 'Earth & Atmospheric Sciences', 'descrformal': 'Earth & Atmospheric Sciences'}, {'value': 'ECE', 'descr': 'Electrical & Computer Engr', 'descrformal': 'Electrical & Computer Engineering'}, {'value': 'ECON', 'descr': 'Economics', 'descrformal': 'Economics'}, {'value': 'EDUC', 'descr': 'Education', 'descrformal': 'Education'}, {'value': 'ELSO', 'descr': 'English Language Support', 'descrformal': 'English Language Support'}, {'value': 'ENGL', 'descr': 'English', 'descrformal': 'English'}, {'value': 'ENGRC', 'descr': 'Engineering Communications', 'descrformal': 'Engineering Communications'}, {'value': 'ENGRD', 'descr': 'Engineering Distribution', 'descrformal': 'Engineering Distribution'}, {'value': 'ENGRG', 'descr': 'Engineering General Interest', 'descrformal': 'Engineering General Interest'}, {'value': 'ENGRI', 'descr': 'Engineering Introduction', 'descrformal': 'Engineering Introduction'}, {'value': 'ENMGT', 'descr': 'Engineering Management', 'descrformal': 'Engineering Management'}, {'value': 'ENTOM', 'descr': 'Entomology', 'descrformal': 'Entomology'}, {'value': 'ENVS', 'descr': 'Environment & Sustainability', 'descrformal': 'Environment & Sustainability'}, {'value': 'FDSC', 'descr': 'Food Science', 'descrformal': 'Food Science'}, {'value': 'FGSS', 'descr': 'Feminist,Gender,Sexuality Stdy', 'descrformal': 'Feminist, Gender & Sexuality Studies'}, {'value': 'FINN', 'descr': 'Finnish', 'descrformal': 'Finnish'}, {'value': 'FREN', 'descr': 'French', 'descrformal': 'French'}, {'value': 'FSAD', 'descr': 'Fiber Science & Apparel Design', 'descrformal': 'Fiber Science & Apparel Design'}, {'value': 'GDEV', 'descr': 'Global Development', 'descrformal': 'Global Development'}, {'value': 'GERST', 'descr': 'German Studies', 'descrformal': 'German Studies'}, {'value': 'GOVT', 'descr': 'Government', 'descrformal': 'Government'}, {'value': 'GRAD', 'descr': 'Graduate Research', 'descrformal': 'Graduate Research'}, {'value': 'GREEK', 'descr': 'Greek', 'descrformal': 'Greek'}, {'value': 'HADM', 'descr': 'Hotel Administration', 'descrformal': 'Hotel Administration'}, {'value': 'HD', 'descr': 'Human Development', 'descrformal': 'Human Development'}, {'value': 'HE', 'descr': 'Human Ecology Nondepartmental', 'descrformal': 'Human Ecology Nondepartmental'}, {'value': 'HEBRW', 'descr': 'Hebrew', 'descrformal': 'Hebrew'}, {'value': 'HIERO', 'descr': 'Hieroglyphic Egyptian', 'descrformal': 'Hieroglyphic Egyptian'}, {'value': 'HINDI', 'descr': 'Hindi', 'descrformal': 'Hindi'}, {'value': 'HIST', 'descr': 'History', 'descrformal': 'History'}, {'value': 'HUNGR', 'descr': 'Hungarian', 'descrformal': 'Hungarian'}, {'value': 'ILRHR', 'descr': 'ILR Human Resource Studies', 'descrformal': 'Human Resource Studies'}, {'value': 'ILRIC', 'descr': 'ILR International & Comp Labor', 'descrformal': 'International & Comparative Labor'}, {'value': 'ILRID', 'descr': 'ILR Interdepartmental', 'descrformal': 'Industrial and Labor Relations Interdepartmental'}, {'value': 'ILRLE', 'descr': 'ILR Labor Economics', 'descrformal': 'Labor Economics'}, {'value': 'ILRLR', 'descr': 'ILR Labor Relations, Law, Hist', 'descrformal': 'Labor Relations, Law and History'}, {'value': 'ILROB', 'descr': 'ILR Organizational Behavior', 'descrformal': 'Organizational Behavior'}, {'value': 'ILRST', 'descr': 'ILR Social Statistics', 'descrformal': 'Social Statistics'}, {'value': 'IM', 'descr': 'Independent Major', 'descrformal': 'Independent Major'}, {'value': 'INDO', 'descr': 'Indonesian', 'descrformal': 'Indonesian'}, {'value': 'INFO', 'descr': 'Information Science', 'descrformal': 'Information Science'}, {'value': 'ITAL', 'descr': 'Italian', 'descrformal': 'Italian'}, {'value': 'JAPAN', 'descr': 'Japanese', 'descrformal': 'Japanese'}, {'value': 'JPLIT', 'descr': 'Japanese Literature', 'descrformal': 'Japanese Literature'}, {'value': 'JUARA', 'descr': 'Judeo Arabic', 'descrformal': 'Judeo Arabic'}, {'value': 'JWST', 'descr': 'Jewish Studies', 'descrformal': 'Jewish Studies'}, {'value': 'KHMER', 'descr': 'Khmer', 'descrformal': 'Khmer'}, {'value': 'KOREA', 'descr': 'Korean', 'descrformal': 'Korean'}, {'value': 'LA', 'descr': 'Landscape Architecture', 'descrformal': 'Landscape Architecture'}, {'value': 'LATA', 'descr': 'Latin American Studies', 'descrformal': 'Latin American Studies'}, {'value': 'LATIN', 'descr': 'Latin', 'descrformal': 'Latin'}, {'value': 'LAW', 'descr': 'Law', 'descrformal': 'Law'}, {'value': 'LEAD', 'descr': 'Leadership', 'descrformal': 'Leadership'}, {'value': 'LEGAL', 'descr': 'Legal Studies', 'descrformal': 'Legal Studies'}, {'value': 'LGBT', 'descr': 'Lesbian,Gay,Bisexual,Trns Stdy', 'descrformal': 'Lesbian, Gay, Bisexual & Transgender Studies'}, {'value': 'LING', 'descr': 'Linguistics', 'descrformal': 'Linguistics'}, {'value': 'LSP', 'descr': 'Latino Studies Program', 'descrformal': 'Latino Studies Program'}, {'value': 'MAE', 'descr': 'Mechanical & Aerospace Eng', 'descrformal': 'Mechanical & Aerospace Engineering'}, {'value': 'MATH', 'descr': 'Mathematics', 'descrformal': 'Mathematics'}, {'value': 'MEDVL', 'descr': 'Medieval Studies', 'descrformal': 'Medieval Studies'}, {'value': 'MGMT', 'descr': 'Graduate Management', 'descrformal': 'Graduate Management'}, {'value': 'MILS', 'descr': 'Military Science', 'descrformal': 'Military Science'}, {'value': 'MSE', 'descr': 'Materials Science & Engr', 'descrformal': 'Materials Science & Engineering'}, {'value': 'MUSIC', 'descr': 'Music', 'descrformal': 'Music'}, {'value': 'NACCT', 'descr': 'Grad Mgmt Acct', 'descrformal': 'Graduate Management Accounting'}, {'value': 'NAVS', 'descr': 'Naval Science', 'descrformal': 'Naval Science'}, {'value': 'NBA', 'descr': 'Grad Mgmt Business Admin', 'descrformal': 'Graduate Management Business Admin'}, {'value': 'NBAB', 'descr': 'Executive Boardroom Electives', 'descrformal': 'Executive Boardroom Business Electives-JGSM'}, {'value': 'NBAY', 'descr': 'Grad Mgmt Business Admin NYT', 'descrformal': 'Graduate Management Business Admin NYT'}, {'value': 'NCC', 'descr': 'Grad Mgmt Common Core', 'descrformal': 'Graduate Management Common Core'}, {'value': 'NCCY', 'descr': 'Grad Mgmt Common Core NYT', 'descrformal': 'Graduate Management Common Core NYT'}, {'value': 'NEPAL', 'descr': 'Nepali', 'descrformal': 'Nepali'}, {'value': 'NES', 'descr': 'Near Eastern Studies', 'descrformal': 'Near Eastern Studies'}, {'value': 'NMI', 'descr': 'Grad Mgmt Individual Study', 'descrformal': 'Graduate Management Individualized Study'}, {'value': 'NRE', 'descr': 'Graduate Management Research', 'descrformal': 'Graduate Management Research'}, {'value': 'NS', 'descr': 'Nutritional Science', 'descrformal': 'Nutritional Science'}, {'value': 'NTRES', 'descr': 'Natural Resources', 'descrformal': 'Natural Resources'}, {'value': 'ORIE', 'descr': 'Op Research & Information Engr', 'descrformal': 'Operations Research & Information Engineering'}, {'value': 'OVST', 'descr': 'Overseas Study', 'descrformal': 'Overseas Study'}, {'value': 'PADM', 'descr': 'Public Administration', 'descrformal': 'Public Administration'}, {'value': 'PE', 'descr': 'Physical Education & Athletics', 'descrformal': 'Physical Education & Athletics'}, {'value': 'PERSN', 'descr': 'Persian', 'descrformal': 'Persian'}, {'value': 'PHIL', 'descr': 'Philosophy', 'descrformal': 'Philosophy'}, {'value': 'PHYS', 'descr': 'Physics', 'descrformal': 'Physics'}, {'value': 'PLBIO', 'descr': 'Plant Biology', 'descrformal': 'Plant Biology'}, {'value': 'PLBRG', 'descr': 'Plant Breeding', 'descrformal': 'Plant Breeding'}, {'value': 'PLHRT', 'descr': 'Horticulture Sciences', 'descrformal': 'Horticulture Sciences'}, {'value': 'PLPPM', 'descr': 'Plant Pathology', 'descrformal': 'Plant Pathology'}, {'value': 'PLSCI', 'descr': 'Plant Sciences', 'descrformal': 'Plant Sciences'}, {'value': 'PLSCS', 'descr': 'Soil & Crop Sciences', 'descrformal': 'Soil & Crop Sciences'}, {'value': 'PMA', 'descr': 'Performing and Media Arts', 'descrformal': 'Performing and Media Arts'}, {'value': 'POLSH', 'descr': 'Polish', 'descrformal': 'Polish'}, {'value': 'PORT', 'descr': 'Portuguese', 'descrformal': 'Portuguese'}, {'value': 'PSYCH', 'descr': 'Psychology', 'descrformal': 'Psychology'}, {'value': 'PUBPOL', 'descr': 'Public Policy', 'descrformal': 'Public Policy'}, {'value': 'PUNJB', 'descr': 'Punjabi', 'descrformal': 'Punjabi'}, {'value': 'REAL', 'descr': 'Real Estate', 'descrformal': 'Real Estate'}, {'value': 'RELST', 'descr': 'Religious Studies', 'descrformal': 'Religious Studies'}, {'value': 'ROMS', 'descr': 'Romance Studies', 'descrformal': 'Romance Studies'}, {'value': 'RUSSA', 'descr': 'Russian', 'descrformal': 'Russian'}, {'value': 'RUSSL', 'descr': 'Russian Literature', 'descrformal': 'Russian Literature'}, {'value': 'SANSK', 'descr': 'Sanskrit', 'descrformal': 'Sanskrit'}, {'value': 'SHUM', 'descr': 'Society for Humanities', 'descrformal': 'Society for the Humanities'}, {'value': 'SINHA', 'descr': 'Sinhalese', 'descrformal': 'Sinhala'}, {'value': 'SNLIT', 'descr': 'Sanskrit Literature', 'descrformal': 'Sanskrit Literature'}, {'value': 'SOC', 'descr': 'Sociology', 'descrformal': 'Sociology'}, {'value': 'SPAN', 'descr': 'Spanish', 'descrformal': 'Spanish'}, {'value': 'STS', 'descr': 'Science & Technology Studies', 'descrformal': 'Science & Technology Studies'}, {'value': 'STSCI', 'descr': 'Statistical Science', 'descrformal': 'Statistical Science'}, {'value': 'SWAHL', 'descr': 'Swahili', 'descrformal': 'Swahili'}, {'value': 'SWED', 'descr': 'Swedish', 'descrformal': 'Swedish'}, {'value': 'SYSEN', 'descr': 'Systems Engineering', 'descrformal': 'Systems Engineering'}, {'value': 'TAG', 'descr': 'Tagalog', 'descrformal': 'Tagalog'}, {'value': 'TAMIL', 'descr': 'Tamil', 'descrformal': 'Tamil'}, {'value': 'TECH', 'descr': 'Digital Technology & Practice', 'descrformal': 'Digital Technology & Practice'}, {'value': 'TECHIE', 'descr': 'Digital Tech Interdisciplinary', 'descrformal': 'Digital Technology Interdisciplinary Education'}, {'value': 'THAI', 'descr': 'Thai', 'descrformal': 'Thai'}, {'value': 'TIBET', 'descr': 'Tibetan', 'descrformal': 'Tibetan'}, {'value': 'TOX', 'descr': 'Toxicology', 'descrformal': 'Toxicology'}, {'value': 'TURK', 'descr': 'Turkish', 'descrformal': 'Turkish'}, {'value': 'UKRAN', 'descr': 'Ukrainian', 'descrformal': 'Ukrainian'}, {'value': 'UNILWYL', 'descr': 'Learning Where you Live', 'descrformal': 'Learning Where you Live'}, {'value': 'URDU', 'descr': 'Urdu', 'descrformal': 'Urdu'}, {'value': 'VETCS', 'descr': 'Vet Med Clinical Sciences', 'descrformal': 'Veterinary Medicine Clinical Sciences'}, {'value': 'VETMI', 'descr': 'Vet Med Microbiology', 'descrformal': 'Veterinary Medicine Microbiology'}, {'value': 'VIEN', 'descr': 'Viticulture and Enology', 'descrformal': 'Viticulture and Enology'}, {'value': 'VIET', 'descr': 'Vietnamese', 'descrformal': 'Vietnamese'}, {'value': 'VISST', 'descr': 'Visual Studies', 'descrformal': 'Visual Studies'}, {'value': 'VTBMS', 'descr': 'Vet Med BioMedical Sciences', 'descrformal': 'Veterinary Medicine BioMedical Sciences'}, {'value': 'VTMED', 'descr': 'Vet Med Prof Curriculum', 'descrformal': 'Veterinary Medicine Professional Curriculum'}, {'value': 'VTPEH', 'descr': 'Vet Med Public & Ecosys Health', 'descrformal': 'Veterinary Medicine Public and Ecosystem Health'}, {'value': 'VTPMD', 'descr': 'Population Med&Diagnostic Svc', 'descrformal': 'Vet Med Population Medicine & Diagnostic Services'}, {'value': 'WOLOF', 'descr': 'Wolof', 'descrformal': 'Wolof'}, {'value': 'WRIT', 'descr': 'Writing Program', 'descrformal': 'Writing Program'}, {'value': 'YIDSH', 'descr': 'Yiddish', 'descrformal': 'Yiddish'}, {'value': 'YORUB', 'descr': 'Yoruba', 'descrformal': 'Yoruba'}, {'value': 'ZULU', 'descr': 'Zulu', 'descrformal': 'Zulu'}]"

    prompt = input("I am interested in: ")
    #print("USER INPUT: ", prompt)
    #prompt = 'environmental science and cognitive science' #Test prompt

    messages = [ 
        {"role": "system", "content": system_prompt},  
        {"role": "user", "content": prompt}
            ]
    response_text = generate_chat_completion(messages, apikey, apiend)
    
    return response_text

def json_checker(s):

    """if s[2].isupper() != True:
        return 222
    #print("ESS", s)
    first = s.find('{')
    if first == -1:
        return 222
    last = s.rfind('}')
    s = s[first:last+1]

    for x in s:
        if x == "'":
            s = s.replace("'", '"')
    #s = "\'" + s + "\'"
    return s"""
    # Check if the string contains at least one uppercase letter
    if not any(char.isupper() for char in s):
        return None

    # Find the indices of the first '{' and the last '}'
    start_index = s.find('{')
    end_index = s.rfind('}')
    
    # If both '{' and '}' are found, extract the substring between them
    if start_index != -1 and end_index != -1:
        json_string = s[start_index:end_index+1]

        # Replace single quotes with double quotes to ensure valid JSON format
        json_string = json_string.replace("'", '"')

        return json_string
    else:
        return None


def looper():
    x = 0
    while x == 0:
        user_return = user_prompting()
        sliced = json_checker(user_return)

        if sliced == 222:
            print("Your input was invalid, please retry")
            pass
        else:
            #sliced = '{ "CS": "Computer Science", "PHYS": "Physics" }'
            #print("SLICED", sliced)
            json_user_return = json.loads(sliced) # converts str to json
            #print(json_user_return)
            #print('type', type(json_user_return))
            get_all_courses(json_user_return)
        y = input("Continue? (y/n)")
        if y == 'y':
            pass
        else:
            x = 1
looper()
=======
if response.status_code == 200:
    if "application/json" in response.headers.get("content-type"):
        try:
            data = response.json()
            # Process the JSON data
        except json.JSONDecodeError:
            print("Error: Response does not contain valid JSON.")
    else:
        non_json_content = response.text
        print("Error: Non-JSON content received.")
        print(non_json_content)
else:
    print(f"Failed to get data: {response.status_code}")

"""if response.status_code == 200:
    try:
        data = response.json()
        # Process the data
    except json.JSONDecodeError:
        print("Error: Response does not contain valid JSON.")
else:
    print(f"Failed to get data: {response.status_code}")"""
>>>>>>> Stashed changes
