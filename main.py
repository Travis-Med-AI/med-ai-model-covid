from preprocess import preprocess
from evaluate import evaluate


def evaluate_model(files):
    preprocessed = preprocess(files)

    study_type = evaluate(preprocessed)

    return study_type, None

if __name__ == '__main__':
    paths = ['test_images/covid', 'test_images/normal', 'test_images/pneumonia']
    out= evaluate_model(paths)
    print(out)