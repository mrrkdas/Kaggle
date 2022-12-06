def finalize_data(train_data, test_data):

  # Replacing columns
  train_data["ssf_num"] = train_data["secondary__structure_fraction"].map(lambda x: ssf_change(x)) 
  test_data["ssf_num"] = train_data["secondary__structure_fraction"].map(lambda x: ssf_change(x))

  train_data.drop("secondary__structure_fraction", axis = 1, inplace = True)
  test_data.drop("secondary__structure_fraction", axis = 1, inplace = True)
  train_data.drop(["seq_id", "protein_sequence"], axis = 1, inplace = True)
  test_data.drop(["seq_id", "protein_sequence"], axis = 1, inplace = True)


  return train_data, test_data


def score(preds, y_test):
  from scipy.stats import spearmanr

  score = spearmanr(preds, y_test)

  print(score)

def make_submmission(preds, name):
  submission = pd.read_csv("/content/sample_submission.csv")
  submission["tm"] = preds.round()

  submission.to_csv(name, index = False)

def ssf_change(random_sff_):
  random_ssf = random_sff_
  random_ssf = random_ssf.replace("(", "")
  random_ssf = random_ssf.replace(")", "")
  random_ssf = random_ssf.strip()
  random_ssf_array = np.array(random_ssf.split(","))
  random_ssf_array = random_ssf_array.astype(np.float64)

  return mean(random_ssf_array)