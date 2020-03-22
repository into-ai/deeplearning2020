from typing import TYPE_CHECKING

import kerasltisubmission as klti
from kerasltisubmission.exceptions import KerasLTISubmissionBadResponseException

if TYPE_CHECKING:  # pragma: no cover
    import keras.models


class Submission:
    def __init__(
        self,
        user_token: klti.AnyIDType,
        assignment_id: klti.AnyIDType,
        model: "keras.models.Model",
    ):
        self.user_token = user_token
        self.assignment_id = assignment_id
        self.model = model

    def submit(self, verbose: bool = False, strict: bool = False) -> None:
        provider = klti.LTIProvider(
            input_api_endpoint="https://neuralnet.xopic.de/ltiprovider",
            submission_api_endpoint="https://neuralnet.xopic.de/ltiprovider/submit",
            user_token=self.user_token,
        )

        submission = klti.Submission(assignment_id=self.assignment_id, model=self.model)

        try:
            results = provider.submit(submission, verbose=verbose, strict=strict)
            for assignment_id, result in results.items():
                print(f"Assignment {assignment_id} erfolgreich abgegeben!")
                print(
                    f"Dein Model hat eine Accuracy von {round(result.get('accuracy') * 100, ndigits=1)}% auf unseren Validierungsdaten."
                )
                print(
                    f"Du erhältst {round(result.get('grade') * 100, ndigits=1)}% der Punkte auf dieses Assignment."
                )
                print(
                    f"Falls du bereits eine Abgabe mit höherer Bewertung abgegeben hast, wird automatisch das bessere Ergebnis gewählt."
                )
        except KerasLTISubmissionBadResponseException as e:
            print(e.message)
        except Exception as e:
            print(str(e))
