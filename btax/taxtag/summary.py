import transformers
import spacy

undisputed_best_model = transformers.MBartForConditionalGeneration.from_pretrained(
    "ml6team/mbart-large-cc25-cnn-dailymail-nl-finetune"
)
tokenizer = transformers.MBartTokenizer.from_pretrained("facebook/mbart-large-cc25")
summarization_pipeline = transformers.pipeline(
    task="summarization",
    model=undisputed_best_model,
    tokenizer=tokenizer,
)
summarization_pipeline.model.config.decoder_start_token_id = tokenizer.lang_code_to_id[
    "nl_XX"
]

#Creating the summary with pretrained model and saving to a csv file in case an error and appending to dataframe 
counter=0
def summarise(_nl_list:list):
    summary=[]
    for text in _nl_list:
        

        t= summarization_pipeline(
            text,
            do_sample=True,
            top_p=0.75,
            top_k=50,
            num_beams=4,
            min_length=50,
            early_stopping=True,
            truncation=True,
        )[0]["summary_text"]

        summary.append(t)

        counter=counter+1
        print(counter)
    return summary

