# datasette-google-analytics

A [Datasette](https://datasette.io/) plugin that adds Google Analytics tracking code to your Datasette instance.

## Installation

Install this plugin in the same environment as Datasette:

```sh
pip install datasette-google-analytics
```

## Usage

You need to provide your Google Analytics tracking ID when you start Datasette.

### Using metadata.json

Create a `metadata.json` file with the following contents:

```json
{
    "plugins": {
        "datasette-google-analytics": {
            "tracking_id": "G-XXXXXXXXXX"
        }
    }
}
```

Replace `G-XXXXXXXXXX` with your actual Google Analytics 4 tracking ID.

Then start Datasette with:

```
datasette --metadata metadata.json your-database.db
```

## Development

To set up this plugin locally:

```sh
cd datasette-google-analytics
pip install -e .
```
