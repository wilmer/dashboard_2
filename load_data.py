import sys, os
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "winerama.settings")

import django

django.setup()

from app.models import Country


def save_review_from_row(review_row):
    country = Country()
    country.country_name = review_row[0]
    country.country_code = review_row[1]
    country.iso_codes = review_row[2]
    country.population = review_row[3]
    country.area = review_row[4]
    country.area = review_row[5]
    country.save()


# the main function for the script, called by the shell
if __name__ == "__main__":

    # Check number of arguments (including the command name)
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        reviews_df = pd.read_csv(sys.argv[1])
        print reviews_df

        # apply save_review_from_row to each review in the data frame
        reviews_df.apply(
            save_review_from_row,
            axis=1
        )

        print "There are {} reviews in DB".format(Country.objects.count())

    else:
        print "Please, provide Country info file path"
