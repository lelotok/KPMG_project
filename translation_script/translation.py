import pandas as pd
from deep_translator import GoogleTranslator
import config_translation as config

#Opening file
df = pd.read_csv(config.PATH_TO_CSV)

#Looping through every rows of scaped texts
for index, rows in df.iterrows():
    # Transform array to string or the translation will give an error
    text = "".join(df[config.COL_TO_BE_TRANSL][index])
    to_translate = text

    transl = []

   
        # To prevent the max characters limitations error to stop the script to finish looping throught the entire file
    if len(text) > 5000:
        to_translate = text[:4999]
        translated = GoogleTranslator(source='auto', target=config.TARGET_LANG).translate(to_translate)
        transl.append(translated)
    
    else:
        translated = GoogleTranslator(source='auto', target=config.TARGET_LANG).translate(to_translate)
        transl.append(translated)

    # Saving each translations in .txt file
    outpout = open('translations/translation_index_{}.txt'.format(index), 'w')
    outpout.write(translated)
    outpout.close()


# Create a new column with the translated text in the dataframe
transl_val = pd.Series(transl)
df[config.TRANL_COL] = transl_val

# Save new dataframe in new .csv file
df.to_csv(config.PATH_TO_NEW_CSV)