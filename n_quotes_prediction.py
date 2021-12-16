import tensorflow as tf
import numpy as np


def network_output_to_text(network_output: int):
    '''
    change the output to some nice text instead but this 
    is the categories the model is trained on.
    '''
    if network_output == 0:
        return "between 0 and 10 quotes"
    elif network_output == 1:
        return "between 10 and 100 quotes"
    elif network_output == 2:
        return "between 100 and 500 quotes"
    elif network_output == 3:
        return "between 500 and 1000 quotes"
    elif network_output == 4:
        return "over 1000 quotes"
def main():
    '''
    categorical inputs to the network:
    - gender: "male", "female" or "other"
    - occupation: "politician", "athlete", "actor", "lawyer", 
                  "researcher", "journalist", "musician", "businessperson", 
    - topic: "art", "sport", "economy & finance", "politics", "health & science"
    - emotion: "joy", "anger", "fear", "neutral", "sad", "calm"
    
    Notes: 
     - make sure that everything is lowercase
    '''
    # Example input
    
    age = 55
    nationality = 'united states of america'
    gender = 'male'
    occupation = 'politician'
    topic = 'politics'
    emotion = 'anger'

    # format the input exactly like this
    input_example = {'age': tf.convert_to_tensor([np.array(age)]),
        'nationality': tf.convert_to_tensor([np.array(nationality)]),
        'gender': tf.convert_to_tensor([np.array(gender)]), 
        'occupation': tf.convert_to_tensor([np.array(occupation)]) ,
        'topic': tf.convert_to_tensor([np.array(topic)]),
        'emotion': tf.convert_to_tensor([np.array(emotion)]),
        
        }

    # This is how you load the model
    model = tf.keras.models.load_model('<path to model folder>')

    # This is how you predict and interpret the output
    pred = model.predict(input_example)
    res = np.argmax(tf.nn.softmax(pred), axis=1)
    print(network_output_to_text(res))

if __name__ == "__main__":
    main()