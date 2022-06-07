import pandas as pd
from deep_translator import GoogleTranslator

#Opening file
df = pd.read_csv('data/data_03.csv',sep="|",encoding='utf-8')

#Looping through every rows of scaped texts
for index, rows in df.iterrows():
    # Transform array to string or the translation will give an error
    text = "".join(df['fr_body'][index])
    to_translate = text

    transl = []

    #try:
        # To prevent the max characters limitations error to stop the script to finish looping throught the entire file
    if len(text) > 5000:
        to_translate = text[:4999]
        translated = GoogleTranslator(source='auto', target='english').translate(to_translate)
        transl.append(translated)
    
    else:
        translated = GoogleTranslator(source='auto', target='english').translate(to_translate)
        transl.append(translated)

    # Saving each translations in .txt file
    outpout = open('translations/translation_index_{}.txt'.format(index), 'w')
    outpout.write(translated)
    outpout.close()

    # except:
    #     pass

# Create a new column with the translated text in the dataframe
transl_val = pd.Series(transl)
df['transl_engl'] = transl_val

# Save new dataframe in new .csv file
df.to_csv('data/data_translated_02.csv', index=False)