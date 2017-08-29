import sys

import qi

import logging



class RobotController(object):

    def __init__(self, ip = '10.30.0.110', port = 9559, useSpanish = True):
        self.ip = ip
        self.port = port
        self.useSpanish = useSpanish
        self.session = qi.Session()

    def set_limits(self):
        self.hr = 130

    def set_sentences(self):
        self.welcomeSentence = "Hola, \\pau=400\\ mi nombre es Nano. \\pau=500\\ Te estaré acompañando en sesión. \\pau=500\\ Estoy aquí para cuidar tus signos y ayudarte a mejorar en tu rehabilitación."
        self.hrIsUpSentence = 'Parece que estás empezando a estar cansado,\\pau=400\\ todo está bien?'
        self.postureCorrectionSentence = 'Trata de enderezarte,\\pau=400\\ pon la espalda recta'



    def connect_to_robot(self):

        try:
            self.session.connect("tcp://" + self.ip + ":" + str(self.port))

        except RuntimeError:
            logging.debug("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port) +".\n"
                          "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)

        self.animatedSpeechProxy = self.session.service("ALAnimatedSpeech")

        self.tts = self.session.service("ALTextToSpeech")

        self.configuration = {"bodyLanguageMode":"contextual"}

    def say(self, textToSay):
        self.tts.say(textToSay)


    def get_data(self, data):
        self.ecg = data['ecg']
        self.angles = data['angles']
        if self.ecg > self.hr:
            self.say(self.hrIsUpSentence)

        if self.angles[0] < 90:
            self.say(self.postureCorrectionSentence)



def main():
    nao = RobotController(ip = '10.30.0.110', useSpanish = True)
    nao.connect_to_robot()
    nao.say()

if __name__ == '__main__':
    main()
