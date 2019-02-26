# loyalty_score
kaggle loyalty score predictor

This is a loyalty score predictor for the ELO merchants competition on kaggle. 

Part one: parse the data
The dataset comes in four main files. From those files, the label for which we are to predict a score is the card_id, and the score we are supposed to be predicting is the loyalty score. because of the size of the files, they are imported into a database, and then SQL was used to extract the necessary features.
