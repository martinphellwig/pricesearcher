# Senior Software Engineer - APIs - Code Test

Hello 👋!

Thank you for applying to Pricesearcher!

As part of your application process we would like you to complete a short
technical challenge to assist in our evaluation of your application.

Your solution, as well as more complex ideas, improvements
and suggestions will be discussed further at interview stage should your
application progress.

## Task

### Description

You have been provided with 2 files of varying sizes, qualities, contents and
formats. These files contain a list of randomly generated products from various
brands and retailers.

Your task is to write a small command line application that on startup ingests this
data as quickly and efficiently as possible. For the sake of keeping this test short
it is fine to load it into memory, you do not need to use a database.

Following this your application should start an API server with two endpoints:

- An endpoint to retrieve a single product by its `id`
- An endpoint that retrieves the N cheapest products (where N is a configurable number that the client can specify)

Your API endpoints should return the product data as JSON with the
following fields:

- `id` as a string
- `name` as a string
- `brand` as a string
- `retailer` as a string
- `price` as a float
- `in_stock` as a boolean

Any fields that aren't available for a product should be returned as `null`.

The first file ([products.csv.gz](products.csv.gz)) is in the CSV file format and
compressed with GZIP.

The second file ([products.json](https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json))
is in the JSON file format and is located in an AWS S3 bucket. Your application
should download this once when it starts up.

### Implementation

You are free to implement this using whatever technologies you feel appropriate
although as this is a primarily Python focussed role so it would be nice to see
that used.

There is no time limit on how long you can spend on the task but around 2 to 3
hours is probably a good guide. As mentioned above any further improvements or
ideas you have can be discussed in the interview.

Your submission will be judged on the overall quality of the solution with
various factors such as the following considered:

- Presentation
- Performance
- Simplicity
- Readability
- Reliability
- Scalability
- Extensibility
- Some other words that end in 'ility'

### Submission

Your work should be submitted as a Git repository. Hosted on a Git hosting website
such as Github/Bitbucket or as a zip archive. If hosted publicly, please don't
mention the interview in the repo or code, unless you feel comfortable making it
public you're interviewing with us.

You should document how to run your submission as if the reader were a client
consuming your API and if it relies on any external dependencies, what those
are and how to install them.

For bonus points, include your favourite Gif. This will not affect your
application, unless it is _really_ great.


Good luck!