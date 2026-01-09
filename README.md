# OmniMap

A small NiceGUI prototype for finding and displaying game maps. Work in progress — UX and map lookup/display are not finished.

## Quick start

1. Create and activate a virtualenv (recommended):
   - python3 -m venv venv
   - source venv/bin/activate
2. Install dependencies:
   - pip install -r utils.txt
3. Run the app:
   - python main.py
4. Open http://localhost:8081 and try the input field.

## What’s in the repo

- main.py — UI (input, submit button, placeholder image)
- functions.py — handlers (clear_input, handle_submit)
- curated_map_urls.txt — simple map name → image URL mapping
- utils.txt — dependency list (nicegui, pillow, requests)

## Current behavior / notes

- Submitting prints a normalized version of the input and clears the field.
- The app currently does not replace the displayed image based on input — that’s the next step.
- curated_map_urls.txt contains example mappings to use for lookups.

## TODO

- Implement map lookup using curated_map_urls.txt (or a better source)
- Update the image component in-place when a map is found
- Add unit tests and CI
- Improve input parsing and error handling
- Add documentation and license