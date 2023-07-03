import argparse

nick_before_leet = []

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--words", help="words to be used to generate nicks", dest="words", nargs='*')
    parser.add_argument("-o", "--output", help="file to write the output", dest="output")

    arguments = parser.parse_args().words
    output = parser.parse_args().output
    return [arguments, output]


def write_to_file(nicknames, output):
    with open(output, 'a') as file:
        file.write(nicknames.strip() + "\n")


def dot_underscore(words, output):

    global nick_before_leet
    generated_nicks = ""
    for i in range(len(words)):
        underscore = name_with_dot = justJoined = words[i]
        for j in range(len(words)):
            if i == j:
                continue
            else:
                underscore += f"_{words[j]}"
                name_with_dot += f".{words[j]}"
                justJoined += words[j]
                generated_nicks += f"""{name_with_dot}
_{name_with_dot}
{name_with_dot}_
_{name_with_dot}_
{underscore}
_{underscore}
{underscore}_
_{underscore}_
{justJoined}
"""
    write_to_file(generated_nicks, output)
    nick_before_leet += generated_nicks.split()


def first_letter(words, output):
    global nick_before_leet
    counter = 0
    index = 0

    while counter < len(words):
        if counter == index:
            counter += 1
            continue
        else:
            generated_nicks = f"""
{words[index][0:1]}{words[counter]}
{words[index][0:1]}.{words[counter]}
{words[index][0:1]}_{words[counter]}
{words[counter]}{words[index][0:1]}
{words[counter]}.{words[index][0:1]}
{words[counter]}_{words[index][0:1]}
            """
            
            write_to_file(generated_nicks, output)
            nick_before_leet += generated_nicks.split()
            if counter == (len(words) - 1) and index < len(words):
                counter = 0
                index += 1
            else:
                counter += 1

def leet_name(words, output):
    generated_nicks = ""
    for word in  words:
        if word.replace('e', '3') not in words:
            generated_nicks += (word.replace('e','3') + "\n") 
        if word.replace('o', '0') not in words:
            generated_nicks += (word.replace('o','0') + "\n")
        if word.replace('s', '5') not in words:
            generated_nicks += (word.replace('s','5') + "\n")
        if word.replace('a','4') not in words:
            generated_nicks += (word.replace('a','4') + "\n")
        if word.replace('a', 'v') not in words:
            generated_nicks += (word.replace('a','v') + "\n")
        if word.replace('a', 'x') not in words:
            generated_nicks += (word.replace('a','x') + "\n")
        if word.replace('o', 'x') not in words:
            generated_nicks += (word.replace('o','x') + "\n")
        if word.replace('o', 'v') not in words:
            generated_nicks += (word.replace('o','v') + "\n")

    write_to_file(generated_nicks, output)        


def main():
    global nick_before_leet
    words, output_file = get_arguments()
    first_letter(words, output_file)
    dot_underscore(words, output_file)
    leet_name(nick_before_leet, output_file)
    

main()