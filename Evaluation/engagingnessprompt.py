
# Naive
naive = "Score the following response given the corresponding " + \
        "dialogue context on a continuous scale from 0 to 100, where a score of zero " + \
        "means \'disengaging\' and a score of 100 means \'very engaging\'. Assume " + \
        "the response immediately follows the dialogue context."

dialogue_context = "Dialogue context:"
response = "Response:"
score = "Score:"

# HD
human_directed = "You will be given a conversation between two individuals. You will then be given several potential " + \
        "responses for the next turn in the conversation. " + \
        "Is the response engaging? \n" + \
        "A response is considered engaging if it can engage the user. This might be an inquisitive " +\
        "question or an interesting response that can be followed-up on.\n\n" +\
        "A score of 1 means No: the response is boring and does little to engage the user.\n" +\
        "● Hi there.\n" +\
        "● Oh wow! That's cool!\n\n" +\
        "A score of 2 means Somewhat: the response is not particularly engaging but still leaves room for follow-up.\n" +\
        "● My favourite colour is blue.\n" +\
        "● Nope. I'm not very good with cooking.\n\n" +\
        "A score of 3 means Yes: the response is actively engaging the user and trying to move forward the conversation.\n" +\
        "● I have a feeling that if you can dodge a wrench you can dodge a ball.\n" +\
        "● What kind of shows do you like?\n\n"

# MEEP 
meep = "Score the following response given the corresponding " + \
        "dialogue context on a continuous scale from 0 to 100, where a score of zero " + \
        "means \'disengaging\' and a score of 100 means \'very engaging\'. Assume " + \
        "the response immediately follows the dialogue context. Consider that engagingness of a response " + \
        "is defined by the following qualities: variety of response according to the context, likelihood  " + \
        "of encouraging the other participant to respond, likelihood of encouraging a " + \
        "quality response from the other participant, interestingness, specificity, and likelihood  " + \
        "of creating a sense of belonging for the other participant. "

# MEEP+SA
meep_sa = "Score the following response given the corresponding " + \
        "dialogue context on a continuous scale from 0 to 100, where a score of zero " + \
        "means \'disengaging\' and a score of 100 means \'very engaging\'. Assume " + \
        "the response immediately follows the dialogue context. Consider that engagingness of a response " + \
        "is defined by the following qualities: variety of response according to the context (such as responding " + \
        "to \"Hi how are you?\" with \"I feel magnificent, because I just successfully defended my PhD! How are you?\ " + \
        "instead of \"Good, how are you?\"), likelihood  " + \
        "of encouraging the other participant to respond (such as 'I love legos! I like using them to make funny things. Do you like legos?' " + \
        " instead of 'I like legos.'), likelihood of encouraging a " + \
        "quality response from the other participant, interestingness, specificity, and likelihood  " + \
        "of creating a sense of belonging for the other participant. "

# +R
system_msg = "You are an expert evaluator of dialogue. "

# SPANISH VERSION
# ES(MEEP+SA) 
meep_sa_es = "Evalúa la siguiente respuesta dada el contexto de diálogo correspondiente en una escala " +\
        "continua del 0 al 100, donde una puntuación de cero significa \"desinteresante\" y una puntuación " +\
        "de 100 significa \"muy interesante\". Supongamos que la respuesta sigue inmediatamente después " +\
        "del contexto de diálogo. Considera que la cualidad de una respuesta interesante se define por las siguientes " +\
        "características: variedad de respuesta de acuerdo al contexto (por ejemplo, responder a \"Hola, ¿cómo estás?\" " +\
        "con \"Me siento magnífico porque acabo de defender exitosamente mi tesis doctoral. ¿Y tú?\" en lugar de \"Bien, ¿y tú?\"), " +\
        "probabilidad de incentivar al otro participante a responder (por ejemplo, \"¡Me encantan los legos! Me gusta usarlos " +\
        "para hacer cosas divertidas. ¿Te gustan los legos?\" en lugar de \"Me gustan los legos.\"), probabilidad de incentivar " +\
        "una respuesta de calidad del otro participante, interés, especificidad y probabilidad de crear " +\
        "un sentido de pertenencia para el otro participante. "
dialogue_context_es = "Contexto de diálogo: "
response_es = "Respuesta: "
score_es = "Puntuación:"
role_es =  "Eres experto en evaluación de diálogos."

# CHINESE VERSION
# ZH(MEEP+SA)
meep_sa_zh = "根据相应的对话背景，对以下回应在0到100的连续刻度上进行评分，其中0分表示“不吸引人”，100分表示“非常吸引人”。" +\
        "假设回应紧随对话背景之后。请考虑回应的吸引力是由以下特质定义的：根据背景的回应多样性（例如对“你好，你怎么样？" +\
        "”的回应是“我感觉很棒，因为我刚成功地为我的博士学位进行了答辩！你怎么样？”而不是“好的，你怎么样？”）、" +\
        "鼓励其他参与者回应的可能性（例如：“我喜欢乐高！我喜欢用它们制作有趣的东西。你喜欢乐高吗？”而不是“我喜欢乐高。”）、" +\
        "鼓励其他参与者提供高质量回应的可能性、有趣性、具体性和为其他参与者创造归属感的可能性."
meep_sa_dial_zh = "在这个任务中，您将看到对话的一部分。请为整个对话打分使用0到100的连续分数范围，其中0分表示“不吸引人”，" +\
        "100分表示“非常吸引人”。请考虑每个对话的吸引力取决于以下特质：据对话背景的回应多样性（例如对“你好，你怎么样？”" +\
        "的回应是“我感觉很棒，因为我刚成功地为我的博士学位进行了答辩！你怎么样？”而不是“好的，你怎么样？”）、" +\
        "鼓励其他参与者回应的可能性（例如：“我喜欢乐高！我喜欢用它们制作有趣的东西。你喜欢乐高吗？”而不是“我喜欢乐高。”）、" +\
        "鼓励其他参与者提供高质量回应的可能性、有趣性、具体性和为其他参与者创造归属感的可能性。请综合考虑对话的整体吸引力。"
dialogue_context_zh = "对话背景： "
dialogue_dial_zh = "对话： "
response_zh = "回应： "
score_zh = "评分："
role_zh = "你是一名对话评估的专家。"

# MEEP+SA-DIAL
meep_sa_dial = "In this task, you will be shown part of a dialogue. " + \
        "Score the dialogue on a continuous scale from 0 to 100, where a score of zero " + \
        "means \'disengaging\' and a score of 100 means \'very engaging\'. Consider that engagingness of each dialogue " + \
        "is defined by the following qualities: variety of responses according to the context (such as responding " + \
        "to \"Hi how are you?\" with \"I feel magnificent, because I just successfully defended my PhD! How are you?\ " + \
        "instead of \"Good, how are you?\"), likelihood  " + \
        "of encouraging the other participant to respond (such as 'I love legos! I like using them to make funny things. Do you like legos?' " + \
        " instead of 'I like legos.'), likelihood of encouraging " + \
        "quality responses from the other participant, interestingness, specificity, and likelihood  " + \
        "of creating a sense of belonging for the other participant. Consider the overall engagingness of the conversation."

# GPTSCORE
gptscore = "Answer the question based on the conversation between a human and AI.\n" +\
        "Question: Are the responses of AI engaging? (a) Yes. (b) No."
gptscore_answer_with_yes = "Answer: Yes."

# G-EVAL
geval = "You will be given a conversation between two individuals. You will then be given one potential " + \
        "response for the next turn in the conversation.\n" + \
        "Your task is to rate the responses on one metric.\n" + \
        "Please make sure you read and understand these instructions carefully. Please keep this " + \
        "document open while reviewing, and refer to it as needed.\n" + \
        "Evaluation Criteria:\n" + \
        "Engagingness (1-3) Is the response dull/interesting?\n" + \
        "- A score of 1 (dull) means that the response is generic and dull.\n" + \
        "- A score of 2 (somewhat interesting) means the response is somewhat interesting and could " + \
        "engage you in the conversation (e.g., an opinion, thought)\n" + \
        "- A score of 3 (interesting) means the response is very interesting or presents an interesting fact\n" + \
        "Evaluation Steps:\n" + \
        "1. Read the conversation, the corresponding fact and the response carefully.\n" + \
        "2. Rate the response on a scale of 1-3 for engagingness, according to the criteria above.\n" + \
        "3. Provide a brief explanation for your rating, referring to specific aspects of the response and " + \
        "the conversation.\n" + \
        "Example:"

# G-EVAL-DIAL
geval_dial = "You will be given a conversation between two individuals. " + \
        "Your task is to rate the conversation on one metric.\n" + \
        "Please make sure you read and understand these instructions carefully. Please keep this " + \
        "document open while reviewing, and refer to it as needed.\n" + \
        "Evaluation Criteria:\n" + \
        "Engagingness (1-3) Is the conversation dull/interesting?\n" + \
        "- A score of 1 (dull) means that the conversation is generic and dull.\n" + \
        "- A score of 2 (somewhat interesting) means the conversation is somewhat interesting and could " + \
        "engage you in the conversation (e.g., an opinion, thought)\n" + \
        "- A score of 3 (interesting) means the conversation is very interesting or presents an interesting fact\n" + \
        "Evaluation Steps:\n" + \
        "1. Read the conversation carefully.\n" + \
        "2. Rate the conversation on a scale of 1-3 for engagingness, according to the criteria above.\n" + \
        "3. Provide a brief explanation for your rating, referring to specific aspects of " + \
        "the conversation.\n" + \
        "Example:"
geval_conversation_history = "Conversation History:\n"
geval_response = "Response:\n"
geval_evaluation_form = "Evaluation Form (scores ONLY):\n- Engagingness:"
geval_conversation_for_dial_eval = "Conversation:\n"
