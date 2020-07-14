# Deploying the model on Algorithmia

First, sign up for an Algorithmia account [here](https://algorithmia.com/signup). The free credit should be sufficient for our purpose.

Next, you need to upload files used during model initialization to the Algorithmia data store.
The two files you need are `vocabulary.json` for sentence tokenization and `pytorch_model.bin` that stores pre-trained model weights.
`vocabulary.json` is already in the repo here `torchMojiBot/algorithmia/model/vocabulary.json`. To download `pytorch_model.bin`, simply run `python3 scripts/download_weights.py` from the `torchMojiBot/algorithmia` directory (note that you need to install `wget` to execute the script). The weights will be downloaded to `torchMojiBot/algorithmia/model/pytorch_model.bin`.

Next, run `pip3 install algorithmia` to install the Algorithmia Python client and run `python3 data.py` to upload the model files to the Algorithmia's hosted data store. When prompted, enter your Algorithmia user name and API key. The API key can be found under the "API Keys" tab on the Algorithmia console. After entering the credential, you should see "Model files successfully uploaded!".

Then, on the Algorithmia console:
1. Click "Create New" and select "Algorithm". 
2. Name the algorithm "emojize". 
3. Under "Language" choose "Python3.x" and leave everything else as is. 
4. Click "Create New Algorithm".

You will be prompted with a code snippet that you can use to clone the repo. After cloning the repo,
1. Overwrite `requirements.txt` and `src/emojize.py` with the files in our `emojize/`. `emojize.py` is our prediction script that accepts a text string, runs the torchMoji model and outputs an emoji based on the sentiment of the text.
2. Replace the path placeholder in line 31-32 of `emojize.py` with your file upload paths. You can find them in the Algorithmia console by going to "Data Sources" -> "My Hosted Data" -> "emojize".
3. `git add` `requirements.txt` and `src/emojize.py`, `git commit`, and `git push` (this triggers a build process on the Algorithmia end, so it takes a while).

After pushing, 
1. Go to the "Builds" tab of the "emojize" algorithm on the console. 
2. Locate your most recent Git Hash and click "Publish".
3. (Optional) you can leave release notes, test the model with sample inputs, and select a version number for this model release.

Finally, after successfully deploying, you will get copy-paste code snippet from the console that you can use to invoke the model, like the following:
```
import Algorithmia

input = "this is great!"
client = Algorithmia.client('api key')
algo = client.algo('username/emojize/0.1.0')
algo.set_options(timeout=300) # optional
print(algo.pipe(input).result)
```
