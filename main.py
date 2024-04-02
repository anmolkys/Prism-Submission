# We dint have much time (we wasted a lot in beginning tbh) so there is no use case docs and all. Ig this will be all.
# For the first round we went with a cooking assistant hence the name, but at that point of time we dint know what we were doing and made a half baked code
# with no hopes. But ig thats not what fate decided so we, being grateful, decided to put some effort for the next round. We are not super proud of our first
# attempt so we decided to scrape it off and start over completely. After a series of meetings and discussions (totally for this reason) we decided to make
# the miserable life of students a bit easier by integrating the power of transformers into a student's every day life. We are going to automate some 
# tiresome and useless tasks like doing random research assignments and mailing faculty for attendence etc etc... So this is the Student <whatever...>

# For this we went with Crew Ai. What is crew ai?? 
# Cutting-edge framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. Go to website if still reading.
# Basically we tell an agent who he is, give it some tasks and a set of tools it can access, run it and do nothing.
# This is an open source framework. For the llm we tried using Gemeni(cuz free) but later realised the framework is built on open ai and ollama. In our team
# only one person has a GPU so we made him download and train the model and use it for his part. For the others, we just threw money at the problem... got
# the open ai api key. 

# This project is divided into 5 subparts each with their own crew and set of tasks. We can integrate all into one and run but will be very expensive and 
# draining for our laptops. So for demonstration we split them up. If you wish to combine just create a crew with all agents and set procees to heirarichal 
# with a manager llm.

#                                                              Open Source
# We used gemeni for most part and gpt in some places where pydantic errors occured for testing. We wanted to convert everything into open source 
# but due to lack of time we only made one part (Tiny devien) open source by assigning it llama model trained locally. Others can also be made by 
# fine tuning the models for the specific task and assign it to the corresponding agent.
 
#                                                                Latency
# To imporve latency we can run tasks asyncronously as much as possible and assign seperate llms for agents but that will be expensive.

#                                                          Multilingual support
# For Multiligual support, we can detect the input language from voice to text converter and store it to a variable. This variable can be passed along
# to every agent to give output in the corresponding language.
# Or if thats too much work

# Anyways lets begin with the code ....

# For input, we can receive the voice and use wispher model to convert to text and pass along this text as query. The model is taken from replicate.

import replicate

output = replicate.run(
    "openai/whisper:4d50797290df275329f202e48c76360b3f22b08d28c196cbc54600319435f8d2",
    input={
        "audio": "https://replicate.delivery/mgxm/e5159b1b-508a-4be4-b892-e1eb47850bdc/OSR_uk_000_0050_8k.wav",
        "model": "large-v3",
        "language": "af",
        "translate": False,
        "temperature": 0,
        "transcription": "plain text",
        "suppress_tokens": "-1",
        "logprob_threshold": -1,
        "no_speech_threshold": 0.6,
        "condition_on_previous_text": True,
        "compression_ratio_threshold": 2.4,
        "temperature_increment_on_fallback": 0.2
    }
)

# The language is detected and passed on to all agents to give output in the corresponding language.

# Output voice

import win32con.client

speaker = win32con.client.Dispatch("SAPI.SpVoice")
speaker.Speak("This is text to voice converter")

# This just a simple way to output text. We can also go with more sophistiated AI text-to-speech models such as Synthesia that has 
# inbuilt multilingual support.


# The inputs along with the language is passed along to the crews. This project consists of 5 crews which can work together but here I
# have seperated for easy readability. The crews have kind of unique roles so its better to run seperate anyways. Check them out in the 
# Crew folder