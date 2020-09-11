import data_loader
import test_models


class Test:

    def return_value(self, text):

        # 학습 모델 테스트
        input_seq = self.d_loader.make_predict_input(text, self.word_to_index)
        sentence = self.d_loader.generate_text(input_seq, self.encoder_model, self.decoder_model)
        return sentence

    def __init__(self):
        # --------------------------------------------
        # 데이터로드
        # --------------------------------------------
        self.d_loader = data_loader.DataLoader()

        # 단어 딕셔너리 생성
        self.word_to_index, self.index_to_word = self.d_loader.set_word_dic()

        # 모델로드
        build = test_models.BuildModel(2345, self.d_loader.embedding_dim, self.d_loader.lstm_hidden_dim)

        model = build.train_model()
        model.load_weights("./datasets/seq2seq_model.h5")

        self.encoder_model, self.decoder_model = build.predict_model()
