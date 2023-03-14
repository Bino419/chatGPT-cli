# chatGPT-cli

I just wanted a easy way to use chatGPT, so I created this little CLI  
After cloning this repository, you'll need to install the Python3 requirements  

## Setup

```console
foo@bar:~$ pip3 install -r "requirements.txt"
```

Next, just export OPENAI_API_KEY with your API key, in ~/.bashrc or ~/.bash_profile by adding the following  

```bash
export OPENAI_API_KEY="YOUR_KEY_HERE"
```

## Usage

Execute the cli by running the following  

```console
foo@bar:~$ ./chat.py
```

Example of asking chatGPT a question
```console
foo@bar:~$ ./chat.py
chatGPT(input)> hello ChatGPT, are you recieving this?
chatGPT(response)>
        Yes, I am recieving this.
```
You can adjust the amount of results to return by passing this as a count to chatGPT (note [] are required)

```console
chatGPT(input)> hello ChatGPT, are you recieving this? [5]
chatGPT(response)>
        Yes, I am receiving this.
        Yes, I am receiving this.
        Yes, I am receiving this.
        Yes, I am recieving this.
        Yes, I am.
chatGPT(input)>
```

All commands are stored in **.history** for your convience, just like bash you can press up and down to go through your command history

## Exiting the CLI
You can simply type ***exit*** or use ***CTRL +C***

### Caveats

Don't send chatGPT just the word "test" via the API, you'll get a bunch of randomness spit back at you.
