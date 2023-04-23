# from bark import SAMPLE_RATE, generate_audio, preload_models
import simpleaudio as sa

# # download and load all models
preload_models()

# # generate audio from text
text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""
audio_array = generate_audio(text_prompt)

# NOTE - this is not quite right, the audio file plays very slowly
play_obj = sa.play_buffer(audio_array, 1, 2, SAMPLE_RATE)
play_obj.wait_done()

# play audio directly

print("done")

# play text in notebook
# Audio(audio_array, rate=SAMPLE_RATE)