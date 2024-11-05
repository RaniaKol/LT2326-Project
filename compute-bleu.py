import sys
import sacrebleu

target_test = sys.argv[1]  
target_pred = sys.argv[2]  
refs = []

with open(target_test) as test:
    for line in test: 
        line = line.strip()
        refs.append(line)

print("Reference 1st sentence:", refs[0])

refs = [refs]  
preds = []

with open(target_pred) as pred:  
    for line in pred: 
        line = line.strip()
        preds.append(line)

print("MTed 1st sentence:", preds[0])

# Calculate and print the BLEU score
bleu = sacrebleu.corpus_bleu(preds, refs)
print("BLEU: ", bleu.score)
