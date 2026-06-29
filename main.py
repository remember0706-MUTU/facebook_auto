import sys
from quote_generator import generate_quote_content
from facebook_poster import post_to_facebook

def run():
    quote = generate_quote_content()
    text_en = quote.get("text_en", "")
    full_text = quote["text"] + ("\n\n" + text_en if text_en else "")
    success = post_to_facebook(full_text)
    if success:
        print("Facebook post published successfully!")
    else:
        print("Failed to publish Facebook post")
        sys.exit(1)

if __name__ == "__main__":
    run()
