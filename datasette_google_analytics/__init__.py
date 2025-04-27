from datasette import hookimpl
import markupsafe


@hookimpl
def extra_js_urls(datasette):
    """
    Add Google Analytics script tag that loads the GA tracking code.
    """
    plugin_config = datasette.plugin_config("datasette-google-analytics") or {}
    tracking_id = plugin_config.get("tracking_id")

    if not tracking_id:
        return []

    return [
        {
            "url": f"https://www.googletagmanager.com/gtag/js?id={tracking_id}",
            # NOTE: this hook currently does not support async attribute
        }
    ]


@hookimpl
def extra_body_script(datasette):
    """
    Add the Google Analytics initialization code to the bottom of the body.
    """
    plugin_config = datasette.plugin_config("datasette-google-analytics") or {}
    tracking_id = plugin_config.get("tracking_id")

    if not tracking_id:
        return None

    return {
        "script": f"""
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{tracking_id}');
        """
    }
