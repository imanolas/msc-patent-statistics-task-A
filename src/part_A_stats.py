# function to find duplicates in list
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import statistics
import re
import nltk
import glob
from collections import Counter
from bs4 import BeautifulSoup
import datetime

# function to find duplicates in list.
def has_duplicates(iterable):
    seen = []
    for x in iterable:
        if x in seen:
            return True
    return False

# initialize all the variables-counters for tags.
number_of_docs = 0
no_ipcs = 0
not_ipcs = 0
no_titles = 0
ipcs = 0
classes = 0
abstracts = 0
descriptions = 0

claims = 0
all_previous = 0

abs_and_claims = 0
desc_and_claims = 0
abs_and_desc = 0

words_abs = []
words_desc = []
words_claims = []

en_main = 0
de_main = 0
fr_main = 0

more_than_one_lang_abs = 0
more_than_one_lang_desc = 0
more_than_one_lang_claim = 0

non_eng_abs = 0
non_eng_desc = 0
non_eng_claim = 0

eng_abs = 0
eng_desc = 0
eng_claim = 0

number_section = 0
number_classes = 0
number_subclasses = 0
number_groups = 0
number_subgroups = 0

sections_count = []
classes_count = []
subclasses_count = []
groups_count = []
subgroups_count = []

all_counts = []
ipcs_counts = []
ipcs_array = []
test = []
number_of_patents = []

d_sections = []
d_classes = []
d_subclasses = []
num_pats = []

counter_has_section = 0
counter_has_class = 0
counter_has_subclass = 0
counter_has_group = 0
counter_has_subgroup = 0

# Path of the main folder of patent files.
dir = 'patents/'

# Read all the files from directories and subdirectories.
for subdir, dirs, files in os.walk(dir):
    for file in files:
        filepath =  os.path.join(subdir, file)
        # Read file by file with beautifulSoup.
        soup = BeautifulSoup(open(filepath, encoding="utf8"), 'html.parser')
        number_of_docs += 1
        print(number_of_docs)

        number_of_patents.append(file.split('-')[1])

        # Find the basic tags that we should use.
        ipcrs = soup.find_all('classification-ipcr')
        ipcs = soup.find_all('classification-ipc')
        main_lang = soup.find_all('patent-document')
        abstract = soup.find_all('abstract')
        title = soup.find_all('invention-title')
        description = soup.find_all('description')
        claim = soup.find_all('claims')

        # Start the procedure of computation of stats.
        if ipcrs or ipcs:
            counter_has_section += 1
            counter_has_class += 1
            counter_has_subclass += 1
            counter_has_group += 1
            counter_has_subgroup += 1
            ipcs_array = []
            sections = []
            classes = []
            subclasses = []
            groups = []
            subgroups = []

            for ipc in ipcs:
                if re.match("[A-Z]", ipc('main-classification')[0].text.strip()[0]):
                    ipcs_array.append(ipc('main-classification')[0].text.strip())
                    sections.append(ipc('main-classification')[0].text[:1].strip())
                    classes.append(ipc('main-classification')[0].text[:3].strip())
                    subclasses.append(ipc('main-classification')[0].text[:4].strip())
                    if ipc('main-classification')[0].text.strip()[
                       ipc('main-classification')[0].text.strip().index("/") + 1:len(
                           ipc('main-classification')[0].text.strip())] != "00":
                        groups.append(ipc('main-classification')[0].text.strip()[
                                      0:ipc('main-classification')[0].text.strip().index("/")] + "/00")
                    else:
                        groups.append(ipc('main-classification')[0].text.strip())
                    if ipc('main-classification')[0].text.strip()[
                       ipc('main-classification')[0].text.strip().index("/") + 1:len(
                           ipc('main-classification')[0].text.strip())] != "00":
                        subgroups.append(ipc('main-classification')[0].text.strip())
                    if ipc.find('further-classification'):
                        for ipc_f in ipc('further-classification'):
                            if re.match("[A-Z]", ipc_f.text.strip()[0]):
                                ipcs_array.append(ipc_f.text.strip())
                                sections.append(ipc_f.text[:1].strip())
                                classes.append(ipc_f.text[:3].strip())
                                subclasses.append(ipc_f.text[:4].strip())
                                if ipc('further-classification')[0].text.strip()[
                                   ipc('further-classification')[0].text.strip().index("/") + 1:len(
                                       ipc('further-classification')[0].text.strip())] != "00":
                                    groups.append(ipc('further-classification')[0].text.strip()[
                                                  0:ipc('further-classification')[0].text.strip().index("/")] + "/00")
                                else:
                                    groups.append(ipc('further-classification')[0].text.strip())

                                if ipc('further-classification')[0].text.strip()[
                                   ipc('further-classification')[0].text.strip().index("/") + 1:len(
                                       ipc('further-classification')[0].text.strip())] != "00":
                                    subgroups.append(ipc('further-classification')[0].text.strip())
            for ipcr in ipcrs:
                if re.match("[A-Z]", ipcr.text.strip()[0]):
                    ipcs_array.append(ipcr.text[:13].strip())
                    sections.append(ipcr.text[:1].strip())
                    classes.append(ipcr.text[:3].strip())
                    subclasses.append(ipcr.text[:4].strip())
                    if "/" in ipcr.text[:13]:
                        if ipcr.text[:13].strip()[
                           ipcr.text[:13].strip().index("/") + 1:len(ipcr.text[:13].strip())] != "00":
                            groups.append(ipcr.text[:13].strip()[0:ipcr.text[:13].strip().index("/")] + "/00")
                        else:
                            groups.append(ipcr.text[:13].strip())
                        if ipcr.text[:13].strip()[
                           ipcr.text[:13].strip().index("/") + 1:len(ipcr.text[:13].strip())] != "00":
                            subgroups.append(ipcr.text[:13].strip())
            d_sections += sections
            d_classes += classes
            d_subclasses += subclasses
            ipcs_counts.append(len(set(ipcs_array)))
            sections_count.append(len(set(sections)))
            classes_count.append(len(set(classes)))
            subclasses_count.append(len(set(subclasses)))
            groups_count.append(len(set(groups)))
            subgroups_count.append(len(set(subgroups)))
        else:
            not_ipcs += 1

            # print(ipc.find_next().find_next().text)

        if not title:
            no_titles += 1
        if abstract:
            abstracts += 1
        if description:
            descriptions += 1
        if claim:
            claims += 1
        if claim and abstract and description:
            all_previous += 1
        if claim and abstract:
            abs_and_claims += 1
        if claim and description:
            desc_and_claims += 1
        if abstract and description:
            abs_and_desc += 1

        language_ab = []
        if len(abstract) > 1:
            for abst in abstract:
                language_ab.append(abst["lang"])
            if not has_duplicates(language_ab):
                more_than_one_lang_abs += 1

        language_de = []
        if len(description) > 1:
            for desc in description:
                if not has_duplicates(language_de):
                    more_than_one_lang_desc += 1

        language_cl = []
        if len(claim) > 1:
            for claim_n in claim:
                language_cl.append(claim_n["lang"])
                if not has_duplicates(language_cl):
                    more_than_one_lang_claim += 1

        if main_lang:
            for mainl in main_lang:
                if mainl["lang"] == "EN":
                    en_main += 1
                elif mainl["lang"] == "DE":
                    de_main += 1
                elif mainl["lang"] == "FR":
                    fr_main += 1

        if main_lang:
            for mainl in main_lang:
                if mainl["lang"] == "EN" and abstract:
                    for abst in abstract:
                        if abst["lang"] != "EN":
                            non_eng_abs += 1

        if main_lang:
            for mainl in main_lang:
                if mainl["lang"] == "EN" and description:
                    for desc in description:
                        if desc["lang"] != "EN":
                            non_eng_desc += 1

        if main_lang:
            for mainl in main_lang:
                if mainl["lang"] == "EN" and claim:
                    for claim_n in claim:
                        if claim_n["lang"] != "EN":
                            non_eng_claim += 1

        if main_lang:
            for mainl in main_lang:
                if mainl["lang"] != "EN" and abstract:
                    for abst in abstract:
                        if abst["lang"] == "EN":
                            eng_abs += 1

        if main_lang:
            for mainl in main_lang:
                if mainl["lang"] != "EN" and description:
                    for desc in description:
                        if desc["lang"] == "EN":
                            eng_desc += 1

        if main_lang:
            for mainl in main_lang:
                if mainl["lang"] != "EN" and claim:
                    for claim_n in claim:
                        if claim_n["lang"] == "EN":
                            eng_claim += 1

        if abstract:
            for abst in abstract:
                t = re.sub(r"[^a-zA-Z0-9]", " ", abst.text)
                words_abs.append(len(nltk.word_tokenize(t)))

        if description:
            for desc in description:
                t = re.sub(r"[^a-zA-Z0-9]", " ", desc.text)
                words_desc.append(len(nltk.word_tokenize(t)))

        if claim:
            for claims_n in claim:
                t = re.sub(r"[^a-zA-Z0-9]", " ", claims_n.text)
                words_claims.append(len(nltk.word_tokenize(t)))

# Print and write on file the final stats.
print("Number of all patent-documents: ", number_of_docs)
print("Number of all patents: ", len(list(set(number_of_patents))))
print("Average number of ipc codes per patents: ", statistics.mean(ipcs_counts))
print("Number of patents containing section: ", counter_has_section)
print("Distribution of all the different sections: ", dict(Counter(d_sections)))
print("Average number of sections per patents: ", statistics.mean(sections_count))
print("Number of patents containing classes: ", counter_has_class)
print("Distribution of all the different classes: ", dict(Counter(d_classes)))
print("Average number of classes per patents: ", statistics.mean(classes_count))
print("Number of patents containing subclasses: ", counter_has_subclass)
print("Distribution of all the different subclasses: ", dict(Counter(d_subclasses)))
print("Average number of subclasses per patents: ", statistics.mean(subclasses_count))
print("Number of patents containing groups: ", counter_has_group)
print("Average number of groups per patents: ", statistics.mean(groups_count))
print("Number of patents containing subgroups: ", counter_has_subgroup)
print("Average number of subgroups per patents: ", statistics.mean(subgroups_count))
print("Number of patents not containining Title:", no_titles)
print("Number of patents not containining ipc-codes:", not_ipcs)
print("Number of patents containining abstract:", abstracts)
print("Number of patents containining description:", descriptions)
print("Number of patents containining claims:", claims)
print("Number of patents containining all previous:", all_previous)
print("Number of patents containing abstract and claims:", abs_and_claims)
print("Number of patents containing description and claims:", desc_and_claims)
print("Number of patents containing abstract and description:", abs_and_desc)
print("Number of patents containing abstract in more than 1 language:", more_than_one_lang_abs)
print("Number of patents containing description in more than 1 language:", more_than_one_lang_desc)
print("Number of patents containing claims in more than 1 language:", more_than_one_lang_claim)
print("Number of patents where main language is English:", en_main)
print("Number of patents where main language is German:", de_main)
print("Number of patents where main language is French:", fr_main)
print("Number of English patents containing abstract in non-English:", non_eng_abs)
print("Number of English patents containing description in non-English:", non_eng_desc)
print("Number of English patents containing claims in non-English:", non_eng_claim)
print("Number of non-english patents containing abstract in English:", eng_abs)
print("Number of non-english patents containing description in English:", eng_desc)
print("Number of non-english patents containing claims in English:", eng_claim)
print("Min number of words in abstract:", min(words_abs))
print("Max number of words in abstract:", max(words_abs))
print("Average number of words in abstract:", statistics.mean(words_abs))
print("Min number of words in Description:", min(words_desc))
print("Max number of words in Description:", max(words_desc))
print("Average number of words in Description:", statistics.mean(words_desc))
print("Min number of words in Claims:", min(words_claims))
print("Max number of words in Claims:", max(words_claims))
print("Average number of words in Claims:", statistics.mean(words_claims))

# Write the final stats on .txt file.
with open('patents_stats.txt', 'w', encoding='utf-8') as writer:
    writer.write("******************----STATS----******************\n")
    writer.write("Created at "+str(datetime.datetime.now())+"\n")
    writer.write("-----------------------------------------------------------------------------------------------------------------\n")
    writer.write("******************----STATS of IPCRS codes(section, classes, subclasses, groups, subgroups)----******************\n")
    writer.write("-----------------------------------------------------------------------------------------------------------------\n")
    writer.write("Number of all patent-documents: "+str(number_of_docs)+"\n")
    writer.write("Number of all patents: "+str(len(list(set(number_of_patents))))+"\n")
    writer.write("Average number of ipc codes per patents: " +str(statistics.mean(ipcs_counts))+"\n")
    writer.write("Number of patents containing section: " +str(counter_has_section)+"\n")
    writer.write("Distribution of all the different sections: " + str(dict(Counter(d_sections)))+"\n")
    writer.write("Average number of sections per patents: " +str(statistics.mean(sections_count))+"\n")
    writer.write("Number of patents containing classes: " +str(counter_has_class)+"\n")
    writer.write("Distribution of all the different classes: " + str(dict(Counter(d_classes)))+"\n")
    writer.write("Average number of classes per patents: " +str(statistics.mean(classes_count))+"\n")
    writer.write("Number of patents containing subclasses: " +str(counter_has_subclass)+"\n")
    writer.write("Distribution of all the different subclasses: " + str(dict(Counter(d_subclasses)))+"\n")
    writer.write("Average number of subclasses per patents: " +str(statistics.mean(subclasses_count))+"\n")
    writer.write("Number of patents containing groups: " +str(counter_has_group)+"\n")
    writer.write("Average number of groups per patents: " +str(statistics.mean(groups_count))+"\n")
    writer.write("Number of patents containing subgroups: " +str(counter_has_subgroup)+"\n")
    writer.write("Average number of subgroups per patents: " +str(statistics.mean(subgroups_count))+"\n")
    writer.write("-----------------------------------------------------------------------------------------\n")
    writer.write("******************----STATS of title, abstract, claims, description----******************\n")
    writer.write("-----------------------------------------------------------------------------------------\n")
    writer.write("Number of patents not containining Title: " +str(no_titles)+"\n")
    writer.write("Number of patents not containining ipc-codes: " +str(not_ipcs)+"\n")
    writer.write("Number of patents containining abstract: " +str(abstracts)+"\n")
    writer.write("Number of patents containining description: " +str(descriptions)+"\n")
    writer.write("Number of patents containining claims: " +str(claims)+"\n")
    writer.write("Number of patents containining all previous: " +str(all_previous)+"\n")
    writer.write("Number of patents containing abstract and claims: " +str(abs_and_claims)+"\n")
    writer.write("Number of patents containing description and claims: " +str(desc_and_claims)+"\n")
    writer.write("Number of patents containing abstract and description: " +str(abs_and_desc)+"\n")
    writer.write("Number of patents containing abstract in more than 1 language: " +str(more_than_one_lang_abs)+"\n")
    writer.write("Number of patents containing description in more than 1 language: " +str(more_than_one_lang_desc)+"\n")
    writer.write("Number of patents containing claims in more than 1 language: " +str(more_than_one_lang_claim)+"\n")
    writer.write("Number of patents where main language is English: " +str(en_main)+"\n")
    writer.write("Number of patents where main language is German: " +str(de_main)+"\n")
    writer.write("Number of patents where main language is French: " +str(fr_main)+"\n")
    writer.write("Number of English patents containing abstract in non-English: " +str(non_eng_abs)+"\n")
    writer.write("Number of English patents containing description in non-English: " +str(non_eng_desc)+"\n")
    writer.write("Number of English patents containing claims in non-English: " +str(non_eng_claim)+"\n")
    writer.write("Number of non-english patents containing abstract in English: " +str(eng_abs)+"\n")
    writer.write("Number of non-english patents containing description in English: " +str(eng_desc)+"\n")
    writer.write("Number of non-english patents containing claims in English: " +str(eng_claim)+"\n")
    writer.write("-------------------------------------------------------------------------------------------\n")
    writer.write("******************----STATS of words in Abstract, Description, Claims----******************\n")
    writer.write("-------------------------------------------------------------------------------------------\n")
    writer.write("Min number of words in abstract: " +str(min(words_abs))+"\n")
    writer.write("Max number of words in abstract: " +str(max(words_abs))+"\n")
    writer.write("Average number of words in abstract: " +str(statistics.mean(words_abs))+"\n")
    writer.write("Min number of words in Description: " +str(min(words_desc))+"\n")
    writer.write("Max number of words in Description: " +str(max(words_desc))+"\n")
    writer.write("Average number of words in Description: " +str(statistics.mean(words_desc))+"\n")
    writer.write("Min number of words in Claims: " +str(min(words_claims))+"\n")
    writer.write("Max number of words in Claims: " +str(max(words_claims)))