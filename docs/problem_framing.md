# SmartLend Problem Framing

Complete this document during the Topic 1 lab. Write concise, specific answers grounded in the SmartLend brief and your EDA findings.

## Prediction Task

It's asked to predict the likelyhood of someone not being able to repay their loans from previous credit history. Binary classification? The target variable is "SeriousDlqin2yrs" which represents anyone who was 90+ days past due on any credit account within the next 2 years.

## Likely Users of the Prediction

Loan officers can review the decisions of the model, ensuring that the model is accurate and predicting correctly, the applicants will indirectly be a user as they will be rejected and have to find another loan if the model rejects them.

## Potential Failure Modes

The model can predict a no default, however the applicant defaults which would cause significant financial loss to SmartLend if this becomes a common trend with the model. If the model predicts a default and the applicant would not have defaulted, this impacts the user with being denied a loan, showing on their credit history and loss of income for SmartLend, especially if it becomes a trend with the model then this may have significant financial loss for losing good applicants. 

## Definition of Success

Thorough testing by giving the model real statistical data showing people with vulnerabilities, ranging from terrible, to amazing credit history, ensuring that the model can predict precisely at all levels of credit history. Ensuring that the model is fair to all, set a level of rejection where SmartLend will always pull a profit, but allow for some users with lower credit history a chance for a loan. Thorough testing is required to ensure the model is reliable and it's judgement can be accurate and trustworthy to run on its own, with loan officers regularly checking its outputs for accuracy.
