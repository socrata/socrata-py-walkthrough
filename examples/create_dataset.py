from examples.auth import authorization
from socrata import Socrata

socrata = Socrata(authorization)

with open('files/Sold_Fleet_Equipment.csv', 'rb') as file:
    # Let's make a socrata view, open a revision on it, and then
    # upload and validate our data
    (revision, output_schema) = socrata.create(
        name = "cool dataset",
        description = "~~my first dataset~~"
    ).csv(file)

    (ok, output_schema) = output_schema.wait_for_finish()
    assert ok, output_schema

    (ok, job) = revision.apply(output_schema = output_schema)
    assert ok, job

    revision.open_in_browser()

