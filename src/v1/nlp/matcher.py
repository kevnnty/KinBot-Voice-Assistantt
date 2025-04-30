qa_dictionary = {
    "rwanda coding academy iherereye he": "Iherereye mu Karere ka Nyabihu, mu Ntara y’Iburengerazuba.",
    "umurwa mukuru w’u rwanda ni uwuhe": "Ni Kigali.",
    "ni ryari u rwanda rwabonye ubwigenge": "Ku itariki ya 1 Nyakanga 1962.",
    "ni uwuhe murwa mukuru wa afurika y’i burasirazuba": "Ni Kigali.",
    "ubwiza bw’igihugu cy’u rwanda buri he": "Buri muri Nyungwe, Volcanoes na Akagera, hamwe n’ahandi hatatse igihugu cyiza.",
}

def get_answer(transcription):
    transcription = transcription.strip().lower()
    return qa_dictionary.get(transcription, "Ntabwo nasanze igisubizo cyihariye.")
