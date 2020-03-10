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

    def submit(self) -> None:
        provider = klti.LTIProvider(
            input_api_endpoint="http://localhost:8080",
            submission_api_endpoint="http://localhost:8080/submit",
            user_token=self.user_token,
        )

        submission = klti.Submission(assignment_id=self.assignment_id, model=self.model)

        try:
            provider.submit(submission)
        except KerasLTISubmissionBadResponseException as e:
            print(e.message)
        except Exception as e:
            print(str(e))
